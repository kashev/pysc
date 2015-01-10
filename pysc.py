#!/usr/bin/env python3
# pysc
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
# pysc.py

""" A Scrabble cheater script. Provides all words from given letters. """

# IMPORTS
import argparse
import collections
import enum
import itertools
import json
import string

try:
    from tabulate import tabulate
    pretty_print = True
except ImportError as e:
    pretty_print = False


@enum.unique
class ScrabbleDictionary(enum.Enum):
    """ The different scrabble dictionaries possible. """
    sowpods = "sowpods"
    twl = "twl"
    wwf = "wwf"


class Word:
    """ A class for words, which helps keep track of word score. """
    def __init__(self, word, letters, score_dict):
        self.word = word
        self.score = 0
        letter_list = list(letters)
        for letter in word:
            if letter in letter_list:
                letter_list.remove(letter)
                self.score += score_dict[letter]

    def has_letters(self, required_letters):
        required_list = list(required_letters)
        letter_list = list(self.word)
        for letter in required_list:
            try:
                letter_list.remove(letter)
            except ValueError:
                return False
        return True


def load_anagram_dict(scrabble_dictionary):
    """ Load the scrabble dictionary of choice. """
    DICT_PRE = "dict/"
    DICT_EXT = "_anagram.txt"
    dict_path = DICT_PRE + scrabble_dictionary.value + DICT_EXT

    anagram_dict = collections.defaultdict(list)
    with open(dict_path, 'r') as dict_file:
        for line in dict_file:
            words = line.split()
            anagram_dict[tuple(words[0])] = words[1:]

    return anagram_dict


def load_scoring_dict(scrabble_dictionary):
    """ Load the scoring dictionary. """
    SCORE_PATH = "dict/scores.json"
    with open(SCORE_PATH, 'r') as score_file:
        score_dict = json.loads(score_file.read())
        if scrabble_dictionary is ScrabbleDictionary.wwf:
            return score_dict["wwf"]
        else:
            return score_dict["scrabble"]


def score_word(word, score_dict):
    """ Given a word, score it using the scoring dicitonary. """
    return sum([score_dict[letter] for letter in word])


def find_words(letters, anagram_dict, score_dict, required="", length=None):
    """ Find all the words that can be made from the given letters. """
    BLANK = '.'

    num_blanks = letters.count(BLANK)
    non_blank_letters = ''.join(sorted(letters + required)).replace(BLANK, '')

    target_word_dict = {}
    for blanks in itertools.product(string.ascii_lowercase, repeat=num_blanks):
        letters = sorted(non_blank_letters + ''.join(sorted(blanks)))

        # pick length range
        if length is None:
            length_range = range(2, len(letters) + 1)
        else:
            length_range = [length]

        for word_length in length_range:
            for combination in itertools.combinations(letters, word_length):
                if combination in anagram_dict:
                    for target_string in anagram_dict[combination]:
                        target_word = Word(target_string, non_blank_letters,
                                           score_dict)
                        # Ensure the word has required letters.
                        if not target_word.has_letters(required):
                            continue

                        # Add the word if it doesn't exist
                        if target_string not in target_word_dict:
                            target_word_dict[target_string] = target_word
                        # Otherwise only add the word if the new version is
                        # higher scoring.
                        else:
                            if (target_word_dict[target_string].score <
                                    target_word.score):
                                target_word_dict[target_string] = target_word

    return target_word_dict


def main():
    """ The main body of the script. """
    parser = argparse.ArgumentParser(
        description="A Scrabble cheater script. More information at "
                    "https://github.com/kashev/pysc",
        formatter_class=argparse.RawTextHelpFormatter)

    helpstring = "choose a dictionary:\n"
    for sd in ScrabbleDictionary:
        helpstring += "- {}\n".format(sd.name)

    parser.add_argument("-d", "--sdict", help=helpstring,
                        type=ScrabbleDictionary,
                        default=ScrabbleDictionary.wwf)
    parser.add_argument("-r", "--required", type=str, default="",
                        help="required letters, must be in the word")
    parser.add_argument("-l", "--length", type=int, default=None,
                        help="length of desired words")

    parser.add_argument("letters", type=str,
                        help="Letters from which words will be made")

    args = parser.parse_args()

    anagram_dict = load_anagram_dict(args.sdict)
    score_dict = load_scoring_dict(args.sdict)
    target_word_dict = find_words(args.letters.lower(), anagram_dict,
                                  score_dict, args.required.lower(),
                                  args.length)

    words = [[word.word, word.score, len(word.word)]
             for key, word in target_word_dict.items()]
    words.sort(key=lambda x: x[1], reverse=True)

    headers = ["word", "score", "length"]

    if pretty_print:
        table = tabulate(words, headers=headers)
        print(table)

    else:
        print("{} | {} | {}".format(headers[0], headers[1], headers[2]))
        for word in words:
            print("{} | {} | {}".format(word[0], word[1], word[2]))


if __name__ == '__main__':
    main()

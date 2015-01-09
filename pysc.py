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


@enum.unique
class ScrabbleDictionary(enum.Enum):
    """ The different scrabble dictionaries possible. """
    sowpods = "sowpods"
    twl = "twl"
    wwf = "wwf"


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


def find_words(letters, anagram_dict):
    """ Find all the words that can be made from the given letters. """
    letters = ''.join(sorted(letters))
    target_words = []
    for word_length in range(2, len(letters) + 1):
        for combination in itertools.combinations(letters, word_length):
            if combination in anagram_dict:
                target_words += anagram_dict[combination]
    return set(target_words)


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

    parser.add_argument("letters", type=str,
                        help="Letters from which words will be made")

    args = parser.parse_args()

    anagram_dict = load_anagram_dict(args.sdict)
    score_dict = load_scoring_dict(args.sdict)
    target_words = find_words(args.letters, anagram_dict)

    for word in target_words:
        print("{} | {}".format(word, score_word(word, score_dict)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# pysc
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
# anagram_dict_builder.py

""" A script which builds an anagram dictionary from a dictionary. """
# Credit: Jeff Knupp
# https://github.com/jeffknupp/presser/blob/master/make_anagrams.py

import collections
import os
import string


def build_anagram_dict(infile, outfile):
    with open(infile, 'r') as file_handle:
        words = collections.defaultdict(list)
        letters = set(string.ascii_lowercase + '\n')
        for word in file_handle:
            # Check to see if the word contains only letters in the set
            # (no apostraphies, only an issue if using a poor dictionary)
            # and that the word is of a reasonable length
            if len(set(word) - letters) == 0 and len(word) < 20 or True:
                word = word.strip()
                letter_key = ''.join(sorted(word))
                words[letter_key].append(word)

    anagram_dictionary = [' '.join([key] + value)
                          for key, value in words.items()]
    anagram_dictionary.sort()
    with open(outfile, 'w') as file_handle:
        file_handle.write('\n'.join(anagram_dictionary))


def main():
    """ main function. """

    # Change to script directory.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    for sd in ["sowpods", "twl", "wwf"]:
        infile = '../dict/{}.txt'.format(sd)
        outfile = '../dict/anagram_{}.txt'.format(sd)
        build_anagram_dict(infile, outfile)

if __name__ == '__main__':
    main()

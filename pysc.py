#!/usr/bin/env python3
# pysc
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
# pysc.py

""" A Scrabble cheater script. Provides all words from given letters. """

# IMPORTS
import argparse
import enum

# CONSTANTS
DICT_PATH = "dict/"
DICT_EXT = ".txt"


@enum.unique
class ScrabbleDictionary(enum.Enum):
    """ The different scrabble dictionaries possible. """
    sowpods = "sowpods"
    twl = "twl"
    wwf = "wwf"


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

    dict_file = DICT_PATH + args.sdict.value + DICT_EXT


if __name__ == '__main__':
    main()

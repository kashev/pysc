pysc
====

    pysc
    Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
    README.md

A Scrabble cheater written in Python. Includes multiple dictionaries, including SOWPODS and the Words With Friends Dictionary.

# Why
I wanted this software because the ability to use different dictionaries is important to me. `/usr/share/dict/words` isn't a Scrabble Competition dictionary.

# Requirements
You must have `python` version 3.4 or higher to run this script, for Python enumerations. Additionally, the package [`tabluate`](https://bitbucket.org/astanin/python-tabulate) is required for pretty printing, but isn't strictly required to run the script.

# Instructions
Create the virtual enviornment (using [`virtualenvwrapper`](virtualenvwrapper.readthedocs.org/en/latest/)) by running `mkvirtualenv pysc -p /usr/bin/python3`. Run the script by running `./pysc [letters]`. Run `./pysc -h` for more options.

# Don't Cheat
Cheating while you're playing Words With Friends isn't fulfilling. I intend this tool to be a lightweight, free replacement for WWF's Hindsight, where you can enter your hand and a letter from where you were trying to play, and see what you might have played. Actually playing words that you couldn't come up with isn't nice. Learning to play better next time is.

# Thanks
- Thanks to [ScrabbleHelper](https://code.google.com/p/scrabblehelper/), a more complicated Java project, for the SOWPODS and TWL dictionary files.
- Thanks to [Blog My Brain](http://blogmybrain.com/words-with-friends-cheat/words-with-friends-dictionary.php) for the [Words With Friends](https://zynga.com/games/words-friends) dictionary.
- Thanks to [Justin Peel](http://stackoverflow.com/users/254617/justin-peel) for his useful analysis of this problem on [Stack Overflow](http://stackoverflow.com/a/5521619/1473320).
- Thanks to [Jeff Knupp]() for [even](http://www.jeffknupp.com/blog/2013/01/04/creating-and-optimizing-a-letterpress-cheating-program-in-python/) [more](https://github.com/jeffknupp/presser) useful work on a similar problem.
- Thanks to [James Sweet](http://nojesusnopeas.blogspot.com/) for his table of [Scrabble and Words With Friends letter scores](http://nojesusnopeas.blogspot.com/2012/03/differences-between-words-with-friends.html).
- Thanks to [Sergey Astanin and the tabluate team](https://bitbucket.org/astanin/python-tabulate) for [tabluate](https://pypi.python.org/pypi/tabulate/).

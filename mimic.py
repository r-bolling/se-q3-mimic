#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "r-bolling with help from Kenzie Academy lessons"


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # +++your code here+++
    contents = open(filename, 'r')
    words = contents.read().split()
    words_dict = {}
    i = 0
    while i < len(words):
        if words_dict == {}:
            words_dict[''] = [words[i]]
        elif words_dict.get(words[i - 1]):
            words_dict[words[i - 1]].append(words[i])
        else:
            words_dict[words[i - 1]] = [words[i]]
        i += 1
    contents.close()
    pass
    return words_dict 


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    # +++your code here+++
    i = 0
    count_dict = []
    while i < num_words:
        if i >= num_words:
            break
        for key, value in mimic_dict.items():
            if i == 0:
                print('', random.choice(mimic_dict['']), ' ', end='')
                i += 1
            elif i < num_words:
                test = random.choice(value)
                print(random.choice(value), ' ', end='')
                # count_dict.append(key)
                count_dict.append(random.choice(value))
                i += 1
    finalnum = len(count_dict)
    pass


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')

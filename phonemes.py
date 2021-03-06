#!/usr/bin/env python

#
# Generate words of phonemes.
#
# Based on the pwgen utility, however this is not
# suitable for creating passwords.
#
# pwgen: http://sourceforge.net/projects/pwgen/
#
# Like the pwgen utility this is based on, this file is
# licensed under the GPL.
#

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import itertools
import random
import sys

class _Phoneme(object):
    phoneme = None
    dipthong = False
    not_first = False

    def __init__(self, phoneme, dipthong=False, not_first=False):
        self.phoneme = phoneme
        self.dipthong = dipthong
        self.not_first = not_first

class _Consonant(_Phoneme):
    pass

class _Vowel(_Phoneme):
    pass

_phonemes = [
    _Vowel('a'),
    _Vowel('ae', dipthong=True),
    _Vowel('ah', dipthong=True),
    _Vowel('ai', dipthong=True),
    _Consonant('b'),
    _Consonant('c'),
    _Consonant('ch', dipthong=True),
    _Consonant('d'),
    _Vowel('e'),
    _Vowel('ee', dipthong=True),
    _Vowel('ei', dipthong=True),
    _Consonant('f'),
    _Consonant('g'),
    _Consonant('gh', dipthong=True, not_first=True),
    _Consonant('h'),
    _Vowel('i'),
    _Vowel('ie', dipthong=True),
    _Consonant('j'),
    _Consonant('k'),
    _Consonant('l'),
    _Consonant('m'),
    _Consonant('n'),
    _Consonant('ng', dipthong=True, not_first=True),
    _Vowel('o'),
    _Vowel('oh', dipthong=True),
    _Vowel('oo', dipthong=True),
    _Consonant('p'),
    _Consonant('ph', dipthong=True),
    _Consonant('qu', dipthong=True),
    _Consonant('r'),
    _Consonant('s'),
    _Consonant('sh', dipthong=True),
    _Consonant('t'),
    _Consonant('th', dipthong=True),
    _Vowel('u'),
    _Consonant('v'),
    _Consonant('w'),
    _Consonant('x'),
    _Consonant('y'),
    _Consonant('z'),
]

def _phoneme_generator():
    rs = random.SystemRandom()
    prev_type = _Consonant
    next_type = None
    first = True

    while True:
        if first:
            candidates = [ e for e in _phonemes if not e.not_first ]
            first = False
        else:
            candidates = [ e for e in _phonemes if isinstance(e, next_type) ]

        phoneme = rs.choice(candidates)
        yield phoneme

        if isinstance(phoneme, _Consonant):
            next_type = _Vowel
        else:
            if prev_type == _Vowel or phoneme.dipthong or rs.random() > 0.3:
                next_type = _Consonant
            else:
                next_type = _Vowel
        prev_type = phoneme


def generate_word(length):
    while True:
        ret = ''
        for p in _phoneme_generator():
            ret += p.phoneme
            if len(ret) == length:
                return ret
            elif len(ret) > length:
                break

def positive_int(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError('Must be a positive integer')
    return value

def random_word_length():
    length = int(random.normalvariate(7, 2))
    if length < 1:
        length = 1
    return length

def word_generator(word_length_fn):
    while True:
        yield generate_word(word_length_fn())

def print_words(words, separator='\n'):
    for index, word in enumerate(words):
        if index > 0:
            sys.stdout.write(separator)
        sys.stdout.write(word)
    sys.stdout.write('\n')

def main():
    parser = argparse.ArgumentParser('Generate words of phonemes')
    parser.add_argument('count', type=positive_int, help='Number of words to generate')
    parser.add_argument('length', type=positive_int, nargs='?', help='Length of each word')
    parser.add_argument('--one-line', action='store_true', help='Print all words on a single line')
    args = parser.parse_args()
    if args.length is not None:
        word_length_fn = lambda: args.length
    else:
        word_length_fn = random_word_length
    words = word_generator(word_length_fn)
    words = itertools.islice(words,  args.count)
    if args.one_line:
        print_words(words, separator=' ')
    else:
        print_words(words)

if __name__ == '__main__':
    main()

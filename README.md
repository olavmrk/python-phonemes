phonemes.py
===========

This was a script I wrote to generate strings of phonemes.
It is heavily based on the code in [pwgen](http://sourceforge.net/projects/pwgen/).

Usage
-----

The script takes in two parameters:

```
phonemes.py LENGTH COUNT
```

The first parameter is the word length, while the second is the number of words.
`LENGTH` can be specified as `-`, to generate words of random length.

Examples
--------

Generate 3 words with 5 characters:

```
$ ./phonemes.py 5 3
johng
phush
ohhah
```

Generate 5 words with random length:

```
$ ./phonemes.py - 5
wiesh
aigahvua
xahth
aighush
que
```

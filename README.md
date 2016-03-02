phonemes.py
===========

This was a script I wrote to generate words of phonemes.
It is heavily based on the code in [pwgen](http://sourceforge.net/projects/pwgen/).

Usage
-----

The script takes in two parameters:

```
phonemes.py COUNT [LENGTH]
```

The first parameter is the number of words, while the second is the word length
`LENGTH` is optional.
Leave it off to generate words of random length.

Examples
--------

Generate 3 words with 5 characters:

```
$ ./phonemes.py 3 5
johng
phush
ohhah
```

Generate 5 words with random length:

```
$ ./phonemes.py 5
wiesh
aigahvua
xahth
aighush
que
```

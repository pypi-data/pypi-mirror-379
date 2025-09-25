import os
from random import SystemRandom
import functools
from importlib.resources import files

@functools.lru_cache()
def words():
    f = files("tennyson").joinpath('static/diceware.txt')
    words = f.read_text().splitlines()
    return words

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
punctuation = '.,:;?!*#$^%'

letters = upper + lower
all = upper + lower + numbers + punctuation

def short_password(len):
    rnd = SystemRandom()
    return "".join(rnd.choice(all) for _  in range(len))

def password():
    rnd = SystemRandom()
    return "-".join(rnd.choice(words()) for _  in range(5))

def for_display_passwords():
    rnd = SystemRandom()
    words_ = [rnd.choice(words()) for _ in range(5)]
    chars_ = "".join(rnd.choice(all) for _  in range(20))
    letters_ = "".join(rnd.choice(letters) for _  in range(20))
    numbers_ = "".join(rnd.choice(numbers) for _  in range(20))
    yield "-".join(words_[:4])
    yield "-".join(words_[:5])
    yield " ".join(words_[:5])
    yield ("-".join(words_[:4])) + "-A1"
    yield chars_[:4]
    yield chars_[:8]
    yield chars_[:12]
    yield chars_[:16]
    yield chars_[:20]
    yield numbers_[:8]
    yield numbers_[:12]
    yield numbers_[:16]
    yield numbers_[:20]
    yield letters_[:8]
    yield letters_[:12]
    yield letters_[:16]
    yield letters_[:20]

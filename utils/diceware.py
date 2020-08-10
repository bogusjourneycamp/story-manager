import random

from six.moves import range

from utils.word_list import word_list


def roll_dice(n=5):
    """Rolls a number of dice (default: 5) n times"""
    return "".join([str(random.SystemRandom().randint(1, 6)) for _ in range(5)])


def generate_passphrase(word_count):
    rolls = []
    for i in range(word_count):
        rolls.append(roll_dice())
    # Loop through the list of rolls, looking each up in the wordlist and
    # adding the corresponding word to the passphrase.
    passphrase = ""
    for roll in rolls:
        passphrase += word_list[roll] + " "
    return passphrase.strip()

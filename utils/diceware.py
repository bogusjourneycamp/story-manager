import random

from six.moves import range

from utils.word_list import word_list


def generate_passphrase(word_count):
    rolls = []
    for i in range(word_count):
        #Use systemrandom for more accurate randomness and creates 5 dice rolls
        dice_roll = "".join([str(random.SystemRandom().randint(1, 6)) for _ in range(5)])
        rolls.append(dice_roll)
    # Loop through the list of rolls, looking each up in the wordlist and
    # adding the corresponding word to the passphrase.
    passphrase = ""
    for roll in rolls:
        passphrase += word_list[roll] + " "
    return passphrase.strip()

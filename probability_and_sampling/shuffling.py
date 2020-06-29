import random


class Deck(object):
    def __init__(self, deck):
        self.deck = deck


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Suit:
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4


def shuffle(in_lst):
    l_len = len(in_lst)
    for i in range(l_len - 1, -1, -1):
        get_ran = random.randint(0, i)
        in_lst[i], in_lst[get_ran] = in_lst[get_ran], in_lst[i]
    return in_lst


def shuffle_k(in_lst, k):
    l_len = len(in_lst)
    for i in range(l_len - 1, l_len - k - 1, -1):
        get_ran = random.randint(0, i)
        in_lst[i], in_lst[get_ran] = in_lst[get_ran], in_lst[i]
    return in_lst[-k]


import random


def pick_one_name(names):
    return random.choice(names)


def pick_n_names(names, n):
    return random.sample(names, k=n)

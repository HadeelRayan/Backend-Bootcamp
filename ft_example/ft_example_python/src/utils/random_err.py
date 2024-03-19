import random
def gen_rand_err():
    if random.random()<0.5:
        raise FileExistsError
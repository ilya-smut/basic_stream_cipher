import random

seed = 'Secret Key'

random.seed(seed)

#first = random.randint(1, 10)
#second = random.randint(1, 10)

#state = random.getstate()

plaintext = '0123456789'

def key_gen(plaintext, state):
    length = len(plaintext)
    key = ''
    random.setstate(state)
    for i in range(length):
        key += str(random.randint(0,9))
    return(key, random.getstate())


if __name__ == '__main__':
    seed = 'Secret Key'
    random.seed(seed)
    initial_state = random.getstate()
    plaintext = '0123456789'
    key1, new_state = key_gen(plaintext, initial_state)
    key2, _ = key_gen(plaintext, new_state)
    print(plaintext, key1)
    print(plaintext, key2)
    
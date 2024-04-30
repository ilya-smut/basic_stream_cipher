import random

def state_init(seed):
    # Setting a seed and returning the state of the generator
    random.seed(seed)
    return random.getstate()


def key_gen_bits(plaintext, state):
    # Returns a key in bits of the size of plaintext. Also returns a state of the generator
    length = len(plaintext)
    key = ''
    random.setstate(state)
    for i in range(length):
        key += str(random.randint(0,1))
    return(key, random.getstate())


def string_to_bits(string):
    return ''.join(format(ord(c), '08b') for c in string)


def bits_to_string(bits):
    # Split the bit string into 8-bit chunks
    chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    
    # Convert each 8-bit chunk into its corresponding ASCII character
    chars = [chr(int(chunk, 2)) for chunk in chunks]
    
    # Concatenate all the characters to form the resulting string
    return ''.join(chars)


def xor_bits(bits1, bits2):
    # Ensure both bit strings are of the same length
    if len(bits1) != len(bits2):
        raise ValueError("Bit strings must be of the same length")
    
    # Perform XOR operation bit by bit
    result = ''
    for bit1, bit2 in zip(bits1, bits2):
        result += '1' if bit1 != bit2 else '0'
    
    return result
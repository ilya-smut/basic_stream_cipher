import random
import utils

class StreamCipher:
    def __init__(self, seed):
        self.state = utils.state_init(seed)
        random.setstate(self.state)

    def update(self, new_state):
        self.state = new_state
        random.setstate(self.state)

    def get_state(self):
        return self.state

    def encrypt(self, plaintext):
        bits = utils.string_to_bits(plaintext)
        key, new_state = utils.key_gen_bits(bits, self.state)
        ciphertext = utils.xor_bits(bits, key)
        self.update(new_state)
        return ciphertext, key
    
    def decrypt(self, ciphertext):
        bits = ciphertext
        key, new_state = utils.key_gen_bits(bits, self.state)
        plain_bits = utils.xor_bits(ciphertext, key)
        plaintext = utils.bits_to_string(plain_bits)
        self.update(new_state)
        return plaintext, key
    

if __name__ == '__main__':
    plaintext = 'ILYA SMUT'
    seed = 'SecreT'
    state = utils.state_init(seed)

    a = StreamCipher(seed)
    b = StreamCipher(seed)
    
    print('\n\nAre intial states in sync?', a.get_state() == b.get_state())

    text = 'ILYA SMUT'
    a_cipher, _ = a.encrypt(text)
    print('\nCipher A has performed encryption of Plaintext:', text, '\nCiphertext:', a_cipher)
    print('Are states in sync?', a.get_state() == b.get_state())

    b_plaintext, _ = b.decrypt(a_cipher)
    print('\nCipher B has performed decryption. Decrypted text:', b_plaintext)
    print('Are states in sync?', a.get_state() == b.get_state())

    text = 'I AM COMMUNICATING'
    b_cipher, _ = b.encrypt(text)
    print('\nCipher B has performed encryption:', text, '\nCiphertext:', b_cipher)
    print('Are states in sync?', a.get_state() == b.get_state())

    a_plaintext, _ = a.decrypt(b_cipher)
    print('\nCipher A has performed decryption. Plaintext:', a_plaintext)
    print('Are states in sync?', a.get_state() == b.get_state())
    print()


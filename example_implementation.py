from utils import state_init, key_gen_bits, string_to_bits, bits_to_string, xor_bits


if __name__ == '__main__':

    seed = '110011'
    state = state_init(seed)
    plaintext = 'ILYA SMUT'
    bit_plaintext = string_to_bits(plaintext)
    bit_key, state = key_gen_bits(bit_plaintext, state)
    ciphertext = xor_bits(bit_plaintext, bit_key)
    decrypted_plaintext_bits = xor_bits(ciphertext, bit_key)
    decrypted_plaintext = bits_to_string(decrypted_plaintext_bits) 

    print(
        f'''
        PLAINTEXT:              {plaintext}
        SEED:                   {seed}
        
        PLAINTEXT IN BITS:      {bit_plaintext}
        GENERATED KEY:          {bit_key}
        -------XOR---------------------------------------------------------------------------------------
        CIPHERTEXT:             {ciphertext}
        -------XOR---------------------------------------------------------------------------------------
        DECRYPTED CIPHERTEXT:   {decrypted_plaintext_bits}
        DECRYPTED PLAINTEXT:    {decrypted_plaintext}
        '''
        )
    
import utils
import basic_stream_cipher

if __name__ == '__main__':
    print('\n\nIntialising two streams. One will be used for encryption, another one for decryption.')
    seed = input('Please, enter the seed: ')
    encrypt_stream = basic_stream_cipher.StreamCipher(seed)
    decrypt_stream = basic_stream_cipher.StreamCipher(seed)
    print('Encrypt and Decrypt streams have been initialised.\n')

    message = input('Please, enter the message to encrypt: ')
    print('Are streams in sync?', encrypt_stream.get_state() == decrypt_stream.get_state())

    ciphertext, key = encrypt_stream.encrypt(message)
    print('\nEncryption stream has generated following key based on its state:', key)
    print('Message has been encrypted. State of the encryption stream has been changed.')
    print('Ciphertext:', ciphertext)

    print('\nAre streams in sync?', encrypt_stream.get_state() == decrypt_stream.get_state())

    decrypted_text, key = decrypt_stream.decrypt(ciphertext)
    print('\nDecryption stream has generated following key based on its state:', key)
    print('Decryption stream has decrypted the message. The state has been changed.')
    print('Decrypted text:', decrypted_text)
    print('\nAre streams in sync?', encrypt_stream.get_state() == decrypt_stream.get_state())


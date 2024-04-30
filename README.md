# 🚀 Stream Cipher in Python 🚀

Welcome to my repository! Here, I provide Python code for implementing a basic stream cipher. Presented scripts allow you to understand how a basic stream cipher works.

## 📚 Files Included 📚

Repository contains four incredible files:

1. **`utils.py`**: This is where all the magic happens! It houses various utility functions for the stream cipher. These functions help initialize the generator state, generate a key, convert strings to bits and vice versa, and perform XOR operations on bit strings.
2. **`stream_example_impl.py`**: Want to see the utility functions in action? This file showcases how the functions can be used to implement a basic stream cipher. It includes an example where a plaintext message is encrypted into a ciphertext and then decrypted back into plaintext.
3. **`stream_cipher_interactive.py`**: Get hands-on experience with our interactive file. This script allows you to encrypt and decrypt messages using the stream cipher. It initializes two streams, one for encryption and another for decryption, and checks if they are in sync.
4. **`basic_stream_cipher.py`**: This file is the heart of our repository! It contains a `StreamCipher` class that encapsulates the functionality of the stream cipher. The class includes methods to encrypt and decrypt messages, update the generator state, and get the current state.

## 🎯 Usage 🎯

Ready to dive in? Run the `stream_example_impl.py` or `stream_cipher_interactive.py` scripts. The `stream_example_impl.py` script will automatically encrypt and decrypt a predefined message, while the `stream_cipher_interactive.py` script will prompt you to enter your own message for encryption and decryption. Fancy importing our `StreamCipher` class in `basic_stream_cipher.py` into your Python scripts? Go ahead!

## ⚠️ Note ⚠️

The stream cipher implementation in our repository is purely for educational purposes. Please avoid using it for encrypting sensitive information in real-world applications, as it does not provide a sufficient level of security.

import math
from KeyManipulation import KeyManipulation

class DES:
    def __init__(self, key):
        self.keys = KeyManipulation.generate_key(key)

    def encrypt(self, message):
        #we will convert a message into a binary number
        message = ''.join(format(ord(i), '08b') for i in message)


        #Converting length of array to multiple of 64.
        x = 64*math.ceil(len(message)/64) - len(message)
        message = "0"*x + message

        #Dividing message into 64 bit blocks.
        message_array = KeyManipulation.divide_into_size(message, 64)

        cipher = ""
        for i in message_array:
            ip = KeyManipulation.initial_permutation(i)

            # Feistal Rounds.
            for j in range(16):
                left = ip[:32]
                right = ip[32:]
                ip = right
                expansion = KeyManipulation.expansion_box(right)
                expansion = KeyManipulation.xor(expansion,self.keys[j])
                s_box = KeyManipulation.s_box(expansion)
                right = KeyManipulation.xor(left, s_box)
                ip = ip + right
            # ip = ip[32:] + ip[:32]
            #final Permutaion

            invip = KeyManipulation.inverse_permutation(ip)

            cipher = cipher + invip
        cipher = KeyManipulation.binary_to_text(cipher)
        return cipher


    def decrypt(self, message):
        #we will convert a message into a binary number
        message = ''.join(format(ord(i), '08b') for i in message)

        #Converting length of array to multiple of 64.
        x = 64*math.ceil(len(message)/64) - len(message)
        message = "0"*x + message

        #Dividing message into 64 bit blocks.
        message_array = KeyManipulation.divide_into_size(message, 64)

        plaintext = ""
        for i in message_array:
            ip = KeyManipulation.initial_permutation(i)
            # Feistal Rounds.
            for j in range(16):
                left = ip[:32]
                right = ip[32:]
                ip = left
                expansion = KeyManipulation.expansion_box(left)
                expansion = KeyManipulation.xor(expansion,self.keys[::-1][j])
                s_box = KeyManipulation.s_box(expansion)
                left = KeyManipulation.xor(right, s_box)

                ip = left + ip

            #final Permutaion
            invip = KeyManipulation.inverse_permutation(ip)

            plaintext = plaintext + invip
        plaintext = KeyManipulation.binary_to_text(plaintext)
        return plaintext

if __name__ == "__main__":
    key = "0100010100101000010010000010101101001101011000100101000101100101"   #64 bit key
    cryptography = DES(key)
    message = input("Enter message: ")
    cipher = cryptography.encrypt(message)
    plaintext = cryptography.decrypt(cipher)

    print("Message : ", message)
    print("Key : ", key)
    print("Cipher Message : ",cipher)
    print("Decoded Message : ",plaintext)

    """
    OUTPUT:
        Message :  I AM IRONMAN :)
        Key :  0100010100101000010010000010101101001101011000100101000101100101
        Cipher Message :  Æ♥FWæ@
        u¿ìWdç_
        Decoded Message :  I AM IRONMAN :)

        Message :  Hello, I am jaitej. I am perceiving my BTech in Gitam university.
        Key :  0100010100101000010010000010101101001101011000100101000101100101
        Cipher Message »î°2Ò¤²
        _éJß­ûÞAÕÈÎxPªã    ç3dkEGFÉñ«s☺ß
        Decoded Message :  Hello, I am jaitej. I am perceiving my BTech in Gitam university.

    """
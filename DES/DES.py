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
                expansion = KeyManipulation.expansion_box(right)
                expansion = KeyManipulation.xor(expansion,self.keys[j])
                s_box = KeyManipulation.s_box(expansion)
                right = KeyManipulation.xor(left, s_box)
                left = right
                ip = left + right

            #final Permutaion
            invip = KeyManipulation.inverse_permutation(ip)
            cipher = cipher + invip
        return cipher


    def decrypt(self, message):
        #we will convert a message into a binary number
        # message = ''.join(format(ord(i), '08b') for i in message)

        #Converting length of array to multiple of 64.
        # x = 64*math.ceil(len(message)/64) - len(message)
        # message = "0"*x + message
        # print(len(message))
        #Dividing message into 64 bit blocks.
        message_array = KeyManipulation.divide_into_size(message, 64)

        plaintext = ""
        for i in message_array:
            ip = KeyManipulation.inverse_permutation(i)

            # Feistal Rounds.
            for j in range(16):
                left = ip[:32]
                right = ip[32:]
                expansion = KeyManipulation.expansion_box(right)
                expansion = KeyManipulation.xor(expansion,self.keys[::-1][j])
                s_box = KeyManipulation.s_box(expansion)
                right = KeyManipulation.xor(left, s_box)
                left = right
                ip = left + right

            #final Permutaion
            invip = KeyManipulation.initial_permutation(ip)
            plaintext = plaintext + invip
        return plaintext

key = "0100010100101000010010000010101101001101011000100101000101100101"
a = DES(key)
message = "IamIRonman"
cipher = a.encrypt(message)
print(len(cipher))
# print((cipher))
array = KeyManipulation.divide_into_size(cipher, 8)
for i in array:
    x = int(i, 2)
    print(x)

plaintext = a.decrypt(cipher)
print(plaintext)
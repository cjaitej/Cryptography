import math
from KeyGeneration import KeyGeneration

class DES:
    def __init__(self, key):
        self.key = key
        keys = KeyGeneration.generate_key(self.key)
        # print(len(keys))
        # for i in keys:
            # print(i)

    def encrypt(self, message):
        #we will convert a message into a binary number
        message = ''.join(format(ord(i), '08b') for i in message)

        #Converting length of array to multiple of 64.
        x = 64*math.ceil(80/64) - len(message)
        message = "0"*x + message

        #Dividing message into 64 bit blocks.
        message_array = []
        for i in range(0, len(message), 64):
            message_array.append(message[i:i+64])

        cipher_text = ""


    def decrypt(self, message):
        pass

key = "0100010100101000010010000010101101001101011000100101000101100101"
a = DES(key)
message = "IamGrooooooottttdasd"
a.encrypt(message)

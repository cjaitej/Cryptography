from DES import DES

class TripleDes:
    def __init__(self, key1, key2, key3 = None) -> None:
        self.des1 = DES(key1)
        self.des2 = DES(key2)
        if key3:
            self.des3 = DES(key3)
        else:
            self.des3 = DES(key1)

    def encrypt(self, message):
        temp_cipher = self.des1.encrypt(message)
        temp_cipher = self.des2.decrypt(temp_cipher)
        cipher = self.des3.encrypt(temp_cipher)
        return cipher

    def decrypt(self, cipher):
        temp_plain_text = self.des3.decrypt(cipher)
        temp_plain_text = self.des2.encrypt(temp_plain_text)
        plain_text = self.des1.decrypt(temp_plain_text)
        return plain_text

if __name__ == "__main__":
    key1 = "0111001000110101011101010011100001111000001011110100000100111111"
    key2 = "0100001000111111010001010010100001001000001010110100110101100010"
    cryptography = TripleDes(key1, key2)
    message = "Hello, I am jaitej"
    print("message: ", message)
    print()
    print("Key1: ", key1)
    print("Key2: ", key2)
    print()
    cipher = cryptography.encrypt(message)
    print("Cipher: ", cipher)
    print()
    plain_text = cryptography.decrypt(cipher)
    print("Plain_text: ", plain_text)

    print()
    key1 = "0111001000110101011101010011100001111000001011110100000100111111"
    key2 = "0100001000111111010001010010100001001000001010110100110101100010"
    key3 = "0100000001001101011000110101000101100110010101000110101001010111"
    cryptography = TripleDes(key1, key2, key3)
    message = "Helloooooo!!!! HOW are you ? "
    print("message: ", message)
    print()
    print("Key1: ", key1)
    print("Key2: ", key2)
    print("Key3: ", key3)
    print()
    cipher = cryptography.encrypt(message)
    print("Cipher: ", cipher)
    print()
    plain_text = cryptography.decrypt(cipher)
    print("Plain_text: ", plain_text)

    """
    OUTPUT:
        message:  Hello, I am jaitej

        Key1:  0111001000110101011101010011100001111000001011110100000100111111
        Key2:  0100001000111111010001010010100001001000001010110100110101100010

        Cipher:  Ò
        ÍQt¶º93&j÷¿è↕oB
                       +l☻

        Plain_text:  Hello, I am jaitej



        message:  Helloooooo!!!! HOW are you ?

        Key1:  0111001000110101011101010011100001111000001011110100000100111111
        Key2:  0100001000111111010001010010100001001000001010110100110101100010
        Key3:  0100000001001101011000110101000101100110010101000110101001010111

        Cipher:  ©°Wg☺×ðýô{­!»oZüTÝ7→ØÄM¯µ

        Plain_text:  Helloooooo!!!! HOW are you ?

    """
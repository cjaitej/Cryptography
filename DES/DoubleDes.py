from DES import DES

class DoubleDes:
    def __init__(self, key1, key2) -> None:
        self.des1 = DES(key1)
        self.des2 = DES(key2)

    def encrypt(self, message):
        temp_cipher = self.des1.encrypt(message)
        cipher = self.des2.encrypt(temp_cipher)
        return cipher

    def decrypt(self, cipher):
        temp_plain_text = self.des2.decrypt(cipher)
        plain_text = self.des1.decrypt(temp_plain_text)
        return plain_text

if __name__ == "__main__":
    key1 = "0111001000110101011101010011100001111000001011110100000100111111"
    key2 = "0100001000111111010001010010100001001000001010110100110101100010"
    cryptography = DoubleDes(key1, key2)
    message = "Hello, I am jaitej. I am perceiving my BTech in Gitam university."
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

    """
    OUTPUT:

        message:  Hello, I am jaitej. I am perceiving my BTech in Gitam university.

        Key1:  0111001000110101011101010011100001111000001011110100000100111111
        Key2:  0100001000111111010001010010100001001000001010110100110101100010

        Cipher:  áé9ÙëàûQ
        èC°cÈ¾hïÎ4y
        LÇDÀ*Q►↔O‼¤lr~^Ùë3ïqx)Üôûb+¬g(ej©Úô´8

        Plain_text:  Hello, I am jaitej. I am perceiving my BTech in Gitam university.
    """
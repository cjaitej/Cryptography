import random

class Monoalphabetic_Substitution_Cipher:
    """
    Instead of shifting alphabets by fixed amount as CaeserCipher, randomly characters are shuffled and used as key.
    """
    def __init__(self):
        self.characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.key = self.characters.copy()
        random.shuffle(self.key)

    def encrypt(self, data):
        s = ""
        for i in data:
            if i == " ":
                continue
            i = i.lower()
            index = self.characters.index(i)
            s = s + self.key[index]
        return s

    def decrypt(self, data):
        s = ""
        for i in data:
            if i == " ":
                continue
            i = i.lower()
            index = self.key.index(i)
            s = s + self.characters[index]
        return s


if __name__ == "__main__":
    cryptography = Monoalphabetic_Substitution_Cipher()

    message  = "I am ironman"
    encrypted_message = cryptography.encrypt(message)
    decrypted_message = cryptography.decrypt(encrypted_message)
    print(f"Message = {message} | key = {cryptography.key}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")

    """
    Output:
    Message = I am ironman | key = ['x', 'u', 'j', 'l', 'd', 'v', 'o', 'e', 'k', 'z', 'w', 'n', 'm', 'g', 'r', 'c', 's', 't', 'b', 'p', 'y', 'a', 'i', 'h', 'f', 'q']
    Encrypted message = kxmktrgmxg
    Decrypted message = iamironman
    """
    cryptography2 = Monoalphabetic_Substitution_Cipher()
    message  = "Hello World"
    encrypted_message = cryptography2.encrypt(message)
    decrypted_message = cryptography2.decrypt(encrypted_message)
    print(f"Message = {message} | key = {cryptography.key}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")

    """
    Output:
    Message = Hello World | key = ['c', 'i', 'b', 'j', 's', 'w', 'a', 'd', 'v', 'k', 'm', 'u', 'l', 't', 'p', 'n', 'z', 'y', 'x', 'r', 'h', 'e', 'q', 'g', 'f', 'o']
    Encrypted message = nlssqcqyst
    Decrypted message = helloworld
    """
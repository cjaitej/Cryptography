class CeaserCipher:
    """
    * Ceaser Cipher is one of the simplest Cryptography.
    * It is based on substitution technique, where we replace the character in the message with character using a key.
    * It is a private cryptography where key is known to only sender and receiver.
    """
    def __init__(self, key):
        """
        Defining alphabet table.
        we can use a dictionary which will be representing {key_value: "character"}.
        we can also use a list where the key_value will be reprensented by the index of character.
        """
        self.characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
        self.key = key

    def encrypt(self, data):
        """
        Encrypted_message = (key_value_of_plaintext + key) mod (number_of_characters)
        """
        s = ""
        for i in data:
            i = i.lower()
            index = self.characters.index(i)  #extracting key_value of the respective character.
            s = s + self.characters[(index + self.key)%27]
        return s

    def decrypt(self, data):
        """
        Decrypted_message = (key_value_of_encrypted_message - key) mod (number_of_characters)
        """
        s = ""
        for i in data:
            i = i.lower()
            index = self.characters.index(i) #extracting key_value of the respective character.
            s = s + self.characters[(index - self.key)%27]
        return s

if __name__ == "__main__":

    cryptography = CeaserCipher(key = 5)

    message  = "I am ironman"
    encrypted_message = cryptography.encrypt(message)
    decrypted_message = cryptography.decrypt(encrypted_message)


    print(f"Message = {message} and key = {cryptography.key}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")
import numpy as np

class HillCipher:
    """
    * Hill cipher is substitution cipher.
    * Hill cipher makes use of modulo arithmetic, matrix multiplication, and matrix inverse.
    * It is also a block cipher.
    """
    def __init__(self, key):
        """
        * Converting Key to Key_matrix.
        * Key_matrix must be a square matrix, so the length of the key must be a perfect square which is greater than 2.
            if key = "book", then
                key_matrix = [[1, 14], [14, 10]]

        """
        self.characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.key_matrix = self.generate_key_matrix(key)


    def encrypt(self, message):
        """
        Encryption = (key_matrix x plaintext) mod 26
        """
        message = message.lower()
        message = message.replace(" ", "")
        sub_parts = self.divide_into_sub_parts(message)

        cipher = []
        for i in sub_parts:
            i = i.reshape(2,1)
            x = np.dot(self.key_matrix,i)%26
            for j in x:
                for k in j:
                    cipher.append(self.characters[k])
        return "".join(cipher)

    def decrypt(self, message):
        """
        Decryption = (inverse_of(key_matrix) x Cipher_text) mod 26.
        """
        message = message.lower()
        message = message.replace(" ", "")
        sub_parts = self.divide_into_sub_parts(message)
        det = np.linalg.det(self.key_matrix)//1
        adjoint = np.linalg.inv(self.key_matrix)*det
        inverse = self.modular_multiplicative_inverse(det)
        key = (inverse*adjoint)
        plain_text = []
        for i in sub_parts:
            i = i.reshape(2,1)
            x = np.dot(key, i)
            for j in x:
                for k in j:
                    k = round(k)%26
                    plain_text.append(self.characters[k])
        return "".join(plain_text)

    def modular_multiplicative_inverse(self, n):
        """
        return's modular multiplicative inverce of n.
        """
        for i in range(26):
            if (i*n)%26 == 1:
                return i

    def generate_key_matrix(self, key):
        """
        converts a key_code to key_matrix.
        """
        key_matrix = []
        temp = []
        n = len(key)**(1/2)
        for char in key.lower():
            if len(temp) == n:
                key_matrix.append(temp)
                temp = []
            temp.append(self.characters.index(char))
        key_matrix.append(temp)
        return np.array(key_matrix)

    def divide_into_sub_parts(self,message):
        """
        Divides message into pairs, and returns list of pairs of the message.
        """
        sub_parts = []
        temp = []
        for char in message:
            if len(temp) == self.key_matrix.shape[0]:
                sub_parts.append(temp)
                temp = []
            temp.append(self.characters.index(char))
        while len(temp) != self.key_matrix.shape[0]:
            temp.append(self.characters.index("z"))
        sub_parts.append(temp)
        return np.array(sub_parts)

if __name__ == "__main__":
    cryptography = HillCipher("ddcf")
    print("Key_matrix = ")

    """
    Output:

    Key_matrix =
        [3 3]
        [2 5]
    """

    for i in cryptography.key_matrix:
        print(i)

    message  = "I am ironman"
    encrypted_message = cryptography.encrypt(message)
    decrypted_message = cryptography.decrypt(encrypted_message)

    print(f"Message = {message}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")

    """
    Output:

        Message = I am ironman
        Encrypted message = yqimpaxinn
        Decrypted message = iamironman

    """

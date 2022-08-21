class PlayfairCipher:
    def __init__(self, key):
        """
        Creates a key_matrix using key.
        """
        self.key_matrix = self.generate_key_matrix(key)

    def encrypt(self, data):
        """
        Encryption technique:
            * if both the letter's fall in the same row of the key matrix, replace each with the letter to its right.
            * if both the letter's fall in the same column of the key matrix, replace each with the letter below it.
            * Otherwise each letter is replaced by the one in its row in the column of the other letter.
        """

        data = data.lower() #Converting all the characters in the message to lower case.
        data = data.replace(" ", "")  #removing space (" ") from the message.

        message = self.divide_into_pairs(data)
        encrpted_pairs = []

        for pair in message:
            rows_and_columns = self.find_row_and_column(pair)
            if rows_and_columns[0][0] == rows_and_columns[1][0]:
                """
                If the characters are in the same row, then move right.
                """
                row = rows_and_columns[0][0]
                columns = [(rows_and_columns[0][1] + 1)%5, (rows_and_columns[1][1] + 1)%5]
                cipher = self.key_matrix[row][columns[0]] + self.key_matrix[row][columns[1]]
                encrpted_pairs.append(cipher)

            elif rows_and_columns[0][1] == rows_and_columns[1][1]:
                """
                If the characters are in the same column, then move down.
                """
                column = rows_and_columns[0][1]
                rows = [(rows_and_columns[0][0] + 1)%5, (rows_and_columns[1][0] + 1)%5]
                cipher = self.key_matrix[rows[0]][column] + self.key_matrix[rows[1]][column]
                encrpted_pairs.append(cipher)

            else:
                """
                Otherwise each letter is replaced by the one in its row in the column of the other letter.
                """
                cipher = self.key_matrix[rows_and_columns[0][0]][rows_and_columns[1][1]] + self.key_matrix[rows_and_columns[1][0]][rows_and_columns[0][1]]
                encrpted_pairs.append(cipher)

        return "".join(encrpted_pairs)

    def decrypt(self, data):
        """
        Decryption technique:
            * if both the letter's fall in the same row of the key matrix, replace each with the letter to its left.
            * if both the letter's fall in the same column of the key matrix, replace each with the letter above it.
            * Otherwise each letter is replaced by the one in its row in the column of the other letter.
        """
        data = data.lower()    #Converting all the characters in the message to lower case.
        data.replace(" ", "")   #removing space (" ") from the message.

        message = self.divide_into_pairs(data)
        decrypted_pair = []

        for pair in message:
            rows_and_columns = self.find_row_and_column(pair)
            if rows_and_columns[0][0] == rows_and_columns[1][0]:
                """
                If the characters are in the same row, then move right.
                """
                row = rows_and_columns[0][0]
                columns = [(rows_and_columns[0][1] - 1)%5, (rows_and_columns[1][1] - 1)%5]
                plain_text = self.key_matrix[row][columns[0]] + self.key_matrix[row][columns[1]]
                decrypted_pair.append(plain_text)

            elif rows_and_columns[0][1] == rows_and_columns[1][1]:
                """
                If the characters are in the same column, then move down.
                """
                column = rows_and_columns[0][1]
                rows = [(rows_and_columns[0][0] - 1)%5, (rows_and_columns[1][0] - 1)%5]
                plain_text = self.key_matrix[rows[0]][column] + self.key_matrix[rows[1]][column]
                decrypted_pair.append(plain_text)

            else:
                """
                Otherwise each letter is replaced by the one in its row in the column of the other letter.
                """
                plain_text = self.key_matrix[rows_and_columns[0][0]][rows_and_columns[1][1]] + self.key_matrix[rows_and_columns[1][0]][rows_and_columns[0][1]]
                decrypted_pair.append(plain_text)

        return "".join(decrypted_pair)

    def find_row_and_column(self,message):
        """
        returns list of row and columns of the character pair.
        """
        rows_columns = []
        for character in message:
            if character == "i" or character == "j":
                character = "i"
            for row in range(len(self.key_matrix)):
                if character in self.key_matrix[row]:
                    for coloumn in range(len(self.key_matrix[row])):
                        if self.key_matrix[row][coloumn] == character:
                            rows_columns.append([row, coloumn])
                            break
                    break

        return rows_columns



    def divide_into_pairs(self,message):
        """
        Divides message into pairs, and returns list of pairs of the message.
        """
        message_pairs = []
        temp = ""
        for i in message:
            if len(temp) == 2:
                if temp[0]*2 == temp:
                    temp = temp[0] + "x"
                message_pairs.append(temp)
                temp = ""
            temp = temp + i

        if len(temp) == 1:
            temp = temp + "x"
        message_pairs.append(temp)

        return message_pairs

    def generate_key_matrix(self, key):
        """
        returns a 5x5 key matrix, which will be further used to encrypt and decrypt messages.
        """
        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        visited = []
        key_matrix = []
        temp = []

        #adding character present in key to the key_matrix
        for i in list(key.lower()):
            if len(temp) == 5:
                key_matrix.append(temp)
                temp = []
            if i == "i" or i == "j":
                i = "i"
            if i in visited:
                continue
            temp.append(i)
            visited.append(i)

        #adding the rest of the characters to the key_matrix
        for i in characters:
            if len(temp) == 5:
                key_matrix.append(temp)
                temp = []
            if i == "i" or i == "j":
                i = "i"
            if i in visited:
                continue
            else:
                visited.append(i)
                temp.append(i)
        key_matrix.append(temp)

        return key_matrix

if __name__ == "__main__":
    cryptography = PlayfairCipher("monarchy")

    print("Key_matrix = ")

    for i in cryptography.key_matrix:
        print(i)

    """
    Output:
    Key_matrix =
        ['m', 'o', 'n', 'a', 'r']
        ['c', 'h', 'y', 'b', 'd']
        ['e', 'f', 'g', 'i', 'k']
        ['l', 'p', 'q', 's', 't']
        ['u', 'v', 'w', 'x', 'z']
    """

    message  = "I am ironman"
    encrypted_message = cryptography.encrypt(message)
    decrypted_message = cryptography.decrypt(encrypted_message)

    print(f"\nMessage = {message}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")

    """
    Output:

    Message = I am ironman
    Encrypted message = sbaemnaora
    Decrypted message = iamironman
    """

    message  = "I am groot"
    encrypted_message = cryptography.encrypt(message)
    decrypted_message = cryptography.decrypt(encrypted_message)
    print(f"\nMessage = {message}")
    print(f"Encrypted message = {encrypted_message}")
    print(f"Decrypted message = {decrypted_message}")

    """
    Output:

    Message = I am groot
    Encrypted message = sbnemnrp
    Decrypted message = iamgroot
    """
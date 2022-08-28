from Tables import Table
import math

class KeyManipulation:

    def generate_key(input_key):
        keys = []
        pc1 = KeyManipulation.parity_drop(input_key, "pc1")
        for i in range(1,17):    #Assuming 16 rounds.
            left = pc1[:28]
            right = pc1[28:]
            bits_rotated = Table.shift["bitsrotated"][Table.shift["round"].index(i)]
            left = KeyManipulation.left_shift(left, bits_rotated)
            right = KeyManipulation.right_shift(right, bits_rotated)
            pc1 = left + right
            pc2 = KeyManipulation.parity_drop(pc1, "pc2")
            keys.append(pc2)
        return keys

    def left_shift(key, bits_rotated):
        key = key[bits_rotated:] + key[:bits_rotated]
        return key

    def right_shift(key, bits_rotated):
        key = key[-(bits_rotated): ] + key[:-(bits_rotated)]
        return key

    def initial_permutation(message):
        permuted_message = ""
        ip = Table.IP
        for i in range(len(ip)):
            for j in range(len(ip[i])):
                permuted_message = permuted_message + message[ip[i][j]-1]
        return permuted_message


    def inverse_permutation(message):
        permuted_message = ""
        invip = Table.invIP
        for i in range(len(invip)):
            for j in range(len(invip[i])):
                permuted_message = permuted_message + message[invip[i][j]-1]
        return permuted_message

    def expansion_box(message):
        message_array = KeyManipulation.divide_into_size(message, 4)
        expanded_message = []
        for i in range(len(message_array)):
            if i == len(message_array)-1:
                expanded_message.append(message_array[i-1][-1] + message_array[i] + message_array[0][0])
                return "".join(expanded_message)
            expanded_message.append(message_array[i-1][-1] + message_array[i] + message_array[i+1][0])



    def s_box(message):
        messages = KeyManipulation.divide_into_size(message, 6)
        s_message = []
        for i in range(len(messages)):
            if i == 0:
                box = Table.s1
            elif i == 1:
                box = Table.s2
            elif i == 2:
                box = Table.s3
            elif i == 3:
                box = Table.s4
            elif i == 4:
                box = Table.s5
            elif i == 5:
                box = Table.s6
            elif i == 6:
                box = Table.s7
            elif i == 7:
                box = Table.s8

            row = int(messages[i][0] + messages[i][-1], 2)
            column = int(messages[i][1:-1], 2)
            x = bin(box[row][column])[2:]
            x = "0"*(4*math.ceil(len(x)/4) - len(x)) + x
            s_message.append(x)

        return "".join(s_message)

    def xor(a, b):
        s = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                s = s + "0"
            else:
                s = s + "1"
        return s

    def binary_to_text(binary):
        while binary.startswith("00000000"):
            binary = binary[8:]
        binary = KeyManipulation.divide_into_size(binary, 8)
        text = ""
        for i in binary:
            text = text + chr(int(i, 2))
        return text

    def divide_into_size(message, size):
        message_array = []
        for i in range(0, len(message)-1, size):
            message_array.append(message[i:i+size])
        return message_array

    def parity_drop(input_key, type):
        key = ""
        if type == "pc1":
            pc = Table.PC_1
            for i in range(len(pc)):
                for j in range(len(pc[i])):
                    key = key + input_key[pc[i][j]-1]
        elif type == "pc2":
            pc = Table.PC_2
            for i in range(len(pc)):
                for j in range(len(pc[i])):
                    key = key + input_key[pc[i][j]-1]
        return key


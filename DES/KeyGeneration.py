from Tables import Table

class KeyGeneration:

    def generate_key(input_key):
        keys = []
        pc1 = KeyGeneration.parity_drop(input_key, "pc1")
        for i in range(1,17):    #Assuming 16 rounds.
            left = pc1[:28]
            right = pc1[28:]
            bits_rotated = Table.shift["bitsrotated"][Table.shift["round"].index(i)]
            left = KeyGeneration.left_shift(left, bits_rotated)
            right = KeyGeneration.right_shift(right, bits_rotated)
            pc1 = left + right
            pc2 = KeyGeneration.parity_drop(pc1, "pc2")
            keys.append(pc1)
        return keys

    def left_shift(key, bits_rotated):
        key = key[bits_rotated:] + key[:bits_rotated]
        return key

    def right_shift(key, bits_rotated):
        key = key[-(bits_rotated): ] + key[:-(bits_rotated)]
        return key

    def parity_drop(input_key, type):
        key = ""
        if type == "pc1":
            pc = Table.PC_1
            for i in range(len(pc)):
                for j in range(len(pc[i])):
                    key = key + (input_key[pc[i][j]-1])
        elif type == "pc2":
            pc = Table.PC_2
            for i in range(len(pc)):
                for j in range(len(pc[i])):
                    key = key + (input_key[pc[i][j]-1])
        return key


import numpy as np

class desplazamiento:
    def __init__(self, data, k):
        self.data = data
        self.k = k

    def encrypt(self):
        num_data = np.array([ord(c)-97 for c in self.data])
        data_encryption = (num_data + self.k) % 26
        encryption = [chr(c+97) for c in data_encryption]
        return ''.join(encryption)

    def desencrypt(self):
        num_data = np.array([ord(c)-97 for c in self.data])
        data_decryption = (num_data - self.k) % 26
        decryption = [chr(c+97) for c in data_decryption]
        return ''.join(decryption)

    def cryptanalysis(self):
        possible_words = []
        for i in range(26):
            self.k = i
            possible_words.append(self.desencrypt())
        return possible_words
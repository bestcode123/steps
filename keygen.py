class Keygen:
    def __init__(self, keylim):
        self.keylim = keylim
    def gen_key(self):
        from random import randint
        random_numbers = []
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x',
                    'y', 'z', 1, 2, 3, 4, 5 ,6 , 7, 8, 9, 0]
        key_array = []

        key = ''
        for i in range(self.keylim):
            random_numbers.append(randint(0, len(alphabet) - 1))
        for n in random_numbers:
            key_array.append(alphabet[n])
        for k in key_array:
            key = key + str(k)
        return key
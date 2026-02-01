class Cipher:

    def __init__(self, word):
        self.abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        format_word = list(word.upper())
        self.abc_mod = format_word + [item for item in self.abecedario if item not in format_word]

    def encode(self, data):
        
        data = list(data.upper())
        crypto_word = ""
        for letter in data:
            if letter in self.abecedario:
                index = (self.abecedario.index(letter))
                crypto_word += self.abc_mod[index]
            else:
                crypto_word += letter

        return crypto_word.capitalize()

    def decode(self, data):
        data = list(data.upper())
        not_crypto_word = ""
        for letter in data:
            if letter in self.abc_mod:
                index = (self.abc_mod.index(letter))
                not_crypto_word += self.abecedario[index]
            else:
                not_crypto_word += letter

        return not_crypto_word.capitalize()


#
cipher = Cipher("crypto")
cipher.encode("Hello world")
# "Btggj vjmgp"
#
cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
#
# mplement the keyword encoding and decoding for the Latin alphabet.
# The keyword cipher uses a keyword to rearrange the letters in the alphabet. You should add the provided keyword at the
# beginning of the alphabet.
# A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet.
# The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
# until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
# excluding those already used in the key.
#
# Encryption:

# The keyword is "Crypto"
#
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
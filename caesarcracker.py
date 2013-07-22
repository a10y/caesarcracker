import re

class CaesarCracker:
    
    def __init__(self):
        self.letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def load_wordlist(self, wordlist_file):
        """
        Load a system wordlist file, and associate it 
        with this instance of CaesarCracker.
        """
        try:
            wordlist = []
            words_file = open(wordlist_file, "r").read()
            for line in words_file.split("\n"):
                wordlist.append( line.strip().lower() )  #input all the lowercased-versions of the words
        except:
            print ("Could not load " + wordlist_file + ", does it exist?")
        finally:
            print ("Successfully loaded " + str(len(wordlist)) + " from " + wordlist_file)
            self.wordlist = wordlist
            
    def do_cipher_shift(self, original_text, shift):
        #Strip punctuation from the text so that we don't lose possible dictionary matches.
        #original_text = re.sub(r'[^A-Z|^a-z|\s]', r'', original_text)
        shifted_text = ""
        for word in original_text.split(" "):
            for letter in word:
                if letter in self.letters_upper:
                    idx = self.letters_upper.index(letter)
                    letter = self.letters_upper[ (idx + shift) % len(self.letters_upper) ]

                elif letter in self.letters_lower:
                    idx = self.letters_lower.index(letter)
                    letter = self.letters_lower[ (idx + shift) % len(self.letters_lower) ]

                shifted_text += letter
            shifted_text += " "
        return shifted_text

    def check_percentage_words(self, text):
        #If we are given an empty string, return 0.0% match
        if not text:
            return 0.0
        """
        Computes the percentage of all space-delimited
        words are words contained in the 
        """
        wordcount = 0
        hits = 0
        #Lowercase all the words in the string for direct comparison to the wordlist
        for word in [w.lower() for w in text.split(" ")]:
            char_only_word = "" #Only count words, not numbers. Also ignores punctuation.
            for letter in word:
                if letter in self.letters_lower:
                    char_only_word += letter
            if char_only_word:
                wordcount += 1
                if char_only_word in self.wordlist:
                    hits += 1
        #If we don't have any characters, then this is not a Caesar Cipher. Return 0%.
        if wordcount <= 0:
            return 0.0
        #Else, return the percentage of letter-containing words that are hits in the dictionary
        return float(hits) / wordcount

    def crack(self, ciphertext):
        """
        Crack the cipher!
        """
        shift_percentage_dict = {}
        attempts = 26
        for shift_amount in range(attempts):
            shifted_text = self.do_cipher_shift(ciphertext, shift_amount)
            shift_percentage_dict[shift_amount] = self.check_percentage_words(shifted_text)
            
        best_shift = 0
        for shift in shift_percentage_dict.keys():
            if shift_percentage_dict[shift] > shift_percentage_dict[best_shift]:
                best_shift = shift
        return self.do_cipher_shift(ciphertext, best_shift)

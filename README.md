caesarcracker: A Python class for cracking Caesar ciphers
==========================================================

![Alt text](screenshot.png "Screenshot")


caesarcracker is a Python library for statistical cracking of Caesar ciphertext. It goes through all 26 possible shifts of the ciphertext, and determines which shift leads to the highest percentage occurence of words that exist in the wordlist. Searches through the wordlist are case-insensitive.

Note: This is not quite a "pure" Caesar Cipher, as it allows for punctuation and numbers.

Starting
--------
Ciphering begins with instantiation of the CaesarCracker class.

```
import caesarcracker
cc = caesarcracker.CaesarCracker()
cc.load_wordlist("/usr/share/dict/words")
cc.do_cipher_shift('Hello, World!', 10)
```
The above code instantiates a new CaesarCracker, loads in the system wordlist (this is the wordlist file on my system and for most Unix systems. Do some investigating if the wordlist fails to load on your computer) and does a Caesar shift of size 10. Shifts and cracks in caesarcracker preserve case as well as punctuation, but of course they word for simple Caesar Ciphers as well:

```
>>> cc.crack('O cgtz zu skkz cozn eua. Juctyzgoxy. Iusk Grutk!') #complex cipher
'I want to meet with you. Downstairs. Come Alone!'

>>> cc.crack('SKKZ GZ ZCKRBK') #Classic Caesar Cipher
'MEET AT TWELVE'
```
Current Methods
---------------
**cc.do_cipher_shift(string, num)**: Do an alphabet shift of **num**.

**cc.load_wordlist(wordlist_file)**: Needs to be called before any percentage checking is done. Loads a wordlist file into memory and uses it to match possible plaintext words against.

**cc.check_percentage_words(plaintext)**: Checks the available space-delimited letter groups in the plaintext. Based on the total number of these words, it computes what percentage of words in the text are valid words. This function is used in **cc.crack()** to determine which of the 26 possible shifts leads to the highest percentage of English words in the plaintext.

**cc.crack(ciphertext)**: Crack a Caesar Cipher ciphertext!
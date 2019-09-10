"""
Author: John Rivera

Purpose: Decipher text inputted by the user and calculate the difference in length between the two texts. Then encrypt text inputed by the user and calculate the difference in length between the two texts.  
"""

def encrypt(word):
    word = word.replace(' a','rxr')
    word = word.replace('he','vw')
    word = word.replace('e', 'az az')
    word = word.replace('y', 'eie')
    word = word.replace('u', 'yyy')
    word = word.replace('an', 'uq')
    word = word.replace('th', 'aige')
    word = word.replace('o', 'tzzt')
    return word

def decrypt(word):
    word = word.replace('tzzt', 'o')
    word = word.replace('aige', 'th')
    word = word.replace('uq', 'an')
    word = word.replace('yyy', 'u')
    word = word.replace('eie', 'y')
    word = word.replace('az az', 'e')
    word = word.replace('vw', 'he')
    word = word.replace('rxr', ' a')
    return word

cipher_text = raw_input('Enter cipher text ==> ')
print cipher_text + '\n'

print 'Deciphered as ==>', decrypt(cipher_text)
print 'Difference in length ==> %d\n' %(len(cipher_text)-len(decrypt(cipher_text)))

reg_text = raw_input('Enter regular text ==> ')
print reg_text + '\n'

print 'Encrypted as ==>', encrypt(reg_text)
print 'Difference in length ==>', len(encrypt(reg_text))-len(reg_text)

"""Author: John Rivera riverj5@rpi.edu

   Purpose: This program reads a word from user input and prints whether
   the word is at least 8 characters long, starts with a vowel, 
   alternates vowels and consonants and the consonants are in 
   increasing alphabetical order.

"""

######### Put all your function definitions here
######### I am putting in a template to get you started

def is_alternating(word):
    vowels = ['a','e','i','o','u']
    i = 0
    ## Tests length of word
    if len(word)>=8:
        ## Tests whether word starts with vowel
        if word[0] in vowels:
            while i <= (len(word) - 1):
                ## Tests if index is even number, if it is, letter must be a vowel
                if i%2==0:
                    if word[i] in vowels:
                        i+=1
                    else:
                        return False
                ## Tests if index is odd number. If it is, it must be consonant greater than the previous consonant
                elif i%2 != 0:
                    if i != 1 and not word[i]>word[i-2]:
                        return False
                    if word[i] not in vowels:
                        i+=1
                    else:
                        return False
                if i >= (len(word)):
                    return True                
        else: 
            return False
    else:
        return False


######## This is the main body of your program
######## All code should be below the if statement

######## This if statement is executed when we run the program
######## but not when we import it as a module

#######  Keep the body of your program small, put main
#######  functions in a function, but each function should do
#######  something simple

if __name__ == "__main__":
    word = raw_input("Enter a word => ")
    print word
    word = word.lower()
    if is_alternating(word):
        print "The word '%s' is alternating" %(word)
    else:
        print "The word '%s' is not alternating" %(word)
    

    ## now call your function here and check its output

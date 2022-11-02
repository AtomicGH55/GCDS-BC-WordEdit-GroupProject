'''
Created on Oct 26, 2022

@author: DDrackett25
'''

def righmost(word_input, letter_length):
                            #circulating the rightmost x or LL1 number of letters to the right
    LL1 = letter_length     #the number of characters to move
    running_str = word_input[-LL1:] + word_input[:-LL1] #taking the word, and taking out part of the word, and then putting it back in 
    return running_str      #returning the "mixed" word
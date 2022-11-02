'''
Created on Oct 26, 2022

@author: DDrackett25
'''

def LeftCirc(word_input, letter_length): 
                            #the same thing as right circulation, but it is the opposite
    LL2 = letter_length
    running_str = word_input[LL2:] + word_input[:LL2]
    return running_str  
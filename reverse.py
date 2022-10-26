'''

@author: BShefter25

Created on Oct 10, 2022
Updated on Oct 11, 2022
Updated on Oct 18, 2022

Bugs: 

Description: Reverses the order of the characters starting at 
             position s with a length of l

'''

choice_input = 0
full_word = 0
character = 0


def main():    
    
    full_word = input("Enter The Word(s) ").lower()                             #asking user for input
    choice_input = full_word                                                    #setting choice = to full_words
    
    first = int(input("What Place In The Input Do You Want To Start At? "))     #asking user for start letter
    final = int(input("What Place In The Input Do You Want To End At? "))       #asking user for the end letter
    
    bensvariable = choice_input[first:final]                                    #setting bens variable = choice_input
    output = ''                                                                 #output = space
    for i in range(len(bensvariable)-1,-1,-1):                                  #reversing the output
        output = output + bensvariable[i]                                       #output = variable + output
    
    character = len(full_word)                                                  #finding how many characters there are in the word
    slice_obj1 = slice(0, first)                                                #slicing the 0 letter to the starting user input
    slice_obj2 = slice(first, final)                                            #slicing the user input start and the user input end
    slice_obj3 = slice(final, character)                                        #slicing the final user input to the last character in the string
    
    beginning = full_word[slice_obj1]                                            #setting the beginning of the word equal to the first slice
    middle = full_word[slice_obj2]                                              #setting the middle of the word equal to the second slice
    ending = full_word[slice_obj3]                                              #setting the end of the word equal to the third slide
    
    for i in range(len(middle)-1,-1,-1):                                        #reversing the output
        output_1 = output + middle[i]                                           #setting output equal to the middle plus initial output
    output_1 = beginning + output + ending                                       #adding the revered output to the beginning and end output
    print("Your New Word Is", output_1)                                         #printing out the final output
    
    
   
if __name__ == '__main__':
    main()
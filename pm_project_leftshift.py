'''
Created on Oct 26, 2022

@author: jsaidi24
'''



def LeftShift(amount, string):  # these are the variables im using, but the PM will make it so they work for the main 
    
    shifted = ''  # this is to show the string 
    shifted = string[:-amount]
    
    amount_of_hashtags = (len(string) - len(shifted)) * "#"
    shifted = amount_of_hashtags + shifted
    
    
    return shifted # the final result that we want 
 
def main():
    print(LeftShift("somethingelse",5))
    




if __name__ == '__main__':
    main()
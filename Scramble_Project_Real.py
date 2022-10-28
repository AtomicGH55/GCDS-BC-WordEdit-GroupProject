'''
Created on Oct 18, 2022

@author: BCalhoun24
'''
import RightCirc
import LeftCirc                                                                                     #Brings in functions
import reverse

def main():
    
    data_loop = True                                                                                #sets variable for loop later
    counter = 0
    
    print('LS = LeftShift')
    print('RS = RightShift')
    print('LC = LeftCirc')
    print('RC = RightCirc')
    print('LC = LeftCirc')
    print('REV = Reverse')
    print('MC = ChaosWord')
    
    while data_loop == True:                                                                        #Asks for data input
        try:
            
            data_input = input('Input data here(Function-integer/word form): ')
            
        except ValueError:
            print('Input data in proper orientation.')
            continue
        
        data_split = data_input.split("/")                                                          #Begins seperation of full data input into list
        
        variable_count = len(data_split)                                                            #Finds length of new list
        
        running_str = data_split[variable_count-1]                                                  #Finds what the word/string being scrambled is
        
        while counter < variable_count - 1:                                                         #Begins loop
            
            function_split = data_split[counter].split("-")
            
            if function_split[0] == (LS):
                
                running_str = LeftShift(running_str , function_split[1])
                
            elif function_split[0] == (RS):
                
                running_str = RightShift(running_str , function_split[1])
                
            elif function_split[0] == (LC):
                
                running_str = LeftCirc(running_str , function_split[1])
                
            elif function_split[0] == 'RC':
                
                running_str = RightCirc(running_str , function_split[1])
                
            elif function_split[0] == 'REV':
                
                scramble_split = list(function_split[1])
                
                running_str = Reverse(running_str , scramble_split[0] , scramble_split[1])
                
            elif function_split[0] == 'MC':
                
                scramble_split = list(function_split[1])
                
                running_str = ChaosWord(running_str , scramble_split[0] , scramble_split[1] , scramble_split[2] , scramble_split[3])
                
            else:
                print("DATA INPUT ERROR")
                return                                                                              #Fail safe for data issues

            data_loop = False
            
            counter = counter + 1
    
    print(running_str)
            
       
if __name__ == '__main__':
    main()
'''
Created on Oct 18, 2022

@author: BCalhoun24
'''
import RightCirc
import get_chaos_word
import LeftCirc                                                                                     #Brings in functions
import reverse
import pm_project_leftshift
import PM_project

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
            
            if function_split[0] == 'RS':
                
                function_split1 = int(function_split[1])

                running_str = pm_project_leftshift.LeftShift(running_str , function_split1)
                
            elif function_split[0] == 'LS':
                
                function_split1 = int(function_split[1])

                running_str = PM_project.RightShift(running_str , function_split1)
                
            elif function_split[0] == 'LC':
                
                function_split1 = int(function_split[1])

                running_str = LeftCirc.LeftCirc(running_str , function_split1)
                
            elif function_split[0] == 'RC':
                
                function_split1 = int(function_split[1])

                running_str = RightCirc.righmost(running_str , function_split1)
                
            elif function_split[0] == 'REV':
                
                scramble_split = list(function_split[1])

                scramble_split0 = int(scramble_split[0])
                scramble_split1 = int(scramble_split[1])
                
                running_str = reverse.reverse(running_str , scramble_split0 , scramble_split1)
                
            elif function_split[0] == 'MC':
                
                scramble_split = list(function_split[1])
                
                scramble_split0 = int(scramble_split[0])
                scramble_split1 = int(scramble_split[1])
                scramble_split2 = int(scramble_split[2])
                scramble_split3 = scramble_split[3]

                running_str = get_chaos_word.get_chaos_word(running_str , scramble_split0 , scramble_split1 , scramble_split2 , scramble_split3)
                
            else:
                print("DATA INPUT ERROR")
                return                                                                              #Fail safe for data issues

            data_loop = False
            
            counter = counter + 1
    
    print(running_str)
            
       
if __name__ == '__main__':
    main()
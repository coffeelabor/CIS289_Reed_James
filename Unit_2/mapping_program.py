'''
/***************************************************************
* Name: mapping program
* Author: Reed James
* Created: 6 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: program that uses map and lambda
*               Input: Ozymandias by shelley 
*               Output: various output conditions
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''

def length_of_each_string(stringParam):
    return [stringParam, len(stringParam)]

def greater_than_ten_items(listParam):
    lambda_output = list(filter(lambda param: len(param)> 9, listParam))
    return lambda_output

def output_length_of_string(listParam):
    for i in listParam:
        print(len(i), end=" ")
    
if __name__ == "__main__":

    single_string = "iCantThinkOfAWord"

    word_list = ["I met a", "traveller", "from an antique", "land, Who", "said—Two vast and trunkless", "legs of stone", "Stand in the desert....Near", "them, on", "the sand,", "Half", "sunk a shattered visage lies"]

    string_output = length_of_each_string(single_string) 

    lambda_output = greater_than_ten_items(word_list)
    
    map_output = map(length_of_each_string, word_list)
    
    print("OUTPUT 1")
    print(string_output)
    print("\nOUTPUT 2")
    print(list(lambda_output))
    print("\nOUTPUT 3")
    print(list(map_output))
    print("\nOUTPUT 4")
    output_length_of_string(word_list)

'''
/***************************************************************
* Name: File I/O and Analysis Program
* Author: Reed James
* Created: 15 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: program that looks at files
*               Input: Moby dick, Sense and Sensibility
*               Output: Word analysis
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''
import re

def regex_helper(w_to_search,in_line):
    clean_line = re.sub(r'[^\w\s]', '', in_line)
    result = len(re.findall(f"\s{w_to_search}\s", clean_line, flags=re.IGNORECASE))
    return result

def search_helper(w_to_search, in_file):
    count = 0
    for line in in_file:
        if(regex_helper(w_to_search, line) == 0):
            continue
        else:
            count = count + regex_helper(w_to_search, line)
    return count

def find_word_old(in_file):
    word = 'old'
    result = search_helper(word, in_file)
    print(f'The word "{word}" appears {result} times')


def find_word_water(in_file):
    word = 'water'
    result = search_helper(word, in_file)
    print(f'The word "{word}" appears {result} times')



def find_average_sentence_length(in_file):
    # clean_file = re.sub(r'[^\w\s]', '', in_file)
    # split_file = clean_file.split('.')
    # split_file = in_file.split('.')
    # print('test', split_file)
    pass



if __name__ == "__main__":
    with open('Moby_Dick_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
        print("OUTPUT 1 Moby Dick")
        find_word_old(input_file)
    with open('Moby_Dick_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
        print("\nOUTPUT 2 Moby Dick")
        find_word_water(input_file)
    with open('Moby_Dick_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
        print("\nOUTPUT 3 Moby Dick")
        # find_average_sentence_length(input_file)
    with open('Sense_and_Sensibility_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
        print("\nOUTPUT 4 Sense and Sensibility")
        find_word_old(input_file)
    with open('Sense_and_Sensibility_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
        print("\nOUTPUT 5 Sense and Sensibility")
        find_word_water(input_file)

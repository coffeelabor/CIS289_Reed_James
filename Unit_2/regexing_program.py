'''
/***************************************************************
* Name: regexing program
* Author: Reed James
* Created: 6 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: program that uses regex on a phrase
*               Input: dune quote
*               Output: various search results
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''
import re

def find_num_of_words_with_letter(phraseParam):
    result = len(re.findall("f", phraseParam, flags=re.IGNORECASE))
    return result

def find_num_of_words_begin_with_letter(phraseParam):
    result = len(re.findall("\sf", phraseParam, flags=re.IGNORECASE))
    return result

def find_num_of_times_word_appears(phraseParam):
    result = len(re.findall("\snot\s", phraseParam, flags=re.IGNORECASE))
    return result

def update_passage(phraseParam):
    new_string_passage_1 = re.sub("I", "You", phraseParam)
    new_string_passage_2 = re.sub("my", "your", new_string_passage_1)
    new_string_passage_3 = re.sub("me", "you", new_string_passage_2)
    return new_string_passage_3

if __name__ == "__main__":
    string_passage = "“I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune"

    print("OUTPUT 1")
    print(find_num_of_words_with_letter(string_passage))
    print("\nOUTPUT 2")
    print(find_num_of_words_begin_with_letter(string_passage))
    print("\nOUTPUT 3")
    print(find_num_of_times_word_appears(string_passage))
    print("\nOUTPUT 4")
    print(update_passage(string_passage))

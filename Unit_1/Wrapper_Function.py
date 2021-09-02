'''
/***************************************************************
* Name: Wrapper Function
* Author: Reed James
* Created: 1 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: Program that uses decorator functions
*               Input:  two numbers
*               Output: one number
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''

def decorator_func(func):
    def mulitply_params(num1, num2):
        times2 = num1*2
        times3 = num2*3
        return func(times2, times3)

    return mulitply_params

@decorator_func
def divide_function(num1, num2):
    answer = int(num1/num2)
    return answer

if __name__ == "__main__":
    dec_answer = divide_function(36, 4)
    print(dec_answer)
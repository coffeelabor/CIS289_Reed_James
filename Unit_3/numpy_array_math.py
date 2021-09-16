'''
/***************************************************************
* Name: NumPy Array Math Program
* Author: Reed James
* Created: 15 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: program that looks at numpy arrays
*               Input: two 2d arrays
*               Output: different properties of each array
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''
import numpy as np

def print_arr(arr):
    print('Array: \n',arr)

def print_shape(arr):
    print('Shape: \n', arr.shape)

def print_two_by_two(arr):
    result = arr[0:2, 0:2]
    print('Two x Two \n', result)

def print_bool_value(arr):
    result = np.where(arr % 2 == 0, True, np.where((arr+1) % 2 == 0, False, 'Decimal'))
    print('Bool Val: \n', result)

def sum_elementwise(arr1, arr2):
    result = np.add(arr1, arr2)
    print('Summed: \n', result)

def multipy_elementwise(arr1, arr2):
    result = np.multiply(arr1, arr2)
    print('Multiplied: \n', result)

def print_sum_elements(arr):
    print('Sum of Elements: \n\t', arr.sum())

def print_product_elements(arr):
    print('Product of Elements: \n\t', arr.prod())

def print_max_min(arr):
    print(f'Max and Min\n\tMax: {arr.max()}\n\tMin: {arr.min()}')

if __name__ == "__main__":
    arr_1 = np.array([[10,15,20],[2,3,4],[9,14.5,18]])
    arr_2 = np.array([[1,2,5],[8,0,12],[11,3,22]])

    print_arr(arr_1)
    print_shape(arr_1)
    print_two_by_two(arr_1)
    print_bool_value(arr_1)
    sum_elementwise(arr_1,arr_2)
    multipy_elementwise(arr_1, arr_2)
    print_sum_elements(arr_2)
    print_product_elements(arr_2)
    print_max_min(arr_2)
'''
/***************************************************************
* Name: Insurance Quote Assignment
* Author: Reed James
* Created: 1 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: Program to give user insurance costs
*               Input:  Driver Name, driver age, desired coverage
*               Output: annual insurance cost
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''


def getDriverName():
    while True:
        try:
            driver_name = str(input("Please enter your name: "))
            if(driver_name.isalpha()):
                print('Thank you for the name')
            else:
                print("Please enter you name using letters")
                raise ValueError
            return driver_name
        except ValueError:
            print(TypeError)

def getDriverAge():
    while True:
        try:
            driver_age = int(input("Please enter your age (numbers only): "))
            if(driver_age > 15):
                print('Thank you for the age')
                return driver_age
            else:
                print('Age must be greater than 16')
                raise ValueError
        except ValueError:
            print(ValueError)

def getDesiredCoverage():
    while True:
        try:
            desired_coverage_level = input("Please enter your desired coverage lever.  Choose from: SM, L, F: ")
            if(desired_coverage_level.lower() == 'sm'):
                print('Thank you for the coverage input')
                return 0
            elif(desired_coverage_level.lower() == 'l'):
                print('Thank you for the coverage input')
                return 1
            elif(desired_coverage_level.lower() == 'f'):
                print('Thank you for the coverage input')
                return 2
            else:
                print('Must choose either SM, L, of F')
                raise ValueError
        except ValueError:
            print(ValueError)

def findCoverageAmount(info):
    age_16 = [2593, 2957, 6930]
    age_25 = [608, 691, 1745]
    age_35 = [552, 627, 1564]
    age_45 = [525, 596, 1469]
    age_55 = [494, 560, 1363]
    age_65 = [515, 585, 1402]
    if(info[1] < 25):
        return age_16[info[2]]
    elif(info[1] < 35):
        return age_25[info[2]]
    elif(info[1] < 45):
        return age_35[info[2]]
    elif(info[1] < 55):
        return age_45[info[2]]
    elif(info[1] < 65):
        return age_55[info[2]]
    elif(info[1] >= 65):
        return age_65[info[2]]
    else:
        print('Error')
        return -1

def getAccidentInfo(amount):
    while True:
        try:
            answer = str(input('Have you ever been in a car accident? please enter yes or no: '))
            if(answer[0].lower() == 'y'):
                amount = amount + (amount*.41)
                return amount
            elif(answer[0].lower() == 'n'):
                return amount
            else:
                raise ValueError
        except ValueError:
            print(ValueError)


if __name__ == "__main__":
    
    driver_name = getDriverName()
    driver_age = getDriverAge()
    desired_coverage_level = getDesiredCoverage()

    driver_info = [driver_name, driver_age, desired_coverage_level]
    
    coverage_amount = findCoverageAmount(driver_info)
    accident_info = getAccidentInfo(coverage_amount)
    
    driver_info = {'ID': 1, 'name': driver_name, 'age': driver_age, 'level': desired_coverage_level, 'subamount': coverage_amount, 'total amount': accident_info}
    
    for k, v in driver_info.items():
        print(k, ':', v)
    

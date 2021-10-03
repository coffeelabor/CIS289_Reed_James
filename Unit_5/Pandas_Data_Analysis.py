'''
/***************************************************************
* Name: 
* Author: Reed James
* Created: 29 Sept 2021
* Course: CIS 289 - Python
* Version: Python 3.8.2
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: 
*               Input: 
*               Output: 
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''
import pandas as pd


def Print_Data_Info(dataInput, step):
    print(f'\n******************* STEP {step} *************************')
    print(dataInput.shape)
    print(dataInput.head())
    print(list(dataInput.columns))
    print(f'******************* END STEP {step} ***********************')

def Create_Dataframe_Pos_50_To_Delete(dataInput):
    sum_pub = dataInput.groupby(by=['publisher']).sum()
    sort_sum_pub = sum_pub.sort_values('positive_ratings', ascending=False)
    rows_to_delete = sort_sum_pub[sort_sum_pub['positive_ratings'] < 50].index
    data_rows_to_delete = (list(rows_to_delete))
    return data_rows_to_delete

def Create_Dataframe_At_Least_Pos_50(dataInput, dataToDelete):
    cleaned_dataframe = dataInput[dataInput.publisher.isin(
        dataToDelete) == False]
    return cleaned_dataframe

def Sort_New_Dataframe(dataInput):
    sorted_dataframe = dataInput.sort_values(
        'positive_ratings', ascending=False)
    return sorted_dataframe

def Remove_Less_Than_20000_Owners(dataInput):

    rows_to_delete = dataInput[dataInput['owners'] == '0-20000'].index
    list_rows_to_delete = list(rows_to_delete)
    print(list_rows_to_delete[0:10])
    cleaned_dataframe = dataInput.drop(list_rows_to_delete)
    return cleaned_dataframe

if __name__ == "__main__":

    # sg === steam games
    sg_all = pd.read_csv('steam.csv', index_col='appid')
    bad_publishers = Create_Dataframe_Pos_50_To_Delete(sg_all)
    good_publishers = Create_Dataframe_At_Least_Pos_50(sg_all, bad_publishers)
    sorted_ratings = Sort_New_Dataframe(good_publishers)
    removed_owners = Remove_Less_Than_20000_Owners(sorted_ratings)

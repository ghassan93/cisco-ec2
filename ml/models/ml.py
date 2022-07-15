# Import Libraries:
from copy import copy
from ml.models.module import System_one, System_three, System_two, tokenize, Google_Names
import numpy as np
import pandas as pd

InputName_SystemOne = []
CiscoName = []
CustomersReselt_SystemOne = []
AccuracyRecelt_SystmOne = []
InputName_SystemTwo = []
GoogleName = []
CustomersReselt_SystemTwo = []
AccuracyRecelt_SystemTwo = []
NewNameList = []
CustomersReselt_SystemThree = []
InputName_SystemThree = []
AccuracyRecelt_SystmThree = []
Output = []
data = []




def insert_sys1(cisconame):

    df = pd.read_csv("ml/data/savant_data.csv")
    df['customer_tokenized'] = df['Active customers'].apply(
    lambda x: tokenize(x.lower()))




    CiscoCustomerName = cisconame
    
    if len(CiscoCustomerName) <= 100:
        for i in CiscoCustomerName:
            short_list_sorted, similarity_scores_u = System_one(i)
            for index, item in enumerate(short_list_sorted):
                if item != 0:
                    search = np.where(similarity_scores_u == item)
                    name = df['Active customers'][search[0]]
                    nameToAppend1 = name.values[0]
                    InputName_SystemOne.append(nameToAppend1)
                else:
                    sms = 'NO Similarity'
                    InputName_SystemOne.append(sms)
            CiscoName.append([i])
            CustomersReselt_SystemOne.append(InputName_SystemOne[:3])
            AccuracyRecelt_SystmOne.append(short_list_sorted)
            InputName_SystemOne.clear()
            try:
                GoogleNameRecoummend = Google_Names(i)
                x2 = GoogleNameRecoummend
                short_list_sorted, similarity_scores_u = System_two(x2)
                for index, item in enumerate(short_list_sorted):
                    if item != 0:
                        search = np.where(similarity_scores_u == item)
                        name = df['Active customers'][search[0]]
                        nameToAppend2 = name.values[0]
                        InputName_SystemTwo.append(nameToAppend2)
                    else:
                        sms = 'NO Similarity'
                        InputName_SystemTwo.append(sms)
                GoogleName.append([x2])
                CustomersReselt_SystemTwo.append(InputName_SystemTwo[:3])
                AccuracyRecelt_SystemTwo.append(short_list_sorted)
                InputName_SystemTwo.clear()
            except:
                    sms = ""
                    GoogleNameRecoummend = 'nul'
                    GoogleName.append(sms)
                    CustomersReselt_SystemTwo.append(sms)
                    InputName_SystemTwo.clear()
            try:
                AbbreviationOne = 'Independent School District'
                if AbbreviationOne in GoogleNameRecoummend:
                    query_text_u = [GoogleNameRecoummend]
                    df2 = pd.DataFrame({'Customers': query_text_u})
                    df2['customer_tokenized'] = df2['Customers'].apply(
                            lambda x: tokenize(str(x).lower()))
                    partOne = df2['customer_tokenized'][0][0]
                    NewName = f"{partOne}" + " isd"
                    short_list_sorted, similarity_scores_u = System_three(
                            NewName)
                    for index, item in enumerate(short_list_sorted):
                        if item != 0:
                            search = np.where(similarity_scores_u == item)
                            name = df['Active customers'][search[0]]
                            nameToAppend3 = name.values[0]
                            InputName_SystemThree.append(nameToAppend3)
                        else:
                            sms = 'NO Similarity'
                            InputName_SystemThree.append(sms)
                    NewNameList.append([NewName])
                    CustomersReselt_SystemThree.append(
                            InputName_SystemThree[:3])
                    AccuracyRecelt_SystmThree.append(short_list_sorted)
                    InputName_SystemThree.clear()

                AbbreviationTwo = 'County Public Schools'
                if AbbreviationTwo in GoogleNameRecoummend:
                    query_text_u = [GoogleNameRecoummend]
                    df2 = pd.DataFrame({'Customers': query_text_u})
                    df2['customer_tokenized'] = df2['Customers'].apply(
                            lambda x: tokenize(str(x).lower()))
                    partOne = df2['customer_tokenized'][0][0]
                    NewName = f"{partOne}" + " cps"
                    short_list_sorted, similarity_scores_u = System_three(
                            NewName)
                    for index, item in enumerate(short_list_sorted):
                        if item != 0:
                            search = np.where(similarity_scores_u == item)
                            name = df['Active customers'][search[0]]
                            nameToAppend3 = name.values[0]
                            InputName_SystemThree.append(nameToAppend3)
                        else:
                            sms = 'NO Similarity'
                            InputName_SystemThree.append(sms)
                    NewNameList.append([NewName])
                    CustomersReselt_SystemThree.append(InputName_SystemThree)
                    AccuracyRecelt_SystmThree.append(short_list_sorted)
                    InputName_SystemThree.clear()

                AbbreviationThree = 'Unified School District'
                if AbbreviationThree in GoogleNameRecoummend:
                    query_text_u = [GoogleNameRecoummend]
                    df2 = pd.DataFrame({'Customers': query_text_u})
                    df2['customer_tokenized'] = df2['Customers'].apply(
                            lambda x: tokenize(str(x).lower()))
                    partOne = df2['customer_tokenized'][0][0]
                    partTwo = df2['customer_tokenized'][0][1]
                    if partTwo != "unified":
                        NewName = f"{partOne}" + f" {partTwo}" + " USD"
                    else:
                        NewName = f"{partOne}" + " USD"

                    short_list_sorted, similarity_scores_u = System_three(
                            NewName)
                    for index, item in enumerate(short_list_sorted):
                        if item != 0:
                            search = np.where(similarity_scores_u == item)
                            name = df['Active customers'][search[0]]
                            nameToAppend3 = name.values[0]
                            InputName_SystemThree.append(nameToAppend3)
                        else:
                            sms = 'NO Similarity'
                            InputName_SystemThree.append(sms)
                    NewNameList.append([NewName])
                    CustomersReselt_SystemThree.append(InputName_SystemThree)
                    AccuracyRecelt_SystmThree.append(short_list_sorted)
                    InputName_SystemThree.clear()
                else:
                    NewNameList.append(['NO Similarity'])
                    CustomersReselt_SystemThree.append(['NO Similarity'])
            except:
                sms = ""
                NewNameList.append(sms)
                CustomersReselt_SystemThree.append(sms)


            if len(CustomersReselt_SystemThree[0]) >= 2:
                ResultFrom3Path = [*CustomersReselt_SystemThree[0],
                                       *CustomersReselt_SystemTwo[-1], *CustomersReselt_SystemOne[-1]]
            else:
                ResultFrom3Path = [*CustomersReselt_SystemOne[-1],
                                       *CustomersReselt_SystemTwo[-1], *CustomersReselt_SystemThree[0]]

            result = pd.DataFrame(ResultFrom3Path, columns=['Matches'])
            result = result[result['Matches'] != "NO Similarity"]
            result = result.drop_duplicates()
            result = list(result['Matches'])
            my_list = result[:4]
            CustomersReselt_SystemThree.clear()
            my_dictionary = dict()
            if len(my_list) != 0:
                for index, value in enumerate(my_list):
                    my_dictionary[f"match{index}"] = value
                    while index < 3:
                        index += 1
                        my_dictionary[f'match{index}'] = ""
            else:
                my_list = [""]
                for index, value in enumerate(my_list):
                    my_dictionary[f"match{index}"] = value
                    while index < 3:
                        index += 1
                        my_dictionary[f'match{index}'] = ""
            Output_data = {
                    "CiscoCustomerName": CiscoName[-1],
                    "GoogleName": GoogleNameRecoummend,
                    "Matches": my_dictionary
                }

            data.append(Output_data)
        Output = copy(data)
        data.clear()
        return Output
    else:
        return{"message": "100 Customers MAX Per Call"}

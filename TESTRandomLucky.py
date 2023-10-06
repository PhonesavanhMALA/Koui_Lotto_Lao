import random
import time
from datetime import datetime
import os

import pandas as pd

KDEV =""

List_NumberLucky = []

def RandomLucky():
    CheckTrue = True
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    # MainNumRan = pd.read_excel('NumRan.xlsx',converters={'Six_DigitNumber':str})
    MainNumRan = pd.read_excel('EXCEL/RandomLucky.xlsx',converters={'Six_DigitNumber':str})
    MainFilter = pd.read_excel('EXCEL/LIST_FILTER.xlsx',converters={'Six_DigitNumber':str})
    L_MainFilter = MainFilter['NumFilter'].tolist()
    L_MainData = MainData['Six_DigitNumber'].tolist()
    numOfLucky = MainNumRan['NUMRAN'].tolist()
    CheckGetList = []
    CheckDuplicateList = []
    SCheckGetList = ""
    storeList = []
    
    
    sTring_Lucky = ""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_time = f'{current_time}'
    # for i in range (9):
    i = 0
    # while len(CheckDuplicateList) <= 8:
    RestTime = 0
    KWIN = 0
    Ninenie = 0
    duplicateValue = 0
    countRow = 0
    dupli = []
    limite_Number = []
    CheckRichard = 0
    while KWIN <= 3:
        print(limite_Number)
        num = random.choice(numOfLucky)
        i = 0
        time.sleep(0.1)
        # while i != num:
        #     i +=1
        Result_Lotto = str(random.choice(L_MainData))
        get_luk = int(Result_Lotto[3])
        get_Last_two = int(Result_Lotto[4:])
        storeList.append(Result_Lotto)
        
        if (get_luk == 4) or (get_Last_two >= 50) and (get_Last_two % 2 != 0):
            storeList.append(Result_Lotto)
        else:
            print(f"THE NUMBER {Result_Lotto} HAS DELETED\n")
            print(f"{'*' * 100}")
            L_MainData.remove(Result_Lotto)
        countElement = storeList.count(Result_Lotto)
        
        ### ເພີ່ມສາມໂຕທຳອິດເຂົ້າ
        if len(limite_Number) < 3:
            limite_Number.append(Result_Lotto)
            dupli.append(countElement)
            print(limite_Number)
            print(dupli)
            RNumber = f"THE DRAW IS: {Result_Lotto}"
            RDup = f"DUPLICATE {countElement} TIMES:"
            with open('EXCEL/KWIN14.txt', mode="w") as lucky:
                lucky.write(f"{RNumber}\n{RDup}")
        if countRow == 14:
            os.system('cls')
            print(KDEV)    
            countRow = 0
            Ninenie += 1
            RestTime +=1                
            length_OF_Maindata = len(L_MainData)
            length_OF_storeList = len(storeList)
                
            print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
            print("----------------------------------------------------------")
            print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_storeList} <<<<<")
            
        
        print(f"Total Of {Result_Lotto} and Duplicate: {countElement}")
        countRow += 1
        CheckRichard += 1
        
        if CheckRichard == 4289:
            if countElement == 1 and Result_Lotto in L_MainData:
                L_MainData.remove(Result_Lotto)
                print(f"THE NUMBER {Result_Lotto} HAS DELETED FROM MAIN DATA")
            if countElement == 1 and Result_Lotto in storeList:
                storeList.remove(Result_Lotto)
                print(f"THE NUMBER {Result_Lotto} HAS DELETED FROM STORE DATA")
            CheckRichard = 0
            time.sleep(8)
        
        # if RestTime == 4289:
        #     time.sleep(88)
            
        ### ຖ້າໂຕເລກທີ່ຊ້ຳໃຫມ່ໄດ້ຫລາຍກ່ວາໂຕເລກປັດຈຸບັນ ໃຫ້ເອົາໂຕເລກປັດຈຸບັນທີ່ຊ້ຳຫນ້ອຍທີ່ສຸດອອກ
        s = 0
        if len(limite_Number) <= 3:
            CheckTrueMinimum = False
            for elem in dupli:
                if countElement > elem:
                    ### find low west in duplicate
                    if Result_Lotto in limite_Number:
                        dupli[index] = int(dupli[index])+1
                    elif s < elem:
                        s = elem
                        ### Find position by value
                        index = dupli.index(s)
                        CheckTrueMinimum = True
                    if CheckTrueMinimum:
                        limite_Number[index] = Result_Lotto
                        dupli[index] = countElement
                        RNumber = f"THE DRAW IS: {limite_Number}"
                        RDup = f"DUPLICATE {dupli} TIMES: "
                        with open('EXCEL/KWIN14.txt', mode="w") as lucky:
                            lucky.write(f"\n{RNumber}\n{RDup}")
                            print(KDEV)
                            print(f"THE DRAW IS: {limite_Number}")
                            print(f"THE DUPLICATE: {dupli}")
                            print(f"{'*' * 100}")
                            time.sleep(14)
            
        # # elif countElement
        # if int(countElement) == 16:
        #     print("THE DRAW IS:::::::::::")
        #     print(Result_Lotto)
        #     KWIN += 1
        #     with open('EXCEL/KWIN.txt', mode="a") as lucky:
        #         lucky.write(f"\n{Result_Lotto}")
            
        # get_Mid_Of_Result = Result_Lotto[2:]
        # get_luk = Result_Lotto[3]
        # get_First = Result_Lotto[0]
        # get_Last_three = Result_Lotto[3:]
        # get_First_three = Result_Lotto[:3]
        # # print(get_First)
        # print(get_First_three)
        # i += 1
        # # if get_Mid_Of_Result == "63" or get_Mid_Of_Result == "36" or get_luk == "5":
        # # if get_First == "4":
        #     # if get_Mid_Of_Result == "6353" or get_Mid_Of_Result == "3653" or get_Mid_Of_Result == "5653" or get_Mid_Of_Result == "5353" or get_Last_three == "316" or get_Last_three == "356" or get_Last_three == "396":
        # if get_First_three == "302":    
        #     CheckGetList.append(Result_Lotto)
        #     print(Result_Lotto)
        #     if Result_Lotto in CheckGetList:
        #         CheckDuplicateList.append(Result_Lotto)
        #         print("THE DRAW IS::::::::::::::::::::::::::::::")            
        #         print(Result_Lotto)           
        #         with open('EXCEL/KWIN.txt', mode="a") as lucky:
        #             lucky.write(f"\n{Result_Lotto}")
                
    # if i == 5000:
    #     time.sleep(3)
    #     i = 0
    # for u in range(6):
    #     # print(u)
    #     num = random.choice(numOfLucky)
    #     i = 0
    #     # if u > 0:
    #     #     time.sleep(0.5)
    #     while i != num:
    #         i +=1
    #     Result_Lotto = random.choice(L_MainData)        
    #     if Result_Lotto not in L_MainFilter:
    #         # print(Result_Lotto)
    #         sTring_Lucky = f"{Result_Lotto}\n"
    #         if CheckTrue:
    #             CheckTrue = False 
    #             with open('EXCEL/RandomLucky.txt', mode="a") as lucky:
    #                 lucky.write(f"\n{current_time}\n{sTring_Lucky}")
    #         else:
    #             with open('EXCEL/RandomLucky.txt', mode="a") as lucky:
    #                 lucky.write(f"{sTring_Lucky}")
    #     else:
    #         with open('EXCEL/WAS PASS.txt', mode="a") as lucky:
    #                 lucky.write(f"{sTring_Lucky}")
    
RandomLucky()

# def TESTRAN():
#     CheckTrue = True
#     MainFilter = pd.read_excel('EXCEL/LIST_FILTER.xlsx',converters={'Six_DigitNumber':str})
#     L_MainFilter = MainFilter['NumFilter'].tolist()
#     print(MainFilter)
    
# TESTRAN()
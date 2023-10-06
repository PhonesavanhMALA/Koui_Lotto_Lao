import random
import time
from datetime import datetime
import os

import pandas as pd
KDEV =""

def RandomLucky():
    ## Declear
    ## Default Luk
    # L_Getluk = [0,1,2,3,4,5,6,7,8,9]
    storeList = []
    L_Getluk = [1,5]
    CheckTrue = True
    limited_Number = []
    dupli = []
    CheckRichard = 0
    countRow = 0
    round = 0
    
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    # Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    # # #*** F1
    # # # Filter grether or lower
    MainData = MainData.loc[MainData['Stateright'].astype(int) < 50]
    # # filter even or odd
    MainData = MainData.loc[MainData['Stateright'].astype(int) %2 == 0]
    ### Get all
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # return
    V_Running = True
    i = 0
    countNumLoop = 0
    while V_Running:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        current_time = f'{current_time}'
        theDraw = str(random.choice(L_MainData))
        if len(limited_Number) < 8:
            storeList.append(theDraw)
            countElement = storeList.count(theDraw)
            limited_Number.append(theDraw)
            dupli.append(countElement)
            print(current_time)
            print(limited_Number)
            print(dupli)
            RNumber = f"THE DRAW IS: {theDraw}"
            RDup = f"DUPLICATE {countElement} TIMES:"
            with open('EXCEL/14GETLAST.txt', mode="w") as lucky:
                lucky.write(f"{RNumber}\n{RDup}")
        else:
            storeList.append(theDraw)
            countElement = storeList.count(theDraw)
            print(i)
            limited_Number[i] = theDraw
            dupli[i] = countElement
            length_OF_Maindata = len(L_MainData)
            length_OF_storeList = len(storeList)
            i +=1
            if countRow == 14:
                os.system('cls')
                countRow = 0
            countRow +=1
            
            # if countNumLoop == 3636:
            #     time.sleep(10)
            #     countNumLoop = 0
            # countNumLoop +=1
            # time.sleep(2)
            print(current_time)
            print(theDraw)
            print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
            print("----------------------------------------------------------")
            print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_storeList} <<<<<")
            print("----------------------------------------------------------")
            print("LIMITED NUMBER => ", limited_Number)
            print("DUPLICATE COUNT NUM =>", dupli)
            if i == 8:
                i = 0
            ranDomInLMain = str(random.choice(L_MainData))
            L_MainData.remove(ranDomInLMain)
            
            if len(L_MainData) <= 0:
                print("FINISH")
                with open('EXCEL/14GETLAST.txt', mode="w") as lucky:
                    lucky.write(f"LIMITED LIST{limited_Number}\nDUPLICATE LIST:{dupli}")
RandomLucky()
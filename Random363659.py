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
    
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    # Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    # #*** F1
    # # Filter grether or lower
    MainDataF1 = MainData.loc[MainData['Stateright'].astype(int) >= 50]
    # # filter even or odd
    MainDataF1 = MainDataF1.loc[MainDataF1['Stateright'].astype(int) %2 != 0]
    
    # #*** F2
    # # Filter grether or lower
    MainDataF2 = MainData.loc[MainData['Stateright'].astype(int) < 50]
    # # filter even or odd
    MainDataF2 = MainDataF2.loc[MainDataF2['Stateright'].astype(int) %2 == 0]
    
    # ### Combine Dataframe
    C_MainData = pd.concat([MainDataF1, MainDataF2], axis=0)
    L_MainData = C_MainData['Six_DigitNumber'].tolist()
    
    ### Get all
    L_MainData = C_MainData['Six_DigitNumber'].tolist()
    # return
    V_Running = True
    countElement = 1
    containNumber = [6,8,1,9,4]
    countRow = 0
    for i in range(10):
        while V_Running:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            current_time = f'{current_time}'
            if len(L_MainData) > 0:
                theDraw = str(random.choice(L_MainData))
                storeList.append(theDraw)
                ### ເພີ່ມສາມໂຕທຳອິດເຂົ້າ
                if len(limited_Number) < 8:
                    ### Check if theDraw contain number:
                    wasAdded = True
                    for e_num in theDraw:
                        if int(e_num) in containNumber and (theDraw not in limited_Number):
                            countElement = storeList.count(theDraw)
                            limited_Number.append(theDraw)
                            dupli.append(countElement)
                            wasAdded = False
                    if wasAdded:
                        L_MainData.remove(theDraw) 
                    print(current_time)
                    print(limited_Number)
                    print(dupli)
                    RNumber = f"THE DRAW IS: {theDraw}"
                    RDup = f"DUPLICATE {countElement} TIMES:"
                    with open('EXCEL/14KWIN.txt', mode="w") as lucky:
                        lucky.write(f"{RNumber}\n{RDup}")
                    if countRow == 14:
                        os.system('cls')
                        countRow = 0
                    countRow +=1
                else:
                    # print(len(limited_Number))
                    if len(limited_Number) == 8:
                        F_Draw = ""
                        s = 0
                        length_OF_Maindata = len(L_MainData)
                        length_OF_Store = len(storeList)
                        countElement = storeList.count(theDraw)
                        print(current_time)
                        print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                        print("----------------------------------------------------------")
                        print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_Store} <<<<<")
                        print(theDraw)
                        print(countElement)
                        if countRow == 14:
                            # os.system('cls')
                            countRow = 0
                        countRow +=1
                        for elem in dupli:
                            if countElement > elem and theDraw != F_Draw:
                                ### find low west in duplicate
                                if theDraw in limited_Number:
                                    p = 0
                                    for eachNum in limited_Number:
                                        if eachNum == theDraw:
                                            limited_Number[p] = theDraw
                                            dupli[p] = countElement
                                            F_Draw = theDraw
                                        p+=1
                                else:       
                                    limited_Number[s] = theDraw
                                    dupli[s] = countElement
                                    F_Draw = theDraw
                                    RNumber = f"THE DRAW IS: {limited_Number}"
                                    RDup = f"DUPLICATE {dupli} TIMES: "
                                with open('EXCEL/14KWIN.txt', mode="w") as lucky:
                                    lucky.write(f"\n{RNumber}\n{RDup}")
                                    print(current_time)
                                    print(KDEV)
                                    print(f"THE DRAW IS: {limited_Number}")
                                    print(f"THE DUPLICATE: {dupli}")
                                    print(f"{'*' * 100}")
                                    
                            s+=1
                    
                if len(L_MainData) >= 1:
                    ranRemove = str(random.choice(L_MainData))   
                    L_MainData.remove(ranRemove)
            else:
                print("FINISH GOODLUCK!")
                return
                if len(storeList) > 8:
                    os.system('cls')
                    length_OF_Maindata = len(L_MainData)
                    length_OF_Store = len(storeList)
                    print(current_time)
                    print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                    print("----------------------------------------------------------")
                    print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_Store} <<<<<")
                    ### Make dictionary
                    TheDrawDictionary = {
                        "The Draw": limited_Number
                    }
                    ### Convert to dataframe
                    dataframe = pd.DataFrame(TheDrawDictionary)
                    ### Export to excel
                    dataframe.to_excel(f'363659Option/TheDraw 363659.xlsx', index=False, header=True, sheet_name="THEDRAW")
                    V_Running = False
                    with open('EXCEL/14KWIN.txt', mode="a") as lucky:
                        lucky.write(f"\n\n{limited_Number}\n{dupli}\nTHE TOTAL OF STORE DATA IS: {length_OF_Store}")
                        print(current_time)
                        print(KDEV)
                        print(f"THE DRAW IS: {limited_Number}")
                        print(f"THE DUPLICATE: {dupli}")
                        print(f"{'*' * 100}")
                    with open('EXCEL/363659TheDraw.txt', mode="a") as lucky:
                        lucky.write(f"\n{limited_Number}\n{dupli}\nTHE TOTAL OF STORE DATA IS: {length_OF_Store}")
                    
                    
                    countElement = storeList.count(theDraw)
                    theDraw = str(random.choice(storeList))
                    if countRow == 14:
                        os.system('cls')
                        countRow = 0
                    F_Draw = ""
                    s = 0
                    for elem in dupli:
                        if countElement > elem and theDraw != F_Draw:
                            ### find low west in duplicate
                            limited_Number[s] = theDraw
                            dupli[s] = countElement
                            F_Draw = theDraw
                            RNumber = f"THE DRAW IS: {limited_Number}"
                            RDup = f"DUPLICATE {dupli} TIMES: "
                            with open('EXCEL/14KWIN.txt', mode="w") as lucky:
                                lucky.write(f"\n{RNumber}\n{RDup}")
                                print(current_time)
                                print(KDEV)
                                print(f"THE DRAW IS: {limited_Number}")
                                print(f"THE DUPLICATE: {dupli}")
                                print(f"{'*' * 100}")
                        s+=1
                    countRow +=1
                    storeList.remove(theDraw)
                    
                else:
                    print("STOPPPP")
                    V_Running = False
                ### Clear console
                if countRow == 14:
                    os.system('cls')
                    countRow = 0
        i+=1
RandomLucky()
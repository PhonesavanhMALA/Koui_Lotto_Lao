import random
import time
from datetime import datetime
import os

import pandas as pd
KDEV =""

def RandomLucky():
    ## Declear
    ## Default Luk
    L_Getluk = [0,1,2,3,4,5,6,7,8,9]
    storeList = []
    # L_Getluk = [4,5]
    CheckTrue = True
    limited_Number = []
    dupli = []
    CheckRichard = 0
    countRow = 0
    # container = [99,96,90,85,82,81,77,70,69,64,62,61,60,59,55,54,53,50]
    
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    # Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    ## filter even or odd
    # MainData = MainData.loc[MainData['Stateright'].astype(int) %2 == 0]
    ## Filter grether or lower
    # MainData = MainData.loc[MainData['Stateright'].astype(int) < 50]
    
    # ##*** F1
    # ## Filter grether or lower
    # MainDataF1 = MainData.loc[MainData['Stateright'].astype(int) < 50]
    # ### filter even or odd
    # MainDataF1 = MainDataF1.loc[MainDataF1['Stateright'].astype(int) %2 == 0]
    # print(len(MainDataF1))
    
    # ##*** F2
    # ### Filter grether or lower
    # MainDataF2 = MainData.loc[MainData['Stateright'].astype(int) == 27]
    # print(len(MainDataF2))
    # print(MainDataF2)
    # time.sleep(10)
    # ### filter even or odd
    # # MainDataF2 = MainDataF2.loc[MainDataF2['Stateright'].astype(int) %2 == 0]
    # ##*** F3
    # ### Filter grether or lower
    # MainDataF3 = MainData.loc[MainData['Stateright'].astype(int) == 67]
    # print(len(MainDataF3))
    # print(MainDataF3)
    # time.sleep(10)
    # ### filter even or odd
    # # MainDataF3 = MainDataF3.loc[MainDataF3['Stateright'].astype(int) %2 == 0]
    
    
    # ### Combine Dataframe
    # C_MainData = pd.concat([MainDataF1, MainDataF2,MainDataF3], axis=0)
    # L_MainData = C_MainData['Six_DigitNumber'].tolist()
    
    ### Get all
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # return
    V_Running = True
    while V_Running:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        current_time = f'{current_time}'
        
        if len(L_MainData) > 0:
            theDraw = str(random.choice(L_MainData))
            g_LastTwo = int(theDraw[4:])
            g_LastOne = int(theDraw[5:])
            # P1 = int(theDraw[0])
            # P2 = int(theDraw[1])
            # P3 = int(theDraw[2])
            # P4 = int(theDraw[3])
            # P5 = int(theDraw[4])
            # P6 = int(theDraw[5])
            
            
            ### ເພີ່ມ8ໂຕທຳອິດເຂົ້າ
            if len(limited_Number) < 8:
                print("THE RAN DRAW", theDraw)
                storeList.append(theDraw)
                countElement = storeList.count(theDraw)
                limited_Number.append(theDraw)
                dupli.append(countElement)
                print(current_time)
                print(limited_Number)
                print(dupli)
                RNumber = f"THE DRAW IS: {theDraw}"
                RDup = f"DUPLICATE {countElement} TIMES:"
                with open('EXCEL/THEDRAW.txt', mode="w") as lucky:
                    lucky.write(f"{RNumber}\n{RDup}")
            else:
                
                eachNum = list(set(theDraw))
                approve = 0
                if len(L_MainData) > 0 and (len(limited_Number)<8):
                    countElement = storeList.count(theDraw)
                    if (g_LastOne == 8 or g_LastTwo == 27 or g_LastTwo == 67):
                            storeList.append(theDraw)
                            countElement = storeList.count(theDraw)
                            ranDomInLMain = str(random.choice(L_MainData))
                            L_MainData.remove(ranDomInLMain)
                    else:
                        L_MainData.remove(theDraw)
                        print(current_time)
                        print(f"THE NUMBER {theDraw} HAS DELETED\n")
                        print(f"{'*' * 100}")
                    if countRow == 14:
                        os.system('cls')
                        print(current_time)
                        print(KDEV)    
                        countRow = 0              
                        length_OF_Maindata = len(L_MainData)
                        length_OF_storeList = len(storeList)
                        # return
                        print(current_time)
                        print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                        print("----------------------------------------------------------")
                        print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_storeList} <<<<<")
                        if length_OF_storeList < 30:
                            print(storeList)
                    print('\n')
                    print(current_time)
                    print(f"Total Of {theDraw} and Duplicate: {countElement}")
                    countRow += 1
                    # CheckRichard += 1
            # print(len(L_MainData))
                
            ### ຖ້າໂຕເລກທີ່ຊ້ຳໃຫມ່ໄດ້ຫລາຍກ່ວາໂຕເລກປັດຈຸບັນ ໃຫ້ເອົາໂຕເລກປັດຈຸບັນທີ່ຊ້ຳຫນ້ອຍທີ່ສຸດອອກ
            if len(limited_Number) == 8 or (g_LastOne == 8 or g_LastTwo == 27 or g_LastTwo == 67):
                F_Draw = ""
                s = 0
                storeList.append(theDraw)
                countElement = storeList.count(theDraw)
                ranDomInLMain = str(random.choice(L_MainData))
                L_MainData.remove(ranDomInLMain)
                # print("COUNT ELEMENT =: ", countElement)
                # print("RANDRAW =: ", theDraw)
                if countRow == 14:
                    os.system('cls')
                    countRow = 0
                countRow += 1
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
                        with open('EXCEL/THEDRAW.txt', mode="w") as lucky:
                            lucky.write(f"\n{RNumber}\n{RDup}")
                            print(current_time)
                            print(KDEV)
                            print(f"THE DRAW IS: {limited_Number}")
                            print(f"THE DUPLICATE: {dupli}")
                            print(f"{'*' * 100}")
                    else:
                        if countRow == 14:
                            os.system('cls')
                            countRow = 0
                        countRow += 1
                        length_OF_Maindata = len(L_MainData)
                        length_OF_Store = len(storeList)
                        print(current_time)
                        print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                        print("----------------------------------------------------------")
                        print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_Store} <<<<<")
                        print("\n-----------------------------------------------------")
                        print(current_time)
                        print(KDEV)
                        print(f"THE DRAW IS: {limited_Number}")
                        print(f"THE DUPLICATE: {dupli}")
                        print(f"{'*' * 100}")
                        ranDomInLMain = str(random.choice(L_MainData))
                        L_MainData.remove(ranDomInLMain)
                    s+=1
                    
            else:
                ranDomInLMain = str(random.choice(L_MainData))
                L_MainData.remove(ranDomInLMain)
                length_OF_Maindata = len(L_MainData)
                length_OF_Store = len(storeList)
                print(current_time)
                print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                print("----------------------------------------------------------")
                print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_Store} <<<<<")
                print("----------------------------------------------------------")
                print(limited_Number)
                print("----------------------------------------------------------")
                print(dupli)
                pass
                if countRow == 14:
                    os.system('cls')
                    countRow = 0
                countRow += 1
                if length_OF_Store < 30:
                    print(storeList)
                if len(limited_Number) < 8:
                    print(limited_Number)
                
            # if len(L_MainData) >= 1:                
            #     L_MainData.remove(str(random.choice(L_MainData)))  
        else:
            print("FINISH THEDRAW")
            print(len(storeList))
            return
            if len(storeList) > 8:
                if length_OF_storeList < 30:
                    print(storeList)
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
                countElement = storeList.count(theDraw)
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
                        with open('EXCEL/THEDRAW.txt', mode="w") as lucky:
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
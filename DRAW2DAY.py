import random
import time
from datetime import datetime
import os

import pandas as pd

KDEV =""
congrats = """ '   .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
'  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
'  | |     ______   | || |     ____     | || | ____  _____  | || |    ______    | || |  _______     | || |      __      | || |  _________   | || |    _______   | || |              | |
'  | |   .' ___  |  | || |   .'    `.   | || ||_   \|_   _| | || |  .' ___  |   | || | |_   __ \    | || |     /  \     | || | |  _   _  |  | || |   /  ___  |  | || |      _       | |
'  | |  / .'   \_|  | || |  /  .--.  \  | || |  |   \ | |   | || | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || | |_/ | | \_|  | || |  |  (__ \_|  | || |     | |      | |
'  | |  | |         | || |  | |    | |  | || |  | |\ \| |   | || | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |     | |      | || |   '.___`-.   | || |     | |      | |
'  | |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\   |_  | || | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || |    _| |_     | || |  |`\____) |  | || |     | |      | |
'  | |   `._____.'  | || |   `.____.'   | || ||_____|\____| | || |  `._____.'   | || | |____| |___| | || ||____|  |____|| || |   |_____|    | || |  |_______.'  | || |     |_|      | |
'  | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |     (_)      | |
'  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  """

### ວິທີຄຳນວນp
"""
1.Container ໃຫ້ເບິ່ງງວດກ່ອນໜ້ານີ້ແລ້ວນຳເອົາໂຕເລກມາ, ເບິ່ງນາມສັດຫລັກທີ່ໃຫຍ່ສຸດຖ້າຊ້ຳກັບໂຕອອກແມ່ນໃຫ້ຈັບເອົາໂຕເລກນັ້ນເຂົ້ານຳ
ຕົວຢ່າງ: 429749, ນາມສັດ:25,06,03,09 ໃຫ້ເອົາເລກ9ໄປໃສ່ໃນ Container
2.
"""
#### x>2 and x<=3
def THEDRAW():
    CanRemove = False
    Bok = ['73','33','08','48','88','00','20','60','23','63','32','72']
    Num = ['79','39','71','31','70','30','01','41','81','02','42','82','10','50','90','24','64','29','69']
    Pik = ['80','40','68','28','27','67','26','66','25','65','03','43','83','04','44','84','16','56','96','17','57','97','19','59','99','21','61','22','62']
    SeeKha = ['78','38','77','37','76','36','75','35','74','34','05','45','85','06','46','86','07','47','87','09','49','89','11','51','91','12','52','92','13','53','93','14','54','94','15','55','95','18','58','98']
    
    ShortCut = ['26','28','40','44','06','12','14','36','38','46','99','97','65','61','59','57','91','89','85','75','77','53','55','93','95']
    MYLIST = pd.read_excel(f'282859/ListDraw.xlsx', converters={'MYLIST':str})
    MainList = MYLIST['MYLIST'].tolist()
    
    # print(MainList)
    # return
    
    DATA_MAINDRAW = pd.read_excel('282859/0001ATHEDRAW.xlsx',sheet_name="Num will draw",converters={'FullDraw':str})
    L_MAINDRAW = DATA_MAINDRAW['FullDraw'].tolist()
    
    
    L_DrawToday = []
    # print(L_MAINDRAW)
    # return
    for lDraw in L_MAINDRAW:
        g_Draw = lDraw.split(',')
        for c_Draw in g_Draw:
            if c_Draw != "," and c_Draw != "" and str(c_Draw) != 'nan':
                L_DrawToday.append(c_Draw)
        # print(g_Draw)
    # print(L_DrawToday)
    # return
    # ## Declear
    # ## Default LukJ
    # # L_Getluk = [0,1,2,3,4,5,6,7,8,9]
    storeList = []
    CheckTrue = True
    limited_Number = []
    dupli = []
    CheckRichard = 0
    countRow = 0
    container = ['4','7']
    # container = ['2','5','8','9']    ### container <= 4 if > 4 then get only first 4 lowest
    # container = ['0','1','2','3','4',"5","6","7","8","9"]
    # contain_LUK = ['0','1','2','3','4',"5","6","7","8","9"]
    contain_LUK = ['3','9','2']
    # CheckDraw = ['564','864','64']
    UnContain = [22,29,68,87,39,62,32,39,34,"03",24,74,93,76]
    L_Uncontain = []
    for un_val in UnContain:
        L_Uncontain.append(str(un_val))
    # print(L_Uncontain)
    # return
    # SKIP_ContaiLastTwo = ['31','04','34','25','40']
    # Special_LIKE = ['08','40','88','38','25','65','27','67','36','29','69','32','72','31','71','80','23','63','35','75','09','49','89','02','42','82']
    Special_LIKE = ['27','67','29','69','36','35','75','76','09','49','80','89','39','79','24','64','23','63','40']
    # Special_LIKE = ['36']
    # Special_LIKE2 = ['']
    # FIRST_POSITION >= 5
    L_DrawToday = L_DrawToday+Special_LIKE
    # print(L_DrawToday)
    
    
    M_LastFour = pd.read_excel('282859/LASTFOUR.xlsx',converters={'L4':str})
    L_LastFour = M_LastFour['L4'].tolist()
    # print(L_LastFour)
    
    
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    # Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    
    # filter_L = [3,4,19,21,25,43,44,59,61,65,83,84,99,24,64,27,76,88,8]
    # filter_L = [3,4,19,21,25,43,44,59,61,65,83,84,99,24,64,27,76,88,8]
    
    # ## filter even or odd
    # MainData = MainData.loc[MainData['Stateright'].astype(int) % 2 != 0]
    # # ## Filter grether or lower
    # MainData = MainData.loc[MainData['Stateright'].astype(int) == 64]
    
    # PD_FILTER = pd.DataFrame()
    
    # for f_val in filter_L:
    #     print(f_val)
    #     New_MainData = MainData.loc[MainData['Stateright'].astype(int) == f_val]
    #     PD_FILTER = pd.concat([PD_FILTER, New_MainData], axis=0)
        # PD_FILTER += MainData
        # print(MainData)
    
    # print(PD_FILTER)
    # print(len(PD_FILTER))
    # MainData = PD_FILTER
    # return
    
    # print(MainData)
    # time.sleep(2)
    
    # ### *** F1
    # ### Filter grether or lower
    # MainDataF1 = MainData.loc[MainData['Stateright'].astype(int) <= 50]
    # # filter even or odd
    # # MainDataF1 = MainDataF1.loc[MainDataF1['Stateright'].astype(int) %2 == 0]
    # print(len(MainDataF1))
    # time.sleep(3)
    
    # ###*** F2
    # ### Filter grether or lower
    # MainDataF2 = MainData.loc[MainData['Stateright'].astype(int) > 50]
    # # filter even or odd
    # MainDataF2 = MainDataF2.loc[MainDataF2['Stateright'].astype(int) %2 != 0]
    # print(len(MainDataF2))
    # print(MainDataF2)
    # time.sleep(2)
    # ###*** F3
    ### Filter grether or lower
    # MainDataF3 = MainData.loc[MainData['Stateright'].astype(int) <= 50]
    # ### filter even or odd
    # MainDataF3 = MainDataF3.loc[MainDataF3['Stateright'].astype(int) %2 != 0]
    # print(len(MainDataF3))
    # print(MainDataF3)
    # time.sleep(10)
    
    
    ##Combine Dataframe
    # C_MainData = pd.concat([MainDataF1, MainDataF2], axis=0)
    # L_MainData = C_MainData['Six_DigitNumber'].tolist()
    # print(len(C_MainData))
    # print(C_MainData)
    # print(len(L_MainData))
    # print(L_MainData)
    # time.sleep(4)
    
    ### Get all
    L_MainData = MainData['Six_DigitNumber'].tolist()
    L_Not_GFirst = ['0','6','9']
    print("MAIN DATA")
    # print(L_MainData)
    # time.sleep(10)
    V_Running = True
    low = 0
    height = 0
    while V_Running:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        current_time = f'{current_time}'
        
        if len(L_MainData) >= 20 and len(L_MainData) < 30:
            print("LAST RAN DOM IS", L_MainData)
            with open('EXCEL/LASTDRAW.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE LAST DRAW IS:{L_MainData}")
                
                
        #### To get list of W2 
        if len(L_MainData) <= 50 and len(L_MainData) >= 40:
            print("222222222222222222222")
            print("222222222222222222222")
            make_w2 = ""
            for value in L_MainData:
                new_value = value[-2:]
                make_w2 += '\n' + new_value
            with open('WASDRAW/W2.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE W2 {current_time}:\n{make_w2}")
                
                
        #### To get list of W3
        if len(L_MainData) <= 300 and len(L_MainData) >= 250:
            print("333333333333333333333")
            print("333333333333333333333")
            make_w3 = ""
            for value in L_MainData:
                new_value = value[-3:]
                make_w3 += '\n' + new_value
            with open('WASDRAW/W3.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE W3 {current_time}:\n{make_w3}")
                
                
        #### To get list of W4
        if len(L_MainData) <= 350 and len(L_MainData) >= 300:
            print("444444444444444444444")
            print("444444444444444444444")
            make_w4 = ""
            for value in L_MainData:
                new_value = value[-4:]
                make_w4 += '\n' + new_value
            with open('WASDRAW/W4.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE W4 {current_time}:\n{make_w4}")
                
        #### To get list of W5
        if len(L_MainData) <= 400 and len(L_MainData) >= 350:
            print("THE W5", L_MainData)
            print("555555555555555555555")
            print("555555555555555555555")
            make_w5 = ""
            for value in L_MainData:
                new_value = value[-5:]
                make_w5 += '\n' + new_value
            with open('WASDRAW/W5.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE W5 {current_time}:\n{make_w5}")
                
        #### To get list of W6
        if len(L_MainData) <= 500 and len(L_MainData) >= 450:
            print("666666666666666666666")
            print("666666666666666666666")
            print("THE W6", L_MainData)
            make_w6 = ""
            for value in L_MainData:
                new_value = value
                make_w6 += '\n' + new_value
            with open('WASDRAW/W6.txt', mode="w") as LastDraw:
                LastDraw.write(f"THE W6 {current_time}:\n{make_w6}")
            
        if len(L_MainData) > 0:
            theDraw = str(random.choice(L_MainData))
            countElement = storeList.count(theDraw)
            length_OF_Maindata = len(L_MainData)
            length_OF_Store = len(storeList)
            g_first = str(theDraw[0])
            g_LUK = theDraw[3]
            g_last = theDraw[-1]
            g_Twodigit = theDraw[-2:]
            g_Threedigit = theDraw[-3:]
            g_lastFour = theDraw[-4:]
            print(g_lastFour)
            
            
            L_F = str(theDraw[1])
            L_M = str(theDraw[3])
            L_L = str(theDraw[-1])
            
            tain_F = ("1",)
            tain_M = ("5","2","9","8","7","4")
            tain_L = ("1","3","4","5","9")
            
            # if g_LUK in contain_LUK:
            #     print("THE DRAW IS::::", theDraw)
            #     print("G LUK IS HERE:::::::::",g_LUK)
            #     time.sleep(2)
            ### ເພີ່ມ8ໂຕທຳອິດເຂົ້າ
           
                
            
            
            if len(limited_Number) < 8:
                # time.sleep(2)
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
                print("THE RAN DRAW", theDraw)
                g_singleNumber = list(set(theDraw))
                g_singleNumber = list(theDraw)
                print("G_SINGLENUMBER: ", g_singleNumber)
                approve = 0
                isIn_Container = False
                # print("THE DRAW NOW", theDraw)
                keyDraw = False
                Jlouse = 0
                
                
                
                for sNumber in g_singleNumber:
                    if sNumber in container:
                        Jlouse += 1
                        print(Jlouse)
                        # isIn_Container = True
                # for sNumber in g_singleNumber:
                #     # print(sNumber)
                #     sNumber = str(sNumber)
                    
                #     ### Count Duplicate in g_singleNumber:
                #     sCount = theDraw.count(sNumber)
                #     if sCount >= 2 and keyDraw == False:
                #         keyDraw = True
                #         Jlouse += 1
                #     elif sCount == 4 and keyDraw == False:
                #         keyDraw = True
                # for check_contain in g_singleNumber:
                    # if (check_contain in container):
                    #     isIn_Container = True
                        
                    # if keyDraw and Jlouse >= 1:
                    #     if (check_contain in container) and (g_LUK in contain_LUK) and (g_Twodigit in L_DrawToday or g_Twodigit in Special_LIKE):
                    #         isIn_Container = True
                    
                            # time.sleep(4)
                    # if (check_contain in container) and (g_LUK in contain_LUK) and (g_Twodigit in L_DrawToday):
                    #     isIn_Container = True
                    
                    
                    # if (sNumber in container) and (g_Twodigit not in SKIP_ContaiLastTwo) and (g_Twodigit in Num or g_Twodigit in SeeKha or g_Twodigit in Pik or g_Twodigit in Special_LIKE) and (g_LUK in contain_LUK):
                    #     isIn_Container = True
                    # if (sNumber in container and sNumber not in UnContain) and(g_lastFour not in L_LastFour) and (g_Twodigit not in SKIP_ContaiLastTwo) and (g_LUK in contain_LUK) and (g_Twodigit in Num or g_Twodigit in Special_LIKE or g_Twodigit in SeeKha):
                    # if (sNumber in container):
                        # if int(sNumber) >=5:
                        #     height += 1
                        # else:
                        #     low +=1
                    # if (sNumber in container) and (g_LUK in contain_LUK) and (g_Twodigit not in SKIP_ContaiLastTwo) and (g_Twodigit in Num or g_Twodigit in Pik or g_Twodigit in SeeKha or g_Twodigit in Special_LIKE):
                    # if (sNumber in container):
                        # isIn_Container = True
                    # isIn_Container = True
                    
                # for val in container:
                #     if val in g_singleNumber:
                #         # isIn_Container = True
                #         # if (g_Twodigit in SeeKha or g_Twodigit in Special_LIKE or g_Twodigit in Num):
                #         if (g_LUK in contain_LUK):
                #             isIn_Container = True
                
                
                # if Jlouse >=2:
                # if  Jlouse >= 1 and (g_Twodigit in Pik or g_Twodigit in SeeKha or g_Twodigit in Special_LIKE) and (g_LUK in contain_LUK):
                # print(g_Threedigit)
                if (L_F in tain_F and L_M in tain_M and L_L in tain_L):
                    isIn_Container = True
                    Jlouse = 0
                # if (g_Twodigit in Num or g_Twodigit in Pik or g_Twodigit in Special_LIKE) and (g_LUK in contain_LUK):
                #     isIn_Container = True
                #     Jlouse = 0
                        
                
                # if (low >= 2 or low <=3) and (height >=2):
                #     isIn_Container = True
                #     print(f"{congrats}")
                #     print("LOW: ", low)
                #     print("HEIGHT: ", height)
                #     low = 0
                #     height = 0
                        # time.sleep(8)
                # isIn_Container = True
                if isIn_Container and (len(limited_Number)==8):
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    print("WORKING COMPLIE")
                    # print(g_Twodigit)
                # if Jlouse >= 2 and (len(limited_Number)==8):
                    F_Draw = ""
                    s = 0
                    storeList.append(theDraw)
                    for elem in dupli:
                        if countElement > elem and theDraw != F_Draw:
                            CanRemove = True
                            print("CHECKING THE CLIENT IS RUNING::::")
                            ### find low west in duplicate
                            if theDraw in limited_Number:
                                p = 0
                                for eachNum in limited_Number:
                                    if eachNum == theDraw:
                                        limited_Number[p] = theDraw
                                        dupli[p] = countElement
                                        F_Draw = theDraw
                                    p+=1
                                
                                print(f"\n>>>>> THE NUMBER OF {theDraw} IS UPDATED!<<<<<")
                                print("----------------------------------------------------------")
                            else:
                                print(f"\n>>>>> THE NUMBER OF {theDraw} IS REPLACED!<<<<<")
                                print("----------------------------------------------------------")
                                limited_Number[s] = theDraw
                                dupli[s] = countElement
                                F_Draw = theDraw
                                RNumber = f"THE DRAW IS: {limited_Number}"
                                RDup = f"DUPLICATE {dupli} TIMES: "
                                print(f"{congrats}")
                                if g_lastFour in L_LastFour:
                                    with open('282859/Duplicate_LastFour.txt', mode="a") as lucky:
                                        lucky.write(f"{g_lastFour}\n")
                                else:
                                    with open('282859/NOT_DRAW_YET.txt', mode="a") as lucky:
                                        lucky.write(f"{g_lastFour}\n")
                            with open('EXCEL/THEDRAW.txt', mode="w") as lucky:
                                lucky.write(f"\n{RNumber}\n{RDup}")
                                print(current_time)
                                print(KDEV)
                                print(f"THE DRAW IS: {limited_Number}")
                                print(f"THE DUPLICATE: {dupli}")
                                print(f"{'*' * 100}")
                        
                        s+=1
                        countRow +=1 
                        length_OF_MAIN = len(L_MainData)
                        if CanRemove and length_OF_MAIN > 0:
                            ranDomInLMain = str(random.choice(L_MainData))
                            if ranDomInLMain in L_MainData:
                                L_MainData.remove(ranDomInLMain)
                else:
                    print(f"THE LENGTH OF MAIN DATA IS:>>>>> {length_OF_Maindata} <<<<<")
                    print("----------------------------------------------------------")
                    print(f"THE LENGTH OF STORE DATA IS:>>>>> {length_OF_Store} <<<<<")
                    print("\n-----------------------------------------------------")
                    print(f"THE NUMBER:{theDraw} HAS DELETED!")
                    L_MainData.remove(theDraw)
                    countRow +=1
                    
                if countRow >= 27:
                    os.system('cls') 
                    countRow = 0     
                               

        else:
            ### Make dictionaery
            theDrawDictionary = {
                "DRAW SixDigit":limited_Number,
            }
    
            ### Convert to dataframe
            dataframe = pd.DataFrame(theDrawDictionary)
            ### Export to excel
            dataframe.to_excel(f'282859/01THEDRAW.xlsx', index=False, header=True, sheet_name="DATA")
            print("FINISH THEDRAW")
            print(len(storeList))
            return
THEDRAW()

### To shutdown after finish running
# os.system("shutdown /s /t 1")
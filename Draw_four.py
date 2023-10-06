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
mustDraws = []

mustDraws = ['718833', '313991', '033207', '043433', '381174', '104980', '117353', '072620', '300423', '405734', '845353', '002130', '071914', '142177', '334570', '370101', '040788', '239371', '340227', '426316', '040213', '036035', '717753', '280104', '007253', '808184', '082110', '236030', '243281', '914613', '713119', '285275', '398473', '333443', '113718', '006091', '033640', '717034', '102904', '139974', '393001', '473318', '272403', '377552', '303204', '178852', '784741', '306202', '845074', '047288', '708311', '014801', '026737', '288401', '845314', '033752', '014419', '833202', '479919', '309391', '490670', '190553', '887435', '207004', '420438', '308881', '303283', '303571', '270373', '800088', '074413', '034688', '474889', '243239', '740789', '137453', '733074', '040219', '173673', '813061', '325257', '103131', '173317', '880716', '723291', '326370', '100470', '230803', '491198', '930543', '206023', '321334', '734270', '084530', '013504', '302903', '182184', '492171', '337717', '783818', '230275', '271704', '199475', '300398', '014504', '170207', '131349', '192148', '237702', '000316', '780237', '881191', '301143', '076240', '335441', '046761', '396030', '731757', '011332', '173574', '716207', '171884', '014940', '283853', '043131', '190020', '202584', '733272', '116218', '236432', '137427', '276313', '383010', '745418', '047673', '802989', '308107', '703225', '724902', '013404', '728313', '702061', '277657', '378484', '730735', '376371', '835400', '034083', '271432', '406714', '420102', '475025', '310557', '376743', '334437', '132952', '003776', '183981', '371081', '700633', '933519', '171020', '735730', '344538', '833671', '910693', '274317', '394772', '243767', '243423', '085452', '427032', '424074', '807484', '912400', '806416']
def THEDRAW(mustDraws):
    
    CheckMustDraw = False
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
    
    M_LastFour = pd.read_excel('282859/LASTFOUR.xlsx',converters={'L4':str})
    L_LastFour = M_LastFour['L4'].tolist()
    
    
    
    
    storeList = []
    CheckTrue = True
    limited_Number = []
    dupli = []
    countRow = 0
    TheDraw_Best = 826480
    # container = ['1','2','3','4','5','6','7','8','9','0'] 
    # contain_LUK = ['1','2','3','4','5','6','7','8','9','0'] 
    # container = ['9']
    contain_LUK = ['5','6','ຄຫ']
    # Special_LIKE = ['27','67','29','69','36','35','75','76','09','49','80','89','39','79','24','64','23','63','40']
    # print(L_DrawToday)
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    Adraw_Excel = pd.read_excel('ADRAW.xlsx',sheet_name="BON",converters={'Six_DigitNumber':str})
    Adraw_Excel_Lang = pd.read_excel('ADRAW.xlsx',sheet_name="Lang",converters={'Six_DigitNumber':str})
    Adraw_Excel_Nar = pd.read_excel('ADRAW.xlsx',sheet_name="Nar",converters={'Six_DigitNumber':str})
    
    
    ### Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    # print(MainData)
    L_Adraws = Adraw_Excel['ADRAW'].tolist()
    L_DrawToday = []
    for val in L_Adraws:
        val = str(val)
        Count_val = len(val)
        if Count_val == 1:
            val = "0"+val
            L_DrawToday.append(str(val))
        else:
            L_DrawToday.append(str(val))
    
    
    
    L_Main_LangDraw = Adraw_Excel_Lang['Lang_Draw'].tolist()
    L_LangDraws = []
    for val in L_Main_LangDraw:
        val = str(val)
        Count_val = len(val)
        if Count_val == 1:
            val = "0"+val
            L_LangDraws.append(str(val))
        else:
            L_LangDraws.append(str(val))
            
    L_Main_Nar = Adraw_Excel_Nar['Nar'].tolist()
    L_NarDraws = []
    for val in L_Main_Nar:
        val = str(val)
        Count_val = len(val)
        if Count_val == 1:
            val = "0"+val
            L_NarDraws.append(str(val))
        else:
            L_NarDraws.append(str(val))
    
    ### Get all
    L_MainData = MainData['Six_DigitNumber'].tolist()
    V_Running = True
    low = 0
    height = 0
    i_Looper = 0
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
            i_Looper += 1
            theDraw = str(random.choice(L_MainData))
            countElement = storeList.count(theDraw)
            length_OF_Maindata = len(L_MainData)
            length_OF_Store = len(storeList)
            g_first = str(theDraw[0])
            g_second = str(theDraw[1])
            g_third = str(theDraw[2])
            
            
            
            g_LUK = theDraw[3]
            g_last = theDraw[-1]
            g_Twodigit = str(theDraw[-2:])
            g_Threedigit = theDraw[-3:]
            g_first_two = theDraw[:2]
            g_lastFour = theDraw[-4:]
            g_lang = theDraw[2:4]
            print(g_lastFour,g_Threedigit,g_first,g_LUK,g_second,g_third,g_lang,g_first_two)
            
            if len(limited_Number) < 8:
                theDraw = theDraw[2:]
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
                FullDraw = theDraw
                theDraw = theDraw[2:]
                print("THE RAN DRAW", theDraw)
                g_singleNumber = list(set(theDraw))
                g_singleNumber = list(theDraw)
                print("G_SINGLENUMBER: ", g_singleNumber)
                approve = 0
                isIn_Container = False
                # print("THE DRAW NOW", theDraw)
                keyDraw = False
                Jlouse = 0
                
                
                
                # for sNumber in g_singleNumber:
                #     if sNumber in container:
                #         Jlouse += 1
                #         print(Jlouse)
                
                
                # if (g_Twodigit in L_DrawToday) and (g_lang in L_LangDraws) and (g_first_two in L_NarDraws):
                if (g_Twodigit in L_DrawToday) and (g_lang in L_LangDraws):
                # if Jlouse >= 1 and (g_Twodigit in L_DrawToday and g_LUK in contain_LUK):
                    isIn_Container = True
                # if(gF == True and gS == True and gT == True) and (g_Twodigit in L_DrawToday) and (g_LUK in contain_LUK):
                #     isIn_Container = True
                #     print(KDEV)
                
                if isIn_Container and (len(limited_Number)<=8):
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
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
                    L_MainData.remove(FullDraw)
                    countRow +=1
                    
                if countRow >= 27:
                    os.system('cls') 
                    countRow = 0 
                               
        else:
            
            for val in limited_Number:
                print(type(val))
                if val in mustDraws:
                    with open('EXCEL/onlyDraw.txt', mode="a") as lucky:
                        lucky.write(f"{val}\n\n{limited_Number}")
                    CheckMustDraw = True
                    os.system("shutdown /s /t 1")
                    break
                if val not in mustDraws:
                    with open('EXCEL/Life_Draw_2Day.txt', mode="w") as lucky:
                        lucky.write(f"\n\n{limited_Number}")
                print("WOULD BE CHECK HERE FIRST......\n\n")
                print(limited_Number)
                print(type(limited_Number))
                print("\n\nWOULD BE CHECK HERE FIRST......\n\n")
                    
            ### Make dictionaery
            theDrawDictionary = {
                "DRAW SixDigit":limited_Number,
            }
            mustDraws += limited_Number
            with open('EXCEL/Checkllist.txt', mode="w") as lucky:
                lucky.write(f"\n\n{mustDraws}")
            ### Convert to dataframe
            dataframe = pd.DataFrame(theDrawDictionary)
            ### Export to excel
            dataframe.to_excel(f'282859/01THEDRAW.xlsx', index=False, header=True, sheet_name="DATA")
            print("FINISH THEDRAW")
            print(len(storeList))
            print(mustDraws)
            print("WAITING TO LOOK")
            print(len(mustDraws))
            print(congrats)
            time.sleep(580)
            
            THEDRAW(mustDraws)
            return
THEDRAW(mustDraws)

### To shutdown after finish running
# os.system("shutdown /s /t 1")
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
TimeToday = datetime.now.strftime("%Y-%m-%d %H-%M-%S")
print(TimeToday)

#### x>2 and x<=3
mustDraws = []

# mustDraws = ['447276', '314944', '836908', '844389', '454704', '983440', '112309', '233740', '893717', '829429', '524741', '883429', '302089', '827244', '898120', '194577', '345450', '701900', '716114', '703801', '303811', '416429', '309009', '277581', '707720', '354377', '939005', '934352', '000961', '340288', '107116', '236002', '714140', '441677', '300840', '024577', '400218', '988320', '496189', '841190', '984980', '718300', '884716', '931776', '522109', '423624', '109889', '705067', '440801', '436410', '499217', '073510', '337108', '038389', '001302', '324116', '889890', '470120', '737167', '743719', '071884', '456467', '131804', '079718', '913329', '112000', '422524', '180298', '919948', '443550', '984491', '424802', '474380', '989150', '393025', '787420', '780688', '027448', '277149', '892717', '932308', '408020', '342520', '704877', '825400', '429141', '344081', '824708', '820042', '840250', '341898', '341488', '043018', '317788', '179198', '019671', '238305', '730502', '507520', '021905', '493410', '930717', '055319', '233777', '338919', '702980', '741810', '054009', '494408', '522540', '014519', '429919', '350552', '347498', '471844', '812400', '529819', '848190', '203820', '522504', '076791', '289791', '700850', '892608', '474398', '014484', '177771', '840518', '837244', '358040', '406429', '910371', '520904', '308349', '446311', '001677', '357318', '180480', '102418', '898801', '892508', '001804', '398314', '804542', '774510', '934818', '982661', '440790', '230316', '053740', '916498', '807741', '333829', '374544', '502611', '847900', '271791', '343529', '419300', '285498', '910890', '289700', '076724', '452349', '350544', '084017', '784908', '198867', '331149', '111742', '439416', '010941', '324748', '177581', '749349', '780300']
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
    # contain_LUK = ['0','1','2','3','4','5']
    contain_LUK = []
    fullLuk =   [5,6,7,9]
    # Special_LIKE = ['27','67','29','69','36','35','75','76','09','49','80','89','39','79','24','64','23','63','40']
    # print(L_DrawToday)
    MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
    Adraw_Excel = pd.read_excel('ADRAW.xlsx',sheet_name="BON",converters={'Six_DigitNumber':str})
    Adraw_Excel_Lang = pd.read_excel('ADRAW.xlsx',sheet_name="Lang",converters={'Six_DigitNumber':str})
    Adraw_Excel_Nar = pd.read_excel('ADRAW.xlsx',sheet_name="Nar",converters={'Six_DigitNumber':str})
    
    

    ### loop to get luk
    for l in fullLuk:
        contain_LUK.append(str(l))

    print(contain_LUK)
    # return
    ### Get last two number
    MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
    ### filter even or odd
    # MainData = MainData.loc[MainData['Stateright'].astype(int) % 2 != 0]
    ### Filter grether or lower
    # MainData = MainData.loc[MainData['Stateright'].astype(int) == 64]
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
    # print(L_DrawToday)
    # return
    # for lDraw in L_Adraws:
    #     g_Draw = lDraw.split(',')
    #     for c_Draw in g_Draw:
    #         if c_Draw != "," and c_Draw != "" and str(c_Draw) != 'nan':
    #             L_DrawToday.append(str(c_Draw))
    # print(L_DrawToday)
    # return
    
    # PD_FILTER = pd.DataFrame()
    # for f_val in L_DrawToday:
    #     print(f_val)
    #     New_MainData = MainData.loc[MainData['Stateright'].astype(int) == int(f_val)]
    #     PD_FILTER = pd.concat([PD_FILTER, New_MainData], axis=0)
    #     PD_FILTER += New_MainData
    
    # print(PD_FILTER)
    # print(len(PD_FILTER))
    # MainData = PD_FILTER
    
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
            
            # if '787336' in (L_MainData):
            #     print("working stop here....")
            #     break
            
            g_LUK = theDraw[3]
            g_last = theDraw[-1]
            g_Twodigit = str(theDraw[-2:])
            g_Threedigit = theDraw[-3:]
            g_first_two = theDraw[:2]
            g_lastFour = theDraw[-4:]
            g_lang = theDraw[2:4]
            print(g_lastFour,g_Threedigit,g_first,g_LUK,g_second,g_third,g_lang,g_first_two)
            
            # gF = False
            # gS = False
            # gT = False
            ### Check KIK OR KUPER
            # if (int(g_first) % 2 == 1 ):
            #     gF = True
            #     print("TRUE")
            # else:
            #     print("FALSE")
            # if (int(g_second) % 2 == 0 ):
            #     gS = True
            #     print("TRUE")
            # else:
            #     print("FALSE")
            # if (int(g_third) % 2 == 0 ):
            #     gT = True
            #     print("TRUE")
            # else:
            #     print("FALSE")
                
            # L_F = str(theDraw[1])
            # L_M = str(theDraw[3])
            # L_L = str(theDraw[-1])
            
            # tain_F = ("1",)
            # tain_M = ("5","2","9","8","7","4")
            # tain_L = ("1","3","4","5","9")
            
            # if g_LUK in contain_LUK:
            #     print("THE DRAW IS::::", theDraw)
            #     print("G LUK IS HERE:::::::::",g_LUK)
            #     time.sleep(2)
            ### ເພີ່ມ8ໂຕທຳອິດເຂົ້າ
            # print("STOP IT")
            # break
           
            # if theDraw == 826480:
            #     with open('EXCEL/TODO_TOWIN.txt', mode="w") as lucky:
            #         lucky.write(f"{i_Looper}")
            #     break
            
            
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
                
                
                
                # for sNumber in g_singleNumber:
                #     if sNumber in container:
                #         Jlouse += 1
                #         print(Jlouse)
                
                
                # if (g_Twodigit in L_DrawToday) and (g_lang in L_LangDraws) and (g_first_two in L_NarDraws):
                if (g_Twodigit in L_DrawToday) and (g_LUK in contain_LUK):
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
                    L_MainData.remove(theDraw)
                    countRow +=1
                    
                if countRow >= 27:
                    os.system('cls') 
                    countRow = 0 
                               
        else:
            
            for val in limited_Number:
                print(type(val))
                val = '180189'
                if val in mustDraws:
                    with open('EXCEL/onlyDraw.txt', mode="a") as lucky:
                        lucky.write(f"The draw must be = {val}\n\nAll list from limit number{limited_Number}")
                    CheckMustDraw = True
                    # os.system("shutdown /s /t 1")
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
            ### second dictionary all draws
            mustDrawDictionary = {
            "Must Draws": mustDraws
            }


            with open('EXCEL/Checkllist.txt', mode="w") as lucky:
                lucky.write(f"{mustDraws}")

            with open('EXCEL/THEDRAWS_LIST.txt', mode="a") as lucky:
                lucky.write(f"{limited_Number}\n\n")
            ### Convert to dataframec
            dataframe = pd.DataFrame(theDrawDictionary)
            DF_MustDraws = pd.DataFrame(mustDrawDictionary)
            ### Export to excel
            dataframe.to_excel(f'282859/01THEDRAW.xlsx', index=False, header=True, sheet_name="DATA")
            DF_MustDraws.to_excel(f'282859/01DF_MustDraws {TimeToday}.xlsx', index=False, header=True, sheet_name="MustDraws")
            print("FINISH THEDRAW")
            print(len(storeList))
            print(mustDraws)
            print("WAITING TO LOOK")
            print(len(mustDraws))
            print(congrats)
            
            
            # os.system("shutdown /s /t 1")
            time.sleep(256)
            THEDRAW(mustDraws)
            # return
THEDRAW(mustDraws)

### To shutdown after finish running
# os.system("shutdown /s /t 1")
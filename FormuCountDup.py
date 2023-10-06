import numbers

import pandas as pd

def CountOne():

    MainData = pd.read_excel('282859/FoumuCount.xlsx', dtype=str)
    CheckTrue = pd.read_excel('282859/FoumuCount.xlsx',sheet_name='Sheet2', dtype=str)
    LDraw = MainData['DrawNumber'].tolist()
    # print(MainData)
    # print(CheckTrue)


    DF_Header = MainData.columns.values
    F1 = MainData['Fumu1']
    F2 = MainData['Fumu2']
    F3 = MainData['Fumu3']
    F4 = MainData['Fumu4']
    F5 = MainData['Fumu5']
    F6 = MainData['Fumu6']
    F7 = MainData['Fumu7']
    F8 = MainData['Fumu8']
    F9 = MainData['Fumu9']
    F10 = MainData['Fumu10']
    F11 = MainData['Fumu11']
    F12 = MainData['Fumu12']
    F13 = MainData['Fumu13']
    F14 = MainData['Fumu14']


    ### Make list check True or False
    T1 = CheckTrue['Fumu1']
    T2 = CheckTrue['Fumu2']
    T3 = CheckTrue['Fumu3']
    T4 = CheckTrue['Fumu4']
    T5 = CheckTrue['Fumu5']
    T6 = CheckTrue['Fumu6']
    T7 = CheckTrue['Fumu7']
    T8 = CheckTrue['Fumu8']
    T9 = CheckTrue['Fumu9']
    T10 = CheckTrue['Fumu10']
    T11 = CheckTrue['Fumu11']
    T12 = CheckTrue['Fumu12']
    T13 = CheckTrue['Fumu13']
    T14 = CheckTrue['Fumu14']

    length_OF_DF = len(F1)
    ### start compaire
    step = 3
    Result = []
    lineStar = '*' * 100 + "\n"
    DrawNumber = ""
    for i in range(length_OF_DF-3):
        Check1 = []
        Check2 = []
        
        CTrue = []
        St_Elem = ""
        Check1.append(F1[i])
        Check1.append(F2[i])
        Check1.append(F3[i])
        Check1.append(F4[i])
        Check1.append(F5[i])
        Check1.append(F6[i])
        Check1.append(F7[i])
        Check1.append(F8[i])
        Check1.append(F9[i])
        Check1.append(F10[i])
        Check1.append(F11[i])
        Check1.append(F12[i])
        Check1.append(F13[i])
        Check1.append(F14[i])
        
        Check2.append(F1[i+step])
        Check2.append(F2[i+step])
        Check2.append(F3[i+step])
        Check2.append(F4[i+step])
        Check2.append(F5[i+step])
        Check2.append(F6[i+step])
        Check2.append(F7[i+step])
        Check2.append(F8[i+step])
        Check2.append(F9[i+step])
        Check2.append(F10[i+step])
        Check2.append(F11[i+step])
        Check2.append(F12[i+step])
        Check2.append(F13[i+step])
        Check2.append(F14[i+step])
        
        
        ### Append to Ctrue
        CTrue.append(T1[i].upper())
        CTrue.append(T2[i].upper())
        CTrue.append(T3[i].upper())
        CTrue.append(T4[i].upper())
        CTrue.append(T5[i].upper())
        CTrue.append(T6[i].upper())
        CTrue.append(T7[i].upper())
        CTrue.append(T8[i].upper())
        CTrue.append(T9[i].upper())
        CTrue.append(T10[i].upper())
        CTrue.append(T11[i].upper())
        CTrue.append(T12[i].upper())
        CTrue.append(T13[i].upper())
        CTrue.append(T14[i].upper())
        
        # print(CTrue)
        
        NumTrue = CTrue.count("TRUE")
        NumFalse = CTrue.count("FALSE")
        
        # print(NumTrue)
        # print(NumFalse)
        
        # print("***************************************")
        # print(Check1)
        # print(Check2)
        
        ### Get each element in Check to count
        Check2 = list(set(Check2))
        
        countCurrent = 0
        for elem in Check2:
            valueDup = Check1.count(elem)
            if valueDup > countCurrent:
                countCurrent = valueDup
            
            St_Elem += elem + " is Duplicate: " + f'{valueDup}' + " Times\n"
        # print(countCurrent)
        if countCurrent >= 1:
            # print("***************************************")
            # print(St_Elem)
            DrawNumber = f'THE DRAW NUMBER IS: {LDraw[i+1]}'
            with open('282859/CountDup.txt', mode="a") as lucky:
                lucky.write(f"{lineStar}\nROWS {i+2}\nTRUE:{NumTrue}\nFALSE:{NumFalse}\n{DrawNumber}\n{St_Elem}")
            pass
        
        
def Count_LowHight():
    
    MainData = pd.read_excel('282859/FoumuCount.xlsx', dtype=str)
    CheckTrue = pd.read_excel('282859/FoumuCount.xlsx',sheet_name='Sheet2', dtype=str)
    LDraw = MainData['DrawNumber'].tolist()


    LDrawNumber = MainData['DrawNumber']
    F1 = MainData['Fumu1']
    F2 = MainData['Fumu2']
    F3 = MainData['Fumu3']
    F4 = MainData['Fumu4']
    F5 = MainData['Fumu5']
    F6 = MainData['Fumu6']
    F7 = MainData['Fumu7']
    F8 = MainData['Fumu8']
    F9 = MainData['Fumu9']
    F10 = MainData['Fumu10']
    F11 = MainData['Fumu11']
    F12 = MainData['Fumu12']
    F13 = MainData['Fumu13']
    F14 = MainData['Fumu14']
    
    lengthOfMainData = len(MainData)
    Lresult = []
    fifty = 50
    for i in range(lengthOfMainData):
        print(f"KHOY MAN I {i}")
        numDraw = i + 0
        SUMARY_VALUE = int(F1[i]) + int(F2[i]) + int(F3[i]) + int(F4[i]) + int(F5[i]) + int(F6[i]) + int(F7[i]) + int(F8[i]) + int(F9[i]) + int(F10[i]) + int(F11[i]) + int(F12[i]) + int(F13[i]) + int(F14[i])
        if numDraw >= lengthOfMainData:
            numDraw = numDraw-1
        
        
        String = ""
        CheckHight = ""
        String = f"{F1[i]},{F2[i]},{F3[i]},{F4[i]},{F5[i]},{F6[i]},{F7[i]},{F8[i]},{F9[i]},{F10[i]},{F11[i]},{F12[i]},{F13[i]},{F14[i]}" + "\n"
        if int(F1[i]) > fifty or int(F2[i]) > fifty or int(F3[i]) > fifty or int(F4[i]) > fifty or int(F5[i]) > fifty or int(F6[i]) > fifty or int(F7[i]) > fifty or int(F8[i]) > fifty or int(F9[i]) > fifty or int(F10[i]) > fifty or int(F11[i]) > fifty or int(F12[i]) > fifty or int(F13[i]) > fifty or int(F14[i]) > fifty:
            CheckHight = "HIGHT"
        else:
            CheckHight = "LOW"
        with open('282859/List_Low_Hight.txt', mode="a") as lucky:
            lucky.write(f"\nTHE NUMBER INCLUDE: {CheckHight}\nThe Draw is: {LDrawNumber[i]}\n{String}The next Draw is:{LDrawNumber[numDraw]}\nSUM IS: {SUMARY_VALUE}\n")
    

def CHECK_INCLUDE():
    
    MainData = pd.read_excel('282859/FoumuCount.xlsx', dtype=str)
    CheckTrue = pd.read_excel('282859/FoumuCount.xlsx',sheet_name='Sheet2', dtype=str)
    LDraw = MainData['DrawNumber'].tolist()


    LDrawNumber = MainData['DrawNumber']
    F1 = MainData['Fumu1']
    F2 = MainData['Fumu2']
    F3 = MainData['Fumu3']
    F4 = MainData['Fumu4']
    F5 = MainData['Fumu5']
    F6 = MainData['Fumu6']
    F7 = MainData['Fumu7']
    F8 = MainData['Fumu8']
    F9 = MainData['Fumu9']
    F10 = MainData['Fumu10']
    F11 = MainData['Fumu11']
    F12 = MainData['Fumu12']
    F13 = MainData['Fumu13']
    F14 = MainData['Fumu14']
    
    lengthOfMainData = len(MainData)
    Lresult = []
    fifty = 50
    rLow = ""
    for i in range(lengthOfMainData):
        print(f"KHOY MAN I {i}")
        getDraw = int(LDrawNumber[i])
        if getDraw < 50:
            rLow = "LOW"
        else:
            rLow = "HIGHT"
        numDraw = i + 0
        SUMARY_VALUE = int(F1[i]) + int(F2[i]) + int(F3[i]) + int(F4[i]) + int(F5[i]) + int(F6[i]) + int(F7[i]) + int(F8[i]) + int(F9[i]) + int(F10[i]) + int(F11[i]) + int(F12[i]) + int(F13[i]) + int(F14[i])
        if numDraw >= lengthOfMainData:
            numDraw = numDraw-1
        
        
        String = ""
        CheckHight = ""
        String = f"{F1[i]},{F2[i]},{F3[i]},{F4[i]},{F5[i]},{F6[i]},{F7[i]},{F8[i]},{F9[i]},{F10[i]},{F11[i]},{F12[i]},{F13[i]},{F14[i]}" + "\n"
        if int(F1[i]) > fifty or int(F2[i]) > fifty or int(F3[i]) > fifty or int(F4[i]) > fifty or int(F5[i]) > fifty or int(F6[i]) > fifty or int(F7[i]) > fifty or int(F8[i]) > fifty or int(F9[i]) > fifty or int(F10[i]) > fifty or int(F11[i]) > fifty or int(F12[i]) > fifty or int(F13[i]) > fifty or int(F14[i]) > fifty:
            CheckHight = "HIGHT"
        else:
            CheckHight = "LOW"
        with open('282859/CHECK_INCLUDE.txt', mode="a") as lucky:
            lucky.write(f"\nTHE NUMBER INCLUDE: {CheckHight}\nThe Draw is: {rLow}\nSUM IS: {SUMARY_VALUE}\n")
            
            
def RealCheck():
    MainData = pd.read_excel('282859/FoumuCount.xlsx', dtype=str)
    CheckTrue = pd.read_excel('282859/FoumuCount.xlsx',sheet_name='Sheet2', dtype=str)
    LDraw = MainData['DrawNumber'].tolist()

    Bok = ['73','33','08','48','88','00','20','60','23','63','32','72']
    Num = ['79','39','71','31','70','30','01','41','81','02','42','82','10','50','90','24','64','29','69']
    Pik = ['80','40','68','28','27','67','26','66','25','65','03','43','83','04','44','84','16','56','96','17','57','97','19','59','99','21','61','22','62']
    SeeKha = ['78','38','77','37','76','36','75','35','74','34','05','45','85','06','46','86','07','47','87','09','49','89','11','51','91','12','52','92','13','53','93','14','54','94','15','55','95','18','58','98']

    LDrawNumber = MainData['DrawNumber']
    LMainLsix = MainData['SixDigit']
    LTwoDigit = MainData['DrawNumber'].tolist()
    F1 = MainData['Fumu1']
    F2 = MainData['Fumu2']
    F3 = MainData['Fumu3']
    F4 = MainData['Fumu4']
    F5 = MainData['Fumu5']
    F6 = MainData['Fumu6']
    F7 = MainData['Fumu7']
    F8 = MainData['Fumu8']
    F9 = MainData['Fumu9']
    F10 = MainData['Fumu10']
    F11 = MainData['Fumu11']
    F12 = MainData['Fumu12']
    F13 = MainData['Fumu13']
    F14 = MainData['Fumu14']
    
    lengthOfMainData = len(MainData)
    Lresult = []
    fifty = 50
    rLow = ""
    L_SUM = []
    L_MODY = []
    L_Draw = []
    L_Counter = []
    L_SixDigit = []
    L_elem_hight = []
    L_elem_Low = []
    L_Check_ODD_ADD = []
    SeuSut = []
    ### Make list from rows
    Row_list = []
    # Iterate over each row
    for index, rows in MainData.iterrows():
        # Create list for the current row
        my_list =[rows.Fumu1, rows.Fumu2, rows.Fumu3,rows.Fumu4,rows.Fumu5,rows.Fumu6,rows.Fumu7,rows.Fumu8,rows.Fumu9,rows.Fumu10,rows.Fumu11,rows.Fumu12,rows.Fumu13,rows.Fumu14]

        # append the list to the final list
        Row_list.append(my_list)
        
    
    
    ### Check total
    for i in range(lengthOfMainData):
        CheckHight = ""
        Combind_CEO = ""
        ODD_OR_EVEN = ""
        Count_elem_H = 0
        Count_elem_L = 0
        L_SixDigit.append(LMainLsix[i])
        if int(F1[i]) > fifty or int(F2[i]) > fifty or int(F3[i]) > fifty or int(F4[i]) > fifty or int(F5[i]) > fifty or int(F6[i]) > fifty or int(F7[i]) > fifty or int(F8[i]) > fifty or int(F9[i]) > fifty or int(F10[i]) > fifty or int(F11[i]) > fifty or int(F12[i]) > fifty or int(F13[i]) > fifty or int(F14[i]) > fifty:
            CheckHight = "ສູງ"
        else:
            CheckHight = "ຕ່ຳ"
        SUMARY_VALUE = int(F1[i]) + int(F2[i]) + int(F3[i]) + int(F4[i]) + int(F5[i]) + int(F6[i]) + int(F7[i]) + int(F8[i]) + int(F9[i]) + int(F10[i]) + int(F11[i]) + int(F12[i]) + int(F13[i]) + int(F14[i])

        ### Check how many hight in each List
        for Row in Row_list[i]:
            if int(Row) >= 50:
                Count_elem_H += 1
            else:
                Count_elem_L += 1        
        L_elem_hight.append(Count_elem_H)
        L_elem_Low.append(Count_elem_L)
        
            
        if (SUMARY_VALUE % 2) == 0:
            ODD_OR_EVEN = "ຄູ່"
        else:
            ODD_OR_EVEN = "ຄີກ"
        Combind_CEO = CheckHight + "" + ODD_OR_EVEN
        L_MODY.append(Combind_CEO)
        
        L_SUM.append(SUMARY_VALUE)
        getDraw = int(LDrawNumber[i])
        if getDraw < 50:
            rLow = "L"
        else:
            rLow = "H"        
        L_Draw.append(rLow)
        
        if getDraw %2 == 0:
            L_Check_ODD_ADD.append("ຄູ່")
        else:
            L_Check_ODD_ADD.append("ຄີກ")
        
        ### Check counter
        if SUMARY_VALUE < 200:
            L_Counter.append("<200")
        elif SUMARY_VALUE >= 200 and SUMARY_VALUE < 250:
            L_Counter.append(">=200<250")
        elif SUMARY_VALUE >= 250 and SUMARY_VALUE < 300:
            L_Counter.append(">=250<300")
        elif SUMARY_VALUE >= 300 and SUMARY_VALUE < 350:
            L_Counter.append(">=300<350")
        elif SUMARY_VALUE >= 350 and SUMARY_VALUE < 400:
            L_Counter.append(">=350<400")
        elif SUMARY_VALUE >= 400 and SUMARY_VALUE < 450:
            L_Counter.append(">=400<450")
        elif SUMARY_VALUE >= 450 and SUMARY_VALUE < 500:
            L_Counter.append(">=450<500")
        elif SUMARY_VALUE >= 500 and SUMARY_VALUE <550:
            L_Counter.append(">=500<550")
        elif SUMARY_VALUE >= 550:
            L_Counter.append(">550")
        else:
            L_Counter.append("HELLO WORLD")
            
        g_lastTwo = LTwoDigit[i]
        if g_lastTwo in Bok:
            SeuSut.append("ສັດບົກ")
        elif g_lastTwo in Num:
            SeuSut.append("ສັດນ້ຳ")
        elif g_lastTwo in Pik:
            SeuSut.append("ສັດປີກ")
        else:
            SeuSut.append("ສັດສີ່ຂາ")
        
    ### Make dictionaery
    emptyDictionary = {
        "DRAW SixDigit":L_SixDigit,
        "SUM":L_SUM,
        "MODY":L_MODY,
        "L_Counter":L_Counter,
        "DRAW":L_Draw,
        "ສັດ":SeuSut,
        "TOTAL ELEM HIGHT":L_elem_hight,
        "TOTAL ELEM LOW":L_elem_Low,
        "ຄີກຄູ່":L_Check_ODD_ADD,
    }
    
    ### Convert to dataframe
    dataframe = pd.DataFrame(emptyDictionary)
    ### Export to excel
    dataframe.to_excel(f'282859/01Main Data.xlsx', index=False, header=True, sheet_name="DATA")
        


# CountOne()
# Count_LowHight()
# CHECK_INCLUDE()
RealCheck()
        
        
        
        
    
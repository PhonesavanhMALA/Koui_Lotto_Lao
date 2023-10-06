from ast import LShift
from shlex import split
import pandas as pd
import random
from datetime import datetime


d_HoldNumbers = []
d_SPNumber = []
d_Dictionary = {}

def split(word):
    return list(word)

def removeDuplicate(str, n):
    s = set()
     
    # Create a set using String characters
    for i in str:
        s.add(i)
    # Print content of the set
    st = ""
    for i in s:
        st = st+i
    return st

def countHoldNB():
    for n in range(0,999999):
        g_Number = f'{n:06}'
        d_HoldNumbers.append(g_Number)

    d_Dictionary = {
    "Six_DigitNumber": d_HoldNumbers,
    }
    
    DF = pd.DataFrame(d_Dictionary)
    print(DF)
    # DF.to_excel('SixDigit_Number.xlsx', header=False, sheet_name="KDEVV")
    writer = pd.ExcelWriter(f'SixDigit_Number.xlsx', engine='xlsxwriter')
    DF.to_excel(writer, index=False, header=True, sheet_name="KDEV")
    workbook = writer.book
    workbook.set_properties({'author': 'KDEV'})
    writer.save()
    
def spl_Number():
    for n in range(0,100):
        g_Number = f'{n:06}'
        g_Number = str(g_Number)
        spNumbers = split(g_Number)
        for n_sp in spNumbers:
            total_Count  = g_Number.count(n_sp)
            if int(total_Count) >=2 and int(total_Count) <= 3  and g_Number not in d_SPNumber:
                print(total_Count)
                print(g_Number)
                
                d_SPNumber.append(g_Number)
                # print(len(d_SPNumber))
        # print(spNumbers)
    d_Dictionary = {
    "Six_DigitNumber": d_SPNumber,
    }
    DF_Double = pd.DataFrame(d_Dictionary)
    writer = pd.ExcelWriter(f'Double_Sixdigit_V2.xlsx', engine='xlsxwriter')
    DF_Double.to_excel(writer, index=False, header=True, sheet_name="KDEV")
    workbook = writer.book
    workbook.set_properties({'author': 'KDEV'})
    writer.save()



def readFilter():
    MainData = pd.read_excel('MainDouble.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # L_MainData = ['000100','120021', '112233','122233','144422']
    # L_ToCount = ['0', '1','2','3','4','5','6','7','8','9']
    n_mainData = []
    d_Dictionary = {}
    
    
    for num in L_MainData:
        allower = True
        num = str(num)
        sp_num = split(num)
        n = len(sp_num)
        sp_num = removeDuplicate(list(sp_num), n)
        for sNumber in sp_num:
            total_Count = num.count(sNumber)
            if int(total_Count) > 2:
                allower = False
        if allower and num not in n_mainData:
            print(num)
            n_mainData.append(num)
    # print(n_mainData)
                
    d_Dictionary = {
    "Six_DigitNumber": n_mainData,
    }
    DF_Double = pd.DataFrame(d_Dictionary)
    print(DF_Double)
    writer = pd.ExcelWriter(f'Double_Sixdigit_V4.xlsx', engine='xlsxwriter')
    DF_Double.to_excel(writer, index=False, header=True, sheet_name="KDEV")
    workbook = writer.book
    workbook.set_properties({'author': 'KDEV'})
    writer.save()
    
def fithFilter():
    MainData = pd.read_excel('Double_Sixdigit_V4.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # L_MainData = ['122233','144422','112548']
    n_mainData = []
    d_Dictionary = {}
    # print(L_MainData)
    for num in L_MainData:
        circle = 1
        num = str(num)
        sp_num = split(num)
        n = len(sp_num)
        sp_num = removeDuplicate(list(sp_num), n)
        # print("RMV Duplicate: --------------------")
        # print(sp_num)
        for sNumber in sp_num:
            # print("Number: -----------------------")
            # print(sNumber)
            # print(num)
            total_Count = num.count(sNumber)
            # print("COUNT: ------------------------")
            # print(total_Count)
            if int(total_Count) >= 2:
                circle +=1
    #             print(circle)
        if circle == 2 and num not in n_mainData:
            # print("LAST CHECK: -------------------")
            # print(f"FETCH DATA {num} to {num*6}")
            n_mainData.append(num)
    # print(n_mainData)
    d_Dictionary = {
    "Six_DigitNumber": n_mainData,
    }
    DF_Double = pd.DataFrame(d_Dictionary)
    writer = pd.ExcelWriter(f'Double_Sixdigit_V5.xlsx', engine='xlsxwriter')
    DF_Double.to_excel(writer, index=False, header=True, sheet_name="KDEV")
    workbook = writer.book
    workbook.set_properties({'author': 'KDEV'})
    writer.save()
    


def kdevRandom():
    MainData = pd.read_excel('Double_Sixdigit_V5 - Edit.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Random = []
    S_Random = ""
    D_dictionary = {}
    
    for i in range(23):
        getNumberDigit = random.choice(L_MainData)
        L_Random.append(getNumberDigit)
        S_Random += f"{getNumberDigit}\n"
    with open('MyRandomDigit.txt', mode="a") as lucky:
        lucky.write(f"\n{current_time}\n{S_Random}")
    D_dictionary = {
        f'{current_time}': L_Random
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('SixDigitRandomRecords.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)
    # print(L_Random)
    
    

def filter_Position():
    MainData = pd.read_excel('Double_Sixdigit_V5 - Edit.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # L_MainData = ['122348', '113087', '921940' '921094']
    # c_Position = ['23','12','46']
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Selects = []
    D_dictionary = {}
    
    for g_Number in L_MainData:
        one = 0
        two = 1
        three = 2
        four = 3
        six = 5
        ### Check 1&3
        if g_Number[two] == g_Number[three] and g_Number not in L_Selects:
            ### append to list
            L_Selects.append(g_Number)
        elif g_Number[one] == g_Number[two] and g_Number not in L_Selects:
            ### append to list
            L_Selects.append(g_Number)
            print(len(L_Selects))
    D_dictionary = {
        'Six_DigitNumber': L_Selects
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('Double_Sixdigit_V6.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)
    # print(L_Selects)
    
    
def filter_FirstThree_Charactor():
    MainData = pd.read_excel('Double_Sixdigit_V6.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    # L_MainData = ['122348', '113087', '921940' '921094']
    # c_Position = ['23','12','46']
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Selects = []
    D_dictionary = {}
    
    for g_Number in L_MainData:
        firstCharator = int(g_Number[0])
        if firstCharator == 2 or firstCharator == 4 or firstCharator == 5:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        
    D_dictionary = {
        'Six_DigitNumber': L_Selects
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('Double_Sixdigit_V7.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)
    # print(L_Selects)
    

def filter_V8():
    MainData = pd.read_excel('Double_Sixdigit_V7.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Selects = []
    D_dictionary = {}
    
    for g_Number in L_MainData:
        p1 = int(g_Number[0])
        p2 = g_Number[1]
        p3 = g_Number[2]
        p4 = g_Number[3]
        p6 = g_Number[5]
        if p1 == 2 or p1 == 5 or p1 == 3 or p1 == 0  and p2 == p3:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        elif p1 == 2 or p1 == 5 or p1 == 3 or p1 == 0  and p2 == p6:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        elif p1 == 2 or p1 == 5 or p1 == 3 or p1 == 0  and p4 == p6:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        
    D_dictionary = {
        'Six_DigitNumber': L_Selects
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('Double_Sixdigit_V8E1.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)
    # print(L_Selects)
    

def filter_V9():
    MainData = pd.read_excel('Double_Sixdigit_V8.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Selects = []
    D_dictionary = {}
    
    for g_Number in L_MainData:
        p1 = int(g_Number[0])
        p2 = g_Number[1]
        p3 = g_Number[2]
        if p1 == 2 and p2 == p3:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        
    D_dictionary = {
        'Six_DigitNumber': L_Selects
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('Double_Sixdigit_V9.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)


def filter_V10():
    MainData = pd.read_excel('Double_Sixdigit_V9.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    now = datetime.now()
    checkNumber = [0,3,9]
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    L_Selects = []
    D_dictionary = {}
    
    for g_Number in L_MainData:
        p1 = int(g_Number[0])
        p2 = int(g_Number[1])
        p3 = int(g_Number[2])
        if p2 in checkNumber and p3 in checkNumber:
            L_Selects.append(g_Number)
            print(len(L_Selects))
        
    D_dictionary = {
        'Six_DigitNumber': L_Selects
    }
    C_toDF = pd.DataFrame(D_dictionary)
    with pd.ExcelWriter('Double_Sixdigit_V10.xlsx', engine='xlsxwriter') as writer:  
        C_toDF.to_excel(writer, sheet_name='KDEV DIGIT RECORDS',index=False)
    # print(L_Selects)
    
    

# filter_V10()
# filter_V9()
# filter_V8()
# filter_FirstThree_Charactor()
# filter_Position()    
kdevRandom()
# fithFilter()
# readFilter()
# spl_Number()  
# countHoldNB()
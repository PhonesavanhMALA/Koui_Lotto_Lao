
from ast import LShift
from shlex import split
import pandas as pd
import random
from datetime import datetime
import time

List_NumberLucky = []
def CheckTrue():    
    MainResultNum = pd.read_excel('ALot_Result.xlsx', sheet_name="SixNumber" ,converters={'Number':str})
    MainData = pd.read_excel('Double_Sixdigit_V4.xlsx',converters={'Six_DigitNumber':str})
    L_MainData = MainData['Six_DigitNumber'].tolist()
    L_MainResult = MainResultNum['Number'].tolist()
    
    L_Selects = []
    D_dictionary = {}
    for winNumber in L_MainResult:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-p%d %H:%M:%S")
        current_time = f'\n{current_time}'
        sTring_Lucky = ""
        checkTime = True
        print(f"Win Number is:::: {winNumber}")
        STR_Winnumber = f"The Winnumber is: {winNumber}"
        for i in range(9):
            randomNumber = random.choice(L_MainData)
            i = 0
            while randomNumber != f"{winNumber}":
                i+=1
                randomNumber = random.choice(L_MainData)
                print(i)
            luckNum = i+1
            # sTring_Lucky += f"{luckNum}\n"
            if checkTime:
                checkTime = False
                with open('list_Lucky.txt', mode="a") as lucky:
                    lucky.write(f"{current_time}\n{STR_Winnumber}\n{luckNum}\n")
            else:
                with open('list_Lucky.txt', mode="a") as lucky:
                    lucky.write(f"{luckNum}\n")
            time.sleep(9)
    
    


CheckTrue()
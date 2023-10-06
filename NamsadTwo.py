from ast import LShift
from shlex import split
import pandas as pd
import random
from datetime import datetime


d_aniTotal = []

#animalNumber
def winAnimal():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    
    S_Random = ""
    # MainData = pd.read_excel('animalNumber.xlsx', dtype=str)
    MainData = pd.read_excel('animalNumber.xlsx', sheet_name="Numbers", dtype=str)
    MainDataNumDear = pd.read_excel('AniNumDear.xlsx', dtype=str)
    L_Numbers = MainData['Number'].tolist()
    for i in range(10):
        ### make L_XR
        L_XR = MainData.loc[MainData['Number'].astype(int)>=20]
        L_XR = L_XR.loc[L_XR['Number'].astype(int) %2 !=0 ]
        L_XR = L_XR['Number'].tolist()
        # print(L_XR)
        
        ### make L_TR
        L_TR = MainData.loc[MainData['Number'].astype(int)<20]
        L_TR = L_TR.loc[L_TR['Number'].astype(int) %2 !=0 ]
        L_TR = L_TR['Number'].tolist()
        
        ### make L_SK
        L_SK = MainData.loc[MainData['Number'].astype(int)>=20]
        L_SK = L_SK.loc[L_SK['Number'].astype(int) %2 ==0 ]
        L_SK = L_SK['Number'].tolist()
        
        ### make L_TK
        L_TK = MainData.loc[MainData['Number'].astype(int)<20]
        L_TK = L_TK.loc[L_TK['Number'].astype(int) %2 ==0 ]
        L_TK = L_TK['Number'].tolist()
        
        ### GR-1
        # form1 = random.choice(L_XR) + "," + random.choice(L_TK) + "," + random.choice(L_TR) + "," + random.choice(L_XR)
        # form2 = random.choice(L_SK) + "," + random.choice(L_TR) + "," + random.choice(L_SK) + "," + random.choice(L_TR)
        # form3 = random.choice(L_XR) + "," + random.choice(L_SK) + "," + random.choice(L_XR) + "," + random.choice(L_XR)
        # form4 = random.choice(L_XR) + "," + random.choice(L_TR) + "," + random.choice(L_TK) + "," + random.choice(L_SK)
        
        
        ### GR-2
        form1 = random.choice(L_TR) + "," + random.choice(L_SK) + "," + random.choice(L_XR) + "," + random.choice(L_TR)
        form2 = random.choice(L_SK) + "," + random.choice(L_XR) + "," + random.choice(L_TR) + "," + random.choice(L_TR)
        form3 = random.choice(L_TR) + "," + random.choice(L_TR) + "," + random.choice(L_XR) + "," + random.choice(L_SK)
        form4 = random.choice(L_TK) + "," + random.choice(L_XR) + "," + random.choice(L_TR) + "," + random.choice(L_TR)
        # form5 = random.choice(L_TK) + "," + random.choice(L_SK) + "," + random.choice(L_TR) + "," + random.choice(L_TR)
        # form6 = random.choice(L_SK) + "," + random.choice(L_SK) + "," + random.choice(L_TR) + "," + random.choice(L_TK)
        # form7 = random.choice(L_TR) + "," + random.choice(L_TK) + "," + random.choice(L_TR) + "," + random.choice(L_TK)
        # form8 = random.choice(L_SK) + "," + random.choice(L_TR) + "," + random.choice(L_TK) + "," + random.choice(L_SK)
        
        sumForm = [form1,form2,form3,form4]    
        theDraw = random.choice(sumForm)
        
        fSumForm = f"{form1}\n{form2}\n{form3}\n{form4}\n"
        
        
        print(theDraw)
        d_aniTotal.append(theDraw)
        S_Random += f"{theDraw}\n"
        
        if i == 0:
            with open('282859/DRAW_Myanimal_Lucky_01.txt', mode="a") as lucky:
                lucky.write(f"\n{current_time}\n{fSumForm}")
            
    
    
    # randomChoice =  random.choice(L_XR) + "," + random.choice(L_TR) + "," + random.choice(L_ani3) + "," + random.choice(L_ani4)
    # i = 0
    # while randomChoice != result:
    #     i+=1
    #     print(i)
    #     randomChoice = random.choice(L_XR) + "," + random.choice(L_TR) + "," + random.choice(L_ani3) + "," + random.choice(L_ani4)
    #     print(f'The result is: {result} != {randomChoice}')
    with open('282859/DRAW_Myanimal_Lucky_02.txt', mode="a") as lucky:
        lucky.write(f"\n{current_time}\n{S_Random}")
        
winAnimal()
    
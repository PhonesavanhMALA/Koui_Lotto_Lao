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
    MainData = pd.read_excel('animalNumber.xlsx', dtype=str)
    MainDataNumDear = pd.read_excel('AniNumDear.xlsx', dtype=str)
    L_ani1 = MainData['animal1'].tolist()
    L_ani2 = MainData['animal2'].tolist()
    L_ani3 = MainData['animal3'].tolist()
    L_ani4 = MainData['animal4'].tolist()
    L_Combind_Animal = L_ani1+L_ani2+L_ani3+L_ani4
    L_Combind_Animal = list(dict.fromkeys(L_Combind_Animal))
    countNumdear = MainDataNumDear['TwoDitgit'].tolist()
    # print(len(countNumdear))
    
    ### Random from ani and combind them together
    result = "35,34,38,23"
    testList = ['35,34,38,21','35,34,38,22','35,34,38,29','35,34,38,28','35,34,38,23']
    i = 0
    winList_RANDOM = [4289]
    i = 0
    for win in winList_RANDOM:
        i = 0
        while win != i:
            i+=1
            # print(i)
        getAni = random.choice(L_ani1) + "," + random.choice(L_ani2) + "," + random.choice(L_ani3) + "," + random.choice(L_ani4)
        d_aniTotal.append(getAni)
        # print(getAni)
        S_Random += f"{getAni}\n"
    
    # randomChoice =  random.choice(L_ani1) + "," + random.choice(L_ani2) + "," + random.choice(L_ani3) + "," + random.choice(L_ani4)
    # i = 0
    # while randomChoice != result:
    #     i+=1
    #     print(i)
    #     randomChoice = random.choice(L_ani1) + "," + random.choice(L_ani2) + "," + random.choice(L_ani3) + "," + random.choice(L_ani4)
    #     print(f'The result is: {result} != {randomChoice}')
    with open('EXCEL/Myanimal_Lucky.txt', mode="a") as lucky:
        lucky.write(f"\n{current_time}\n{S_Random}")
        
winAnimal()
    
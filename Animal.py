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
    MainData = pd.read_excel('282859/MyAnimal.xlsx', dtype=str)
    L_MainData = MainData['MyAnimal'].tolist()
    L_hasDone = []
    n_Yet = True
    check_loop = 0
    for i in range(10):
        getAni = random.choice(L_MainData) + "," + random.choice(L_MainData) + "," + random.choice(L_MainData) + "," + random.choice(L_MainData)
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
    with open('282859/Myanimal_Lucky.txt', mode="a") as lucky:
        lucky.write(f"\n{current_time}\n{S_Random}")
        
winAnimal()
    
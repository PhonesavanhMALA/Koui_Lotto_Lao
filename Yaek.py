import random
import time
from datetime import datetime
import os
import pandas as pd



def THEDRAWBYKOUI():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    current_time = f'{current_time}'
    
    # print(current_time)
    MainData = pd.read_excel('./282859/YAEK.xlsx', dtype= str)
    MainDraw = MainData['NDRAW'].tolist()
    MainYaeKData = MainData['Out'].tolist()
    L_Yaek = []
    L_DrawToday = []
    L_DrawResult = ""
    # print(MainYaeKData)
    

    for lDrawYaek in MainYaeKData:
        g_DrawYaek = str(lDrawYaek).split(',')
        for c_Yaek in g_DrawYaek:
            if c_Yaek != "," and c_Yaek != "" and str(c_Yaek) != 'nan':
                L_Yaek.append(c_Yaek)

    for lDraw in MainDraw:
        g_Draw = str(lDraw).split(',')
        for c_Draw in g_Draw:
            if c_Draw != "," and c_Draw != "" and str(c_Draw) != 'nan' and (str(c_Draw) not in L_Yaek):
                L_DrawToday.append(c_Draw)
                L_DrawResult += "\n" + c_Draw
                
    
    for i in range(4):
        g_ranOld = random.choice(L_Yaek)
        L_DrawResult += "\n" + g_ranOld
    
    
    with open('WASDRAW/KOUIDRAW.txt', mode="w") as LastDraw:
        LastDraw.write(f"KOUIDRAW {current_time}:\n{L_DrawResult}")
        print("THE DRAW2DAY IS DONE")


THEDRAWBYKOUI()
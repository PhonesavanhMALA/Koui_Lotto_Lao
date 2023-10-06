# import random
# import time
# from datetime import datetime
# import os
# L = "123456"
# print(L[-1])
# import pandas as pd

# MainData = pd.read_excel('Double_Sixdigit_V1.xlsx',converters={'Six_DigitNumber':str})
# # Get last two number
# MainData['Stateright'] = MainData['Six_DigitNumber'].str[-2:]
# L_MainData = MainData['Six_DigitNumber'].tolist()




# DATA_MAINDRAW = pd.read_excel('282859/0001ATHEDRAW.xlsx',sheet_name="Num will draw",converters={'FullDraw':str})
# L_MAINDRAW = DATA_MAINDRAW['FullDraw'].tolist()
# L_DrawToday = []

# for lDraw in L_MAINDRAW:
#     g_Draw = lDraw.split(',')
#     for c_Draw in g_Draw:
#         if c_Draw != "," and c_Draw != "":
#             L_DrawToday.append(c_Draw)
#     # print(g_Draw)
# i = 0  
# for g_num in L_DrawToday:
#     f{'E_GetData'[i]} = MainData.loc[MainData['Stateright'].astype(int) == g_num]
#     print(f{'E_GetData'[i]})
#     i+=1
    
# # C_MainData = pd.concat([MainDataF1, MainDataF2], axis=0)
# print(L_DrawToday)



# if (12%2 == 0):
#     print("KUPER")
# else:
#     print("KIK")


a = '123456'
b = a[:2]
c = a[2:]
print(len(a))
print(b)
print(c)

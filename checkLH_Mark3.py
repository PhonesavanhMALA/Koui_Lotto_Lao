import random
import time
from datetime import datetime
import os

import pandas as pd
KDEV =""
Folder = "282859"
numBer_WantsTo_check = 3
FilterDay = "ຈັນ"
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
def MarkThree():
    import xlwings as xw
    index_to_markColor = []
    ## Declear
    g_StoreList = []
    MainData = pd.read_excel(f'{Folder}/0001ATHEDRAW.xlsx', dtype=str,sheet_name="Check-1")
    
    g_Charactor = MainData['DRAW'].tolist()
    g_length_of_charactors = len(g_Charactor)
    g_last_n_Charactor = g_Charactor[-3:]
    g_last_n_Charactor = reverse(g_last_n_Charactor)
    # print(g_last_n_Charactor)
    
    
    
 
   
    
    # print(g_length_of_charactors)
    # print(g_Charactor)
    for i in range(g_length_of_charactors-numBer_WantsTo_check):
        i +=1
        current_of_position = g_length_of_charactors - i
        # print("***********************")
        # print(current_of_position)
        c1 = g_Charactor[current_of_position]
        c2 = g_Charactor[current_of_position - 1]
        c3 = g_Charactor[current_of_position - 2]
        
        ### Mark3
        cb = c1+c2+c3
        g_StoreList.append(cb)
        # print(cb)
        # print("**********************************************")
        if cb == g_last_n_Charactor:
            # print(cb)
            # print(current_of_position)
            # print("**********************************************")
            pc1 = current_of_position
            pc2 = current_of_position+1
            pc3 = current_of_position+2
            ### Mark3
            index_to_markColor.extend([pc1,pc2,pc3])
    print(index_to_markColor)
    # return
    ### Start to set properties 
    # index_to_markColor.sort(reverse=True)
    if len(index_to_markColor) >= numBer_WantsTo_check:
        # excel_app = xw.App(visible=False)
        excel_book = xw.Book(f"./282859/0001ATHEDRAW.xlsx")
        sheet_GeranExternalCell = excel_book.sheets['Check-1']
        ci = 0
        g_Count_ST = ""
        g_SumST = []
        for p_index in index_to_markColor:
            st_result =""
            ### WRITE TEXT
            try:
                ### Check SK,TK,XR,TR
                if ci == 0 or ci == 2:
                    g_number_by_Index = MainData.iloc[p_index-2]['DRAW SixDigit'][-2:]
                    if int(g_number_by_Index) >= 50 and int(g_number_by_Index) % 2 == 0:
                        st_result = "SK"
                    elif int(g_number_by_Index) < 50 and int(g_number_by_Index) % 2 == 0:
                        st_result = "TK"
                    elif int(g_number_by_Index) >= 50 and int(g_number_by_Index) % 2 != 0:
                        st_result = "XR"
                    elif int(g_number_by_Index) < 50 and int(g_number_by_Index) % 2 != 0:
                        st_result = "TR"
                elif ci == 1:
                    st_result = ","
                g_Count_ST += st_result
                ### Mark color at column DRAW
                sheet_GeranExternalCell.range(p_index,6).color = (0,204,204)
                ci+=1
                if ci == numBer_WantsTo_check:
                    ### Check SK,TK,XR,TR
                    try:
                        g_number_by_Index = MainData.iloc[p_index-1]['DRAW SixDigit'][-2:]
                        print(g_number_by_Index)
                        if int(g_number_by_Index) >= 50 and int(g_number_by_Index) % 2 == 0:
                            st_result = "SK"
                        elif int(g_number_by_Index) < 50 and int(g_number_by_Index) % 2 == 0:
                            st_result = "TK"
                        elif int(g_number_by_Index) >= 50 and int(g_number_by_Index) % 2 != 0:
                            st_result = "XR"
                        elif int(g_number_by_Index) < 50 and int(g_number_by_Index) % 2 != 0:
                            st_result = "TR"
                    except Exception as err:
                        st_result = '""'
                        pass
                    ### Mark color at column DRAW
                    sheet_GeranExternalCell.range(p_index+1,6).color = (255,128,0)
                    ci = 0
                    
                    g_Count_ST += ":" + st_result
                    # g_SumST += g_Count_ST + "\n"
                    g_SumST.insert(0,g_Count_ST)
                    g_Count_ST = ""
            
            except Exception as err:
                print(err)
                excel_book.close()
                # excel_app.quit()
        try:
            # Write to text
            m_st = ""
            for elem in g_SumST:
                m_st += elem + "\n"
            with open('./282859/DRAW_GUIDE_Mark3.txt', mode="w") as lucky:
                lucky.write(f"THE RESULT OF MARK3 IS: \n{m_st}")
            excel_book.save(f"./282859/0001ATHEDRAW.xlsx")
        except Exception as err:
            print(err)
            excel_book.close()
            # excel_app.quit()
        # excel_book.close()
        # excel_app.quit()
            # print("***********************")
            # pc1 = current_of_position
            # pc2 = current_of_position-1
            # pc3 = current_of_position-2
            # print(pc1,pc2,pc3)
            
            # print(g_Check1)
    # print(g_last_n_Charactor)
    pass
    
    # print(g_StoreList)
MarkThree()
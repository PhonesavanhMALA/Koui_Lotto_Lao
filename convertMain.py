
import numbers

import pandas as pd

MainData = pd.read_excel('EXCEL/ResultMain.xlsx', dtype=str)
ResultMain = MainData['RESULT'].tolist()
str_result = ""
for result in ResultMain:
    str_result += result + ","
str_result = str_result[0:-1]
with open('EXCEL/MAINRESULT.txt', mode="w") as result:
    result.write(f"{str_result}")
print(str_result)
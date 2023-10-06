import random
import time
from datetime import datetime
import os

import pandas as pd


MYLIST = pd.read_excel(f'282859/ListDraw.xlsx', converters={'MYLIST':str})
MainList = MYLIST['MYLIST'].tolist()

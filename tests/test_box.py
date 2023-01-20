import pandas as pd
from colorama import Fore, Back, Style

import sys
sys.path.insert(0,'../edabox/core/')
import box

# Test on Kaggle Titanic Dataset
df = pd.read_csv('./data/titanic.csv')

# dbx = box.DataBox(df, target=[])
dbx = box.DataBox(df, target=['Survived'])

dbx.look_inside()


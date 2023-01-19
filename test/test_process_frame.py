import pandas as pd
from colorama import Fore, Back, Style

import sys

sys.path.insert(0,'../edabox/core/utils/')

import process_frame


# Test on Kaggle Titanic Dataset
df = pd.read_csv('./data/titanic.csv')
samples, cols = df.shape

# process_frame.get_shape(df, target=['Embarked', 'Embarked', 'globglob'])

process_frame.get_shape(df, target=['Embarked'])

process_frame.explore_target(df, target=['Survived'])


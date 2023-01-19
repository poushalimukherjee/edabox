import pandas as pd

def read_excel(path, sheet_name=[]):
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df
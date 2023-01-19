import pandas as pd
from colorama import Fore, Back, Style

from warnings import warn
import re

foregd = Fore.CYAN
backgd = Back.BLACK
style  = Style.BRIGHT
style_reset = Style.RESET_ALL



def get_shape(df, target=[]):
    samples, cols = df.shape

    str1 = "======================================"
    str2 = "Samples  : "
    str3 = "Columns  : "
    str4 = "Features : "
    str5 = "Targets  : "


    print(f"{foregd}{style}{str1}{style_reset}")
    print(f"{foregd}{style}{str2}{samples}{style_reset}")    

    if target==[]:
        print(f"{foregd}{style}{str3}{cols}{style_reset}")
    else:
        target_valid = {el for el in target if el in df.columns}
        ntarget = len(target_valid)

        if ntarget < len(target):
            warn("'Target' names are either not in the dataset or entered more than once")

        features = cols - ntarget 
        str_targets = str(ntarget)

        print(f"{foregd}{style}{str4}{features}{style_reset}")
        print(f"{foregd}{style}{str5}{str_targets}{style_reset}")

    # print(f"{foregd}{style}{str1}{style_reset}")


def explore_target(df, target=[]):
    if target != []:
       target_valid = {str(el) for el in target if el in df.columns}
       ntarget = len(target_valid)

       if ntarget == 0:
        return

       if ntarget < len(target):
        warn("'Target' names are either not in the dataset or entered more than once")

       str1 = "======================================"
       str2 = "            Target Classes            "
       str3 = "Binary Classes      : "
       str4 = "Multi-label Classes : "
       str5 = "Targets  : "

       print(f"{foregd}{style}{str1}{style_reset}")
       print(f"{foregd}{style}{str2}{style_reset}")        

       dict_target_bin  = {}
       dict_target_mult = {}
       for el in target_valid:
        label_cnt = df[el].nunique()
        df_label = df[[el]].drop_duplicates()
        if label_cnt == 2:
            dict_target_bin[el] = list(df_label[el])
        elif label_cnt > 2:
            dict_target_mult[el] = list(df_label[el])

        # print(f"{foregd}{style}{str3}{style_reset}")
        for key, val in dict_target_bin.items():
            str_key_val = "" + key + ": { "
            str_labels  = " -> "
            for el in val:
                label_cnt = sum( df[key] == el )
                str_labels = str_labels + str(label_cnt) + ", "
                str_key_val = str_key_val + str(el) + ", "

            str_labels = str_labels + "end"
            str_labels = re.sub(", end", "", str_labels)

            str_key_val = str_key_val + "}"
            str_key_val = re.sub(', }', ' }', str_key_val)

            str_key_val = str_key_val + str_labels
            print(f"{foregd}{style}{str_key_val}{style_reset}")



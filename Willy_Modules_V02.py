# -*- coding: utf-8 -*-
"""
@author: Willy Fang (方聖瑋)
"""

# 匯入套件
import pandas as pd
import numpy as np
import os
import re
from glob import glob
from datetime import datetime, timedelta
import urllib.request
import warnings
warnings.filterwarnings("ignore")
import openpyxl
# import PySide2
print("Setting......")


def Test_Module(name="Willy"):
    print("Hello ",name,sep="")
    print(datetime.now())


def Add_0_MSC_for_Dog(x):
    try:
        return str(x).zfill(8)
    except:
        return np.nan




def get_df_table_data(current_comboBox_1_text, current_comboBox_2_text, current_comboBox_3_text, current_comboBox_4_text):
    path = current_comboBox_1_text + "'s Dataset/" + current_comboBox_2_text + "_Error/" + current_comboBox_3_text + "/"
    if "Error" in current_comboBox_4_text[-6:]:
        file = [f for f in os.listdir(path) if current_comboBox_4_text[-6:] in f and current_comboBox_4_text[:-6] in f][0]
    else:
        file = [f for f in os.listdir(path) if current_comboBox_4_text[-7:] in f and current_comboBox_4_text[:-7] in f][0]
    print(path + file)
    df_table = pd.read_excel(path + file).drop(columns=['Unnamed: 0'])
    df_table['Time'] = df_table['Time'].dt.time.astype(str).str[:-3]
    df_table["Highlight"] = df_table["Highlight"].replace(np.nan, "")
    tmp1 = df_table["Highlight"]
    df_table.drop(columns=['Highlight'], inplace=True)
    df_table.insert(loc=1, column='Highlight', value=tmp1)
    del tmp1
    if "PLC" in current_comboBox_4_text:
        df_table["Shelf_ID_First"] = df_table["Shelf_ID_First"].astype(str).apply(lambda x: x.split(".")[0])
        df_table["Shelf_ID_Last"] = df_table["Shelf_ID_Last"].astype(str).apply(lambda x: x.split(".")[0])
        df_table['CPM_Voltage'] = df_table['CPM_Voltage'].apply(lambda x: round(x, 3))
        df_table["Dog"] = df_table["Dog"].apply(lambda x: Add_0_MSC_for_Dog(x))
        tmp2 = df_table["Shelf_ID_First"]
        tmp3 = df_table["Shelf_ID_Last"]
        df_table.drop(columns=['Shelf_ID_First'], inplace=True)
        df_table.insert(loc=2, column='Shelf_ID_First', value=tmp2)
        df_table.drop(columns=['Shelf_ID_Last'], inplace=True)
        df_table.insert(loc=3, column='Shelf_ID_Last', value=tmp3)
        del tmp2, tmp3
        df_table.drop(columns=['Shelf_ID_First'], inplace=True)
        df_table.rename(columns={'Shelf_ID_Last': 'Shelf_ID'}, inplace=True)
        df_table.loc[df_table["Shelf_ID"].str[4:7] > df_table["Shelf_ID"].shift(1).str[4:7], "Position_Move"] = '車頭往前'
        df_table.loc[df_table["Shelf_ID"].str[4:7] < df_table["Shelf_ID"].shift(-1).str[4:7], "Position_Move"] = '車頭往前'
        df_table.loc[df_table["Shelf_ID"].str[4:7] < df_table["Shelf_ID"].shift(1).str[4:7], "Position_Move"] = '車頭往後'
        df_table.loc[df_table["Shelf_ID"].str[4:7] > df_table["Shelf_ID"].shift(-1).str[4:7], "Position_Move"] = '車頭往後'
        df_table.loc[df_table["Shelf_ID"].str[1:4] > df_table["Shelf_ID"].shift(1).str[1:4], "Position_Move"] = '車頭往左'
        df_table.loc[df_table["Shelf_ID"].str[1:4] < df_table["Shelf_ID"].shift(-1).str[1:4], "Position_Move"] = '車頭往左'
        df_table.loc[df_table["Shelf_ID"].str[1:4] < df_table["Shelf_ID"].shift(1).str[1:4], "Position_Move"] = '車頭往右'
        df_table.loc[df_table["Shelf_ID"].str[1:4] > df_table["Shelf_ID"].shift(-1).str[1:4], "Position_Move"] = '車頭往右'
        tmp4 = df_table["Position_Move"]
        df_table.drop(columns=['Position_Move'], inplace=True)
        df_table.insert(loc=2, column='Position_Move', value=tmp4)
        df_table["Position_Move"] = df_table["Position_Move"].replace(np.nan, "")
        del tmp4
    elif "ShuttleProc" in current_comboBox_4_text:
        # df_table.drop(columns=['INFO', "##"], inplace=True)
        df_table.drop(columns=["##"], inplace=True)
        if "MissStation" in current_comboBox_2_text:
            df_table["Fix_Times"] = df_table["Fix_Times"].replace(np.nan, "")
            # tmp5 = df_table["Fix_Times"]
            # df_table.drop(columns=['Fix_Times'], inplace=True)
            # df_table.insert(loc=2, column='Fix_Times', value=tmp5)
            # del tmp5

    return df_table







print("Running Willy_Module.py")
print("Done!")
Test_Module()
print("Let's Start!")
print()
print()

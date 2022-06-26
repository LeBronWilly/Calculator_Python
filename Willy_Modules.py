# -*- coding: utf-8 -*-
"""
@author: Willy Fang (方聖瑋)
"""

# 匯入套件
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
myfont=FontProperties(fname='微软正黑体.ttf')
legend_font=FontProperties(fname='微软正黑体.ttf', size=20)
import matplotlib.font_manager as font_manager
sns.set(color_codes=True,font=myfont.get_family())
import os
import sys
from glob import glob
# np.set_printoptions(suppress=True)
# pd.set_option('display.max_columns', 2500, 'display.max_rows', 1000)
from datetime import datetime, timedelta


print("Setting......")
# from scipy import stats
# import scipy.stats as st
# from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
import sklearn.ensemble
import sklearn
import sklearn.utils._typedefs
import sklearn.neighbors._partition_nodes
import warnings
warnings.filterwarnings("ignore")
# import statsmodels.api as sm
# from statsmodels.sandbox.regression.predstd import wls_prediction_std
# from statsmodels.stats.outliers_influence import summary_table
# import openpyxl
# import sqlite3
# pd.set_option('display.max_colwidth', -1)
# from pandas.io import sql
# from functools import reduce
# import gc



# Test
def Test_Module(name="Willy"):
    print("Hello ", name, sep="")
    print(datetime.now())


# 匯入車子的csv數據（一次處理後）
def GetSCData_PreliminaryProcessing(SC_num, start_date="2021-01-01", end_date="2021-07-31", only_date=None):
    # 匯入車子的csv數據
    df = GetSCData_csv2(SC_num, start_date, end_date, only_date)
    try:
        # 修正48車的一項數據
        if SC_num==48:
            try:
                df.loc[df["Time"]=="2021-06-30 12:45:27.188200","ForkUnloadCount"]=12714.0
            except:
                pass
        # 將Dog值轉換成String型態
        df["Dog"] = df["Dog"].astype(int).astype(str).apply(lambda x:Add_0_MSC_for_Dog(x))
        # 增加數個欄位數據
        df = Add_Field(df)
        # 增加有無載貨的欄位數據(Flag)
        df["Loading_Fork"] = df["ForkLoadCount"]-df["ForkUnloadCount"]
        df = Processing_Fork(df)
        # 增加Time_Gap的欄位數據
        df["Time_Gap"] = (df['Time']-df['Time'].shift(1)).dt.total_seconds()
        # 從Raw Data選出所需的數據欄位
        try:
            df = df[['Time',"Time_Gap",'CPM_Voltage','ΔCPM_Voltage','CPM_Energy','ΔCPM_Energy',"CPM_Temperture",
                     'Position_X',"Abs(ΔPosition_X)","ΔPosition_X", 'Velocity_X',
                     'Position_Y',"Abs(ΔPosition_Y)","ΔPosition_Y",'Velocity_Y',
                     'Loading_Fork',"ForkLoadCount","ForkUnloadCount",
                     'Position_F',"Abs(ΔPosition_F)","ΔPosition_F",'Velocity_F',"Position_Z",
                     'BTA_Voltage','BTA_Current',"BTA_Temperture",'Dog',"SSR1","SSR2"]]
        except:
            df = df[['Time',"Time_Gap",'CPM_Voltage','ΔCPM_Voltage','CPM_Energy','ΔCPM_Energy',"CPM_Temperture",
                     'Position_X',"Abs(ΔPosition_X)","ΔPosition_X", 'Velocity_X',
                     'Position_Y',"Abs(ΔPosition_Y)","ΔPosition_Y",'Velocity_Y',
                     'Loading_Fork',"ForkLoadCount","ForkUnloadCount",
                     'Position_F',"Abs(ΔPosition_F)","ΔPosition_F",'Velocity_F',"Position_Z",
                     'BTA_Voltage','BTA_Current',"BTA_Temperture",'Dog']]
            print("(PS. No SSR1 and SSR2!)")
        # 若有較大的資料斷層現象(此定義Time_Gap>50)，將Δ變成NAN值
        df.loc[df["Time_Gap"]>50,["Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","ΔPosition_X",
                              "Abs(ΔPosition_Y)","ΔPosition_Y","Abs(ΔPosition_F)","ΔPosition_F"]]=np.nan
        return df
    except:
        if only_date!=None:
            print("　SC No."+str(SC_num)+" has no PLC data on",only_date)
        else:
            print("　SC No."+str(SC_num)+" has no PLC data between",start_date,"and",end_date)
        return None



# 匯入車子的PLC數據
def GetSCData_csv2(SC_num, start_date="2021-01-01", end_date="2021-07-31", only_date=None):
    print("Loading SC No." + str(SC_num) + " PLC Data......")
    path = "../" + str(SC_num) + "車OK/L/Log/"

    folders_name = sorted([f for f in os.listdir(path) if "20" in f])
    folders_path = [path + f for f in folders_name]
    # 匯入限制時間區間的數據
    if start_date != None and end_date != None:
        folders_path = [folder_path for folder_path in folders_path if (folder_path.split("/")[-1] >= start_date) and
                        (folder_path.split("/")[-1] <= end_date)]
    elif only_date != None:
        folders_path = [folder_path for folder_path in folders_path if (folder_path.split("/")[-1] == only_date)]
    dates_list = folders_name

    data_files_fullpath = []
    df_list = []
    for folder_path in folders_path:
        data_files_fullpath = []
        data_files_fullpath.extend(glob(folder_path + '/Plc/*Shuttle_20*.csv'))
        for data_file_fullpath in sorted(data_files_fullpath):
            # 匯入數據，並匯入特定的欄位
            try:
                df_tmp = pd.read_csv(data_file_fullpath, usecols=['time', 'CPM_Voltage', "CPM_Temperture",
                                                                  'Position_X', 'Velocity_X',
                                                                  'Position_Y', 'Velocity_Y', "Position_Z",
                                                                  "ForkLoadCount", "ForkUnloadCount", 'Position_F',
                                                                  'Velocity_F',
                                                                  'BTA_Voltage', 'BTA_Current', "BTA_Temperture", 'Dog',
                                                                  "SSR1", "SSR2"])
            except:
                df_tmp = pd.read_csv(data_file_fullpath, usecols=['time', 'CPM_Voltage', "CPM_Temperture",
                                                                  'Position_X', 'Velocity_X',
                                                                  'Position_Y', 'Velocity_Y', "Position_Z",
                                                                  "ForkLoadCount", "ForkUnloadCount", 'Position_F',
                                                                  'Velocity_F',
                                                                  'BTA_Voltage', 'BTA_Current', "BTA_Temperture",
                                                                  'Dog'])
            df_tmp = df_tmp.dropna()
            # 加入完整的Time Series，並從str轉成datetime型態
            df_tmp["time"] = folder_path.split("/")[-1] + " " + df_tmp["time"]
            df_tmp["time"] = pd.to_datetime(df_tmp["time"], format="%Y/%m/%d %H:%M:%S.%f")
            df_list.append(df_tmp)
    if df_list != []:
        df = pd.concat(df_list, axis=0, ignore_index=True)
        df_list = []
        df.rename(columns={'time': 'Time'}, inplace=True)
        return df
    else:
        return None


# 增加數個欄位數據
def Add_Field(df):
    df['Loading_Fork'] = df['ForkLoadCount']-df['ForkUnloadCount']
    df['ΔCPM_Voltage'] = df['CPM_Voltage']-df['CPM_Voltage'].shift(1)
    df['CPM_Energy'] = (1/2)*38.88*(df['CPM_Voltage']**2)
    df['ΔCPM_Energy'] = df['CPM_Energy']-df['CPM_Energy'].shift(1)
    
    df['ΔPosition_X'] = df['Position_X']-df['Position_X'].shift(1)
    df['ΔPosition_Y'] = df['Position_Y']-df['Position_Y'].shift(1)
    df['ΔPosition_F'] = df['Position_F']-df['Position_F'].shift(1)
    df["Abs(ΔPosition_X)"] = abs(df["ΔPosition_X"])
    df["Abs(ΔPosition_Y)"] = abs(df["ΔPosition_Y"])
    df["Abs(ΔPosition_F)"] = abs(df["ΔPosition_F"])
    
    return df



# 增加有無載貨的欄位數據(Flag)
def Processing_Fork(df):
    # 增加暫時的Fork欄位(Flag)
    df["Fork"] = np.nan
    # 設置Flag判斷是否真的是載貨/卸貨
    df.loc[(df["ForkLoadCount"]-df["ForkLoadCount"].shift(1)==1) & 
           ((abs(df["Position_F"]-df["Position_F"].shift(4))>5) | (abs(df["Position_F"]-df["Position_F"].shift(3))>5) | 
            (abs(df["Position_F"]-df["Position_F"].shift(2))>5) | (abs(df["Position_F"]-df["Position_F"].shift(1))>5))
           , "Fork"] = 'Fork_Start'
    df.loc[(df["ForkUnloadCount"]-df["ForkUnloadCount"].shift(1)==1) & 
           ((abs(df["Position_F"]-df["Position_F"].shift(4))>5) | (abs(df["Position_F"]-df["Position_F"].shift(3))>5) | 
            (abs(df["Position_F"]-df["Position_F"].shift(2))>5) | (abs(df["Position_F"]-df["Position_F"].shift(1))>5))
           , "Fork"] = 'Fork_End'
    
    # 填入正確的Loading_Fork欄位(Flag)
    fork_notnull_index_list = list(df[~df['Fork'].isnull()].index)
    for i in range(len(fork_notnull_index_list)):
        if i==0:
            if df["Fork"].iloc[fork_notnull_index_list[i]] == "Fork_Start":
                df["Loading_Fork"].iloc[0:fork_notnull_index_list[i]] = 0
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:fork_notnull_index_list[i+1]] = 1
            else:
                df["Loading_Fork"].iloc[0:fork_notnull_index_list[i]] = 1
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:fork_notnull_index_list[i+1]] = 0
        elif i==len(fork_notnull_index_list)-1:
            if df["Fork"].iloc[fork_notnull_index_list[i]] == "Fork_Start":
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:] = 1
            else:
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:] = 0
        else:
            if df["Fork"].iloc[fork_notnull_index_list[i]] == "Fork_Start":
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:fork_notnull_index_list[i+1]] = 1
            else:
                df["Loading_Fork"].iloc[fork_notnull_index_list[i]:fork_notnull_index_list[i+1]] = 0
    # Fork欄位到此已經無用，實際上可刪除
    df = df.drop(columns=['Fork'])
    return df



# 增加充電/放電的欄位數據(Flag)
def Select_Fields_Add_Flag_Charge(df):
    data = df
    # Flag欄位在這裡作為標註Charge_Start或是Charge_End，否則就是NAN值
    data["Flag"] = np.nan
    # Charge欄位在這裡作為標註1(充電)或是0(放電)，否則就是NAN值
    data["Charge"] = np.nan
    
    # 設定第一個row的flag
    if data["BTA_Current"].iloc[0]>0.0:
        data["Flag"].iloc[0] = "Charge_Start"
    else:
        data["Flag"].iloc[0] = "Charge_End"
    
    # 充電開始的Flag
    data.loc[(data["BTA_Current"]>0.0) & 
             (data["BTA_Current"].shift(1)<0.0) & 
             (data["BTA_Current"].shift(-1)>0.0)
             , "Flag"] = 'Charge_Start'
    # 放電開始的Flag
    data.loc[(data["BTA_Current"]<0.0) & 
             (data["BTA_Current"].shift(1)>0.0) & 
             (data["BTA_Current"].shift(-1)<0.0)
             , "Flag"] = 'Charge_End'
    
    # 若遇到數據斷層，重新判斷Flag(充電開始的Flag)
    data.loc[(data["Time_Gap"]>10) & 
             (data["BTA_Current"]>0.0)
             , "Flag"] = 'Charge_Start'
    data.loc[(data["Time_Gap"].isnull()) & 
             (data["BTA_Current"]>0.0)
             , "Flag"] = 'Charge_Start'
    # 若遇到數據斷層，重新輸入Time_Gap(0.5s)
    data.loc[(data["Time_Gap"]>10) & 
             (data["BTA_Current"]>0.0)
             , "Time_Gap"] = 0.5
    
    # 若遇到數據斷層，重新判斷Flag(放電開始的Flag)
    data.loc[(data["Time_Gap"]>50) & 
             (data["BTA_Current"]<0.0)
             , "Flag"] = 'Charge_End'
    
    
    
    # 判斷此row數據是否為充電狀態(1)or放電狀態(0)
    data.loc[(data["BTA_Current"]>0.0), "Charge"] = 1
    data.loc[(data["BTA_Current"]<0.0), "Charge"] = 0
    
    # 排除放電時ΔCPM_Voltage>1的情況
    # 數據會有本來應該是在是充電(1)時，卻依然標示放電(0)的情況(把應該是1的0轉成1)
    data.loc[(data["ΔCPM_Voltage"]>=1.0) & 
             (data["Charge"]==0.0), "Charge"] = 1
    data.loc[((data["ΔCPM_Voltage"].shift(1)>=1.0) & (data["ΔCPM_Voltage"]<=0.0)) & 
             (data["Charge"]==0.0), "Charge"] = 1
    
    return data




### Discharge


# 篩選放電的數據
def Select_Discharge(df):
    # Charge標註0時則表示此row為放電
    data = df[df["Charge"]==0.0].reset_index(drop=True)
    return data



# 增加Discharge放電的Group欄位
def Add_Discharge_Group_Num_Field(df):
    data = df
    data["Discharge_Group"] = np.nan
    
    flag_notnull_index_list = list(data[~data['Flag'].isnull()].index)
    g=1
    for i in range(len(flag_notnull_index_list)):
        if i != len(flag_notnull_index_list)-1:
            data["Discharge_Group"].iloc[flag_notnull_index_list[i]:flag_notnull_index_list[i+1]]=g
            g+=1
        else:
            data["Discharge_Group"].iloc[flag_notnull_index_list[i]:]=g
    group_col = data.pop(data.columns[-1])
    data.insert(1, group_col.name, group_col)
    return data



# 若要篩選出在運行的數據，排除待機的數據(若ΔXY>Delete_Below_Num，則判斷為有在運行)
# 若要篩選出在待機的數據，排除運行的數據(若ΔXY=0、ΔF<=0.005，則判斷為有在待機)
def Remove_Illegal_CPM_Voltage(df, Select_Idle=False, Delete_Below_Num=0.1):
    data=df
    # 篩選出在運行的數據(若ΔXY>Delete_Below_Num，則判斷為有在運行)
    if Select_Idle==False:
        data = data[(data["Abs(ΔPosition_X)"]>Delete_Below_Num) | (data["Abs(ΔPosition_Y)"]>Delete_Below_Num) | 
                    ((data["Abs(ΔPosition_F)"]>=0.5) | (abs(df["Position_F"])>=5))]
    # 篩選出在待機的數據(若ΔXY=0、V_XY=0、ΔF<=0.005，則判斷為有在待機)
    else:
        data = data[(data["Abs(ΔPosition_X)"]==0.0) & (data["Velocity_X"]==0.0) & 
                    (data["Abs(ΔPosition_Y)"]==0.0) & (data["Velocity_Y"]==0.0) & 
                    ((abs(data["Position_F"])<=0.005) & (data["Abs(ΔPosition_F)"]<=0.005))]
        data = Drop_Idle_Last6(data)
    return data



# 增加放電時，X橫移的Group欄位
def Add_X_Group_Num_Field(df):
    tmpX = df[(df["Abs(ΔPosition_X)"]>0) & 
           (df["Abs(ΔPosition_X)"]>df["Abs(ΔPosition_Y)"]) & 
           (df["Abs(ΔPosition_X)"]>df["Abs(ΔPosition_F)"]) & 
           (df["Abs(ΔPosition_F)"]<=0.005)].reset_index()
    
    
    tmpX["diff_index"] = tmpX['index']-tmpX['index'].shift(1)
    tmpX["diff_index"].iloc[0:1] = 1
    
    tmpX.loc[tmpX["Flag"]=="Charge_End","diff_index"]=9999
    tmpX["X_Group"] = 0
    tmpX = tmpX.drop(columns=['index'])
    
    g=0        
    diff_index_not1_list = list(tmpX[tmpX["diff_index"]>1.0].index)
    if 0 not in diff_index_not1_list:
        diff_index_not1_list.insert(0,0)
    for i in range(len(diff_index_not1_list)):
        g+=1
        if i==0:
            tmpX["X_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
        elif i==len(diff_index_not1_list)-1:
            tmpX["X_Group"].iloc[diff_index_not1_list[i]:] = g
        else:
            tmpX["X_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
    
    group_col = tmpX.pop(tmpX.columns[-1])
    tmpX.insert(2, group_col.name, group_col)
    return tmpX



# 增加放電時，Y走行的Group欄位
def Add_Y_Group_Num_Field(df):
    tmpY = df[(df["Abs(ΔPosition_Y)"]>0) & 
           (df["Abs(ΔPosition_Y)"]>df["Abs(ΔPosition_X)"]) & 
           (df["Abs(ΔPosition_Y)"]>df["Abs(ΔPosition_F)"]) & 
           (df["Abs(ΔPosition_F)"]<=0.005)].reset_index()
    
    tmpY["diff_index"] = tmpY['index']-tmpY['index'].shift(1)
    tmpY["diff_index"].iloc[0:1] = 1
    
    tmpY.loc[tmpY["Flag"]=="Charge_End","diff_index"]=9999
    tmpY["Y_Group"] = 0
    tmpY = tmpY.drop(columns=['index'])
    
    g=0
    diff_index_not1_list = list(tmpY[tmpY["diff_index"]>1.0].index)
    if 0 not in diff_index_not1_list:
        diff_index_not1_list.insert(0,0)
    for i in range(len(diff_index_not1_list)):
        g+=1
        if i==0:
            tmpY["Y_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
        elif i==len(diff_index_not1_list)-1:
            tmpY["Y_Group"].iloc[diff_index_not1_list[i]:] = g
        else:
            tmpY["Y_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
    
    group_col = tmpY.pop(tmpY.columns[-1])
    tmpY.insert(2, group_col.name, group_col)
    return tmpY



# 增加放電時，Y走行的Group欄位
def Add_Fork_Group_Num_Field(df):
    tmpF = df[(df["Abs(ΔPosition_F)"]>=0.005) | (abs(df["Position_F"])>=5)].reset_index()
    
    tmpF["diff_index"] = tmpF['index']-tmpF['index'].shift(1)
    tmpF["diff_index"].iloc[0:1] = 1
    
    tmpF.loc[tmpF["Flag"]=="Charge_End","diff_index"]=9999
    tmpF["Fork_Group"] = 0
    tmpF = tmpF.drop(columns=['index'])
    
    g=0
    diff_index_not1_list = list(tmpF[tmpF["diff_index"]>1.0].index)
    if 0 not in diff_index_not1_list:
        diff_index_not1_list.insert(0,0)
    for i in range(len(diff_index_not1_list)):
        g+=1
        if i==0:
            tmpF["Fork_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
        elif i==len(diff_index_not1_list)-1:
            tmpF["Fork_Group"].iloc[diff_index_not1_list[i]:] = g
        else:
            tmpF["Fork_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
    
    group_col = tmpF.pop(tmpF.columns[-1])
    tmpF.insert(2, group_col.name, group_col)
    return tmpF



# 增加放電時，Idle待機的Group欄位
def Add_Idle_Group_Num_Field(df):
    tmpIdle = df[(df["Abs(ΔPosition_X)"]<=0) & (df["Velocity_X"]<=0.0) & 
                 (df["Abs(ΔPosition_Y)"]<=0) & (df["Velocity_Y"]<=0.0) & 
                 ((abs(df["Position_F"])<0.0025) & (df["Abs(ΔPosition_F)"]<=0.0025))].reset_index()
    
    tmpIdle["diff_index"] = tmpIdle['index']-tmpIdle['index'].shift(1)
    tmpIdle["diff_index"].iloc[0:1] = 1
    
    tmpIdle.loc[tmpIdle["Flag"]=="Charge_End","diff_index"]=9999
    tmpIdle["Idle_Group"] = 0
    tmpIdle = tmpIdle.drop(columns=['index'])
    
    g=0
    diff_index_not1_list = list(tmpIdle[tmpIdle["diff_index"]>1.0].index)
    if 0 not in diff_index_not1_list:
        diff_index_not1_list.insert(0,0)
    for i in range(len(diff_index_not1_list)):
        g+=1
        if i==0:
            tmpIdle["Idle_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
        elif i==len(diff_index_not1_list)-1:
            tmpIdle["Idle_Group"].iloc[diff_index_not1_list[i]:] = g
        else:
            tmpIdle["Idle_Group"].iloc[diff_index_not1_list[i]:diff_index_not1_list[i+1]] = g
    
    
    group_col = tmpIdle.pop(tmpIdle.columns[-1])
    tmpIdle.insert(2, group_col.name, group_col)
    return tmpIdle



# 移除在Idle待機時，每個Discharge_Group倒數前6個rows的數據(確保要準備充電的前幾秒時，排除掉會有ΔCPM_Voltage先充的現象數據)
def Drop_Idle_Last6(df):
    data=df.reset_index(drop=True)
    drop_index_list=[]
    for i in set(data["Discharge_Group"]):
        drop_index_list.extend(data[data["Discharge_Group"]==i].index[-6:])
    data = data.drop(drop_index_list)
    return data



# 增加完Group欄位後，進行GroupBy的運算(Behavior_Group = "Discharge_Group" or "X_Group" or "Y_Group" or "Idle_Group")
def GroupBy_MileageSum(df, Behavior_Group=None, Split_Fork=False):
    # 所有非待機的行為情況(橫移+走行)
    if Behavior_Group==None:
        if Split_Fork==True:
            data = df[["Discharge_Group","Time_Gap","Loading_Fork","ΔCPM_Voltage","ΔCPM_Energy","Position_X","Position_Y",
                       "Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","CPM_Voltage","Time"]].groupby(["Discharge_Group","Loading_Fork"], as_index=False).agg({'Time_Gap':'sum','ΔCPM_Voltage':'sum','ΔCPM_Energy':'sum','Abs(ΔPosition_X)':'sum','Abs(ΔPosition_Y)':'sum',"Abs(ΔPosition_F)":"sum",'CPM_Voltage':['max',"mean","median"],"Time":["count","first","last"]})
            data.columns = ['Discharge_Group', 'Loading_Fork',"Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","Max_CPM_V","Mean_CPM_V","Median_CPM_V","N_Discharge_data","Time_Start","Time_End"]
        else:
            data = df[["Discharge_Group","Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Position_X","Position_Y",
                       "Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","CPM_Voltage","Time"]].groupby(["Discharge_Group"], as_index=False).agg({'Time_Gap':'sum','ΔCPM_Voltage':'sum','ΔCPM_Energy':'sum','Abs(ΔPosition_X)':'sum','Abs(ΔPosition_Y)':'sum',"Abs(ΔPosition_F)":"sum",'CPM_Voltage':['max',"mean","median"],"Time":["count","first","last"]})
            data.columns = ['Discharge_Group',"Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","Max_CPM_V","Mean_CPM_V","Median_CPM_V","N_Discharge_data","Time_Start","Time_End"]
        
        data["Time_Start"] = pd.to_datetime(data["Time_Start"], format="%Y/%m/%d %H:%M:%S.%f")
        data["Time_End"] = pd.to_datetime(data["Time_End"], format="%Y/%m/%d %H:%M:%S.%f")
        
    # 劃分橫移、走行、待機、叉臂的行為情況
    else:
        if Split_Fork==True:
            data = df[[Behavior_Group,"Time_Gap","Discharge_Group","Loading_Fork","ΔCPM_Voltage","ΔCPM_Energy","Position_X","Position_Y",
                       "Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","CPM_Voltage","Time"]].groupby([Behavior_Group, "Discharge_Group","Loading_Fork"], as_index=False).agg({'Time_Gap':'sum','ΔCPM_Voltage':'sum','ΔCPM_Energy':'sum','Abs(ΔPosition_X)':'sum','Abs(ΔPosition_Y)':'sum',"Abs(ΔPosition_F)":"sum",'CPM_Voltage':['max',"mean","median"],"Time":["count","first","last"]})
            data.columns = [Behavior_Group, "Discharge_Group", 'Loading_Fork',"Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","Max_CPM_V","Mean_CPM_V","Median_CPM_V","N_"+Behavior_Group+"_data","Time_Start","Time_End"]
        
            if Behavior_Group!="Idle_Group":
                Mean_Median_Velocity = df[[Behavior_Group, "Discharge_Group","Loading_Fork","Velocity_"+Behavior_Group[0]]].groupby([Behavior_Group, "Discharge_Group","Loading_Fork"], as_index=False).agg({"Velocity_"+Behavior_Group[0]:["mean","median","max"]})
                Mean_Median_Velocity.columns = [Behavior_Group, "Discharge_Group","Loading_Fork","Mean_Velocity","Median_Velocity","Max_Velocity"]
                data["Mean_Velocity"], data["Median_Velocity"], data["Max_Velocity"] = Mean_Median_Velocity["Mean_Velocity"], Mean_Median_Velocity["Median_Velocity"], Mean_Median_Velocity["Max_Velocity"]
                del Mean_Median_Velocity
        else:
            data = df[[Behavior_Group,"Time_Gap","Discharge_Group","ΔCPM_Voltage","ΔCPM_Energy","Position_X","Position_Y",
                       "Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","CPM_Voltage","Time"]].groupby([Behavior_Group, "Discharge_Group"], as_index=False).agg({'Time_Gap':'sum','ΔCPM_Voltage':'sum','ΔCPM_Energy':'sum','Abs(ΔPosition_X)':'sum','Abs(ΔPosition_Y)':'sum',"Abs(ΔPosition_F)":"sum",'CPM_Voltage':['max',"mean","median"],"Time":["count","first","last"]})
            data.columns = [Behavior_Group, "Discharge_Group","Time_Gap","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","Max_CPM_V","Mean_CPM_V","Median_CPM_V","N_"+Behavior_Group+"_data","Time_Start","Time_End"]
            
            if Behavior_Group!="Idle_Group":
                Mean_Median_Velocity = df[[Behavior_Group, "Discharge_Group","Loading_Fork","Velocity_"+Behavior_Group[0]]].groupby([Behavior_Group, "Discharge_Group","Loading_Fork"], as_index=False).agg({"Velocity_"+Behavior_Group[0]:["mean","median","max"]})
                Mean_Median_Velocity.columns = [Behavior_Group, "Discharge_Group","Loading_Fork","Mean_Velocity","Median_Velocity","Max_Velocity"]
                data["Mean_Velocity"], data["Median_Velocity"], data["Max_Velocity"] = Mean_Median_Velocity["Mean_Velocity"], Mean_Median_Velocity["Median_Velocity"], Mean_Median_Velocity["Max_Velocity"]
                del Mean_Median_Velocity
        
        data["Time_Start"] = pd.to_datetime(data["Time_Start"], format="%Y/%m/%d %H:%M:%S.%f")
        data["Time_End"] = pd.to_datetime(data["Time_End"], format="%Y/%m/%d %H:%M:%S.%f")
        
    
    data["Time_YYMM"] = data["Time_Start"].dt.to_period('M')
    if Behavior_Group=="Fork_Group":
        data["Sum(Abs(ΔPosition))"] = (data["Abs(ΔPosition_F)"])/1000
    else:
        data["Sum(Abs(ΔPosition))"] = (data["Abs(ΔPosition_X)"] + data["Abs(ΔPosition_Y)"])/1000
    data["Sum(Abs(ΔCPM_Voltage))"] = abs(data["ΔCPM_Voltage"])
    data["Sum(Abs(ΔCPM_Energy))"] = abs(data["ΔCPM_Energy"])
    data["Time_Gap"] = data["Time_Gap"]-0.5
    return data



### Charge

# 篩選充電的數據
def Select_Charge(df):
    data = df[(df["Charge"]==1.0) & (df["BTA_Current"]>0.0)].reset_index(drop=True)
    return data


# 增加Charge充電的Group欄位
def Add_Charge_Group_Num_Field(df):
    data = df
    data["Charge_Group"] = np.nan
    
    flag_notnull_index_list = list(data[~data['Flag'].isnull()].index)
    g=1
    for i in range(len(flag_notnull_index_list)):
        if i != len(flag_notnull_index_list)-1:
            data["Charge_Group"].iloc[flag_notnull_index_list[i]:flag_notnull_index_list[i+1]]=g
            g+=1
        else:
            data["Charge_Group"].iloc[flag_notnull_index_list[i]:]=g
    group_col = data.pop(data.columns[-1])
    data.insert(1, group_col.name, group_col)
    return data


# 取得Charge行為的數據（整合）
def Get_Charge_Data_Preprocessed(df):
    df["V%"] = ((df["CPM_Voltage"]-25.5)/(48.0-25.5))*100
    group_col = df.pop(df.columns[-1])
    df.insert(4, group_col.name, group_col)
    
    df["ΔV%"] = df["V%"]-df["V%"].shift(1)
    group_col = df.pop(df.columns[-1])
    df.insert(5, group_col.name, group_col)
    df.loc[df["Flag"]=="Charge_Start","ΔV%"]=np.nan
    
    tmp=df[["Charge_Group","CPM_Voltage","V%"]].groupby(["Charge_Group"], as_index=False).max()
    for i in tmp.values:
        df.loc[(df["Charge_Group"]==i[0]) & 
                                   (df["CPM_Voltage"]==i[1]) & 
                                   (df["V%"]==i[2]) & 
                                   (df["ΔV%"]>0),"Flag"]="Peak"
    Peak_list=list(df[df["Flag"]=="Peak"].index)
    Charge_list=list(df[df["Flag"]=="Charge_Start"].index)
    Charge_Peak=[]
    for c in Charge_list:
        for p in Peak_list:
            if p>c:
                Charge_Peak.append([c,p])
                Peak_list.remove(p)
                break
            else:
                continue
    for cp in Charge_Peak:
        df.loc[cp[0]:cp[1],"Flag"]=1
    # 電量歸類調整
    df["ΔV%"] = df["ΔV%"].shift(-1)
    df.loc[df["Time_Gap"].isnull(),"Time_Gap"]=0.5
    return df



def Get_Real_Charge_Data(df, Split_Percent=86.5, Get_Below=True):
    df = df[((df["Flag"] == 1) | (df["Flag"] == "1")) &
            ~(df["Charge_Group"].isin(set(df[df["Time_Gap"] < 0]["Charge_Group"])))]

    if Get_Below == True or Get_Below == "True":
        return df[(df["V%"] < Split_Percent)]
    elif Get_Below == False or Get_Below == "False":
        return df[(df["V%"] >= Split_Percent)]
    elif Get_Below == None or Get_Below == "None":
        return df



def GroupBy_Charge(df, Is_Below=True):
    data = df.groupby(["Charge_Group"], as_index=False).agg({'Time_Gap':'sum',"V%":["min","max"],'ΔV%':[np.sum, lambda x:sum(np.array(x)<-1)],'ΔCPM_Voltage':'sum','ΔCPM_Energy':'sum','Abs(ΔPosition_X)':'sum','Abs(ΔPosition_Y)':'sum','Abs(ΔPosition_F)':'sum',"Time":["count","min","max"]})
    data.columns = ['Charge_Group', 'Time_Gap',"V%_Start","V%_End","ΔV%","Count_NegΔV%","ΔCPM_Voltage","ΔCPM_Energy","Abs(ΔPosition_X)","Abs(ΔPosition_Y)","Abs(ΔPosition_F)","N_data","Time_Start","Time_End"]
    data = data[(data["ΔV%"]>0) & (data["ΔCPM_Voltage"]>0) & (data["Time_Gap"]>0)]
    data["Time_Gap"] = data["Time_Gap"]-0.5
    data["Total ΔXY"] = data["Abs(ΔPosition_X)"]+data["Abs(ΔPosition_Y)"]
    return data[(data["Count_NegΔV%"]<=1)]




### Draw_Plt


def Draw_Plt_All_V(data, SC_num, Split_Fork=False, Fork_Flag=True):
#     if SC_num!=7:
#         data=data[data["超級電容伏特消耗量(V)"]<=11]
    data=data[(data["N_Discharge_data"]>=5)]
    
    if Split_Fork==False:
        Lin_Reg = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data["超級電容伏特消耗量(V)"]), 
                                                                       data["車子運行之距離(m)"])
        print(SC_num,"X橫移+Y走行")
        print("資料數：",len(data),sep="")
        print(round(Lin_Reg.coef_[0],4))
        print(round(1/Lin_Reg.coef_[0],4))
        print("截距：",Lin_Reg.intercept_)
        print("10V可行距離：",Lin_Reg.predict([[10]]))
        print("19.5V可行距離：",Lin_Reg.predict([[19.5]]))
    else:
        data1=data[data["Loading_Fork"]==1]
        data0=data[data["Loading_Fork"]==0]
        Lin_Reg1 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data1["超級電容伏特消耗量(V)"]), 
                                                                       data1["車子運行之距離(m)"])
        Lin_Reg0 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data0["超級電容伏特消耗量(V)"]), 
                                                                       data0["車子運行之距離(m)"])
        print(SC_num,"X橫移+Y走行")
        print("沒載貨")
        print("資料數：",len(data0),sep="")
        print(round(Lin_Reg0.coef_[0],4))
        print(round(1/Lin_Reg0.coef_[0],4))
        print("截距：",Lin_Reg0.intercept_)
        print("10V可行距離：",Lin_Reg0.predict([[10]]))
        print("19.5V可行距離：",Lin_Reg0.predict([[19.5]]))
        print("有載貨")
        print("資料數：",len(data1),sep="")
        print(round(Lin_Reg1.coef_[0],4))
        print(round(1/Lin_Reg1.coef_[0],4))
        print("截距：",Lin_Reg1.intercept_)
        print("10V可行距離：",Lin_Reg1.predict([[10]]))
        print("19.5V可行距離：",Lin_Reg1.predict([[19.5]]))
        print("斜率差：", round(Lin_Reg0.coef_[0]-Lin_Reg1.coef_[0], 4))
    
    
    fig, ax1 = plt.subplots(figsize=(24,24))
    plt.title('SC_'+str(SC_num)+"'s 超級電容伏特消耗量 & 運行距離",fontproperties=myfont, fontsize=60)
    plt.xlabel('超級電容伏特消耗量(V)',fontproperties=myfont, fontsize=50)
    plt.ylabel('運行距離(m)',fontproperties=myfont, fontsize=50)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    
    
    
    
    if Split_Fork==False:
        tmp_row = [pd.Series([0], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns), 
                   pd.Series([20], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns)]
        plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data, label=None)
        plt.plot(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg.predict(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (All)', color="green", linewidth = '8')
    else:
        if Fork_Flag==True:
            tmp_row = [pd.Series([0], index=pd.DataFrame(data1["超級電容伏特消耗量(V)"]).columns), 
                       pd.Series([20], index=pd.DataFrame(data1["超級電容伏特消耗量(V)"]).columns)]
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data1, label=None,c="red", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg1.predict(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (All with Fork)', color="brown", linewidth = '8')
        else:
            tmp_row = [pd.Series([0], index=pd.DataFrame(data0["超級電容伏特消耗量(V)"]).columns), 
                       pd.Series([20], index=pd.DataFrame(data0["超級電容伏特消耗量(V)"]).columns)]
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data0, label=None,c="green", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg0.predict(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (All without Fork)', color="olivedrab", linewidth = '8')
        
    
    
    
    
    plt.legend(loc="upper left",fontsize=23)
    plt.ylim((0,300))
    if SC_num!=7:
        plt.xlim((0,15))
    else:
        plt.xlim((0,20))
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
    
    print("==========================")
    return




def Draw_Plt_X_V(data, SC_num, Split_Fork=False, Fork_Flag=True, V_State=None, All_Cart=False):
    data=data[(data["N_X_Group_data"]>=5)]
    if V_State=="Full":
        data=data[(data["Max_CPM_V"]>=44)]
    elif V_State=="Medium":
        data=data[(data["Max_CPM_V"]>=40) & (data["Max_CPM_V"]<44)]
    elif V_State=="Low":
        data=data[(data["Max_CPM_V"]>=36) & (data["Max_CPM_V"]<40)]
    
    if Split_Fork==False:
        Lin_Reg = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data["超級電容伏特消耗量(V)"]), 
                                                                       data["車子運行之距離(m)"])
        print(SC_num,"X橫移")
        print("資料數：",len(data),sep="")
        print("截距：",round(Lin_Reg.intercept_, 4))
        print(Lin_Reg.predict([[10]]))
        print("m/V：",round(Lin_Reg.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg.coef_[0], 4))
        print("最大距離47m單程：",round((47-Lin_Reg.intercept_)/Lin_Reg.coef_[0], 4))
        Max_Distance_X_One_Trip_V.append(round((1/Lin_Reg.coef_[0])*47*2, 4))
    else:
        data1=data[data["Loading_Fork"]==1]
        data0=data[data["Loading_Fork"]==0]
        Lin_Reg1 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data1["超級電容伏特消耗量(V)"]), 
                                                                       data1["車子運行之距離(m)"])
        Lin_Reg0 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data0["超級電容伏特消耗量(V)"]), 
                                                                       data0["車子運行之距離(m)"])
        print(SC_num,"X橫移")
        print("無載貨")
        print("資料數：",len(data0),sep="")
        print("m/V：",round(Lin_Reg0.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg0.coef_[0], 4))
        print("截距：",round(Lin_Reg0.intercept_, 4))
        print(Lin_Reg0.predict([[10]]))
        print("最大距離47m單程（考慮截距）：",round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
        print("有載貨")
        print("資料數：",len(data1),sep="")
        print("m/V：",round(Lin_Reg1.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg1.coef_[0], 4))
        print("截距：",round(Lin_Reg1.intercept_, 4))
        print(Lin_Reg1.predict([[10]]))
        print("最大距離47m單程（考慮截距）：",round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
        
        if V_State=="Full" and Fork_Flag==True and All_Cart==False: # Fork_Flag==True可避免重複寫入
            Distance_X_47m_FullV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_FullV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
            
        elif V_State=="Medium" and Fork_Flag==True and All_Cart==False:
            Distance_X_47m_MediumV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_MediumV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
            
        elif V_State=="Low" and Fork_Flag==True and All_Cart==False:
            Distance_X_47m_LowV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_LowV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
            
        
        
    
    fig, ax1 = plt.subplots(figsize=(20,20))
    if All_Cart==False:
        plt.title('SC_'+str(SC_num)+"'s 超級電容伏特消耗量 & X橫移運行距離",fontproperties=myfont, fontsize=60)
    else:
        plt.title("所有車子 超級電容伏特消耗量 & X橫移運行距離",fontproperties=myfont, fontsize=60)
        print("多消耗比率",round(((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0])/((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0])-1,4))
    plt.xlabel('超級電容伏特消耗量(V)',fontproperties=myfont, fontsize=50)
    plt.ylabel('X橫移運行距離(m)',fontproperties=myfont, fontsize=50)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.axhline(y=47, color='black', linestyle='--', linewidth = '5')

    
    tmp_row = [pd.Series([0], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns), 
               pd.Series([20], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns)]
    
    if Split_Fork==False:
        plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data, label=None)
        plt.plot(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg.predict(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (X)', color="green", linewidth = '8')
    else:
        if Fork_Flag==False:
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data0, label=None,c="green", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                     Lin_Reg0.predict(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True)), 
                     label='Linear Regression Line (X without Fork)', color="olivedrab", linewidth = '8')
            plt.axvline(x=(47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], color='black', linestyle='--', linewidth = '5')
        else:
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data1, label=None,c="red", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                     Lin_Reg1.predict(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True)), 
                     label='Linear Regression Line (X with Fork)', color="brown", linewidth = '8')
            plt.axvline(x=(47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], color='black', linestyle='--', linewidth = '5')

        
        
    
    plt.legend(loc="upper left",fontsize=23)
    plt.ylim((0,50))
    if SC_num!=7:
        plt.xlim((0,2.5))
    else:
        plt.xlim((0,2.5))
    
    
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
    
    print("==========================")
    return




def Draw_Plt_Y_V_Poly(data, SC_num, Split_Fork=False, Fork_Flag=True, V_State=None, All_Cart=False):
    data=data[(data["N_Y_Group_data"]>=5)]
    if V_State=="Full":
        data=data[(data["Max_CPM_V"]>=44)]
    elif V_State=="Medium":
        data=data[(data["Max_CPM_V"]>=40) & (data["Max_CPM_V"]<44)]
    elif V_State=="Low":
        data=data[(data["Max_CPM_V"]>=36) & (data["Max_CPM_V"]<40)]
    
    if Split_Fork==False:
        poly = PolynomialFeatures(degree=2)
        poly.fit(pd.DataFrame(data["超級電容伏特消耗量(V)"]))
        X2 = poly.transform(pd.DataFrame(data["超級電容伏特消耗量(V)"]))
        Lin_Reg = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(X2, data["車子運行之距離(m)"])
        print(SC_num,"Y走行")
        print("資料數：",len(data),sep="")
        print("截距：",round(Lin_Reg.intercept_,4))
        print([round(i,4) for i in Lin_Reg.coef_])
        ans = (-Lin_Reg.coef_[1]+np.sqrt(Lin_Reg.coef_[1]**2-4*(Lin_Reg.coef_[2])*(Lin_Reg.intercept_+Lin_Reg.coef_[0]-48)))/(2*Lin_Reg.coef_[2])
#         ans = (-Lin_Reg.coef_[1]+np.sqrt(Lin_Reg.coef_[1]**2-4*(Lin_Reg.coef_[2])*(+Lin_Reg.coef_[0]-48)))/(2*Lin_Reg.coef_[2])
        print("最大距離48m單程：",round(ans,4))
        Max_Distance_Y_One_Trip_V.append(round(ans*2,4))
    else:
        data1=data[data["Loading_Fork"]==1]
        poly = PolynomialFeatures(degree=2)
        poly.fit(pd.DataFrame(data1["超級電容伏特消耗量(V)"]))
        X2_1 = poly.transform(pd.DataFrame(data1["超級電容伏特消耗量(V)"]))
        
        data0=data[data["Loading_Fork"]==0]
        poly = PolynomialFeatures(degree=2)
        poly.fit(pd.DataFrame(data0["超級電容伏特消耗量(V)"]))
        X2_0 = poly.transform(pd.DataFrame(data0["超級電容伏特消耗量(V)"]))
        
        Lin_Reg1 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(X2_1, data1["車子運行之距離(m)"])
        Lin_Reg0 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(X2_0, data0["車子運行之距離(m)"])
        print(SC_num,"Y走行")
        print("無載貨")
        print("資料數：",len(data0),sep="")
        print("截距：",round(Lin_Reg0.intercept_,4))
        print([round(i,4) for i in Lin_Reg0.coef_])
        ans = (-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-48)))/(2*Lin_Reg0.coef_[2])
#         ans = (-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(+Lin_Reg0.coef_[0]-48)))/(2*Lin_Reg0.coef_[2])
        print("最大距離48m單程：",round(ans,4))
#         print("最大距離48m單程：",round((1/Lin_Reg0.coef_[0])*48, 4))
        print("有載貨")
        print("資料數：",len(data1),sep="")
        print("截距：",round(Lin_Reg1.intercept_,4))
        print([round(i,4) for i in Lin_Reg1.coef_])
        ans = (-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-48)))/(2*Lin_Reg1.coef_[2])
#         ans = (-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(+Lin_Reg1.coef_[0]-48)))/(2*Lin_Reg1.coef_[2])
        print("最大距離48m單程：",round(ans,4))
#         print("最大距離48m單程：",round((1/Lin_Reg1.coef_[0])*48, 4))

        
    
        if V_State=="Full" and Fork_Flag==True and All_Cart==False:
            Distance_Y_44m_FullV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-44)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_4m_FullV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-4)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_44m_FullV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-44)))/(2*Lin_Reg1.coef_[2]),4))
            Distance_Y_4m_FullV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-4)))/(2*Lin_Reg1.coef_[2]),4))
        elif V_State=="Medium" and Fork_Flag==True and All_Cart==False:
            Distance_Y_44m_MediumV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-44)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_4m_MediumV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-4)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_44m_MediumV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-44)))/(2*Lin_Reg1.coef_[2]),4))
            Distance_Y_4m_MediumV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-4)))/(2*Lin_Reg1.coef_[2]),4))
        elif V_State=="Low" and Fork_Flag==True and All_Cart==False:
            Distance_Y_44m_LowV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-44)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_4m_LowV_Unfork.append(round((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-4)))/(2*Lin_Reg0.coef_[2]),4))
            Distance_Y_44m_LowV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-44)))/(2*Lin_Reg1.coef_[2]),4))
            Distance_Y_4m_LowV_Fork.append(round((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-4)))/(2*Lin_Reg1.coef_[2]),4))
    
    
    
    fig, ax1 = plt.subplots(figsize=(24,24))
    if All_Cart==False:
        plt.title('SC_'+str(SC_num)+"'s 超級電容伏特消耗量 & Y走行運行距離",fontproperties=myfont, fontsize=60)
    else:
        plt.title("所有車子 超級電容伏特消耗量 & Y走行運行距離",fontproperties=myfont, fontsize=60)
        print("多消耗比率",round(((-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-48)))/(2*Lin_Reg1.coef_[2]))/((-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-48)))/(2*Lin_Reg0.coef_[2]))-1,4))
    plt.xlabel('超級電容伏特消耗量(V)',fontproperties=myfont, fontsize=50)
    plt.ylabel('Y走行運行距離(m)',fontproperties=myfont, fontsize=50)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.axhline(y=48, color='black', linestyle='--', linewidth = '5')
    
    
    if Split_Fork==False:
        Y_predict = Lin_Reg.predict(X2)
        plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data, label=None)
        plt.plot(np.sort(data["超級電容伏特消耗量(V)"]), 
                 Y_predict[np.argsort(data["超級電容伏特消耗量(V)"])]
                 , label='Linear Regression Line (Y)', color="green", linewidth = '8')
    else:
        Y_predict1 = Lin_Reg1.predict(X2_1)
        Y_predict0 = Lin_Reg0.predict(X2_0)
        if Fork_Flag==False:
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data0, label=None,c="green", marker='s',alpha=0.3)
            plt.plot(np.sort(data0["超級電容伏特消耗量(V)"]), 
                     Y_predict0[np.argsort(data0["超級電容伏特消耗量(V)"])], 
                     label='Linear Regression Line (Y without Fork)', color="olivedrab", linewidth = '8')
            plt.axvline(x=(-Lin_Reg0.coef_[1]+np.sqrt(Lin_Reg0.coef_[1]**2-4*(Lin_Reg0.coef_[2])*(Lin_Reg0.intercept_+Lin_Reg0.coef_[0]-48)))/(2*Lin_Reg0.coef_[2]), color='black', linestyle='--', linewidth = '5')
        else:
            plt.scatter("超級電容伏特消耗量(V)","車子運行之距離(m)", data=data1, label=None,c="red", marker='s',alpha=0.3)
            plt.plot(np.sort(data1["超級電容伏特消耗量(V)"]), 
                     Y_predict1[np.argsort(data1["超級電容伏特消耗量(V)"])], 
                     label='Linear Regression Line (Y with Fork)', color="brown", linewidth = '8')
            plt.axvline(x=(-Lin_Reg1.coef_[1]+np.sqrt(Lin_Reg1.coef_[1]**2-4*(Lin_Reg1.coef_[2])*(Lin_Reg1.intercept_+Lin_Reg1.coef_[0]-48)))/(2*Lin_Reg1.coef_[2]), color='black', linestyle='--', linewidth = '5')
        
    
    plt.legend(loc="upper left",fontsize=23)
    plt.ylim((0,50))
    
    if SC_num!=7:
        plt.xlim((0,2.5))
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
    else:
        plt.xlim((0,5.0))
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
    
    
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
    
    print("==========================")
    return




def Draw_Plt_Idle_V(data, SC_num, Split_Fork=False, Fork_Flag=True, All_Cart=False):
#     data=data[(data["N_Idle_Group_data"]>=5) & (data["超級電容伏特消耗量(V)"]<=48-25.5) & (data["Time_Gap"]<=2000)]
    data=data[(data["N_Idle_Group_data"]>=5)]

    fig, ax1 = plt.subplots(figsize=(24,24))
    if All_Cart==False:
        plt.title('SC_'+str(SC_num)+"'s 超級電容伏特消耗量 & Idle待機時間(sec)",fontproperties=myfont, fontsize=60)
    else:
        plt.title("所有41台車 超級電容伏特消耗量 & Idle待機時間(sec)",fontproperties=myfont, fontsize=60)
    plt.xlabel('超級電容伏特消耗量(V)',fontproperties=myfont, fontsize=50)
    plt.ylabel('Idle待機時間(sec)',fontproperties=myfont, fontsize=50)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    
    
    # 不劃分有無載貨
    if Split_Fork==False:
        Lin_Reg = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data["超級電容伏特消耗量(V)"]), 
                                                                       data["Time_Gap"])
        print(SC_num,"Idle待機")
        print(Lin_Reg.score(pd.DataFrame(data["超級電容伏特消耗量(V)"]), data["Time_Gap"]))
        print(Lin_Reg.intercept_)
        print(Lin_Reg.predict([[10]]))
        print("sec/V：",round(Lin_Reg.coef_[0], 4))
        print("V/sec：",round(1/(Lin_Reg.coef_[0]), 4))
        print("10V可撐秒數：",round(Lin_Reg.predict([[10]])[0], 4), "轉成分鐘：", round(Lin_Reg.predict([[10]])[0]/60, 4))
        print("19.5V可撐秒數：",round(Lin_Reg.predict([[19.5]])[0], 4), "轉成分鐘：", round(Lin_Reg.predict([[19.5]])[0]/60, 4))
        if All_Cart==False:
            Idle_Time_10V.append(round(Lin_Reg.predict([[10]])[0]/60, 4))
            Idle_Time_19dot5V.append(round(Lin_Reg.predict([[19.5]])[0]/60, 4))
            Idle_Time_secV.append(round(Lin_Reg.coef_[0], 4))
            Idle_Time_Vsec.append(round(1/(Lin_Reg.coef_[0]), 4))
        
        tmp_row = [pd.Series([0], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns), 
                   pd.Series([30], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns)]
        plt.scatter("超級電容伏特消耗量(V)","Time_Gap", data=data, label=None)
        plt.plot(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg.predict(pd.DataFrame(data["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True)), 
                 label='Regression Line (All Idle)', color="green", linewidth = '8')
    
    # 劃分有無載貨
    else:
        if Fork_Flag==False:
            data0=data[data["Loading_Fork"]==0]
            Lin_Reg0 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data0["超級電容伏特消耗量(V)"]), 
                                                                            data0["Time_Gap"])
            print(SC_num,"Idle待機")
            print("沒載貨")
            print("sec/V：",round(Lin_Reg0.coef_[0], 4))
            print("V/sec：",round(1/(Lin_Reg0.coef_[0]), 4))
            print("10V可撐秒數：",round(Lin_Reg0.predict([[10]])[0], 4), "轉成分鐘：", round(Lin_Reg0.predict([[10]])[0]/60, 4))
            print("19.5V可撐秒數：",round(Lin_Reg0.predict([[19.5]])[0], 4), "轉成分鐘：", round(Lin_Reg0.predict([[19.5]])[0]/60, 4))
            tmp_row = [pd.Series([0], index=pd.DataFrame(data0["超級電容伏特消耗量(V)"]).columns), 
                       pd.Series([30], index=pd.DataFrame(data0["超級電容伏特消耗量(V)"]).columns)]
            plt.scatter("超級電容伏特消耗量(V)","Time_Gap", data=data0, label=None,c="green", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg0.predict(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (Idle without Fork)', color="olivedrab", linewidth = '8')
        
        else: 
            data1=data[data["Loading_Fork"]==1]
            Lin_Reg1 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data1["超級電容伏特消耗量(V)"]), 
                                                                        data1["N_Idle_Group_data"])
        
            print(SC_num,"Idle待機")
            print("沒載貨")
            print("sec/V：",round(Lin_Reg1.coef_[0], 4))
            print("V/sec：",round(1/(Lin_Reg1.coef_[0]), 4))
            print("10V可撐秒數：",round(Lin_Reg1.predict([[10]])[0], 4), "轉成分鐘：", round(Lin_Reg1.predict([[10]])[0]/60, 4))
            print("19.5V可撐秒數：",round(Lin_Reg1.predict([[19.5]])[0], 4), "轉成分鐘：", round(Lin_Reg1.predict([[19.5]])[0]/60, 4))
            tmp_row = [pd.Series([0], index=pd.DataFrame(data1["超級電容伏特消耗量(V)"]).columns), 
                       pd.Series([30], index=pd.DataFrame(data1["超級電容伏特消耗量(V)"]).columns)]
            plt.scatter("超級電容伏特消耗量(V)","Time_Gap", data=data1, label=None,c="red", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
                 Lin_Reg1.predict(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
                 , label='Linear Regression Line (Idle with Fork)', color="brown", linewidth = '8')


    plt.legend(loc="upper left",fontsize=23)
    plt.xlim((0,20+0.5))
    plt.ylim((0,30*60+50))
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(100))
    
    print("==========================")
    return



def Draw_Plt_Fork_V(data, SC_num, Split_Fork=False, Fork_Flag=True, V_State=None, All_Cart=False):
    data=data[(data["N_Fork_Group_data"]<=12) & (data["N_Fork_Group_data"]>=10)]
    
    if Split_Fork==False:
        Lin_Reg = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data["超級電容伏特消耗量(V)"]), 
                                                                       data["車子叉臂的距離(m)"])
        print(SC_num,"X橫移")
        print("資料數：",len(data),sep="")
#         print(Lin_Reg.score(pd.DataFrame(data["超級電容伏特消耗量(V)"]), data["車子叉臂的距離(m)"]))
        print("截距：",round(Lin_Reg.intercept_, 4))
        print("m/V：",round(Lin_Reg.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg.coef_[0], 4))
        print("1.6m：",round((1.6-Lin_Reg.intercept_)/Lin_Reg.coef_[0], 4))
#         print("最大距離47m單程：",round((47-Lin_Reg.intercept_)/Lin_Reg.coef_[0], 4))
#         Max_Distance_X_One_Trip_V.append(round((47-Lin_Reg.intercept_)/Lin_Reg.coef_[0]*2, 4))
#         Max_Distance_X_One_Trip_V.append(round((1/Lin_Reg.coef_[0])*47*2, 4))
    else:
        data1=data[data["Loading_Fork"]==1]
        data0=data[data["Loading_Fork"]==0]
        Lin_Reg1 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data1["超級電容伏特消耗量(V)"]), 
                                                                       data1["車子叉臂的距離(m)"])
        Lin_Reg0 = sklearn.linear_model.LinearRegression(n_jobs=-1).fit(pd.DataFrame(data0["超級電容伏特消耗量(V)"]), 
                                                                       data0["車子叉臂的距離(m)"])
        print(SC_num,"X橫移")
#         print(Lin_Reg.score(pd.DataFrame(data["超級電容伏特消耗量(V)"]), data["車子叉臂的距離(m)"]))
        print("無載貨（取貨）")
        print("資料數：",len(data0),sep="")
        print("m/V：",round(Lin_Reg0.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg0.coef_[0], 4))
        print("截距：",round(Lin_Reg0.intercept_, 4))
        print("1.6m：",round((1.6-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
#         print("最大距離47m單程（考慮截距）：",round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
#         print("最大距離47m單程：",round((1/Lin_Reg0.coef_[0])*47, 4))
        print("有載貨（放貨）")
        print("資料數：",len(data1),sep="")
        print("m/V：",round(Lin_Reg1.coef_[0], 4))
        print("V/m：",round(1/Lin_Reg1.coef_[0], 4))
        print("截距：",round(Lin_Reg1.intercept_, 4))
        print("1.6m：",round((1.6-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
#         print("最大距離47m單程（考慮截距）：",round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
#         print("最大距離47m單程：",round((1/Lin_Reg1.coef_[0])*47, 4))
        
        '''
        if V_State=="Full" and Fork_Flag==True and All_Cart==False: # Fork_Flag==True可避免重複寫入
#             Slope_Distance_X_One_Trip_V_FullV_Unfork.append(1/Lin_Reg0.coef_[0])
#             Slope_Distance_X_One_Trip_V_FullV_Fork.append(1/Lin_Reg1.coef_[0])
            Distance_X_47m_FullV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_FullV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
            
        elif V_State=="Medium" and Fork_Flag==True and All_Cart==False:
#             Slope_Distance_X_One_Trip_V_MediumV_Unfork.append(1/Lin_Reg0.coef_[0])
#             Slope_Distance_X_One_Trip_V_MediumV_Fork.append(1/Lin_Reg1.coef_[0])
            Distance_X_47m_MediumV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_MediumV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
            
        elif V_State=="Low" and Fork_Flag==True and All_Cart==False:
#             Slope_Distance_X_One_Trip_V_LowV_Unfork.append(1/Lin_Reg0.coef_[0])
#             Slope_Distance_X_One_Trip_V_LowV_Fork.append(1/Lin_Reg1.coef_[0])
            Distance_X_47m_LowV_Unfork.append(round((47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], 4))
            Distance_X_47m_LowV_Fork.append(round((47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], 4))
        '''  
        
        
    
    fig, ax1 = plt.subplots(figsize=(20,20))
    if All_Cart==False:
        plt.title('SC_'+str(SC_num)+"'s 超級電容伏特消耗量 & Fork叉臂距離",fontproperties=myfont, fontsize=60)
    else:
        plt.title("所有車子 超級電容伏特消耗量 & Fork叉臂距離",fontproperties=myfont, fontsize=60)
    plt.xlabel('超級電容伏特消耗量(V)',fontproperties=myfont, fontsize=50)
    plt.ylabel('Fork叉臂距離(m)',fontproperties=myfont, fontsize=50)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=30)
#     plt.axhline(y=47, color='black', linestyle='--', linewidth = '5')

    
#     tmp_row = [pd.Series([1], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns), 
#                pd.Series([20], index=pd.DataFrame(data["超級電容伏特消耗量(V)"]).columns)]
    
    if Split_Fork==False:
        plt.scatter("超級電容伏特消耗量(V)","車子叉臂的距離(m)", data=data, label=None)
        plt.plot(pd.DataFrame(data["超級電容伏特消耗量(V)"]), 
                 Lin_Reg.predict(pd.DataFrame(data["超級電容伏特消耗量(V)"]))
                 , label='Linear Regression Line (Fork)', color="green", linewidth = '8')
    else:
        if Fork_Flag==False:
            if All_Cart==False:
#                 tmp_data=data0[(data0["車子叉臂的距離(m)"]>=1.5) & (data0["車子叉臂的距離(m)"]<=1.65) & (data0["Loading_Fork"]==0)]
#                 tmp_data["超級電容伏特消耗量(V)"] = 1.6*tmp_data["超級電容伏特消耗量(V)"]/tmp_data["車子叉臂的距離(m)"]
#                 Pickup_V.append(round(np.mean(tmp_data["超級電容伏特消耗量(V)"]),4))
                Pickup_V.append(round(np.mean(data0[(data0["車子叉臂的距離(m)"]>=1.5) & (data0["車子叉臂的距離(m)"]<=1.65) & (data0["Loading_Fork"]==0)]["超級電容伏特消耗量(V)"]),4))
#                 Pickup_V.append(round(np.mean(data0[(data0["車子叉臂的距離(m)"]>=1.55) & (data0["車子叉臂的距離(m)"]<=1.65) & (data0["Loading_Fork"]==0)]["超級電容伏特消耗量(V)"]),4))
            plt.scatter("超級電容伏特消耗量(V)","車子叉臂的距離(m)", data=data0, label=None,c="green", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data0["超級電容伏特消耗量(V)"]), 
                     Lin_Reg0.predict(pd.DataFrame(data0["超級電容伏特消耗量(V)"])), 
                     label='Linear Regression Line (Fork: Pickup)', color="olivedrab", linewidth = '8')
#             plt.axvline(x=(47-Lin_Reg0.intercept_)/Lin_Reg0.coef_[0], color='black', linestyle='--', linewidth = '5')
        else:
            if All_Cart==False:
#                 tmp_data=data1[(data1["車子叉臂的距離(m)"]>=1.5) & (data1["車子叉臂的距離(m)"]<=1.65) & (data1["Loading_Fork"]==1)]
#                 tmp_data["超級電容伏特消耗量(V)"] = 1.6*tmp_data["超級電容伏特消耗量(V)"]/tmp_data["車子叉臂的距離(m)"]
#                 Release_V.append(round(np.mean(tmp_data["超級電容伏特消耗量(V)"]),4))
                Release_V.append(round(np.mean(data1[(data1["車子叉臂的距離(m)"]>=1.5) & (data1["車子叉臂的距離(m)"]<=1.65) & (data1["Loading_Fork"]==1)]["超級電容伏特消耗量(V)"]),4))
#                 Release_V.append(round(np.mean(data1[(data1["車子叉臂的距離(m)"]>=1.55) & (data1["車子叉臂的距離(m)"]<=1.65) & (data1["Loading_Fork"]==1)]["超級電容伏特消耗量(V)"]),4))
            plt.scatter("超級電容伏特消耗量(V)","車子叉臂的距離(m)", data=data1, label=None,c="red", marker='s',alpha=0.3)
            plt.plot(pd.DataFrame(data1["超級電容伏特消耗量(V)"]), 
                     Lin_Reg1.predict(pd.DataFrame(data1["超級電容伏特消耗量(V)"])), 
                     label='Linear Regression Line (Fork: Release)', color="brown", linewidth = '8')
#             plt.axvline(x=(47-Lin_Reg1.intercept_)/Lin_Reg1.coef_[0], color='black', linestyle='--', linewidth = '5')

            
    
#         plt.plot(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
#                  Lin_Reg1.predict(pd.DataFrame(data1["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
#                  , label='Linear Regression Line (X with Fork)', color="brown", linewidth = '8')
#         plt.plot(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True), 
#                  Lin_Reg0.predict(pd.DataFrame(data0["超級電容伏特消耗量(V)"]).append(tmp_row,ignore_index=True))
#                  , label='Linear Regression Line (X without Fork)', color="olivedrab", linewidth = '8')
        
        
    
    plt.legend(loc="upper left",fontsize=23)
    plt.ylim((0,2.5))
    plt.xlim((0,2.0))
    
    
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    
    print("==========================")
    return



def Add_0_MSC_for_Dog(x):
    try:
        return str(x).zfill(8)
    except:
        return np.nan



# https://clay-atlas.com/blog/2020/09/21/python-cn-note-string-padding-zero/
def Add_0_MSC(x):
    try:
        return str(x).zfill(3)
    except:
        return np.nan



def StrReplace_MSC(x):
    try:
        return x.replace("穿梭車","MSC_")
    except:
        return np.nan





def Import_Data_ETL(SC_num, Start_date="2021-01-01", End_date="2021-06-30",
                    Select_Charge_Data=False, Select_Idle_Data=False, Behavior=None, Get_Below=None):
    print("【" + 'SC_' + str(SC_num) + "'s data from", Start_date, "to", End_date + "】")
    df = GetSCData_PreliminaryProcessing(SC_num, start_date=Start_date, end_date=End_date)
    df = Select_Fields_Add_Flag_Charge(df)

    # (非充電)放電狀態
    if Select_Charge_Data == False or Select_Charge_Data == "False":
        df = Add_Discharge_Group_Num_Field(Select_Discharge(df))
        df = Remove_Illegal_CPM_Voltage(df, Select_Idle=Select_Idle_Data, Delete_Below_Num=0.1)
        if Behavior == "X_Group":
            # 橫移行為
            df = Add_X_Group_Num_Field(df)
            df = GroupBy_MileageSum(df, Behavior_Group=Behavior, Split_Fork=True)  # X Behavior Data
        elif Behavior == "Y_Group":
            # 直行行為
            df = Add_Y_Group_Num_Field(df)
            df = GroupBy_MileageSum(df, Behavior_Group=Behavior, Split_Fork=True)  # Y Behavior Data
        elif Behavior == "Fork_Group":
            # 插臂行為
            df = Add_Fork_Group_Num_Field(df)
            df = GroupBy_MileageSum(df, Behavior_Group=Behavior, Split_Fork=True)  # Fork Behavior Data
        elif Select_Idle_Data == True or Select_Idle_Data == "True":
            # 待機狀態
            df = Add_Idle_Group_Num_Field(df)
            df = GroupBy_MileageSum(df, Behavior_Group="Idle_Group", Split_Fork=False)  # Idle Behavior Data
        elif Behavior == None or Behavior == "None":
            # 所有移動行為（以一次放電為單位）
            df = GroupBy_MileageSum(df, Behavior_Group=Behavior, Split_Fork=True)  # Full Behavior Data
        else:
            print("Wrong Parameter!")
            return
        df = df.rename(columns={'Sum(Abs(ΔCPM_Voltage))': '超級電容伏特消耗量(V)',
                                'Sum(Abs(ΔPosition))': '車子運行之距離(m)',
                                "Sum(Abs(ΔCPM_Energy))": "超級電容能源消耗量(J)"})
        return df

    # 充電狀態
    elif Select_Charge_Data == True or Select_Charge_Data == "True":
        # 篩選充電電量情況（小於86.5%、大於86.5%、不篩選）
        df = Add_Charge_Group_Num_Field(Select_Charge(df))
        df = Get_Real_Charge_Data(Get_Charge_Data_Preprocessed(df), Get_Below=Get_Below)
        return df

    else:
        print("Wrong Parameter!")
        return





print("Running Willy_Module.py")
print("Done!")
Test_Module()
print("Let's Start!")
print()
print()

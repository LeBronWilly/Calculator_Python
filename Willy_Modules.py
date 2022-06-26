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





print("Running Willy_Module.py")
print("Done!")
Test_Module()
print("Let's Start!")
print()
print()

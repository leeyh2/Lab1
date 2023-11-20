import pandas as pd

data = pd.read_csv('Income Data1.csv')
print(data)
import numpy as np
five_num_sum = np.percentile(data['income'], [0, 25, 50, 75,100], interpolation='linear')
print('income min: ' , five_num_sum[0])
print('income Q1: ' , five_num_sum[1])
print('income median: ' , five_num_sum[2])
print('income Q3: ' , five_num_sum[3])
print('income max: ' , five_num_sum[4])

print(data['income'].var())
print(data['income'].std())

from scipy import  stats
r,p = stats.pearsonr(data['education'], data['prestige'])

print("Pearson correlation coefficient: ", r)
print("p-value: ", p)
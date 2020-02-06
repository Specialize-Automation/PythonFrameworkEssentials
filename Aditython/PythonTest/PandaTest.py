__author__ = 'Aditya Roy'

from pandas import *

# Read the excel (Get the reference of excel)
df = read_excel('E:/TestData.xlsx', sheet_name='sheet1')

print('Column count => {0}'.format(len(df.columns)))
print('Row count => {0}'.format(len(df.index)))

# Loop to get all data
print (df.index)

for i in df.index:
    print(df['UserName'][i])
    print(df['Password'][i])

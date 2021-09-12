import pandas as p
import seaborn as sb
import numpy as n
%matplotlib inline
import matplotlib.pyplot as pl
import time
import matplotlib.pyplot as plt
#from statsmodels.tsa.seasonal import seasonal_decompose

pdata_frame = p.read_csv('https://raw.githubusercontent.com/jerichoad/temp/main/DDoS_Modeling_data.csv', sep=',', index_col ='Sl Num', names = ["Sl Num", "Time", "Source","Destination","Volume", "Protocol"])

#pdata_frame.head(n=999)
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1521388078))
pdata_frame['Newtime'] = pdata_frame['Time'].apply(lambda x:time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(x))))
plt.scatter(pdata_frame['Time'],pdata_frame['Volume'])
#plt.show() # Depending on whether you use IPython or interactive mode, etc.

_time = pdata_frame['Newtime'] #Time column of the data frame
edited_time = []
for row in pdata_frame.iterrows():
            arr = str(_time).split(':')
            time_till_mins = str(arr[0]) + str(arr[1])
            edited_time.append(time_till_mins) # the rounded off time
source = pdata_frame['Source'] # source address

connection_count = {} # dictionary that stores count of connections perminute
for s in source:
  for x in edited_time :
    if x in connection_count :
      value = connection_count[x]
      value = value + 1
      connection_count[x] = value
    else:
      connection_count[x] = 1
new_count_df = (_time, source, connection_count) #count # date #source

print(new_count_df)
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(new_count_df, model='additive')
result.plot()
pyplot.show()

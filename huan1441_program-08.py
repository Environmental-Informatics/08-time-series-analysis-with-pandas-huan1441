# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Author: Tao Huang (huan1441)
#
# Created: Mar 6, 2020
#
# Script: ABE65100 huan1441_program-08.py
#
# Purpose: Script to process the discharge for the Wabash River from March 17, 2015
#          to March 24, 2016, and generate 3 plots for the streamflow.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd
import matplotlib.pyplot as plt

# a variable for input filename (txt)

inputfile = "WabashRiver_DailyDischarge_20150317-20160324.txt"

# import the discharge data(starting from 26th line) and store into 'raw_data'

raw_data = pd.read_table(inputfile,
                         header=None,
                         names=['agency','gauge_No','datetime','timezone','streamflow','remark'],
                         delimiter='\t',
                         skiprows=26)

# convert the raw datetime to a datetime format array

datetime = pd.to_datetime(raw_data['datetime'])

flow = list(raw_data['streamflow'])

streamflow = pd.DataFrame(flow,index=datetime,columns=['streamflow'])

# # generate a plot of daily average streamflow

# calculate the daily mean streamflow

flow_daily = streamflow.resample('D').mean()

flow_daily.plot(figsize=(12,6),style='bo')
plt.title("Daily Average Streamflow for Wabash River")
plt.legend(["Daily Mean"], loc='best',edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

plt.savefig("Daily Average Streamflow for Wabash River.pdf")

# # generate a plot of 10 days with highest streamflow

# sort the daily streamflow and extract the top 10 highest values

flow_10d_max = flow_daily.sort_values(by='streamflow',ascending=False).head(10)

flow_10d_max.plot(figsize=(8,6),style='ro')
plt.title("Top 10 Highest Daily Average Streamflow for Wabash River")
plt.legend(["Highest Daily"], loc='best',edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

plt.savefig("Top 10 Highest Daily Average Streamflow for Wabash River.pdf")

# # generate a plot of monthly average streamflow

# calculate the daily mean streamflow

flow_monthly = streamflow.resample('M').mean()

flow_monthly.plot(figsize=(8,6),style='g^')
plt.title("Monthly Average Streamflow for Wabash River")
plt.legend(["Monthly Mean"], loc='best',edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

plt.savefig("Monthly Average Streamflow for Wabash River.pdf")

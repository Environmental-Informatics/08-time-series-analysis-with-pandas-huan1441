# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Author: Nikolay Koldunov, Tao Huang (huan1441)
#
# Created: Mar 6, 2020
#
# Script: ABE65100 huan1441_PandasDatesDemo.py
#
# Purpose: Codes from the tutorial Time Series Analysis with Pandas
#          process the time series datasets of Arctic Oscillation (AO)
#          and North Atlantic Oscillation (NAO).
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import datetime

#!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii

ao = np.loadtxt('monthly.ao.index.b50.current.ascii')

ao[0:2]

ao.shape

dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')

dates.shape

AO = Series(ao[:,2], index=dates)

AO.plot()

AO['1980':'1990'].plot()

AO['1980-05':'1981-03'].plot()

AO[120]

AO['1960-01']

AO['1960']

AO[AO > 0]

#!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/norm.nao.monthly.b5001.current.ascii

nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)

NAO.index

aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

aonao.plot(subplots=True)

aonao.head()

aonao['NAO']

aonao.NAO

aonao['Diff'] = aonao['AO'] - aonao['NAO']
aonao.head()

del aonao['Diff']
aonao.tail()

aonao['1981-01':'1981-03']

aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')

aonao.mean()

aonao.max()

aonao.min()

aonao.mean(1)

aonao.describe()

AO_mm = AO.resample("A").mean()
AO_mm.plot(style='g--')

AO_mm = AO.resample("A").median()
AO_mm.plot()

AO_mm = AO.resample("3A").apply(np.max)
AO_mm.plot()

AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()

AO_mm

aonao.rolling(window=12, center=False).mean().plot(style='-g')

aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')

aonao.corr()

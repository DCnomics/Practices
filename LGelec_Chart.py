
# coding: utf-8

# In[ ]:


import pandas as pd
import pandas_datareader.data as web
Ready_LG = web.DataReader("KRX:066570", "google", "2010-01-02", "2017-08-17")

ma5 = Ready_LG['Close'].rolling(window=5).mean()
Ready_LG['Volume'] != 0

pd.rolling_mean(Ready_LG['Close'], 5)
Ready_LG.head()

LG = Ready_LG[Ready_LG['Volume'] !=0]
LG.tail(5)

ma5 = LG['Close'].rolling(window=5).mean()
ma10 = LG['Close'].rolling(window=10).mean()
ma20 = LG['Close'].rolling(window=20).mean()
ma60 = LG['Close'].rolling(window=60).mean()
ma120 = LG['Close'].rolling(window=120).mean()

LG.insert(len(LG.columns), "MA5", ma5)
LG.tail(5)

LG.insert(len(LG.columns), "MA10", ma10)
LG.insert(len(LG.columns), "MA20", ma20)
LG.insert(len(LG.columns), "MA60", ma60)
LG.insert(len(LG.columns), "MA120", ma120)

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib')

plt.plot(LG.index, LG['MA5'], label="MA5", color="purple" )
plt.plot(LG.index, LG['MA10'], label="MA10", color="royalblue")
plt.plot(LG.index, LG['MA20'], label="MA20", color="orange")
plt.plot(LG.index, LG['MA60'], label="MA60", color="green")
plt.plot(LG.index, LG['MA120'], label="MA120", color="grey")
plt.legend(loc='best')
plt.grid()


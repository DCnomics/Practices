
# coding: utf-8

# In[4]:


import pandas as pd
import pandas_datareader.data as web

Ready_MedyTox = web.DataReader("086900.KQ", "yahoo", "2010-01-02", "2017-08-17")

ma5 = Ready_MedyTox['Close'].rolling(window=5).mean()
Ready_MedyTox['Volume'] != 0

pd.rolling_mean(Ready_MedyTox['Close'], 5)
Ready_MedyTox.head()

MedyTox = Ready_MedyTox[Ready_MedyTox['Volume'] !=0]
MedyTox.tail(5)

ma5 = MedyTox['Close'].rolling(window=5).mean()
ma10 = MedyTox['Close'].rolling(window=10).mean()
ma20 = MedyTox['Close'].rolling(window=20).mean()
ma60 = MedyTox['Close'].rolling(window=60).mean()
ma120 = MedyTox['Close'].rolling(window=120).mean()

MedyTox.insert(len(MedyTox.columns), "MA5", ma5)
MedyTox.tail(5)

MedyTox.insert(len(MedyTox.columns), "MA10", ma10)
MedyTox.insert(len(MedyTox.columns), "MA20", ma20)
MedyTox.insert(len(MedyTox.columns), "MA60", ma60)
MedyTox.insert(len(MedyTox.columns), "MA120", ma120)

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib')

plt.plot(MedyTox.index, MedyTox['MA5'], label="MA5", color="purple" )
plt.plot(MedyTox.index, MedyTox['MA10'], label="MA10", color="royalblue")
plt.plot(MedyTox.index, MedyTox['MA20'], label="MA20", color="orange")
plt.plot(MedyTox.index, MedyTox['MA60'], label="MA60", color="green")
plt.plot(MedyTox.index, MedyTox['MA120'], label="MA120", color="grey")
plt.legend(loc='best')
plt.grid()

MedyTox.head(120)


# In[ ]:





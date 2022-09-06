#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


def get_historic_price(symbol, exchange = 'bitfinex', after='2022-08-01'):
    url = 'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'.format(symbol = symbol, exchange = exchange)
    resp = requests.get(url, params = {
        'periods' : '3600',
        'after' : str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data['result']['3600'], columns = [
        'CloseTime', 'OpenPrice', 'HighPrice', 'Lowprice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit = 's')
    df.set_index('CloseTime', inplace = True)
    return df


# In[5]:


last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
last_week


# In[10]:


btc = get_historic_price('btc', 'bitstamp', after = last_week)


# In[11]:


eth = get_historic_price('eth', 'bitstamp', after = last_week)


# In[25]:


167/24


# In[24]:


btc.describe()


# In[12]:


btc.head()


# In[22]:


btc['ClosePrice'].plot(figsize=(15, 7))


# In[23]:


eth.head()


# In[26]:


from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

#bokeh creating interractive charts, nice when you need it, less nice for printing to pdf/html
#matplotlib is still majorily more popular


# In[27]:


output_notebook()


# In[29]:


p1 = figure(x_axis_type = 'datetime', title = 'Crypto prices', width = 800)
p1.grid.grid_line_alpha = 0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

p1.line(btc.index, btc['ClosePrice'], color = '#f2a900', legend_label = 'Bitcoin')
#p1.line(eth.index, eth['ClosePrice'], color = '#A6CEE3', legend_label = 'Ether')

p1.legend.location = 'top_left'

show(p1)


# In[ ]:


#Excel writer is a component from the pandas package


# In[31]:


#writer = pd.ExcelWriter['cryptos.xlsm']
#crypto file


# In[ ]:


#btc.to_excel(writer, sheet_name='Bitcoin')
#eth.to_excel(writer, sheet_name='Ether')
#writer.save()


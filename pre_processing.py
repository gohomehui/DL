#!/usr/bin/env python
import numpy as np
import pandas as pd

df_ILMN = pd.read_csv('/Users/hjia/projects/fi/data/yahooquote/ILMN.csv')
for i in range(0,df_ILMN.last_valid_index()-370,20):
    if(df_ILMN.loc[i:i+119,'Close'].max()-df_ILMN.loc[i+120,'Close'])/df_ILMN.loc[i+120,'Close']>0.3 and (df_ILMN.loc[i:i+119,'Close'].min()-df_ILMN.loc[i+120,'Close'])/df_ILMN.loc[i+120,'Close']<-0.3:
        print df_ILMN.loc[i+120:i+370,'Open'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'High'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Low'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Close'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Volume'].to_string(index=False).replace('\n',',')+'\t'+ 'risk'
    elif(df_ILMN.loc[i:i+119,'Close'].min()-df_ILMN.loc[i+120,'Close'])/df_ILMN.loc[i+120,'Close']<-0.3:
        print df_ILMN.loc[i+120:i+370,'Open'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'High'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Low'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Close'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Volume'].to_string(index=False).replace('\n',',')+'\t'+ 'negative'
    elif(df_ILMN.loc[i:i+119,'Close'].max()-df_ILMN.loc[i+120,'Close'])/df_ILMN.loc[i+120,'Close']>0.3:
        print df_ILMN.loc[i+120:i+370,'Open'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'High'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Low'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Close'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Volume'].to_string(index=False).replace('\n',',')+'\t'+ 'positive'
    else:
        print df_ILMN.loc[i+120:i+370,'Open'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'High'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Low'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Close'].to_string(index=False).replace('\n',',')+'\t'+ \
        df_ILMN.loc[i+120:i+370,'Volume'].to_string(index=False).replace('\n',',')+'\t'+ 'netural'
        
import pandas as pd
cov19=pd.read_csv('cov19.csv')
cov19=cov19.fillna(0)
cov19['Province/State']=cov19['Province/State'].replace(0,'NA')
cov19.to_csv('cov19clean.csv',index=False)

ebola=pd.read_csv('ebola.csv')
ebola=ebola.fillna(0)
ebola.to_csv('ebolaclean.csv',index=False)

#%%
import pandas as pd 
# %%
df=pd.read_csv('customer_data.csv')
# %%
df.head(5)
# %%
df.isnull().sum()
# %%

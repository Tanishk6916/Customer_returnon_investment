#%%
import pandas as pd

# %%
df=pd.read_csv('customer_data.csv')

# %%
df.info()
# %%
df.describe()
# %%customer acquasition cost
df['CAC']=df['cost']/df['conversion_rate']
# %% return on investment
df['ROI']=((df['revenue']-df['cost'])/df['cost'])*100
# %% profit margin
df['PM']=((df['revenue']-df['cost'])/df['revenue'])*100
# %%revenue per conversion 
df['RPC']=df['revenue']/df['conversion_rate']
# %%
channel_summary=df.groupby('channel')[['cost','conversion_rate','revenue','CAC','ROI','PM','RPC']].mean().reset_index()
print(channel_summary)
# %%
df.head()
# %%
roi_summary = df.groupby('channel')['ROI'].mean().reset_index()
roi_summary.head()
# %%
roi_summary['ROI_group'] = pd.cut(roi_summary['ROI'],
                                  bins=[0,100,200,400,600,1000, roi_summary['ROI'].max()],
                                  labels=['Very Low','Low','Medium','High','Very High','Extreme'])

print('ROI_group')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(x='channel', y='ROI', data=roi_summary.sort_values(by='ROI', ascending=False))
plt.title('Average ROI per Marketing Channel', fontsize=14)
plt.xlabel('Marketing Channel')
plt.ylabel('Average ROI (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# %%
plt.figure(figsize=(8,5))
sns.countplot(x='ROI_group', data=roi_summary, order=['Very Low','Low','Medium','High','Very High','Extreme'])
plt.title('Number of Channels in Each ROI Category', fontsize=14)
plt.xlabel('ROI Group')
plt.ylabel('Number of Channels')
plt.tight_layout()
plt.show()


# %%
sns.scatterplot(x='CAC', y='ROI', hue='channel', data=df, s=100)
plt.title('CAC vs ROI per Channel')
plt.xlabel('Customer Acquisition Cost (₹)')
plt.ylabel('Return on Investment (%)')
plt.tight_layout()
plt.show()


# %%

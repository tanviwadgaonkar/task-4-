#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df=pd.read_csv(r'C:\Users\Tanvi\Downloads\USvideos.csv')
df.head()


# In[3]:


df.shape


# In[4]:


df.drop_duplicates()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.info


# In[8]:


columns_to_remove = ['thumbnail_link', 'description']
df = df.drop(columns=columns_to_remove)
df.info()


# In[9]:


df.head()


# In[10]:


df.shape


# In[11]:


from datetime import datetime


# In[12]:


import datetime


# In[13]:


df['trending_date']=df['trending_date'].apply(lambda x:datetime.datetime.strptime(x,'%y.%d.%m'))
df.head(3)


# In[14]:


df['publish time']=pd.to_datetime(df['publish_time'])
df.head(2)


# In[18]:


df['publish_month']=df['publish time'].dt.month
df['publish_day']=df['publish time'].dt.day
df['publish_hour']=df['publish time'].dt.hour
df.head(2)


# In[19]:


print(sorted(df["category_id"].unique()))
[1,2,10,15,17,20,222,23,24,25,26,27,28,29,30,43]


# In[23]:


df['category_name']=np.nan
df.loc[(df['category_id']==1),"category_name"]='films and animation'
df.loc[(df['category_id']==2),"category_name"]='peoples'
df.loc[(df['category_id']==3),"category_name"]='movies'
df.loc[(df['category_id']==22),"category_name"]='pets and animalas'
df.head()


# In[26]:


df['year']=df['publish time'].dt.year
yearly_counts=df.groupby('year')['video_id'].count()
yearly_counts.plot(kind='bar',xlabel='Year',ylabel='Total publish count ',title='total publish videos per year')
plt.show()   


# In[30]:


channel_title = df.groupby('channel_title')['views'].sum().reset_index()
top_channel = channel_title.sort_values(by='views', ascending=False).head(5)

plt.bar(top_channel['channel_title'], top_channel['views'])
plt.xlabel('Channel Title', fontsize=14)
plt.ylabel('Total Views', fontsize=14)
plt.title('Top 5 Channels by Total Views', fontsize=14)
plt.tight_layout()
plt.show()



# In[34]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
sns.countplot(x='category_name', data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=30)
plt.title('Videos Count by Category')
plt.show()


# In[35]:


videos_per_hour=df['publish_hour'].value_counts().sort_index()
plt.figure(figsize=(12,6))
sns.barplot(x=videos_per_hour.index,y=videos_per_hour.values,palette='rocket')
plt.title('number of videos published per hour')
plt.xlabel('hour of day')
plt.ylabel('number of videos')
plt.xticks(rotation=90)
plt.show()


# In[40]:


df['publish_time']=pd.to_datetime(df['publish_time'])
df['publish_date']=df['publish_time'].dt.date
videos_count_by_date=df.groupby('publish_date').size()
plt.figure(figsize=(12,6))
sns.lineplot(data=videos_count_by_date)
plt.title('number of videos published per hour')
plt.xlabel('publish date')
plt.ylabel('number of videos')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





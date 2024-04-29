#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("student scores.csv")


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# # Drop Unnamed Column

# In[8]:


df = df.drop("Unnamed: 0", axis = 1)


# In[9]:


print(df.head())


# # Gender Distribution

# In[26]:


plt.figure(figsize= (5,5))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# In[36]:


# from the above chart we have analysed that
# the number of females in datais more than the number of males


# In[37]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":'mean'})


# In[16]:


print(gb)


# In[28]:


plt.figure(figsize= (4,4))
sns.heatmap(gb, annot = True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# In[35]:


# from the above chart we have concluded that the education of the parents have a good impact on their scores


# In[22]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":'mean'})


# In[23]:


print(gb1)


# In[30]:


plt.figure(figsize= (4,4))
sns.heatmap(gb1, annot = True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# In[ ]:


# from the above chart we have concluded that the Martital Status of the parents have negligible impact on their scores


# In[31]:


sns.boxplot(data = df, x = "MathScore")
plt.show()


# In[32]:


sns.boxplot(data = df, x = "ReadingScore")
plt.show()


# In[33]:


sns.boxplot(data = df, x = "WritingScore")
plt.show()


# In[34]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[49]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["groupA", "groupB", "groupC", "groupD", "groupE"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist, labels = l, autopct = "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()
print(mlist)


# In[48]:


ax = sns.countplot(data = df, x = 'EthnicGroup')
ax.bar_label(ax.containers[0])


# In[ ]:





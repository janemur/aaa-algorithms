#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('simple_english_wiki_pagelinks.csv')


# ### Подготовливаем данные
# Начиная джойнить каждый "слой" ищем, где содержится ALgorithm
# В итоге находим его на 4

# In[34]:


df.head()


# In[35]:


an = df[df['pl_from'] == 747593]


# In[ ]:





# In[36]:


an


# In[37]:


lvl2 = pd.merge(an, df, how="left", left_on=['pl_to'], right_on=["pl_from"])


# In[38]:


lvl2


# In[39]:


lvl3 = pd.merge(lvl2, df, how="left", left_on=['pl_to_y'], right_on=["pl_from"])
lvl3[lvl3['pl_title']=='Logic']


# In[40]:


lvl4 = pd.merge(lvl3, df, how="inner", left_on=['pl_to'], right_on=["pl_from"])
lvl4


# In[41]:


lvl4.columns = [1,2,3,4,5,6,7,8,9,10, 11,12]


# In[42]:


lvl4[lvl4[11]=='Algorithm']


# ### Задание 1 и 2
# Минимальный путь равен 4, для ответа на задание 2 подойдет любой из путей из столбца 8. Как вариант -- Logic

# In[43]:


lvl4[lvl4[11]=='Algorithm']


# In[44]:


lvl5 = pd.merge(lvl4, df, how="inner", left_on=[12], right_on=["pl_from"])
lvl5


# In[45]:


lvl5[(lvl5['pl_title'] == 'Algorithm') & (lvl5[11] == 'Logic') & (lvl5[2] != 'Computer_programming')]


# In[46]:


lvl5[13] = lvl5[2]+lvl5[5]+lvl5[8]+lvl5[11]
lvl5.head(67)


# In[47]:


lvl5.head(15)


# In[48]:


lvl4[lvl4[11] == 'Algorithm']


# In[49]:


lvl4[12] = lvl4[2]+lvl4[5]+lvl4[8]+lvl4[11]


# ### Задание 3 и 4
# Минимальный путь лежит из Logic, его длина 29

# In[50]:


lvl4[(lvl4[11] == 'Algorithm')]


# In[51]:


l = lvl4.iloc[:,-2]
l[l == 'Algorithm']


# In[52]:


lvl5 = lvl5[(lvl5[2]!='Computer_programming') ]


# In[ ]:





# In[ ]:





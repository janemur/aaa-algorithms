#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('simple_english_wiki_pagelinks.csv')


# ### Подготовливаем данные
# Начиная джойнить каждый "слой" ищем, где содержится ALgorithm
# В итоге находим его на 4

# In[2]:


df.head()


# ### Решение к заданию 1 и 2

# In[3]:


# Создаем первый слой, где оставляем только строки, которые ведут от Analytics. Его id 747593. 
lvl1 = df[df['pl_from'] == 747593]
lvl1


# In[4]:


# Джойним первый слой
lvl2 = pd.merge(lvl1, df, how="left", left_on=['pl_to'], right_on=["pl_from"])
lvl2


# In[5]:


# Джойним второй слой
lvl3 = pd.merge(lvl2, df, how="left", left_on=['pl_to_y'], right_on=["pl_from"])
lvl3


# In[6]:


# Проверим смогли ли мы добраться до ALgorithm за третий уровень.  
lvl3[lvl3['pl_title']=='Algorithm']
# Результатов нет, джойним еще уровень


# In[7]:


lvl4 = pd.merge(lvl3, df, how="inner", left_on=['pl_to'], right_on=["pl_from"])
lvl4


# In[8]:


# Переименуем колнны в удобный вид для дальнейшего исследования
lvl4.columns = [1,2,3,4,5,6,7,8,9,10,11,12]


# In[9]:


# Проверим получилось ли сейчас дойди до Algorithm. 
lvl4[lvl4[11]=='Algorithm']
# Результаты найдены


# In[10]:


l4 = lvl4[lvl4[11]=='Algorithm']


# In[11]:


(l4[2]+l4[5]+l4[8]+l4[11]).str.len().min()


# ### Ответ на задание 1 и 2
# Минимальный путь равен 4, для ответа на задание 2 подойдет любой из путей из столбца 8. Как вариант -- Logic

# ### Решение к  заданию 3 и 4

# In[12]:


lvl5 = pd.merge(lvl4, df, how="inner", left_on=[12], right_on=["pl_from"])
lvl5


# In[13]:


l5 = lvl5[lvl5['pl_title']=='Algorithm']


# In[14]:


# Посчитаем минимальный путь для пятого слоя, получаем 30
(l5[2]+l5[5]+l5[8]+l5[11]+l5['pl_title']).str.len().min()


# In[15]:


lvl5 = lvl5[(lvl5[2]!='Computer_programming') & (lvl5['pl_title']=='Logic')]


# In[16]:


# Создаем 6-ой слой
lvl6 = pd.merge(lvl5, df, how="inner", left_on=['pl_to'], right_on=["pl_from"])
lvl6


# In[17]:


l6 = lvl6[lvl6['pl_title_y']=='Algorithm']


# In[18]:


# Получаем минимальный путь - 29
(l6[2]+l6[5]+l6[8]+l6[11]+l6['pl_title_x']+l6['pl_title_y']).str.len().min()


# ### Ответ к заданиям 3 и 4

# Минимальный путь - 29. На него ведет статья Logic 

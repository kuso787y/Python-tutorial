
# coding: utf-8

# # 有一個知名網站的使用者log 檔 web.txt
# 1.請試用python 計算web.txt 內共有多少行?
# 2.請找出前三最多人看的商品pid
# 3.請計算每個使用者uid 看過多少商品

# In[109]:

count = 0
with open(r'C:\Users\Administrator\Desktop\web.txt') as txt:
    for line in txt:
        count+=1
print('請試用python 計算web.txt 內共有多少行?\n{}'.format(count))


# In[112]:

from collections import Counter
c = Counter()
a = []
with open(r'C:\Users\Administrator\Desktop\web.txt','r') as txt:
    for line in txt:
        if 'pid=' in line.lower():
            a.append(line.split(";")[3])
for w in a:
    c[w] += 1
print('請找出前三最多人看的商品pid\n{}'.format(c.most_common(3)))


# In[113]:

from collections import Counter
c = Counter()
with open(r'C:\Users\Administrator\Desktop\web.txt','r') as txt:
    for line in txt:
        if 'act=view' in line.lower():
            user = line.split(";")[2].split("=")[1]
            if user != '':
                c[user] +=1
print ('請計算每個使用者uid 看過多少商品\n{}'.format(c))


# In[84]:

dic={}
dic={'a':'1','a':'1'}
dic.update({'a':'1'})
print (dic)


# In[89]:

#'U46488849': 32
a = []
b=[]
with open(r'C:\Users\Administrator\Desktop\web.txt','r') as txt:
    for line in txt:
        if 'pid=' in line.lower() and 'U46488849' in line.lower():
            b.append(line.split(";")[2].split("=")[1])
            b.append(line.split(";")[3].split("=")[1])
print (b)


# In[ ]:




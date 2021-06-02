#!/usr/bin/env python
# coding: utf-8

# # Cats and Dogs:- MAB assignment 1

# Below is cat dog result. will be used by adversary and our algo.
# The words will be treated as experts, one true expert is there

# In[1]:


import functools
@functools.lru_cache(maxsize=1280000)# for memoizing for easy retrival
def cd(s1,s2):
    dog=0
    cat=0
    ######################################
    def common(str1,str2):
        res =[]
        i=0
        for char in str1:              
            if char not in str2:
                continue
            else:
                str2 = str2.replace(char, '', 1)
                i+=1
#                 print(char)
                    
        return i
    #########################################
    set1=set()
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            dog+=1
    cat=common(s1,s2)-dog
    stri=str(cat)+"C "+str(dog)+"D"
    return stri


# In[2]:


def return_dataset():
    dataset=[]
    import csv
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ') #, quotechar='|')
        for row in reader:
            for j in range(len(row)):
                dataset.append(row[j])
    return dataset
                


# In[3]:


dataset_full=return_dataset()


# In[4]:


def finalist(datlist):
    finalist=[]
    for i in range(len(datlist)):
        str=datlist[i]
        count=0
        for j in range(len(str)):
            for k in range(j+1,len(str)):
                if str[j]==str[k]:
                    count=1
        if count==0: finalist.append(str)
    return(finalist)


# In[5]:


datset=finalist(dataset_full)
# datset


# Each word will be an expert, will produce two bits of output 

# Lessgo bois, we code the majo algo, but first avdversary putter

# In[6]:


def ldim(word,aset):
    count=0
    branches=[]
    for test in aset:
        branch=cd(word,test)
        if branch not in branches:
            count+=1
            branches.append(branch)
    return count        


# In[7]:



def best_choice(aset):
    max_branch=0
    word=aset[0]# default just in 
    for test in aset:
        count=ldim(test,aset)
        if count>max_branch:
            word=test
            max_branch=count
    return word


# In[11]:


def finalgo():
    ################### Base defs#################

    def predict(word,aset):
         a=[]
         for i in aset:
            a.append([i,cd(word,i)])
         return a
    ############################################
    #we choose the word that produces "greatest branching".
    totset=datset
    count=0
    dictset={}
    while totset: 
#         word=totset[0]
        word=best_choice(totset)
        #now we find yt predicts
        ytot=predict(word,totset)
        for i in ytot:#getting yts
            y=i[1]
            w=i[0]
            if y in dictset:
                dictset[y].append(w)
            else:
                dictset[y]=[w]
        print(word)
        yt=input()
        if yt=="0C 4D":
            return word
#             return count
        else:
            totset=dictset[yt]
            count+=1
#             tree.append([count,totset])
            dictset={}
    return ""        







# In[9]:


finalgo()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:41:01 2019

@author: vikash
"""



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:58:53 2019

@author: vikash
"""
##In the followinng program we are using  100% dominance properties only

import pandas as pd
import numpy as np
import math


    
def MAE(dataset):
       
    def dom(a,b):
        s1=sum(a)
        s2=sum(b)
        if(s1<s2):#this because of 100% dominance 
            for i in range(len(a)):
                if(a[i]>b[i]):
                    return False
                    break
            return True
    
        else:
            for i in range(len(a)):
                if(a[i]>b[i]):
                    return False
                    break
            return True
    
    
    #This function calculate mean square diffrance similarity measures..
    def MSD(u1,u2,maxx,minn):
        Axy=0#user give rating to same item as active user
        ss=0
        diff=maxx-minn
        for i in range(len(u2)):
            if(pd.isnull(u2[i])):
                pass
            else:
                Axy+=1
                ss+=((u1[i]-u2[i])*(u1[i]-u2[i]))/diff
        return (1-(1/Axy)*ss)
    
    #This functin will calculate cosine similarity..
    def cosine_Similarity(u1,u2):
        sumu1u2=0
        sqsumu1=0
        sqsumu2=0
        
        for i in range(len(u2)):
            if(pd.isnull(u2[i])):
                pass
            else:
                sumu1u2+=(u1[i]*u2[i])
                sqsumu1+=(u1[i]*u1[i])
                sqsumu2+=(u2[i]*u2[i])
        return sumu1u2/((math.sqrt(sqsumu1))*math.sqrt(sqsumu2))
    #This function will calculate correlation similarity
    
    def correlation(u1,u2, avgu1, avgu2):
        sumu1u2=0
        sqsumu1=0
        sqsumu2=0
        #print(avgu1)
        #print(avgu2)
        for i in range(len(u2)):
            if(pd.isnull(u2[i])):
                pass
            else:
                sumu1u2+=((u1[i]-avgu1)*(u2[i]-avgu2))
                
                sqsumu1+=((u1[i]-avgu1)*(u1[i]-avgu1))
                sqsumu2+=((u2[i]-avgu2)*(u2[i]-avgu2))
        #print(sumu1u2/(math.sqrt(sqsumu1*sqsumu2)))
        return sumu1u2/(math.sqrt(sqsumu1*sqsumu2))
    
           
     
           
#########################################
    userMain=dataset.iloc[0, 1:]#target user
    
    r=[]#this array will store item which is rated by target user starting index 0
    d=[]
    d.append(0)
    len(userMain)
    for i in range(len(userMain)):
        if(not(pd.isnull(userMain[i]))):
            d.append(i+1)
            r.append(i)
    
    testdata=dataset.iloc[1: ,1:]#other user ratings
    
    testreq=testdata.iloc[:,r]#Ratings of other user on same item as target user excluding target user
    
    
    allUser=dataset.iloc[:,d]#Ratings of other user on same item as target user including target user

    
    #allUser.to_csv('rating2.csv', encoding='utf-8', index=False)

    #print(userMain)
    #print(r)
    #print(testdata)
    #print(testreq)
    a=[]#array store the rating given by user 1 to items
    for item in r:
        a.append(userMain[item])
    testarr=testreq.values
    
    len(allUser.values[0])
    
    allUser.values[0][0]
    #len(allUser.values)
    
    #x.fillna(1000).iloc[1:].subtract(y,axis=1)  
    
    
    #Folowing line will find the diffrence matrix           
    x=allUser
    y=x.iloc[:,1:]
    y
    first_row = y.iloc[[0]].values[0]
    
    t=y.apply(lambda row: abs(row - first_row), axis=1)
    
    #idx=['u1','u2','u3','u4','u5','u6','u7','u8','u9','u10']
    idx=[]
    for i in range(1,(len(t)+1)):
        idx.append("u"+str(i))
    
    
    
    
    t.index=idx
    
    tt=t.iloc[1:,:]
    tt
    #tt.to_csv('diffrence.csv', encoding='utf-8', index=True)#writing the diffrence dataframe to csv file
    ##############
    wna=tt.fillna(1000)#varaible without null value
    

    
    
    
    
    
    
    ############################
    arr1=[]
    arr2=[]
    for i in range(len(tt.index)):
        
        for j in range((i+1),len(tt.index)):
            #print(wna.loc[tt.index[i]])
            #print(wna.loc[tt.index[j]])
            des=dom(wna.loc[tt.index[i]],wna.loc[tt.index[j]])
            #print(des)
            if(des):
                #print(des)
                arr1.append(wna.index[i])
                arr2.append(wna.index[j])
    
    
    ###########
    arr3=[]  #Cx This array contain non dominated set of user(Cx)
    tar='u1'#u1 is the active user...
    for item in idx:
        if((item not in arr2) and item != 'u1'):
            arr3.append(item)
        
   # print("Similar user are ") 
   # for item in arr3:
       # print(item)
        
    ################
    idx2=[]
    for i in range(1,(len(allUser)+1)):
        idx2.append("u"+str(i))
    idx2
    m1=allUser.iloc[:,1:]
    m1
    m1.index=idx2#all usier ratings same as the active user including index 
    arr4=[]#set of item from Cx with rating on item same as active user
    for item in idx2:
        if(item in arr3):
            arr4.append(m1.loc[item])
    
    ###Calulation of MSD
            
    maxx=max(m1.max())
    minn=min(m1.min())
    
    
    #MSD(m1.loc['u1'],m1.loc['u2'],maxx,minn)
    #cosine_Similarity(m1.loc['u1'],m1.loc['u2'])
    #f = open("mmsd0.6).txt", "w")#this wille create a text file.
    
    
    ####Following loop will show the MSD of all the element in arr3
    mmsd=[]#this array will store user with maximal msd
    #print("List of similar user which has lowest mean square diffrence")
    for item in arr3:
        #print(item)
        mm=MSD(m1.loc['u1'],m1.loc[item],maxx,minn)
        #print(mm)
        if(mm>=0.6):
            mmsd.append(item)
           # f.write("Mean Square Diffrence of item {} is-:{}".format(item,mm)) 
            #print("Mean Square Difference of item {} is-:{}".format(item,mm))
    ########################
    mcs=[]#Thia array will store user with maximal cosine similarity value
    for item in arr3:
        mm=cosine_Similarity(m1.loc['u1'],m1.loc[item])
        if(mm>=0.96):
            mcs.append(item)
           # f.write("Mean Square Diffrence of item {} is-:{}".format(item,mm)) 
            #print("Cosine Similarity of item {} is-:{}".format(item,mm))
    ############
    mpc=[]#This array will store user with maximal correlation value
    for item in arr3:
        summ=0
        count=0
        for i in range(len(m1.loc[item])):
            if(pd.isnull(m1.loc[item][i])):
                pass
            else:
                count+=1
                summ+=m1.loc[item][i]
           
        mm=correlation(m1.loc['u1'],m1.loc[item],(sum(m1.loc['u1']))/(len(m1.loc[item])),summ/count)    
        if(mm>=0.9):
            mpc.append(item)
            #print("Pearson Correlation Similarity of item {} is:-{}".format(item,mm))
    #############
    idx2=idx
    idx2.remove('u1')
    testdata.index=idx2
    testdata
    #############
    
     
    ################
    #Now Item Recommendation
    #For MSD
    
    #notRatedAu=[]#this array wiill store item which are not rate by ative user
    arrreturn=[]#This array store item which to be return
    ##########################
    #for mean square diffrence
    dictMSD={}  
    for i in range(len(userMain)):
        if(not((pd.isnull(userMain[i])))):
            sumMSD=0
            count=0
            for j in range(len(mmsd)):
                #print(sumMSD)
                if(pd.isnull(testdata.loc[mmsd[j]][i])):
                    pass
                else:
                    sumMSD+=(testdata.loc[mmsd[j]][i])
                    count+=1
                #sumMSD+=((testdata.fillna(0)).loc[mmsd[j]][i])
            #sumMSD=sumMSD/(len(mmsd))
            try:
                sumMSD=sumMSD/(count)
                dictMSD[i+1]=sumMSD
            except ZeroDivisionError:
                dictMSD[i+1]=2.5
    sums=0
    for item in dictMSD:
        sums+=abs(dictMSD[item]-userMain[item-1])
    sums=sums/len(dictMSD)
    arrreturn.append(sums)
        
                
    
        
    ##For Cosine SImilarity
    dictCS={}
    for i in range(len(userMain)):
        if(not((pd.isnull(userMain[i])))):
            sumCS=0
            count=0
            for j in range(len(mcs)):
                if(pd.isnull(testdata.loc[mcs[j]][i])):
                    pass
                else:
                    sumCS+=(testdata.loc[mcs[j]][i])
                    count+=1
                    
            try:
                sumCS=sumCS/count
                dictCS[i+1]=sumCS
            except ZeroDivisionError:
                dictCS[i+1]=2.5
        
    
    sums=0
    for item in dictCS:
        sums+=abs(dictCS[item]-userMain[item-1])
    sums=sums/len(dictCS)
    arrreturn.append(sums)  

    
    ############
    ##For Pearson Correlation
    dictPC={}
    for i in range(len(userMain)):
        if(not((pd.isnull(userMain[i])))):
            sumPC=0
            count=0
            for j in range(len(mpc)):
                if(pd.isnull(testdata.loc[mpc[j]][i])):
                    pass
                else:
                    sumPC+=(testdata.loc[mpc[j]][i])
                    count+=1
                    
            try:
                sumPC=sumPC/count
                dictPC[i+1]=sumPC
            except ZeroDivisionError:
                dictPC[i+1]=2.5
    sums=0
    for item in dictPC:
        sums+=abs(dictPC[item]-userMain[item-1])
    sums=sums/len(dictPC)
    arrreturn.append(sums)
    
    
    return arrreturn

dataset=pd.read_csv("newdataset.csv")
size=len(dataset)
sumMSD=0
sumCS=0
sumPC=0
for i in range(len(dataset)):
    ds=dataset
    up=ds.iloc[i,:]
    ds.iloc[i,:]=ds.iloc[0,:]
    ds.iloc[0,:]=up
    upi=ds.iloc[i,0]
    ds.iloc[i,0]=ds.iloc[0,0]
    ds.iloc[0,0]=upi
    mae=MAE(ds)
    sumMSD+=mae[0]
    sumCS+=mae[1]
    sumPC+=mae[2]
print(sumMSD/size)
print(sumCS/size)
print(sumPC/size)
    
        


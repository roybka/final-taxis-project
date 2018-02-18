# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import gc

numfiles=12
csize=10**7
ww=range(numfiles)

for k in ww: 
    means=[]
    sizes=[]
    i=k+1
    fns=['trip_data_'+str(i)+'.csv']
    fns_f=['trip_fare_'+str(i)+'.csv']
   
    
    td=pd.read_csv(fns[0],chunksize=csize)
    tf=pd.read_csv(fns_f[0],chunksize=csize)
    
    stop=0
    cntr=0
    while stop==0:
        cntr=cntr+1
        chunk=td.get_chunk()
        chunkf=tf.get_chunk()
        if chunk.shape[0]<csize:
            stop=1
        allpass=chunk.T.values[7]#chunk.passenger_count
        alltippercs=chunkf.T.values[8]/chunkf.T.values[5]
        means.append([np.mean(alltippercs[np.argwhere(np.asarray(allpass)==1)]),np.mean(alltippercs[np.argwhere(np.asarray(allpass)==2)]),np.mean(alltippercs[np.argwhere(np.asarray(allpass)==3)]),np.mean(alltippercs[np.argwhere(np.asarray(allpass)==4)])])    
        sizes.append(chunk.shape[0])
    td.close()
    tf.close()
    savestr=   "dat"+str(i)
    np.save(savestr,means,sizes)   
    gc.collect()
shapes=[]
meansa1=[]
meansa2=[]
meansa3=[]
for i in range (11):
    k=i+1
    a=np.load("dat"+str(k)+".npy")
    meansa1.append(a[0,0])
    meansa2.append(a[0,1])
    meansa3.append(a[0,2])
    shapes.append(a.shape)
a=np.array(meansa1)
b= np.array(meansa2) 
c=np.array(meansa3)
plt.bar([1-.5,2-.5,3-.5],[a.mean(),b.mean(),c.mean()],width=1)
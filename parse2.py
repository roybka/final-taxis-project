# -*- coding: utf-8 -*-
"""
Created on Mon May 01 16:00:11 2017

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

numfiles=12
csize=10**7
import scipy.io
import numpy as np
import pandas as pd
import gc
w=range(numfiles-8)
ww=[x+8 for x in w]
for k in ww: 
    alllocs=[]
    alltips=[]
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
        alldrops=chunk.T.values[7]#chunk.passenger_count
        alltippercs=chunkf.T.values[8]/chunkf.T.values[5]
        x1=chunk.T.values[10]
        y1=chunk.T.values[11]
        x2=chunk.T.values[12]
        y2=chunk.T.values[13]
        
        x1=x1.astype(float)
        x2=x2.astype(float)
        y1=y1.astype(float)
        y2=y2.astype(float)
        alltippercs=alltippercs.astype(float)
        locs=[x1,x2,y1,y2]
        alllocs.append(locs)
        alltips.append(alltippercs)
        
    td.close()
    tf.close()
    savestr=   "locdat"+str(i)+'.mat'
    scipy.io.savemat(savestr, dict(locs=locs, alltips=alltips)) 
    gc.collect()
    
    
    
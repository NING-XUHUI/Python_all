#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:03:57 2021

@author: ningxuhui
"""

#%%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpl.rcParams['legend.fontsize'] = 10

#%%
data = pd.read_csv("./FMW/L-wanqu_FMW.csv")

#%% 
time = 0.0005
vX = 0
vY = 0
vZ = 0
#%%

colums = data.columns

#%%

print(colums)

#%%

accX = data["Trigno Avanti sensor 10: Acc 10.X (IM)"]
accY = data["Trigno Avanti sensor 10: Acc 10.Y (IM)"]
accZ = data["Trigno Avanti sensor 10: Acc 10.Z (IM)"]

#%%
gyroX = data["Trigno Avanti sensor 10: Gyro 10.X (IM)"]
gyroY = data["Trigno Avanti sensor 10: Gyro 10.Y (IM)"]
gyroZ = data["Trigno Avanti sensor 10: Gyro 10.Z (IM)"]

#%%
sX = [0]
sY = [0]
sZ = [0]

#%%
for i in accX:
    sX.append(vX * time + (i * time ** 2) / 2)
    vX = vX + i * time
    
for i in accY:
    sY.append(vY * time + (i * time ** 2) / 2)
    vY = vY + i * time

for i in accZ:
    sZ.append(vZ * time + (i * time ** 2) / 2)
    vZ = vZ + i * time


#%%

pX = [0]
pY = [0]
pZ = [0]

#%%


for i in range(len(sX) - 1):
    pX.append(sX[i] * gyroX[i])


for i in range(len(sY) - 1):
    pY.append(sY[i] * gyroY[i])
    
for i in range(len(sZ) - 1):
    pZ.append(sZ[i] * gyroZ[i])
    
    
#%%

pX = [i * 1000 for i in pX]
pY = [i * 1000 for i in pY]
pZ = [i * 1000 for i in pZ]


#%%

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter3D(pX[10000:20000], pY[10000:20000], pZ[10000:20000], cmap=plt.cm)
plt.legend()
plt.show()













    
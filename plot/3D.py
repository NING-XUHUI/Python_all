#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:21:53 2021

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
data = pd.read_csv("./FMW/L-quzhou_FMW.csv")

#%%
time = 0.0005
vX = 0.0
vY = 0.0
vZ = 0.0

vX1 = 0.0
vY1 = 0.0
vZ1 = 0.0

#%%
accX = data["Trigno Avanti sensor 9: Acc 9.X (IM)"]
accY = data["Trigno Avanti sensor 9: Acc 9.Y (IM)"]
accZ = data["Trigno Avanti sensor 9: Acc 9.Z (IM)"]

accX1 = data["Trigno Avanti sensor 10: Acc 10.X (IM)"]
accY1 = data["Trigno Avanti sensor 10: Acc 10.Y (IM)"]
accZ1 = data["Trigno Avanti sensor 10: Acc 10.Z (IM)"]

#%%
gyroX = data["Trigno Avanti sensor 9: Gyro 9.X (IM)"]
gyroY = data["Trigno Avanti sensor 9: Gyro 9.Y (IM)"]
gyroZ = data["Trigno Avanti sensor 9: Gyro 9.Z (IM)"]

gyroX1 = data["Trigno Avanti sensor 10: Gyro 10.X (IM)"]
gyroY1 = data["Trigno Avanti sensor 10: Gyro 10.Y (IM)"]
gyroZ1 = data["Trigno Avanti sensor 10: Gyro 10.Z (IM)"]

#%%
sX = [0]
sY = [0]
sZ = [0]

sX1 = [0]
sY1 = [0]
sZ1 = [0]


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


for i in accX1:
    sX1.append(vX1 * time + (i * time ** 2) / 2)
    vX1 = vX1 + i * time
    
    
for i in accY1:
    sY1.append(vY1 * time + (i * time ** 2) / 2)
    vY1 = vY1 + i * time

for i in accZ1:
    sZ1.append(vZ1 * time + (i * time ** 2) / 2)
    vZ1 = vZ1 + i * time
#%%
#fig = plt.figure()
#ax = Axes3D(fig)


#ax.scatter3D(sX,sY,sZ)
#plt.show()

#%%

pX = [0]
pY = [0]
pZ = [0]

pX1 = [0]
pY1 = [0]
pZ1= [0]
#%%

for i in range(len(sX) - 1):
    pX.append(sX[i] * gyroX[i])

for i in range(len(sY) - 1):
    pY.append(sY[i] * gyroY[i])
    
for i in range(len(sZ) - 1):
    pZ.append(sZ[i] * gyroZ[i])
    
    
for i in range(len(sX1) - 1):
    pX1.append(sX1[i] * gyroX1[i])

for i in range(len(sY1) - 1):
    pY1.append(sY1[i] * gyroY1[i])
    
for i in range(len(sZ1) - 1):
    pZ1.append(sZ1[i] * gyroZ1[i])
    
    
    
#%%
pX = [ i * 100 for i in pX]
pY = [ i * 100 for i in pY]
pZ = [ i * 100 for i in pZ]

pX1 = [ i * 100 for i in pX1]
pY1 = [ i * 100 for i in pY1]
pZ1 = [ i * 100 for i in pZ1]

#%%
fig = plt.figure()
ax = Axes3D(fig)
#ax.scatter3D(pX[10000:20000], pY[10000:20000], pZ[10000:20000], label='9')
#ax.scatter3D(pX1[10000:20000], pY1[10000:20000], pZ1[10000:20000], label='10')
ax.scatter3D(pX[4000], pY[4000], pZ[4000], label='1s')
ax.scatter3D(pX[8000], pY[8000], pZ[8000], label='2s')
ax.scatter3D(pX[12000], pY[12000], pZ[12000], label='3s')
ax.scatter3D(pX[16000], pY[16000], pZ[16000], label='4s')
ax.scatter3D(pX[20000], pY[20000], pZ[20000], label='5s')
plt.legend()
#plt.colorbar()
plt.show()    
#%%
    
print(len(pX))
print(len(pY))
print(len(pZ))

#%%
print(pX[10000])

    
#%%
fig = plt.figure()
ax = Axes3D(fig)    
ax.scatter3D(accX[0:10000], accY[0:10000], accZ[0:10000], cmap=plt.cm, label='9')

#ax.scatter3D(accX1[0:20000], accY1[0:20000], accZ1[0:20000], cmap=plt.cm, label='10') 
plt.legend()
plt.show()

#%%

times = data["X[s]"]    
    
    
#%% 

print(len(times))
    
print(len(accX))   
#%%
plt.plot(times[0:20000], accX1[0:20000]) 
plt.plot(times[0:20000], accY1[0:20000]) 
plt.plot(times[0:20000], accZ1[0:20000]) 

plt.show()
    
    
    
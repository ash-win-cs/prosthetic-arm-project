#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:40:44 2021

@author: ubuntu
"""

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy.io

#print(os.listdir('datasets/set3'))


mat = scipy.io.loadmat('/home/ubuntu/Documents/project/Btech_Project/Project documentation/datasets/set3/s1_1kg.mat')
mat = {k:v for k, v in mat.items() if k[0] != '_'}

data = mat['data']

emg1 = []
emg2 = []

for i in data:
    emg1.append(i[1])
    emg2.append(i[0])
    
time = np.array([i/10000 for i in range(0, len(emg1), 1)])

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.subplot(2, 1, 1).set_title('Triceps')
plt.plot(time, emg2)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey", linewidth = "1.4", linestyle = "-.") 

plt.subplot(2, 1, 2)
plt.subplot(2, 1, 2).set_title('Biceps')
plt.plot(time, emg1)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey", linewidth = "1.4", linestyle = "-.") 

fig.tight_layout()
fig_name = 'fig2.png'
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

scale_factor = 20
plt.plot(time, emg1)
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=20)
plt.xlim(xmin / scale_factor, xmax / scale_factor)
plt.ylim(ymin / scale_factor, ymax / scale_factor)

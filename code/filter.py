# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:58:51 2021

@author: ashwincs
"""

#importing libraries
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
#from numpy import linspace, max, min, average, std, sum, sqrt, where, argmax
import scipy.io
import scipy as sp
from scipy import signal

#loading mat file
mat = scipy.io.loadmat('C:/Users/kamalcs/Documents/project/datasets/set3/s1_1kg.mat')
mat = {k:v for k, v in mat.items() if k[0] != '_'}

#import emg data from mat
data = mat['data']

#load emg signal to variables
emg_triceps = []
emg_biceps = []

for i in data:
    emg_biceps.append(i[0])
    emg_triceps.append(i[1])

emg_biceps = np.array(emg_biceps)
emg_triceps = np.array(emg_triceps)

#Loading time w.r.t sampling freq = 10000
fs = 10000    
#time = np.array([i/fs for i in range(0, len(emg_biceps), 1)])
time = np.linspace(0, len(emg_biceps) / fs, len(emg_biceps))

# process EMG signal: remove mean
emg_biceps_meancorrected = emg_biceps - np.mean(emg_biceps)
emg_triceps_meancorrected = emg_triceps - np.mean(emg_triceps)

# create bandpass filter for EMG
high = 20/(fs/2)
low = 350/(fs/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass')

# process EMG signal: filter EMG
emg_biceps_filtered = sp.signal.filtfilt(b, a, emg_biceps_meancorrected)
emg_triceps_filtered = sp.signal.filtfilt(b, a, emg_triceps_meancorrected)


#plotting
fig = plt.figure()
plt.subplot(2, 2, 1)
plt.subplot(2, 2, 1).set_title('Biceps')
plt.plot(time, emg_biceps, label = "sEMG")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.subplot(2, 2, 2)
plt.subplot(2, 2, 2).set_title('emg_biceps_filtered')
plt.plot(time, emg_biceps_filtered, label = "sEMG")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.subplot(2, 2, 3)
plt.subplot(2, 2, 3).set_title('Triceps')
plt.plot(time, emg_triceps, label = "sEMG")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.subplot(2, 2, 4)
plt.subplot(2, 2, 4).set_title('emg_triceps_filtered')
plt.plot(time, emg_triceps_filtered, label = "sEMG")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.legend()
plt.show()

fig.tight_layout()
fig_name = 'fig_filtered.png'
fig.set_size_inches(w=11,h=10)
fig.savefig(fig_name)

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:13:17 2021

@author: ashwincs
"""

#importing libraries
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
#from numpy import linspace, max, min, average, std, sum, sqrt, where, argmax
import scipy.io

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


rms_biceps = []
rms_triceps = []
t = 3
samples = int(t * fs) 
start = 0
end = samples

for i in range(0, len(emg_biceps), samples) :
    rms_biceps.append(np.sqrt(np.sum(np.square(emg_biceps[start:end]) ) / len(emg_biceps)))
    rms_triceps.append(np.sqrt(np.sum(np.square(emg_triceps[start:end])) / len(emg_triceps)))
    start = start + samples
    end = end + samples

k = 0
rms_biceps1 = []
rms_triceps1 = []

for i in range(1, len(emg_biceps)+1):
    rms_biceps1.append(rms_biceps[k])
    rms_triceps1.append(rms_triceps[k])
    if i % samples == 0 :
        k = k + 1

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.subplot(2, 1, 1).set_title('Biceps')
plt.plot(time, emg_biceps, label = "sEMG")
plt.plot(time, rms_biceps1, label = "RMS")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.subplot(2, 1, 2)
plt.subplot(2, 1, 2).set_title('Triceps')
plt.plot(time, emg_triceps, label = "sEMG")
plt.plot(time, rms_triceps1, label = "RMS")
plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=20)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.grid(True, color = "grey")#, linewidth = "1.4", linestyle = "-.") 

plt.legend()
plt.show()

fig.tight_layout()
fig_name = 'fig2.png'
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)

'''
rms_biceps.append(np.sqrt(np.sum(np.square(emg_biceps[start:end]) ) / len(emg_biceps)))
rms_triceps.append(np.sqrt(np.sum(np.square(emg_triceps[start:end])) / len(emg_triceps)))

for i in range(len(emg_biceps)-1):
    rms_biceps.append(rms_biceps[0])
    rms_triceps.append(rms_triceps[0])
'''
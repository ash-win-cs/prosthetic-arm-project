#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:14:17 2020

@author: ubuntu
"""

import pandas as pd
import matplotlib.pyplot as plt

data_set = [
        'time',
        'emg'
]

emg1 = pd.read_csv('triceps1.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 
emg2 = pd.read_csv('triceps2.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 
emg3 = pd.read_csv('triceps3.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 

fig, axs = plt.subplots(3)
fig.suptitle('Raw semg data - triceps')
axs[0].plot(emg1.time, emg1.emg)
axs[1].plot(emg2.time, emg2.emg)
axs[2].plot(emg3.time, emg3.emg)
## plt.savefig('triceps3.pdf')


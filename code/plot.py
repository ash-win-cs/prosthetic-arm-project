#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:14:17 2020
@author: ashwin c s
"""
import pandas as pd
import matplotlib.pyplot as plt

def plot(fname='biceps1.lvm'):
    data_set = [
        'time',
        'emg'
        ]
    
    emg1 = pd.read_csv('/home/ubuntu/Documents/project/Btech_Project/Project documentation/datasets/set1/biceps1.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 
    emg2 = pd.read_csv('/home/ubuntu/Documents/project/Btech_Project/Project documentation/datasets/set1/biceps2.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 
    emg3 = pd.read_csv('/home/ubuntu/Documents/project/Btech_Project/Project documentation/datasets/set1/biceps3.lvm', sep='\t', names = data_set, skiprows = 100, 
                  skipfooter = 10) 

    fig, axs = plt.subplots(3)
    fig.suptitle('Raw semg data - biceps')
    axs[0].plot(emg1.time, emg1.emg)
    axs[1].plot(emg2.time, emg2.emg)
    axs[2].plot(emg3.time, emg3.emg)
    ##plt.savefig('biceps.pdf')

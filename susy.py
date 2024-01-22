# implementation SUSY in python, since it's faster for me to write this up than scower for sources. If the implementation doesn't match the R version published elsewhere, that is on the authors for not fully reporting the calculations involved. 



import sys
import os
import time
import datetime as dt
import math
import numpy as np 
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg


def white_noise(rho, sr, n, mu=0):
    sigma = rho * np.sqrt(sr/2)
    noise = np.random.normal(mu, sigma, n)
    return noise

def sig_seg(signal,seg_size): # in samples
    segment_boundaries = np.arange(0,len(signal),seg_size)
    n = len(segment_boundaries)-1

    signal_segments = {}
    for i in range(n):
        seg_index = np.arange(segment_boundaries[i],segment_boundaries[i+1])
        signal_segments[i] = signal[seg_index]
        
    return signal_segments


def plot_zxcorr_pairs(A,B,maxlag):
    
    fig, axs = plt.subplots(2,2,figsize=(7,7))
    axs[0,0].plot(A)
    axs[1,0].plot(B)
    axs[0,0].set_title('Signal A segment')
    axs[1,0].set_title('Signal B segment')
    #CCC = axs[0,1].xcorr(A, B, usevlines=True, maxlags=maxlag, normed=True, lw=3)
    CCC = XCORR(A,B,maxlag)
    axs[0,1].fill_between(np.arange(-maxlag,maxlag+1),CCC,label = 'Fishers Z')
    axs[0,1].set_ylim([-1,1])
    axs[0,1].set_title('+/- cross-correlations')
    axs[1,1].fill_between(np.arange(-maxlag,maxlag+1),np.arctanh(CCC),label = 'Fishers Z')
    axs[1,1].plot([-maxlag,maxlag],np.arctanh(CCC).mean()*np.array([1,1]),'r',label = 'Average')
    axs[1,1].legend()
    axs[1,1].set_ylim([-3,3])
    axs[1,1].set_title('Fishers Z and Average')
    plt.show()
    
    return np.arctanh(CCC).mean()

def ZXCORR(segA,segB,maxlag):
    # this is inefficient but explicit
    ccc = pd.Series()
    for k in range(-maxlag,0):
        ccc[k] = sp.stats.pearsonr(segA[-k:], segB[:k]).statistic # pearson corr, and so ugly. stats would be a better library
    ccc[0] =  sp.stats.pearsonr(segA, segB).statistic
    for k in range(1,maxlag+1): 
        ccc[k] =sp.stats.pearsonr(segA[:-k], segB[k:]).statistic
    return np.arctanh(ccc).mean()

def XCORR(segA,segB,maxlag):
    # this is inefficient but explicit
    ccc = pd.Series()
    for k in range(-maxlag,0):
        ccc[k] = sp.stats.pearsonr(segA[-k:], segB[:k]).statistic # pearson corr, and so ugly. stats would be a better library
    ccc[0] =  sp.stats.pearsonr(segA, segB).statistic
    for k in range(1,maxlag+1): 
        ccc[k] = sp.stats.pearsonr(segA[:-k], segB[k:]).statistic
    return ccc

# def zxcorr_sims(sig_A_segments,sig_B_segments,maxlags):
#     segment_sims = pd.DataFrame(columns = ['A_seg','B_seg','zxcorr','set'])
#     k = 0
#     for i in range(n):
#         for j in range(n):
#             segment_sims.loc[k,'A_seg'] = i
#             segment_sims.loc[k,'B_seg'] = j
#             segment_sims.loc[k,'zxcorr'] = ZXCORR(sig_A_segments[i],sig_B_segments[j],maxlags)
#             if i==j:
#                 segment_sims.loc[k,'set'] = 'Real'
#             else:
#                  segment_sims.loc[k,'set'] = 'Sup'
#             k+=1
#     return segment_sims 

def zxcorr_sims(sig_A_segments,sig_B_segments,maxlags):
    segment_sims = {}
    real_set = []
    alt_set = []
    n = np.min([len(sig_A_segments),len(sig_A_segments)])
    for i in range(n):
        for j in range(n):
            zr = ZXCORR(sig_A_segments[i],sig_B_segments[j],maxlags)
            if i==j:
                real_set.append(zr)
            else:
                alt_set.append(zr)
    segment_sims['Real'] = np.array(real_set)
    
    segment_sims['Sup'] = np.array(alt_set)
    return segment_sims 
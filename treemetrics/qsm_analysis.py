# -*- coding: utf-8 -*-
"""
@author: Matheus Boni Vicari
"""

import pandas as pd
import numpy as np
import seaborn as sns
from qsm_parser import read_mat
from metrics import cylinder_radius
from metrics import group_avg
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
from numpy.polynomial import Polynomial
from scipy.optimize import curve_fit


def radius_order_analysis(mat_file):
    
    mat_data = read_mat(mat_file)
        
    r = cylinder_radius(mat_data['BVol'],  mat_data['BLen'])

    branch_data = np.hstack((r, mat_data['BOrd']))
    branch_data = pd.DataFrame(branch_data, columns=['Radius', 'Branch order'])
    fig = plt.figure()
    fig = sns.boxplot(x='Branch order', y='Radius',  data=branch_data)
    fig.set(xlabel='Branch order', ylabel='Radius (m)')
    

def volume_order_analysis(mat_file):
    
    mat_data = read_mat(mat_file)
        
    vol = mat_data['BVol'] / 1000.0
    branch_data = np.hstack((vol, mat_data['BOrd']))
    branch_data = pd.DataFrame(branch_data, columns=['Volume',
                                                     'Branch order'])
    fig = plt.figure()
    fig = sns.boxplot(x='Branch order', y='Volume',  data=branch_data)
    fig.set(xlabel='Branch order', ylabel='Volume (m^3)')


def fit_radius_order(mat_file):
    
    mat_data = read_mat(mat_file)
    
    r = cylinder_radius(mat_data['BVol'],  mat_data['BLen'])

    branch_data = np.hstack((r, mat_data['BOrd']))
    branch_data = pd.DataFrame(branch_data, columns=['Radius', 'Branch order'])

    radius_avg = group_avg(branch_data, 'Branch order')
    
    x = np.asarray(radius_avg['Branch order']).astype(float)
    y = np.asarray(radius_avg['Radius']).astype(float)
    popt, pcov = curve_fit(func, x, y, p0=(1, 1, 1))
    xx = np.arange(0, np.max(x) + 1, 1)
    yy = func(xx, *popt)

    plt.plot(xx, yy)
    
    return popt


def fit_volume_order(mat_file):
    
    mat_data = read_mat(mat_file)
    
    branch_data = np.hstack((mat_data['BVol'], mat_data['BOrd']))
    branch_data = pd.DataFrame(branch_data, columns=['Volume', 'Branch order'])

    radius_avg = group_avg(branch_data, 'Branch order')
    
    x = np.asarray(radius_avg['Branch order']).astype(float)
    y = np.asarray(radius_avg['Volume']).astype(float)
    popt, pcov = curve_fit(func, x, y, p0=(1, 1, 1))
    xx = np.arange(0, np.max(x) + 1, 1)
    yy = func(xx, *popt)

    plt.plot(xx, yy)
    
    return popt


def func(x, a, c, d):
    return a*np.exp(-c*x)+d


if __name__ == "__main__":
    
    mat_file = '../data/r6_22_testQSM.mat'
    radius_order_analysis(mat_file)
    fit_radius_order(mat_file)    
    volume_order_analysis(mat_file)
#    fit_volume_order(mat_file)

#plt.figure()
#data1 = np.hstack((mat['BVol'], mat['BOrd']))
#df = pd.DataFrame(data1, columns=['bvol', 'bord'])
#b = sns.boxplot(x='bord', y='bvol',  data=df)
#b = set(xlabel='Branch order', ylabel='Branch volume')
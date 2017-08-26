# -*- coding: utf-8 -*-
"""
@author: Matheus Boni Vicari
"""

import pandas as pd
import numpy as np
import seaborn as sns
from qsm_parser import read_mat
from metrics import cylinder_radius
import matplotlib.pyplot as plt


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
    


if __name__ == "__main__":
    
    mat_file = '../data/r6_22_testQSM.mat'
    radius_order_analysis(mat_file)
    volume_order_analysis(mat_file)

#plt.figure()
#data1 = np.hstack((mat['BVol'], mat['BOrd']))
#df = pd.DataFrame(data1, columns=['bvol', 'bord'])
#b = sns.boxplot(x='bord', y='bvol',  data=df)
#b = set(xlabel='Branch order', ylabel='Branch volume')
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:12:14 2017

@author: Matheus
"""

from scipy.io import loadmat


def read_mat(mat_file):
    
    mat_data = loadmat(mat_file)
    
    return mat_data

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:17:07 2017

@author: Matheus
"""

import numpy as np

def cylinder_radius(volume, length):
    
    return np.sqrt(volume / (np.pi * length))


def group_avg(df, var_name):
    return df.groupby([var_name], as_index=False).mean()

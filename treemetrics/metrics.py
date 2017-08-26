# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:17:07 2017

@author: Matheus
"""

import numpy as np

def cylinder_radius(volume, length):
    
    return np.sqrt(volume / (np.pi * length))

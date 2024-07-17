#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:46:53 2024

@author: leothan
"""

# Imported modules
import numpy as np

def spiral_initial_points(N):
    """
    This functions return a numpy array with 100 random (x,y)-points to be 
    used as entries to the sphere optimization.

    Parameters
    ----------
    N : 
        TYPE:Integer
        DESCRIPTION: numpy array with 100-random points in the rectangle
        [-4.5,4.5]X[-4.5,4.5]

    Returns
    -------
    numpy array with 100-radom points in the rectangle [-4.5,4.5]X[-4.5,4.5]

    """
    x = np.random.uniform(-4,4,size = (1,N))
    y = np.random.uniform(-4,4,size = (1,N))
    points = np.column_stack((x[0],y[0]))
    
    return points
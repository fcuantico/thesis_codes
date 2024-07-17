#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: leothan
"""

# Imported modules
import numpy as np
import statistics as stats
#---- BE2 Algorithms -----------------------------------
from be2_NDC import BE2_NDC
from be2_DC_NVT import BE2_NDC
from be2_DC_VarT import BE2_DC_VarT
from be2_FIRE import BE2_FIRE
#--------------------------------------------------------


class OPTIMIZERS_Data_Collection():
    """
    Data Collection of optimzers
    NOTE: if len(nsteps) == 0 then nsteps = [0,0] to be able to compute
    mean and standard deviation
    """
    
    def __init__(self,initial_points):
        
        #--- Initial Points -------------------------------------------------
        
        points = initial_points
        N = len(points)
        #-
        #----- BACKWARD EULER-(2)---------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = BE2_NDC(r0, h)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0],point[1]))
        
                
            k = k+1
            
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <2:
            nsteps = [0,0]
            
        #------- ATRIBUTES ----------------------------------------------------
        self.be2_avgsteps = stats.mean(nsteps)
        self.be2_stdsteps = stats.stdev(nsteps)
        self.be2_percent_conv = percent_converged
        self.be2_converged = converged
        #---------------------------------------------------------------------
        
        #----- BACKWARD EULER-(2)-NB------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < (N):
            r0 = points[k]
            data = BE2_NDC(r0, h)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0],point[1]))
        
                
            k = k+1
            
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <2:
            nsteps = [0,0]
            
        #------- ATRIBUTES ----------------------------------------------------
        self.be2_NDC_avgsteps = stats.mean(nsteps)
        self.be2_NDC_stdsteps = stats.stdev(nsteps)
        self.be2_NDC_percent_conv = percent_converged
        self.be2_NDC_converged = converged
        #---------------------------------------------------------------------

        
        
        
        #---------------------------------------------------------------------
        #--------------------------------------------------------------------
        
      
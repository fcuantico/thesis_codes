#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: leothan
"""

# Imported modules
import numpy as np
import statistics as stats
from prettytable import PrettyTable 
from nesterov_sutskever_mu_parameter import NAG_SUT_MU

class MU_Data_Collection():
    """
    Data Collection of optimzers
    NOTE: if len(nsteps) == 0 then nsteps = [0,0] to be able to compute
    mean and standard deviation
    """
    
    def __init__(self,N):
        
        #--- Initial Points -------------------------------------------------
        x = np.random.uniform(-4,4,size = (1,N))
        y = np.random.uniform(-4,4,size = (1,N))
        points = np.column_stack((x[0],y[0]))
        #-
        # Specify the Column Names while initializing the Table 
        myTable = PrettyTable(["mu", "percent_conv", 
                               "avg_steps", "std_stes", "min", "max"])       
        #----- Nesterov-SUT -----------------------------------------------
        mu =[0.9, 0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0]
        for i in mu:
            k = 0
            converged = []
            nsteps = []
            while k < (N):
                r0 = points[k]
                data = NAG_SUT_MU(r0,i)
                if data.steps < 1001:
                    (steps,point) = (data.steps, data.positions[0])
                    nsteps.append(data.steps)
                    converged.append((steps,point[0],point[1]))
        
                
                k = k+1
            
            #--- Converged runs stats -------------------------------------------
            len_converged_runs = len(nsteps)        
            percent_converged = ((len_converged_runs)/N)*100
            #--------------------------------------------------------------------
            if len(nsteps) < 2:
                nsteps = [0,0]
            
            percent_conv = percent_converged
            avg_steps = stats.mean(nsteps)
            std_steps = stats.stdev(nsteps)
            nag_converged = converged
            if len(nag_converged) == 0:
                min_steps = 'N/A'
                max_steps = 'N/A'
            else:
                min_steps = min(nag_converged)[0]
                max_steps = max(nag_converged)[0]
            
            data = [f'{i}',percent_conv,avg_steps, std_steps, min_steps, 
                    max_steps]
            
            myTable.add_row(data)
            
           
        
        
        #------- ATRIBUTES ----------------------------------------------------
        self.myTable = myTable
        #self.nag_stdsteps = stats.stdev(nsteps)
        #self.nag_percent_conv = percent_converged
        #self.nag_converged = converged
        #---------------------------------------------------------------------
        #--------------------------------------------------------------------
        
      
        
      
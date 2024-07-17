#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:17:07 2024

@author: leothan
"""

# Imported modules
import numpy as np
import statistics as stats
from prettytable import PrettyTable 
#---- NSTOVSUT Algorithms -----------------------------------
from nesterov_SUT_NDC import NAG_SUT_NDC 
from nesterov_SUT_DC_NVT import NAG_SUT_DCNVT
from nesterov_SUT_DC_VarT import NAG_SUT_DC_VarT
from nesterov_FIRE import NAG_FIRE
#--------------------------------------------------------


class NSTOVSUT_Error_Data_Collection():
    """
    Data Collection of optimzers
    NOTE: if len(nsteps) == 0 then nsteps = [0,0] to be able to compute
    mean and standard deviation
    """
    
    
    
    def __init__(self,initial_point):
        # Specify the Column Names while initializing the Table 
        myTable = PrettyTable(["Method", 
                               "convergence",
                                     "steps",
                                    "x_norm", 
                                   "f_norm", 
                                   "gradf(x_f)"])
        #--- Initial Point -------------------------------------------------
        r0 = initial_point
        #-
        #----- NSTOVSUT-NDC -------------------------------------------------------
        nstovsut_NDC_data = NAG_SUT_NDC(r0)
        method = 'NSTOVSUT_NDC'
        if nstovsut_NDC_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = nstovsut_NDC_data.energy_errors[-1]
            steps = nstovsut_NDC_data.steps
            x_norm = nstovsut_NDC_data.minima_error[-1]
            gradf_xf = nstovsut_NDC_data.norm_forces[-1]
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,f'{x_norm:.3e}',f'{f_norm:.3e}', 
                    f'{gradf_xf:.3e}']
        else:
            conv ="NO"
            #--
            f_norm = '-'
            steps = '-'
            x_norm = '-'
            gradf_xf = '-'
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,x_norm,f_norm,gradf_xf]       
       
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END NSTOVSUT-NDC----------------------------------------------------
        
        #----- NSTOVSUT-DC_NVT -------------------------------------------------------
        nstovsut_DC_NVT_data = NAG_SUT_DCNVT(r0)
        method = 'NSTOVSUT_DC_NVT'
        if nstovsut_DC_NVT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = nstovsut_DC_NVT_data.energy_errors[-1]
            steps = nstovsut_DC_NVT_data.steps
            x_norm = nstovsut_DC_NVT_data.minima_error[-1]
            gradf_xf = nstovsut_DC_NVT_data.norm_forces[-1]
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,f'{x_norm:.3e}',f'{f_norm:.3e}', 
                    f'{gradf_xf:.3e}']
        else:
            conv ="NO"
            #--
            f_norm = '-'
            steps = '-'
            x_norm = '-'
            gradf_xf = '-'
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,x_norm,f_norm,gradf_xf]       
       
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END NSTOVSUT-DC_NVT--------------------------------------------------
        
        #----- NSTOVSUT-DC_VarT -------------------------------------------------------
        nstovsut_DC_VarT_data = NAG_SUT_DC_VarT(r0)
        method = 'NSTOVSUT_DC_VarT'
        if nstovsut_DC_VarT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = nstovsut_DC_VarT_data.energy_errors[-1]
            steps = nstovsut_DC_VarT_data.steps
            x_norm = nstovsut_DC_VarT_data.minima_error[-1]
            gradf_xf = nstovsut_DC_VarT_data.norm_forces[-1]
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,f'{x_norm:.3e}',f'{f_norm:.3e}', 
                    f'{gradf_xf:.3e}']
        else:
            conv ="NO"
            #--
            f_norm = '-'
            steps = '-'
            x_norm = '-'
            gradf_xf = '-'
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,x_norm,f_norm,gradf_xf]     
       
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END NSTOVSUT-DC_VarT--------------------------------------------------
        
        #----- NSTOVSUT-FIRE -------------------------------------------------------
        nstovsut_FIRE_data= NAG_FIRE(r0)
        method = 'NSTOVSUT_FIRE'
        if nstovsut_FIRE_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = nstovsut_FIRE_data.energy_errors[-1]
            steps = nstovsut_FIRE_data.steps
            x_norm = nstovsut_FIRE_data.minima_error[-1]
            gradf_xf = nstovsut_FIRE_data.norm_forces[-1]
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,f'{x_norm:.3e}',f'{f_norm:.3e}', 
                    f'{gradf_xf:.3e}']
        else:
            conv ="NO"
            #--
            f_norm = '-'
            steps = '-'
            x_norm = '-'
            gradf_xf = '-'
            #------ RESULTS ADDED TO TABLE --------------------------------------
            data = [method,conv,steps,x_norm,f_norm,gradf_xf]       
       
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END FIRE--------------------------------------------------
        
        
        #---------------------------------------------------------------------
        #----- Atributes -----------------------------------------------------
        self.myTable = myTable
        
        #---------------------------------------------------------------------
        #--------------------------------------------------------------------
        
      
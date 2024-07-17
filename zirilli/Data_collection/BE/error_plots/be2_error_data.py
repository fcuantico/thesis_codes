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
#---- BE2 Algorithms -----------------------------------
from be2_NDC import BE2_NDC
from be2_DC_NVT import BE2_DC_NVT
from be2_DC_VarT import BE2_DC_VarT
from be2_FIRE import BE2_FIRE
#--------------------------------------------------------


class BE2_Error_Data_Collection():
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
        h = 0.03 #<-- step size
        #-
        #----- BE2-NDC -------------------------------------------------------
        be2_NDC_data = BE2_NDC(r0, h)
        method = 'BE2_NDC'
        if be2_NDC_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = be2_NDC_data.energy_errors[-1]
            steps = be2_NDC_data.steps
            x_norm = be2_NDC_data.minima_error[-1]
            gradf_xf = be2_NDC_data.norm_forces[-1]
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
        #----- END BE2-NDC----------------------------------------------------
        
        #----- BE2-DC_NVT -------------------------------------------------------
        be2_DC_NVT_data = BE2_DC_NVT(r0, h)
        method = 'BE2_DC_NVT'
        if be2_DC_NVT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = be2_DC_NVT_data.energy_errors[-1]
            steps = be2_DC_NVT_data.steps
            x_norm = be2_DC_NVT_data.minima_error[-1]
            gradf_xf = be2_DC_NVT_data.norm_forces[-1]
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
        #----- END BE2-DC_NVT--------------------------------------------------
        
        #----- BE2-DC_VarT -------------------------------------------------------
        be2_DC_VarT_data = BE2_DC_VarT(r0, h)
        method = 'BE2_DC_VarT'
        if be2_DC_VarT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = be2_DC_VarT_data.energy_errors[-1]
            steps = be2_DC_VarT_data.steps
            x_norm = be2_DC_VarT_data.minima_error[-1]
            gradf_xf = be2_DC_VarT_data.norm_forces[-1]
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
        #----- END BE2-DC_VarT--------------------------------------------------
        
        #----- BE2-FIRE -------------------------------------------------------
        be2_FIRE_data= BE2_FIRE(r0, h)
        method = 'BE2_FIRE'
        if be2_FIRE_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = be2_FIRE_data.energy_errors[-1]
            steps = be2_FIRE_data.steps
            x_norm = be2_FIRE_data.minima_error[-1]
            gradf_xf = be2_FIRE_data.norm_forces[-1]
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
        
      
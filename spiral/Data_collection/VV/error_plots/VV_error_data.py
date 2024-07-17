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
from vv_NDC import VV_NDC
from vv_DC_NVT import VV_DC_NVT
from vv_DC_VarT import VV_DC_VarT
from vv_FIRE import VV_FIRE
#--------------------------------------------------------


class VV_Error_Data_Collection():
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
        #----- VV-NDC -------------------------------------------------------
        vv_NDC_data = VV_NDC(r0, h)
        method = 'VV_NDC'
        if vv_NDC_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = vv_NDC_data.energy_errors[-1]
            steps = vv_NDC_data.steps
            x_norm = vv_NDC_data.minima_error[-1]
            gradf_xf = vv_NDC_data.norm_forces[-1]
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
        #----- END VV-NDC----------------------------------------------------
        
        #----- VV-DC_NVT -------------------------------------------------------
        vv_DC_NVT_data = VV_DC_NVT(r0, h)
        method = 'VV_DC_NVT'
        if vv_DC_NVT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = vv_DC_NVT_data.energy_errors[-1]
            steps = vv_DC_NVT_data.steps
            x_norm = vv_DC_NVT_data.minima_error[-1]
            gradf_xf = vv_DC_NVT_data.norm_forces[-1]
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
        #----- END VV-DC_NVT--------------------------------------------------
        
        #----- VV-DC_VarT -------------------------------------------------------
        vv_DC_VarT_data = VV_DC_VarT(r0, h)
        method = 'VV_DC_VarT'
        if vv_DC_VarT_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = vv_DC_VarT_data.energy_errors[-1]
            steps = vv_DC_VarT_data.steps
            x_norm = vv_DC_VarT_data.minima_error[-1]
            gradf_xf = vv_DC_VarT_data.norm_forces[-1]
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
        #----- END VV-DC_VarT--------------------------------------------------
        
        #----- VV-FIRE -------------------------------------------------------
        vv_FIRE_data= VV_FIRE(r0, h)
        method = 'VV_FIRE'
        if vv_FIRE_data.steps < 1000:
            conv = 'Yes'
            #--
            f_norm = vv_FIRE_data.energy_errors[-1]
            steps = vv_FIRE_data.steps
            x_norm = vv_FIRE_data.minima_error[-1]
            gradf_xf = vv_FIRE_data.norm_forces[-1]
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
        
      
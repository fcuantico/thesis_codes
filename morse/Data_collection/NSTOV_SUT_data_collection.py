#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: leothan
"""

# Imported modules
import numpy as np
import statistics as stats
from prettytable import PrettyTable 
#---- BE2 Algorithms -----------------------------------
from nesterov_SUT_NDC import NAG_SUT_NDC
from nesterov_SUT_DC_NVT import NAG_SUT_DCNVT
from nesterov_SUT_DC_VarT import NAG_SUT_DC_VarT
from nesterov_FIRE import NAG_FIRE
#--------------------------------------------------------


class NSTOV_SUT_Data_Collection():
    """
    Data Collection of optimzers
    NOTE: if len(nsteps) == 0 then nsteps = [0,0] to be able to compute
    mean and standard deviation
    """
    
    
    
    def __init__(self,initial_points):
        # Specify the Column Names while initializing the Table 
        myTable = PrettyTable(["Method", "percent_conv", 
                                   "avg_steps", "std_stes", "min", "max"])
        
        #--- Initial Points -------------------------------------------------
        
        points = initial_points
        N = len(points)
        #-
        #----- BE2-NDC -------------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = NAG_SUT_NDC(r0)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0]))
        
                
            k = k+1
            
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <1:
            percent_conv = 0
            avg_steps = '-'
            std_steps = '-'
            min_steps = '-'
            max_steps = '-'
        #--------------------------------------------------------------------
        elif len(nsteps) == 1:     
            percent_conv = percent_converged
            avg_steps = nsteps[0]
            std_steps = '-'
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
        
        else:
            percent_conv = percent_converged
            avg_steps = stats.mean(nsteps)
            std_steps = stats.stdev(nsteps)
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
       
        #------- ATRIBUTES ----------------------------------------------------
        self.nstov_sut_NDC_avgsteps = avg_steps
        self.nstov_stu_NDC_stdsteps = std_steps
        self.nstov_stu_NDC_percent_conv = percent_converged
        self.nstov_stu_NDC_converged = converged
        self.nstov_stu_NDC_min_steps = min_steps
        self.nstov_stu_NDC_max_steps = max_steps
        #---------------------------------------------------------------------
        
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['NSTOV_SUT_NDC',percent_conv,avg_steps, std_steps, min_steps, 
                    max_steps]
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-NDC----------------------------------------------------
        
        #----- BE2-DC_NVT ----------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = NAG_SUT_DCNVT(r0)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0]))
        
                
            k = k+1
            
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <1:
            percent_conv = 0
            avg_steps = '-'
            std_steps = '-'
            min_steps = '-'
            max_steps = '-'
        #--------------------------------------------------------------------
        elif len(nsteps) == 1:     
            percent_conv = percent_converged
            avg_steps = nsteps[0]
            std_steps = '-'
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
        
        else:
            percent_conv = percent_converged
            avg_steps = stats.mean(nsteps)
            std_steps = stats.stdev(nsteps)
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
       
        #------- ATRIBUTES ---------------------------------------------------
        self.nstov_sut_DC_NVT_avgsteps = avg_steps
        self.nstov_sut_DC_NVT_stdsteps = std_steps
        self.nstov_sut_DC_NVT_percent_conv = percent_converged
        self.nstov_sut_DC_NVT_converged = converged
        self.nstov_sut_DC_NVT_min_steps = min_steps
        self.nstov_sut_DC_NVT_max_steps = max_steps
        #---------------------------------------------------------------------
        
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['NSTOV_SUT_DC_NVT',percent_conv,avg_steps, std_steps, min_steps, 
                    max_steps]
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-DC_NVT-------------------------------------------------
       

        #----- BE2-DC_VarT ---------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = NAG_SUT_DC_VarT(r0)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0]))
         
                 
            k = k+1
             
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <1:
            percent_conv = 0
            avg_steps = '-'
            std_steps = '-'
            min_steps = '-'
            max_steps = '-'
         #--------------------------------------------------------------------
        elif len(nsteps) == 1:     
            percent_conv = percent_converged
            avg_steps = nsteps[0]
            std_steps = '-'
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
         
        else:
            percent_conv = percent_converged
            avg_steps = stats.mean(nsteps)
            std_steps = stats.stdev(nsteps)
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
        
        #------- ATRIBUTES ----------------------------------------------------
        self.nstov_sut_DC_VarT_avgsteps = avg_steps
        self.nstov_sut_DC_VarT_stdsteps = std_steps
        self.nstov_sut_DC_VarT_percent_conv = percent_converged
        self.nstov_sut_DC_VarT_converged = converged
        self.nstov_sut_DC_VarT_min_steps = min_steps
        self.nstov_sut_DC_VarT_max_steps = max_steps
        #---------------------------------------------------------------------
         
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['NSTOV_SUT_DC_VarT',percent_conv,avg_steps, std_steps, min_steps, 
                     max_steps]
             
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-DC_VarT------------------------------------------------           
        
        #----- BE2-FIRE ---------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = NAG_FIRE(r0)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0]))
         
                 
            k = k+1
             
        #--- Converged runs stats -------------------------------------------
        len_converged_runs = len(nsteps)        
        percent_converged = ((len_converged_runs)/N)*100
        #--------------------------------------------------------------------      
        if len(nsteps) <1:
            percent_conv = 0
            avg_steps = '-'
            std_steps = '-'
            min_steps = '-'
            max_steps = '-'
         #--------------------------------------------------------------------
        elif len(nsteps) == 1:     
            percent_conv = percent_converged
            avg_steps = nsteps[0]
            std_steps = '-'
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
         
        else:
            percent_conv = percent_converged
            avg_steps = stats.mean(nsteps)
            std_steps = stats.stdev(nsteps)
            min_steps = min(converged)[0]
            max_steps = max(converged)[0]
        
        #------- ATRIBUTES ----------------------------------------------------
        self.nstov_sut_fire_avgsteps = avg_steps
        self.nstov_sut_fire_stdsteps = std_steps
        self.nstov_sut_fire_percent_conv = percent_converged
        self.nstov_sut_fire_converged = converged
        self.nstov_sut_fire_min_steps = min_steps
        self.nstov_sut_fire_max_steps = max_steps
        #---------------------------------------------------------------------
         
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['NSTOV_SUT_FIRE',percent_conv,avg_steps, std_steps, min_steps, 
                     max_steps]
             
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-DC_VarT------------------------------------------------
        self.myTable = myTable
        
        #---------------------------------------------------------------------
        #--------------------------------------------------------------------
        
      
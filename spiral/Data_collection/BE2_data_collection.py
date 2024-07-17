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
from be2_NDC import BE2_NDC
from be2_DC_NVT import BE2_DC_NVT
from be2_DC_VarT import BE2_DC_VarT
from be2_FIRE import BE2_FIRE
#--------------------------------------------------------


class BE2_Data_Collection():
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
        self.be2_NDC_avgsteps = avg_steps
        self.be2_NDC_stdsteps = std_steps
        self.be2_NDC_percent_conv = percent_converged
        self.be2_NDC_converged = converged
        self.be2_NDC_min_steps = min_steps
        self.be2_NDC_max_steps = max_steps
        #---------------------------------------------------------------------
        
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['BE2_NDC',percent_conv,avg_steps, std_steps, min_steps, 
                    max_steps]
            
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-NDC----------------------------------------------------
        
        #----- BE2-DC_NVT -------------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = BE2_DC_NVT(r0, h)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0],point[1]))
        
                
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
        self.be2_DC_NVT_avgsteps = avg_steps
        self.be2_DC_NVT_stdsteps = std_steps
        self.be2_DC_NVT_percent_conv = percent_converged
        self.be2_DC_NVT_converged = converged
        self.be2_DC_NVT_min_steps = min_steps
        self.be2_DC_NVT_max_steps = max_steps
        #---------------------------------------------------------------------
        
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['BE2_DC_NVT',percent_conv,avg_steps, std_steps, min_steps, 
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
            data = BE2_DC_VarT(r0, h)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0],point[1]))
         
                 
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
        self.be2_DC_VarT_avgsteps = avg_steps
        self.be2_DC_VarT_stdsteps = std_steps
        self.be2_DC_VarT_percent_conv = percent_converged
        self.be2_DC_VarT_converged = converged
        self.be2_DC_VarT_min_steps = min_steps
        self.be2_DC_VarT_max_steps = max_steps
        #---------------------------------------------------------------------
         
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['BE2_DC_VarT',percent_conv,avg_steps, std_steps, min_steps, 
                     max_steps]
             
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-DC_VarT--------------------------------------------------            
        
        #----- BE2-FIRE ---------------------------------------------------
        k = 0    #<-- counter
        h = 0.03 #<-- step size
        converged = []
        nsteps = []
        while k < len(points):
            r0 = points[k]
            data = BE2_FIRE(r0, h)
            if data.steps < 1001:
                (steps,point) = (data.steps, data.positions[0])
                nsteps.append(data.steps)
                converged.append((steps,point[0],point[1]))
         
                 
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
        self.be2_fire_avgsteps = avg_steps
        self.be2_fire_stdsteps = std_steps
        self.be2_fire_percent_conv = percent_converged
        self.be2_fire_converged = converged
        self.be2_fire_min_steps = min_steps
        self.be2_fire_max_steps = max_steps
        #---------------------------------------------------------------------
         
        #------ RESULTS ADDED TO TABLE --------------------------------------
        data = ['BE2_FIRE',percent_conv,avg_steps, std_steps, min_steps, 
                     max_steps]
             
        myTable.add_row(data)
        #---------------------------------------------------------------------
        #----- END BE2-DC_VarT------------------------------------------------
        self.myTable = myTable
        
        #---------------------------------------------------------------------
        #--------------------------------------------------------------------
        
      
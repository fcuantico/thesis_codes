#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:34:02 2024

@author: leothan
"""

# Imported modules
import numpy as np
from booth_potential import Booth_Potential

class BE2_DC_VarT():
    
    def __init__(self,r0,h0):
        
        #---- DATA INITIALIZAION ---------------------------------------------
        r0 = np.array(r0)
        h = h0                                         #<-- time steps
        POS = [r0]                                     #<-- Position list
        MIN = 0                                        #<-- Energy minimum
        pos_minima = np.array([1,3])
        #---------------------------------------------------------------------
        E0 = Booth_Potential(r0[0], r0[1]).booth_energy #<-- Initial Energy
        E = [E0]
        #---------------------------------------------------------------------
        F0  = Booth_Potential(r0[0], r0[1]).force_cart #<-- Initial Force
        F = [F0]                                           #<-- Forces List
        norm_force = [ np.linalg.norm(F[0])]
        #----------------------------------------------------------------------
        v0  = np.array([0,0])                              #<-- Initial Velocity
        VEL = [v0]                                         #<-- Velocity list
        #----------------------------------------------------------------------
        Ncycle = 1000
        Np = 0
        Nreset = 0
        #---------------------------------------------------------------------
        t_max = 0.3                                    #<-- Maximum time step
        #--------------------------------------------------------------------
        k=0
        i=0
        #---------------------------------------------------------------------
        while k < (Ncycle):
            k = k + 1
            #------------ NORMALIZED POS ERROR CONVERGENCE --------------------
            up_pos_norm_error = np.linalg.norm(POS[i] - MIN)
            down_pos_norm_error = np.linalg.norm(POS[0]-MIN)
            pos_norm_error = (up_pos_norm_error/down_pos_norm_error)
            #------------------------------------------------------------------
            if pos_norm_error < 10**(-8):
                break
            #----- Direction Correction ---------------------------------------
            if  np.dot(VEL[i],F[i])<=0:
                VEL[i] = v0
                h = h0
                Np = 0
                Nreset = Nreset + 1
            #------ TIME STEP UPDATE -----------------------------------------
            elif np.dot(VEL[i],F[i])>0:
                 Np = Np + 1
                 h = h = min(1.1*h,t_max)
            #------------------------------------------------------------------
            #----- NEW ELEMENT in the lists ----------------------------------- 
            POS.append(0)
            F.append(0)
            norm_force.append(0)
            VEL.append(0)
            E.append(0)
            #--------------- BACKWARD EULER(2)---------------------------------
            #-- POSITION ------------------------------------------------------
            POS[i+1] = POS[i] + VEL[i]*h 
            #-- FORCE ---------------------------------------------------------
            F[i+1] =Booth_Potential(POS[i+1][0], POS[i+1][1]).force_cart
            norm_force[i+1] =  np.linalg.norm(F[i+1])
            #-- VELOCITY ------------------------------------------------------
            VEL[i+1] = VEL[i] + F[i+1]*h
            #-- ENERGY -------------------------------------------------------
            E[i+1] = Booth_Potential(POS[i+1][0], POS[i+1][1]).booth_energy
                        
            #-------------- NORMALIZED ENERGY ERROR CONVERGENCE ---------------            
            if abs(E[i+1]-MIN)/abs(E[0]-MIN) < 10**(-8):
                
                break
            #------------------------------------------------------------------
            
            #------------- NORM OF FORCE CONVERGENCE --------------------------
            if np.linalg.norm(F[i+1])<10**(-8):
                
                break
            #------------------------------------------------------------------
                            
            
            #--- LIST position update------------------------------------------
            i = i + 1
        
        #--------- END OF OPTIMIZTION PROCESS ---------------------------------
        
        #--- COLLECTED DATA ANALYSIS ------------------------------------------
        #----------------------------------------------------------------------
        POS = np.array(POS) #<--- To calculate the position errors
        ini_dist = np.linalg.norm(r0 - pos_minima)
        #---- position error calculation -------------------------------------
        position_errors = np.linalg.norm((POS - pos_minima), axis =1)/ini_dist 
        #---------------------------------------------------------------------
       
        #----------------- Energy Error calculations -------------------------
        E = np.array(E)#<---- To calculate Energy errors
        #---------------------------------------------------------------------
        energy_errors = abs((E - MIN)/(E[0]-MIN))        
        #------- ATRIBUTES ----------------------------------------------------
        self.steps = len(E)
        self.positions = POS
        self.minima_error = position_errors
        self.forces = F
        self.norm_forces = np.array(norm_force)
        self.velocity = VEL
        self.energy = E
        self.energy_errors = energy_errors
        self.Np = Np
        self.Nreset = Nreset
        self.min_force =min(norm_force)
       #----------------------------------------------------------------------
       # END of code ---------------------------------------------------------

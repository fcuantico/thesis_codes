#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:26:48 2023

@author: leothan
"""

# Imported modules
import numpy as np
from maytas_potential import Maytas_Potential

class VV_DC_NVT():
    
    def __init__(self,r0,h0):
        
        #---- DATA INITIALIZAION ---------------------------------------------
        r0 = np.array(r0)
        POS = [r0]                                     #<-- Position list
        MIN = 0                                        #<-- Energy minimum
        pos_minima = np.array([0,0])
        h = h0
        #---------------------------------------------------------------------
        E0=Maytas_Potential(r0[0], r0[1]).maytas_energy
        #<-Initial Energy
        E = [E0]
        #---------------------------------------------------------------------
        F0 = Maytas_Potential(r0[0], r0[1]).force_cart #<-- Initial Force
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
         
        k=0
        i=0        
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
                Np = 0
                Nreset = Nreset + 1
            #------------------------------------------------------------------                

                
            #----- NEW ELEMENT in the lists ----------------------------------- 
            POS.append(0)
            F.append(0)
            norm_force.append(0)
            VEL.append(0)
            E.append(0)
            #--------------- VELOCITY VERLET ----------------------------------
            #-- POSITION ------------------------------------------------------
            POS[i+1] = POS[i] + VEL[i]*h + (F[i]/2)*h**2
            #-- FORCE ---------------------------------------------------------
            F[i+1]=Maytas_Potential(POS[i+1][0], POS[i+1][1]).force_cart
            norm_force[i+1] =  np.linalg.norm(F[i+1])
            #-- VELOCITY ------------------------------------------------------
            VEL[i+1] = VEL[i] + ((F[i]+F[i+1])/2)*h
            #-- ENERGY -------------------------------------------------------
            E[i+1]=Maytas_Potential(POS[i+1][0], POS[i+1][1]).maytas_energy
                        
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


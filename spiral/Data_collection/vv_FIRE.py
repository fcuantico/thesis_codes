#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:26:48 2023

@author: leothan
"""

# Imported modules
import numpy as np
from spiral_potential import Spiral_Potential

class VV_FIRE():
    
    def __init__(self,r0,h0):
        
        #---- DATA INITIALIZAION ---------------------------------------------
        r0 = np.array(r0)
        POS = [r0]                                       #<-- Position list
        MIN = 0                                        #<-- Energy minimum
        pos_minima = np.array([0,0])                   #<-- Position minimum
        h = h0                                         #<-- Time step
        #---------------------------------------------------------------------
        E0 = Spiral_Potential(r0[0], r0[1]).spiral_energy #<-Initial Energy
        E = [E0]
        #---------------------------------------------------------------------
        F0 = Spiral_Potential(r0[0], r0[1]).force_cart #<-- Initial Force
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
        alpha = 0.1                               
        t_max = 0.3                               #<-- Max time step
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
            if pos_norm_error < 0.005:
                break
            #----- FIRE -------------------------------------------------------
            #---- alpha RESET and Half time step setting --------------------
            if  np.dot(VEL[i],F[i])<=0:
                VEL[i] = v0
                h = 0.5*h
                alpha = 0.1
                Np = 0
                Nreset = Nreset + 1
            elif np.dot(VEL[i],F[i])>0:
                Np = Np + 1
                
                #----- FORCE UNITE VECTOR ------------------------------------
                
                fh = F[i]/np.linalg.norm(F[i])                              
                
                #---- FIRE VELOCITY CORRECTION ---------------------
                VEL[i] = (1-alpha)*VEL[i] + alpha*np.linalg.norm(VEL[i])*fh
                #------------------------------------------------------------
                
                #----- alpha, time step UPGRADE ------------------------------
                if  Np>5:
                                    
                    h = min(1.1*h,t_max)
                    
                    
                    alpha = 0.99*alpha
                
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
            F[i+1]=Spiral_Potential(POS[i+1][0], POS[i+1][1]).force_cart
            norm_force[i+1] =  np.linalg.norm(F[i+1])
            #-- VELOCITY ------------------------------------------------------
            VEL[i+1] = VEL[i] + ((F[i]+F[i+1])/2)*h
            #-- ENERGY -------------------------------------------------------
            E[i+1]=Spiral_Potential(POS[i+1][0], POS[i+1][1]).spiral_energy
                        
            #-------------- NORMALIZED ENERGY ERROR CONVERGENCE ---------------            
            if abs(E[i+1]-MIN)/abs(E[0]-MIN) < 0.005:
                
                break
            #------------------------------------------------------------------
            
            #------------- NORM OF FORCE CONVERGENCE --------------------------
            if np.linalg.norm(F[i+1])<0.005:
                
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
        self.alpha = alpha
        self.Nreset = Nreset
        self.min_force =min(norm_force)
        #----------------------------------------------------------------------
        # END of code --------------------------------------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:20:29 2023

@author: leothan
"""

# Imported packages:
import numpy as np
import matplotlib as mpl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 

#--- Imported Methods
from nesterov_SUT_NDC import NAG_SUT_NDC 
from nesterov_SUT_DC_NVT import NAG_SUT_DCNVT
from nesterov_SUT_DC_VarT import NAG_SUT_DC_VarT
from nesterov_FIRE import NAG_FIRE





def NSTOVSUT_lennard_jones_plots(r0):
    
    #--- Backward Euler Algorithms -----------------------------------------
    nstovsut_NDC = NAG_SUT_NDC(r0)
    nstovsut_DC_NVT = NAG_SUT_DCNVT(r0)
    nstovsut_DC_VarT = NAG_SUT_DC_VarT(r0)
    nstovsut_FIRE = NAG_FIRE(r0)
    #-----------------------------------------------------------------------
    #points
    points = [nstovsut_NDC.positions, 
              nstovsut_DC_NVT.positions, 
              nstovsut_DC_VarT.positions,
              nstovsut_FIRE.positions]
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    plt.rc('text.latex', preamble=r'\usepackage{siunitx}')
    #mpl.verbose.level = 'debug-annoying'
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    # Definition of Figure and Axes
    #fig, axes = plt.subplots(1,1,figsize=(12,7),subplot_kw={'projection': '3d'})
    fig=plt.figure(figsize=(10,8))
   
    
    

    def title_and_labels(ax, title):
        ax.set_title(title)
        ax.set_xlabel("$x$", fontsize=16)
        ax.set_ylabel("$y$", fontsize=16)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
        
    
    #-------------- LENNARD-JONES FUNCTION ----------------------------
    x =  np.linspace(0.96, 3.5, 500)
    E = lambda x: 4*((1/x**12)-(1/x**6))
    #----------------------------------------------------------
    
    #--- PLOTS FOR ALL METHODS --------------------------------
   
   
    j = 0
    for k in [1,2,3,4]:
        #-- Plots -------------------------
        axes = fig.add_subplot(2, 2,k)
        p1  = axes.plot(x, E(x), alpha=1.0)
        axes.set_xlim(0.9, 3.25)
        axes.set_ylim(-1.2,2)
        #--- NSTOVSUT-DC-VarT plot annotation -------------------------------
        #if k == 3:
            #xc = points[2][-2]
            #axes.annotate('second to last', xy=(xc, E(xc)), xytext=(1.5, 0.3),
            #arrowprops=dict(facecolor='black', arrowstyle = "->"))
        #if k  == 3:
            # Plot the data on the inset axis
            # Create an inset axis in the bottom right corner
        #    axin = axes.inset_axes([0.3, 0.5, 0.35, 0.35])
            #-- NSTOV inset plots--------------------------------------
            #axin.plot(x, E(x), alpha=0.7)
        #    y1 = points[k-1]
        #    axin.scatter(y1,E(y1), color ="red", marker = '.')
        #    x1 = np.linspace(1.1,1.3,100)
        #    axin.plot(x1,E(x1), alpha=0.7, color = '#1f77b4')
        #    axin.set_title('final optimization point')
            
            # Zoom in on the noisy data in the inset axis
            #axin.set_xlim(0.70, 0.72)
            #axin.set_ylim(209, 212)
         #   axin.set_xlim(1.1,1.3)
            #axin.set_ylim(0.05, -0.05)
            # Add the lines to indicate where the inset axis is coming from
         #   axes.indicate_inset_zoom(axin)
            
        
        #--- NSTOVSUT-FIRE plot annotation -------------------------------
        #if k == 4:
        #    xc = points[k-1][-2]
        #    axes.annotate('second to last', xy=(xc, E(xc)), xytext=(1.5, 0.3),
         #   arrowprops=dict(facecolor='black', arrowstyle = "->"))
        #if k  == 4:
            # Plot the data on the inset axis
            # Create an inset axis in the bottom right corner
         #   axin = axes.inset_axes([0.6, 0.6, 0.3, 0.3])
            #-- NSTOV inset plots--------------------------------------
            #axin.plot(x, E(x), alpha=0.7)
         #   y1 = points[k-1][-1]
         #   axin.scatter(y1,E(y1), color ="red", marker = '.')
         #   x1 = np.linspace(-104993,-104991,100)
         #   axin.plot(x1,E(x1), alpha=0.7, color = '#1f77b4')
         #   axin.set_title('final optimization point')
            
            # Zoom in on the noisy data in the inset axis
            #axin.set_xlim(0.70, 0.72)
            #axin.set_ylim(209, 212)
         #   axin.set_xlim(-104993, -104991)
         #   axin.set_ylim(0.05, -0.05)
            # Add the lines to indicate where the inset axis is coming from
            #axes.indicate_inset_zoom(axin)
            
            
        #---- Axes configuration-------------------------
        if k == 1:
            title_and_labels(axes, 'NSTOVSUT-NDC')
        elif k == 2:
            title_and_labels(axes, 'NSTOVSUT-DC_NVT')
        elif k == 3:
            title_and_labels(axes, 'NSTOVSUT-DC_VarT')
        elif k == 4:
            title_and_labels(axes, 'NSTOVSUTFIRE')

    #------------- POINTS PLOT --------------------------------------------
        for i in points[j]:
            p =i[0]
                   
            axes.scatter(p, E(p), c = "r", marker ='.')
        j = j +1
    #---------------------------------------------------------------------
    
        
    
    plt.subplots_adjust(hspace=0.4)
    plt.savefig('lennard-jones_NSTOVSUT_2dplot_3.png', bbox_inches='tight')
    #plt.savefig('BE_2.png', pad_inches = 2)
    plt.show()
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:20:29 2023

@author: leothan
"""

# Imported packages:
import numpy as np
from vv_NDC import VV_NDC
from vv_DC_NVT import VV_DC_NVT
from vv_DC_VarT import VV_DC_VarT
from vv_FIRE import VV_FIRE

import matplotlib as mpl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 


def VV_morse_plots(r0,h):
    
    #--- Backward Euler Algorithms -----------------------------------------
    vv_NDC = VV_NDC(r0, h)
    vv_DC_NVT = VV_DC_NVT(r0, h)
    vv_DC_VarT = VV_DC_VarT(r0, h)
    vv_FIRE = VV_FIRE(r0, h)
    #-----------------------------------------------------------------------
    #points
    points = [vv_NDC.positions, 
              vv_DC_NVT.positions, 
              vv_DC_VarT.positions,
              vv_FIRE.positions]
    
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
    fig=plt.figure(figsize=(16,20))
   
    
    

    def title_and_labels(ax, title):
        ax.set_title(title)
        ax.set_xlabel("$x$", fontsize=16)
        ax.set_ylabel("$y$", fontsize=16)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    
    #-------------- MORSE FUNCTION ----------------------------
    x = np.linspace(0, 10, 500)
    E = lambda x: (1-np.exp(-(x-1)))**2
    #----------------------------------------------------------
    
    #--- PLOTS FOR ALL METHODS --------------------------------
   
   
    j = 0
    for k in [1,2,3,4]:
        #-- Plots -------------------------
        axes = fig.add_subplot(2, 2,k)
        p1  = axes.plot(x, E(x), alpha=1.0)
        axes.set_xlim(-0.25, 8)
        if k  > 1:
            # Plot the data on the inset axis
            # Create an inset axis in the bottom right corner
            axin = axes.inset_axes([0.32, 0.6, 0.28, 0.28])
            #-- BE inset plots--------------------------------------
            axin.plot(x, E(x), alpha=0.7)
            y1 = points[k-1]
            axin.scatter(y1,E(y1), color ="red", marker = '.')
            #axin.semilogy(x1,y1, color = "gray", linestyle = "dashed")
            
            # Zoom in on the noisy data in the inset axis
            axin.set_xlim(0.4, 1.2)
            axin.set_ylim(-0.2, 0.4)
            
            # Add the lines to indicate where the inset axis is coming from
            axes.indicate_inset_zoom(axin)
            
        #---- Axes configuration-------------------------
        if k == 1:
            title_and_labels(axes, 'VV-NDC')
        elif k == 2:
            title_and_labels(axes, 'VV-DC_NVT')
        elif k == 3:
            title_and_labels(axes, 'VV-DC_VarT')
        elif k == 4:
            title_and_labels(axes, 'VV-FIRE')

    #------------- POINTS PLOT --------------------------------------------
        for i in points[j]:
            p =i[0]
                   
            axes.scatter(p, E(p), c = "r", marker ='.')
        j = j +1
    #---------------------------------------------------------------------
    
        
    
    
    plt.savefig('morse_VV_2dplot.png', bbox_inches='tight')
    #plt.savefig('BE_2.png', pad_inches = 2)
    plt.show()
    
    
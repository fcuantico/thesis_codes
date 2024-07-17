#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:20:29 2023

@author: leothan
"""

# Imported packages:
import numpy as np
from be2_NDC import BE2_NDC
from be2_DC_NVT import BE2_DC_NVT
from be2_DC_VarT import BE2_DC_VarT
from be2_FIRE import BE2_FIRE

import matplotlib as mpl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 


def BE2_morse_plots(r0,h):
    
    #--- Backward Euler Algorithms -----------------------------------------
    be2_NDC = BE2_NDC(r0, h)
    be2_DC_NVT = BE2_DC_NVT(r0, h)
    be2_DC_VarT = BE2_DC_VarT(r0, h)
    be2_FIRE = BE2_FIRE(r0, h)
    #-----------------------------------------------------------------------
    #points
    points = [be2_NDC.positions, 
              be2_DC_NVT.positions, 
              be2_DC_VarT.positions,
              be2_FIRE.positions]
    
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

    

   
    # Defining contour levels
    #levels = np.linspace(-4, 4, 10)
    #levels = np.logspace(-1,1,6,base = 10)
    #------------------------------------------------
    j = 0
    for k in [1,2,3,4]:
        #-- First Plot-  FIRTE-Velocity Verlet ----------------
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
            title_and_labels(axes, 'BE-NDC')
        elif k == 2:
            title_and_labels(axes, 'BE-DC_NVT')
        elif k == 3:
            title_and_labels(axes, 'BE-DC_VarT')
        elif k == 4:
            title_and_labels(axes, 'BE-FIRE')

    #------------- POINTS PLOT --------------------------------------------
        for i in points[j]:
            p =i[0]
                   
            axes.scatter(p, E(p), c = "r", marker ='.')
        j = j +1
    #---------------------------------------------------------------------
    
        
    
    
    plt.savefig('morse_BE_2dplot.png', bbox_inches='tight')
    #plt.savefig('BE_2.png', pad_inches = 2)
    plt.show()
    
    
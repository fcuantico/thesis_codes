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


def VV_spiral_plots(r0,h):
    
    #--- Backward Euler Algorithms -----------------------------------------
    vv_NDC = VV_NDC(r0, h)
    vv_DC_NVT = VV_DC_NVT(r0, h)
    vv_DC_VarT = VV_DC_VarT(r0,h)
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
    
    
    theta  = np.linspace(0,2*np.pi,200)
    radius = np.linspace(0,4,200)

    THETA, R = np.meshgrid(theta,radius)
    #-------------- SPIRAL FUNCTION ----------------------------
    E = lambda r,t: (np.sin(np.pi*r + t/2))**2 + (r**2)/10
    Z = E(R,THETA)

    X, Y = R*np.cos(THETA), R*np.sin(THETA)

   
    # Defining contour levels
    #levels = np.linspace(-4, 4, 10)
    #levels = np.logspace(-1,1,6,base = 10)
    #------------------------------------------------
    j = 0
    for k in [1,3,5,7]:
        #-- First Plot-  FIRTE-Velocity Verlet ----------------
        axes = fig.add_subplot(4, 2, k,projection='3d')
        p1  = axes.plot_wireframe(X, Y, Z,alpha=0.2)
        axes.view_init(80, -60)
        #axes.set_xlim(-7.5, 7.5)
        #axes.set_ylim(-7.5, 7.5)
        #axes.set_zlim(0, 70)
        #---- Axes configuration-------------------------
        if k == 1:
            title_and_labels(axes, 'VV-NDC')
        elif k == 3:
            title_and_labels(axes, 'VV-DC_NVT')
        elif k == 5:
            title_and_labels(axes, 'VV-DC_VarT')
        elif k == 7:
            title_and_labels(axes, 'VV-FIRE')

    #------------- POINTS PLOT --------------------------------------------
        for i in points[j]:
            x =i[0]
            y =i[1]
        
            axes.scatter(x,y, E(x,y), c = "r", s = 20)
        j = j +1
    #---------------------------------------------------------------------
    #--------- CONTOUR PLOT ---------------------------------------------
    j = 0
    for k in [2,4,6,8]:
        axes = fig.add_subplot(4, 2, k)
        #levels = np.logspace(-1,1,8,base = 10)
        #------------------------------------------------
        #-- Plot ----------------------------------------
        cp = axes.contour(X, Y, Z, levels = 15)
        #------------------------------------------------
        #---- Axes configuration-------------------------
        title_and_labels(axes, 'Contour Plot')
        
        
        
    #-----------------------------------------------
        x = []
        y = []
        for i in points[j]:
            x.append(i[0])
            y.append(i[1])
        
        j = j + 1
        axes.scatter(x,y,color='red', marker = ".")
        #axes.set_xlim(-1, 1)
        #axes.set_ylim(-1, 1)
    #--------------------------------------------------------------------
    #plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95,
    #                    wspace=0.4, hspace=0.8)
    #plt.subplots_adjust(hspace=0.8)
            
    
    
    plt.savefig('spiral_VV_3dplot.png', bbox_inches='tight')
    #plt.savefig('BE_2.png', pad_inches = 2)
    plt.show()
    
    
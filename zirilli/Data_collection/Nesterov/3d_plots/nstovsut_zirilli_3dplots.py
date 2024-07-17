#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:20:29 2023

@author: leothan
"""

# Imported packages:
import numpy as np
from nesterov_SUT_NDC import NAG_SUT_NDC 
from nesterov_SUT_DC_NVT import NAG_SUT_DCNVT
from nesterov_SUT_DC_VarT import NAG_SUT_DC_VarT
from nesterov_FIRE import NAG_FIRE

import matplotlib as mpl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 


def NSTOVSUT_zirilli_3dplots(r0):
    
    #--- NSTOVSUT Algorithms -----------------------------------------
    nag_sut_NDC = NAG_SUT_NDC(r0)
    nag_sut_DC_NVT = NAG_SUT_DCNVT(r0)
    nag_sut_DC_VarT = NAG_SUT_DC_VarT(r0)
    nag_sut_FIRE = NAG_FIRE(r0)
    #-----------------------------------------------------------------------
    #points
    points = [nag_sut_NDC.positions, 
              nag_sut_DC_NVT.positions, 
              nag_sut_DC_VarT.positions,
              nag_sut_FIRE.positions]
    
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
    
    
    x =  np.linspace(-10, 10,100)
    y =  np.linspace(-10, 10,100)

    X, Y = np.meshgrid(x,y)

    #-------------- ZIRILLI FUNCTION ----------------------------
    E = lambda x,y: 0.25*x**4 - 0.25*x**2 + 0.1*x + 0.5*y**2

    Z = E(X,Y)

   
    # Defining contour levels
    #levels = np.linspace(-4, 4, 10)
    #levels = np.logspace(-1,1,6,base = 10)
    #------------------------------------------------
    j = 0
    for k in [1,3,5,7]:
        #-- First Plot- 
        axes = fig.add_subplot(4, 2, k,projection='3d')
        p1  = axes.plot_wireframe(X, Y, Z,alpha=0.2)
        axes.view_init(55, -60)
        #axes.set_xlim(-5.5, 5.5)
        #axes.set_ylim(-5.5, 5.5)
        #axes.set_zlim(0, 50)
        #---- Axes configuration-------------------------
        if k == 1:
            title_and_labels(axes, 'NSTOVSUT-NDC')
        elif k == 3:
            title_and_labels(axes, 'NSTOVSUT-DC_NVT')
        elif k == 5:
            title_and_labels(axes, 'NSTOVSUT-DC_VarT')
        elif k == 7:
            title_and_labels(axes, 'NSTOVSUT-FIRE')

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
        levels = np.logspace(-4,4,20,base = 10)
        #------------------------------------------------
        #-- Plot ----------------------------------------
        cp = axes.contour(X, Y, Z, levels = levels)        
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
            
    
    
    plt.savefig('zirilli_NSTOVSUT_3dplot.png', bbox_inches='tight')
    #plt.savefig('BE_2.png', pad_inches = 2)
    plt.show()
    
    
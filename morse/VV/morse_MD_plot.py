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


def morse_MD_plot(points):
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    # Definition of Figure and Axes
    #fig, axes = plt.subplots(1,1,figsize=(12,7),subplot_kw={'projection': '3d'})
    fig,axes=plt.subplots(1,1,figsize=(12,7))



    def title_and_labels(ax):
        ax.set_title('BE2 Optimization', fontsize = 25)
        ax.set_xlabel("$x$", fontsize=16)
        ax.set_ylabel("$y$", fontsize=16)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    #if len(points)<100:
    #    x =  np.linspace(0.96, 1.5, 500)
    
    #else:
    #    x = np.linspace(0.96, 3.5, 500)
    x = np.linspace(0, 10, 500)
    E = lambda x: (1-np.exp(-(x-1)))**2


   
        #-- Plot ----------------------------------------
    #cp  = axes.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    p  = axes.plot(x,E(x), color ='k', alpha=0.5)
    #axes.view_init(60, -63)
    #axes.view_init(45, -60)
       #---- Axes configuration-------------------------
    title_and_labels(axes)
    #-----------------------------------------------
    #--- Adding color bar to plot
    #cb = fig.colorbar(cp) # Add a colorbar to a plot
    #cb.set_label(r"$z$", fontsize=16)
    #-------------

   
    
      
#    x_coord = []
#    y_coord = []
    for i in points:
        x = i[0]
                
        axes.scatter(x, E(x), c = "r", marker = '.')
        #axes.scatter(x,y, marker = ".", c = "r") <--- contour points in
        # in the same 3d graph projected to the xy-plnae
    
    #if len(points)<100:
    #    plt.xlim(0, 10)
    #else:
    #    plt.xlim(0, 3.5)
    axes.set_xlim(-0.5,10)
    
    
    plt.savefig('VV_morse.png', bbox_inches='tight')
    plt.show()
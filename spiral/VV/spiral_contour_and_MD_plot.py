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


def spiral_contour_and_MD_plot(points):
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    # Definition of Figure and Axes
    #fig, axes = plt.subplots(1,1,figsize=(12,7),subplot_kw={'projection': '3d'})
    fig,axes=plt.subplots(1,1,figsize=(12,7))



    def title_and_labels(ax, title):
        ax.set_title(title)
        ax.set_xlabel("$x$", fontsize=16)
        ax.set_ylabel("$y$", fontsize=16)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    
    theta  = np.linspace(0,2*np.pi,200)
    radius = np.linspace(0,4,200)

    THETA, R = np.meshgrid(theta,radius)
    E = lambda r,t: (np.sin(np.pi*r + t/2))**2 + (r**2)/10
    Z = E(R,THETA)

    X, Y = R*np.cos(THETA), R*np.sin(THETA)

   
    # Defining contour levels
    #levels = np.linspace(-4, 4, 10)
    levels = np.logspace(-4,4,10,base = 10)
    #------------------------------------------------
    #-- Plot ----------------------------------------
    cp = axes.contour(X, Y, Z,levels = 10)
    #------------------------------------------------
    #---- Axes configuration-------------------------
    title_and_labels(axes, 'Contour Plot')
    #-----------------------------------------------
    #--- Adding color bar to plot
    #cb = fig.colorbar(cp) # Add a colorbar to a plot
    #cb.set_label(r"$z$", fontsize=16)
    #-------------

   
    
      
    x_coord = []
    y_coord = []
    for i in points:
        x_coord.append(i[0])
        y_coord.append(i[1])
        
    axes.scatter(x_coord,y_coord,color='red')

    #plt.xlim(-2.5, 2.5)
    #plt.ylim(-2.5, 2.5)
    
    plt.show()

        
    



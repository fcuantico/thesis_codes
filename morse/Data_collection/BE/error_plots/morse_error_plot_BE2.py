#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:22:17 2024

@author: leothan
"""

# Imported packages:
import numpy as np
from be2_NDC import BE2_NDC
from be2_DC_NVT import BE2_DC_NVT
from be2_DC_VarT import BE2_DC_VarT
from be2_FIRE import BE2_FIRE
import matplotlib as mpl
import matplotlib.pyplot as plt 


def error_plot_BE2(r0,h):
    
    #--- Backward Euler Algorithms -----------------------------------------
    be2_NDC = BE2_NDC(r0, h)
    be2_DC_NVT = BE2_DC_NVT(r0, h)
    be2_DC_VarT = BE2_DC_VarT(r0, h)
    be2_FIRE = BE2_FIRE(r0, h)
    #-----------------------------------------------------------------------
    # BE2 points
    points_be2 = [be2_NDC.energy_errors,
                  be2_DC_NVT.energy_errors,
                  be2_DC_VarT.energy_errors,
                  be2_FIRE.energy_errors]
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    plt.rc('text.latex', preamble=r'\usepackage{siunitx}')
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    #---  Figure (Canvas) and Axes creation
    fig, axes = plt.subplots(nrows=1,ncols=1)
    
    

    def title_and_labels(ax, title):
        ax.set_title(title,fontsize = 20)
        ax.set_xlabel("$x$", fontsize=12)
        ax.set_ylabel("$y$", fontsize=12)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    #--------- BE2-NDC PLOT ------------------------------------------------
    if be2_NDC.steps <=1000:
        x = np.linspace(1,be2_NDC.steps,be2_NDC.steps)
        y = points_be2[0]
        steps = be2_NDC.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"BE-NDC({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-DC_NVT PLOT ------------------------------------------------
    if be2_DC_NVT.steps <=900:
        x = np.linspace(1,be2_DC_NVT.steps,be2_DC_NVT.steps)
        y = points_be2[1]
        steps = be2_DC_NVT.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"BE-DC_NVT({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-DC_VarT PLOT ------------------------------------------------
    if be2_DC_VarT.steps <=1000:
        x = np.linspace(1,be2_DC_VarT.steps,be2_DC_VarT.steps)
        y = points_be2[2]
        steps = be2_DC_VarT.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"BE-DC_VarT({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-FIRE PLOT ------------------------------------------------
    if be2_FIRE.steps <=1000:
        x = np.linspace(1,be2_FIRE.steps,be2_FIRE.steps)
        y = points_be2[3]
        steps = be2_FIRE.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"BE-FIRE({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    
   
    
    #---- Title and Axes lables ----------------------------------------------
    f_norm = r'$f_{\text{norm}}$'
    title_and_labels(axes, f'Normalized  Function Error {f_norm}')
    #--
    # place a legend outsize of the Axes
    axes.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                frameon=False)


    plt.savefig('morse_error_plot_BE_2.png', bbox_inches='tight')
    #plt.savefig('error_plot_BE_2.png')
    
    
    
    
    

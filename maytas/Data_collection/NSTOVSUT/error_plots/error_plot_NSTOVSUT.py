#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:22:17 2024

@author: leothan
"""

# Imported packages:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 

#---- NSTOVSUT Algorithms -----------------------------------
from nesterov_SUT_NDC import NAG_SUT_NDC 
from nesterov_SUT_DC_NVT import NAG_SUT_DCNVT
from nesterov_SUT_DC_VarT import NAG_SUT_DC_VarT
from nesterov_FIRE import NAG_FIRE


def error_plot_NSTOVSUT(r0):
    
    #--- Backward Euler Algorithms -----------------------------------------
    nstovsut_NDC = NAG_SUT_NDC(r0)
    nstovsut_DC_NVT = NAG_SUT_DCNVT(r0)
    nstovsut_DC_VarT = NAG_SUT_DC_VarT(r0)
    nstovsut_FIRE = NAG_FIRE(r0)
    #-----------------------------------------------------------------------
    # BE2 points
    points_be2 = [nstovsut_NDC.energy_errors,
                  nstovsut_DC_NVT.energy_errors,
                  nstovsut_DC_VarT.energy_errors,
                  nstovsut_FIRE.energy_errors]
    
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
    if nstovsut_NDC.steps <=1000:
        x = np.linspace(1,nstovsut_NDC.steps,nstovsut_NDC.steps)
        y = points_be2[0]
        steps = nstovsut_NDC.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"NSTOVSUT-NDC({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-DC_NVT PLOT ------------------------------------------------
    if nstovsut_DC_NVT.steps <=1000:
        x = np.linspace(1,nstovsut_DC_NVT.steps,nstovsut_DC_NVT.steps)
        y = points_be2[1]
        steps = nstovsut_DC_NVT.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"NSTOVSUT-DC_NVT({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-DC_VarT PLOT ------------------------------------------------
    if nstovsut_DC_VarT.steps <=1000:
        x = np.linspace(1,nstovsut_DC_VarT.steps,nstovsut_DC_VarT.steps)
        y = points_be2[2]
        steps = nstovsut_DC_VarT.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"NSTOVSUT-DC_VarT({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- BE2-FIRE PLOT ------------------------------------------------
    if nstovsut_FIRE.steps <=1000:
        x = np.linspace(1,nstovsut_FIRE.steps,nstovsut_FIRE.steps)
        y = points_be2[3]
        steps = nstovsut_FIRE.steps
        st = f'steps = {steps}'
        axes.scatter(x,y, label = f"NSTOVSUT-FIRE({st})")
        axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    
   
    
    #---- Title and Axes lables ----------------------------------------------
    f_norm = r'$f_{\text{norm}}$'
    title_and_labels(axes, f'Normalized  Function Error {f_norm}')
    #--
    # place a legend outsize of the Axes
    axes.legend(bbox_to_anchor=(0.47, 0.98), loc=2, borderaxespad=0.0,
                frameon=False)


    plt.savefig('maytas_error_plot_NSTOVSUT.png', bbox_inches='tight')
    #plt.savefig('error_plot_BE_2.png')
    
    
    
    
    

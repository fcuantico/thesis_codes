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
    points_nstovsut = [nstovsut_NDC.energy_errors,
                  nstovsut_DC_NVT.energy_errors,
                  nstovsut_DC_VarT.norm_forces,
                  nstovsut_DC_VarT.minima_error,
                  nstovsut_FIRE.norm_forces,
                  nstovsut_FIRE.minima_error]
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    plt.rc('text.latex', preamble=r'\usepackage{siunitx}')
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    #---  Figure (Canvas) and Axes creation
    #fig, axes = plt.subplots(nrows=1,ncols=1)
    fig = plt.figure(figsize=(10,8))
    
    

    def title_and_labels(ax, title):
        ax.set_title(title,fontsize = 20)
        ax.set_xlabel("$x$", fontsize=12)
        ax.set_ylabel("$y$", fontsize=12)
        #ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    #--------- NSTOVSUT-NDC GRADIENT PLOT -------------------------------------------
    #if nstovsut_NDC.steps <=1000:
    #    x = np.linspace(1,nstovsut_NDC.steps,nstovsut_NDC.steps)
    #    y = points_nstovsut[0]
    #    steps = nstovsut_NDC.steps
    #    st = f'steps = {steps}'
    #    axes.scatter(x,y, label = f"NSTOVSUT-NDC({st})")
    #    axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- NSTOVSUT-DC_NVT PLOT ------------------------------------------------
    #if nstovsut_DC_NVT.steps <=1000:
    #    x = np.linspace(1,nstovsut_DC_NVT.steps,nstovsut_DC_NVT.steps)
    #    y = points_nstovsut[1]
    #    steps = nstovsut_DC_NVT.steps
    #    st = f'steps = {steps}'
    #    axes.scatter(x,y, label = f"NSTOVSUT-DC_NVT({st})")
    #    axes.semilogy(x,y,color="gray", linestyle ="dashed")
    
    #--------- NSTOVSUT-DC_VarT GRADIENT PLOT ---------------------------------------
    if nstovsut_DC_VarT.steps <=1000:
        x = np.linspace(1,nstovsut_DC_VarT.steps,nstovsut_DC_VarT.steps)
        y = points_nstovsut[2]
        steps = nstovsut_DC_VarT.steps
        st = f'steps = {steps}'
        ax0 = plt.subplot2grid((2, 2), (0, 0))
        ax0.scatter(x,y, color ='olivedrab',label = f"NSTOVSUT-DC_VarT({st})")
        ax0.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ------------------------------------------
        grad_norm = r'$|\nabla f|$'
        title_and_labels(ax0, f'Gradient Norm {grad_norm}')
        # place a legend outsize of the Axes
        ax0.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- NSTOVSUTDC_VarT x-Norm PLOT -----------------------------------------
    if nstovsut_DC_VarT.steps <=1000:
        x = np.linspace(1,nstovsut_DC_VarT.steps,nstovsut_DC_VarT.steps)
        y = points_nstovsut[3]
        steps = nstovsut_DC_VarT.steps
        st = f'steps = {steps}'
        ax1 = plt.subplot2grid((2, 2), (0, 1))
        ax1.scatter(x,y, color ='olivedrab',label = f"NSTOVSUT-DC_VarT({st})")
        ax1.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables -------------------------------------------
        x_norm = r'$x_{\text{norm}}$'
        title_and_labels(ax1, f'Normalized position error {x_norm}')
        # place a legend outsize of the Axes
        ax1.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- NSTOVSUT-FIRE GRADIENT PLOT  -----------------------------------------
    if nstovsut_FIRE.steps <=1000:
        x = np.linspace(1,nstovsut_FIRE.steps,nstovsut_FIRE.steps)
        y = points_nstovsut[4]
        steps = nstovsut_FIRE.steps
        st = f'steps = {steps}'
        ax2 = plt.subplot2grid((2, 2), (1, 0))
        ax2.scatter(x,y, color='orange',label = f"NSTOVSUT-FIRE({st})")
        ax2.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables -------------------------------------------
        grad_norm = r'$|\nabla f|$'
        title_and_labels(ax2, f'Gradient Norm {grad_norm}')
        # place a legend outsize of the Axes
        ax2.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- NSTOVSUT-FIRE x-Norm PLOT  -----------------------------------------
    if nstovsut_FIRE.steps <=1000:
        x = np.linspace(1,nstovsut_FIRE.steps,nstovsut_FIRE.steps)
        y = points_nstovsut[5]
        steps = nstovsut_FIRE.steps
        st = f'steps = {steps}'
        ax3 = plt.subplot2grid((2, 2), (1, 1))
        ax3.scatter(x,y, color='orange',label = f"NSTOVSUT-FIRE({st})")
        ax3.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables -------------------------------------------
        x_norm = r'$x_{\text{norm}}$'
        title_and_labels(ax3, f'Normalized position error {x_norm}')
        # place a legend outsize of the Axes
        ax3.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    # Create an inset axis in the bottom right corner
    #axin = axes.inset_axes([0.32, 0.42, 0.28, 0.28])
    
    # Plot the data on the inset axis
    #-- NSTOVSUT-DC-VarT inset plot--------------------------------------
    #x1 = np.linspace(1,nstovsut_DC_VarT.steps,nstovsut_DC_VarT.steps)
    #y1 = points_nstovsut[2]
    #axin.scatter(x1,y1, color ="green", marker = '.')
    #axin.semilogy(x1,y1, color = "gray", linestyle = "dashed")
    
    #-- NSTOVSUT-FIRE inset plot--------------------------------------
    #x2 = np.linspace(1,nstovsut_FIRE.steps,nstovsut_FIRE.steps)
    #y2 = points_nstovsut[3]
    #axin.scatter(x2,y2, color ="red", marker = '.')
    #axin.semilogy(x2,y2, color = "gray", linestyle = "dashed")
    
    # Zoom in on the noisy data in the inset axis
    #axin.set_xlim(50, 150)
    #axin.set_ylim(0.000000001, 0.0001)
    
    # Add the lines to indicate where the inset axis is coming from
    #xes.indicate_inset_zoom(axin)
   
    
    #---- Title and Axes lables ----------------------------------------------
    #f_norm = r'$f_{\text{norm}}$'
    #title_and_labels(axes, f'Normalized  Function Error {f_norm}')
    #--
    # place a legend outsize of the Axes
    #axes.legend(bbox_to_anchor=(0.35, 0.25), loc=2, borderaxespad=0.0,
    #            frameon=False)

    plt.subplots_adjust(hspace=0.4)
    plt.savefig('lennard_jones_error_plot_NSTOVSUT_4.png', bbox_inches='tight')
    #plt.savefig('error_plot_BE_2.png')
    
    
    
    
    

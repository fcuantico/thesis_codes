#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:22:17 2024

@author: leothan
"""

# Imported packages:
import numpy as np
from vv_NDC import VV_NDC
from vv_DC_NVT import VV_DC_NVT
from vv_DC_VarT import VV_DC_VarT
from vv_FIRE import VV_FIRE
import matplotlib as mpl
import matplotlib.pyplot as plt 


def error_plot_VV(r0,h):
    
    #--- Velocity Verlet Algorithms -----------------------------------------
    vv_NDC = VV_NDC(r0, h)
    vv_DC_NVT = VV_DC_NVT(r0, h)
    vv_DC_VarT = VV_DC_VarT(r0, h)
    vv_FIRE = VV_FIRE(r0, h)
    #-----------------------------------------------------------------------
    # VV points
    points_be2 = [vv_NDC.energy_errors,
                  vv_DC_NVT.energy_errors,
                  vv_DC_VarT.norm_forces,
                  vv_DC_VarT.minima_error,
                  vv_FIRE.norm_forces,
                  vv_FIRE.minima_error]
    
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
    
    #--------- VV-NDC PLOT ------------------------------------------------
    if vv_NDC.steps <=100:
        x = np.linspace(1,vv_NDC.steps,vv_NDC.steps)
        y = points_be2[0]
        steps = vv_NDC.steps
        st = f'steps = {steps}'
        ax0 = plt.subplot2grid((1, 2), (0, 0))
        ax0.scatter(x,y, label = f"VV-NDC({st})")
        ax0.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ------------------------------------------
        f_norm = r'$f_{\text{norm}}$'
        title_and_labels(ax0, f'Normalized  Function Error {f_norm}')
        # place a legend outsize of the Axes
        ax0.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- VV-DC_NVT PLOT ------------------------------------------------
    if vv_DC_NVT.steps <=100:
        x = np.linspace(1,vv_DC_NVT.steps,vv_DC_NVT.steps)
        y = points_be2[1]
        steps = vv_DC_NVT.steps
        st = f'steps = {steps}'
        ax1 = plt.subplot2grid((1, 2), (0, 1))
        ax1.scatter(x,y, color ='limegreen',label = f"VV-DC_NVT({st})")
        ax1.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ----------------------------------------------
        f_norm = r'$f_{\text{norm}}$'
        title_and_labels(ax1, f'Normalized  Function Error {f_norm}')
        # place a legend outsize of the Axes
        ax1.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- VV-DC_VarT GRADIENT PLOT ---------------------------------------
    if vv_DC_VarT.steps <=1000:
        x = np.linspace(1,vv_DC_VarT.steps,vv_DC_VarT.steps)
        y = points_be2[2]
        steps = vv_DC_VarT.steps
        st = f'steps = {steps}'
        ax2 = plt.subplot2grid((2, 2), (0, 0))
        ax2.scatter(x,y, color ='olivedrab',label = f"VV-DC_VarT({st})")
        ax2.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ----------------------------------------------
        grad_norm = r'$|\nabla f|$'
        title_and_labels(ax2, f'Gradient Norm {grad_norm}')
        # place a legend outsize of the Axes
        ax2.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- VV-DC_VarT x-Norm Plot------------------------------------------------
    if vv_DC_VarT.steps <=1000:
        x = np.linspace(1,vv_DC_VarT.steps,vv_DC_VarT.steps)
        y = points_be2[3]
        steps = vv_DC_VarT.steps
        st = f'steps = {steps}'
        ax3 = plt.subplot2grid((2, 2), (0, 1))
        ax3.scatter(x,y, color ='olivedrab', label = f"VV-DC_VarT({st})")
        ax3.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ----------------------------------------------
        x_norm = r'$x_{\text{norm}}$'
        title_and_labels(ax3, f'Normalized position error {x_norm}')
        # place a legend outsize of the Axes
        ax3.legend(bbox_to_anchor=(0.12, 0.95), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- VV-FIRE GRADIENT PLOT ------------------------------------------------
    if vv_FIRE.steps <=1000:
        x = np.linspace(1,vv_FIRE.steps,vv_FIRE.steps)
        y = points_be2[4]
        steps = vv_FIRE.steps
        st = f'steps = {steps}'
        ax3 = plt.subplot2grid((2, 2), (1, 0))
        ax3.scatter(x,y, color='orange',label = f"VV-FIRE({st})")
        ax3.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ----------------------------------------------
        grad_norm = r'$|\nabla f|$'
        title_and_labels(ax3, f'Gradient Norm {grad_norm}')
        # place a legend outsize of the Axes
        ax3.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    #--------- VV-FIRE x-Norm Plot ------------------------------------------------
    if vv_FIRE.steps <=1000:
        x = np.linspace(1,vv_FIRE.steps,vv_FIRE.steps)
        y = points_be2[5]
        steps = vv_FIRE.steps
        st = f'steps = {steps}'
        ax4 = plt.subplot2grid((2, 2), (1, 1))
        ax4.scatter(x,y, color = 'orange',label = f"VV-FIRE({st})")
        ax4.semilogy(x,y,color="gray", linestyle ="dashed")
        #---- Title and Axes lables ----------------------------------------------
        x_norm = r'$x_{\text{norm}}$'
        title_and_labels(ax4, f'Normalized position error {x_norm}')
        # place a legend outsize of the Axes
        ax4.legend(bbox_to_anchor=(0.12, 0.95), loc=2, borderaxespad=0.0,
                    frameon=False)
    
    
   
    
    #---- Title and Axes lables ----------------------------------------------
    #f_norm = r'$f_{\text{norm}}$'
    #title_and_labels(axes, f'Normalized  Function Error {f_norm}')
    #--
    # place a legend outsize of the Axes
    #axes.legend(bbox_to_anchor=(0.12, 0.15), loc=2, borderaxespad=0.0,
    #            frameon=False)

    plt.subplots_adjust(hspace=0.4)
    plt.savefig('lennard-jones_error_plot_2_VV.png', bbox_inches='tight')
    #plt.savefig('error_plot_BE_2.png')
    
    
    
    
    


import sys
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse,Polygon
from matplotlib.lines import Line2D
import logging

from pathlib import Path



points = []
alpha_value = 1
linewidth_value=0.1
logger = logging.getLogger(__name__)  

#----------------------------------------------
# Parameters settings for figures
#----------------------------------------------
# Set font family
plt.rc('font', family='sans-serif')
# Enable Latex rendering
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath,amssymb}'

# mpl.use('ps') 
# plt.ioff() # Turn interactive plotting off
# plt.ion() # Turn interactive plotting on




class Graph:
    def __init__(self):
        pass

   
    @staticmethod
    def on_click(event):
        """This function manually assists the RSA algorithm.
        """
        global points
        points.append([event.xdata, event.ydata]) #store the point we have selected
        plt.plot(points[-1][0],points[-1][1],'xr')

    @staticmethod 
    def Non_Adjusted_Incl(dir,*ellips):
        
        logger.info('Non_Adjusted_Incl')

        fig, ax = plt.subplots()
        ax.set_aspect('equal', adjustable='box')
        ax.axis((-1, 1,-1, 1))

        a=(-0.5,-0.5,0.5,0.5,-0.5)
        b=(-0.5,0.5,0.5,-0.5,-0.5)
        ax.plot(a,b, '-k', linewidth=1)

        for I in range(len(ellips)):
            # Graphing inclusions
            ellip = Ellipse((ellips[I].center[0],ellips[I].center[1]), ellips[I].majorAxis,\
                 ellips[I].minorAxis, color='b', linestyle='--', angle=np.degrees(ellips[I].theta),fill=False,linewidth=2)
            ax.add_patch(ellip)
            
            # Semi-axes of ellipses
            x1 = ellips[I].center[0] + np.cos(ellips[I].theta) * 0.5 * ellips[I].majorAxis
            y1 = ellips[I].center[1] + np.sin(ellips[I].theta) * 0.5 * ellips[I].majorAxis
            x2 = ellips[I].center[0] - np.cos(np.pi/2-ellips[I].theta) * 0.5 * ellips[I].minorAxis
            y2 = ellips[I].center[1] + np.sin(np.pi/2-ellips[I].theta) * 0.5 * ellips[I].minorAxis
            
            ax.plot(ellips[I].center[0],ellips[I].center[1],'.k',markersize=5)
            ax.annotate("{}".format(I+1), (ellips[I].center[0],ellips[I].center[1]), color='m')

            ax.plot(x1,y1,'.k',markersize=5)
            ax.plot((ellips[I].center[0], x1), (ellips[I].center[1], y1), '-k', linewidth=1) # majorAxis
            ax.plot(x2,y2,'.k',markersize=5)
            ax.plot((ellips[I].center[0], x2), (ellips[I].center[1], y2), '--k', linewidth=1) # minorAxis
            
            poly=ellips[I].Polyline()
            ax.add_patch(plt.Polygon(poly,alpha=1,facecolor="white",\
                edgecolor="black",linewidth=2,fill=True))

        fig.savefig(dir+f'/WARNING_Non_Adjusted_Incl.png',dpi=300, bbox_inches='tight') 
            
        plt.close(fig)
                

    @staticmethod
    def RSA_Figures (globalPrm,inclPrm,rsaPrm,X,Y, GraphLabel, Iter='', assists_RSA=False):
        """Graph all iterations of the RSA algorithm in the domain [-0.5,0.5]^2
        """
        
        globalPrm['logger'].info('RSA_Figures')

        # initPrm
        e_incl=inclPrm.e_incl
        theta_incl=inclPrm.theta_incl
        # rsaPrm
        e_cell_RSA=rsaPrm.e_cell_RSA
        theta_cell_RSA=rsaPrm.theta_cell_RSA
        R_incl=rsaPrm.R_incl
        R_cell_RSA=rsaPrm.R_cell_RSA
        a2_incl=rsaPrm.a2_incl
        a2_cell_RSA=rsaPrm.a2_cell_RSA
        security_factor=rsaPrm.security_factor
        index_Dupl_Incl=rsaPrm.index_Dupl_Incl

        if len(Y.shape)==1:
            Y=Y[np.newaxis,:]
            
        N1=X.shape[0]
        N2=Y.shape[0]

        #---
        fig,ax = plt.subplots() 
        ax.set_aspect('equal', adjustable='box')
        
        if GraphLabel=='Iter':
            a=(-0.5,-0.5,0.5,0.5,-0.5)
            b=(-0.5,0.5,0.5,-0.5,-0.5)
            ax.axis([-0.75,0.75,-0.75,0.75])
        
        if GraphLabel=='Final':
            """Last figure of the RSA algorithm together with the duplication of inclusions intercepting
            boundaries in the domain [0,1]^2.
            """
            a=(0,0,1,1,0)
            b=(0,1,1,0,0)
            ax.axis([-0.25,1.25,-0.25,1.25])

            R_incl_tot=rsaPrm.R_incl_tot
            e_incl_tot=rsaPrm.e_incl_tot
            theta_incl_tot=rsaPrm.theta_incl_tot
            R_cell_RSA_tot=rsaPrm.R_cell_RSA_tot
            e_cell_RSA_tot=rsaPrm.e_cell_RSA_tot
            theta_cell_RSA_tot=rsaPrm.theta_cell_RSA_tot
            

        # ax.set_xticks([]) 
        # ax.set_yticks([])
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_title(r'$\mathrm{RSA}$', fontsize=20)
        ax.plot(a,b, 'k',linestyle='--', linewidth=0.5)
            
            
        for I in range(N1):
            
            Incl = Ellipse((X[I,0],X[I,1]), 2*R_incl[I], 2*R_incl[I]*e_incl[I], facecolor = '#999999ff', linestyle = '-', angle=np.degrees(theta_incl[I][0]),fill=True,linewidth=1.5)
            ax.add_patch(Incl)

            Cell_RSA = Ellipse((X[I,0],X[I,1]), 2*R_cell_RSA[I], 2*R_cell_RSA[I]*e_cell_RSA[I],color='k',linestyle='--', angle=np.degrees(theta_cell_RSA[I][0]),fill=False,linewidth=1.5)
            ax.add_patch(Cell_RSA)
            
            Cell_RSA_SF = Ellipse((X[I,0],X[I,1]), 2*security_factor*R_cell_RSA[I], 2*security_factor*R_cell_RSA[I]*e_cell_RSA[I],color='r',linestyle=':', angle=np.degrees(theta_cell_RSA[I][0]),fill=False,linewidth=1.5)
            ax.add_patch(Cell_RSA_SF)
                    
        if not Y.size==0:
            
            for J in range(N2):

                if GraphLabel=='Iter':

                    Incl = Ellipse((Y[J,0],Y[J,1]), 2*R_incl[N1+J], 2*R_incl[N1+J]*e_incl[N1+J],facecolor='#d0cd00',linestyle='-',alpha=0.5, angle=np.degrees(theta_incl[N1+J][0]),fill=True,linewidth=1.5)
                    ax.add_patch(Incl)

                    Cell_RSA = Ellipse((Y[J,0],Y[J,1]), 2*R_cell_RSA[N1+J], 2*R_cell_RSA[N1+J]*e_cell_RSA[N1+J],color='k',linestyle='--', angle=np.degrees(theta_cell_RSA[N1+J][0]),fill=False,linewidth=1.5)
                    ax.add_patch(Cell_RSA)
                    
                    Cell_RSA_SF = Ellipse((Y[J,0],Y[J,1]), 2*security_factor*R_cell_RSA[N1+J], 2*security_factor*R_cell_RSA[N1+J]*e_cell_RSA[N1+J],color='r',linestyle=':',alpha=0.5, angle=np.degrees(theta_cell_RSA[N1+J][0]),fill=False,linewidth=1.5)
                    ax.add_patch(Cell_RSA_SF)
                
                if GraphLabel=='Final':
                    
                    Incl = Ellipse((Y[J,0],Y[J,1]), 2*R_incl_tot[N1+J], 2*R_incl_tot[N1+J]*e_incl_tot[N1+J],facecolor='#d0cd00',linestyle='-',alpha=0.5, angle=np.degrees(theta_incl_tot[N1+J][0]),fill=True,linewidth=1.5)
                    ax.add_patch(Incl)

                    Cell_RSA = Ellipse((Y[J,0],Y[J,1]), 2*R_cell_RSA_tot[N1+J], 2*R_cell_RSA_tot[N1+J]*e_cell_RSA_tot[N1+J],color='k',linestyle='--', angle=np.degrees(theta_cell_RSA_tot[N1+J][0]),fill=False,linewidth=1.5)
                    ax.add_patch(Cell_RSA)
                    
                    Cell_RSA_SF = Ellipse((Y[J,0],Y[J,1]), 2*security_factor*R_cell_RSA_tot[N1+J], 2*security_factor*R_cell_RSA_tot[N1+J]*e_cell_RSA_tot[N1+J],color='r',linestyle=':',alpha=0.5, angle=np.degrees(theta_cell_RSA_tot[N1+J][0]),fill=False,linewidth=1.5)
                    ax.add_patch(Cell_RSA_SF)

        if assists_RSA:
            # Showing the cursor
            cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = 'r', linewidth = 1)
            
            textToDisplay="Assisting the RSA process!"
            N=len(textToDisplay)
            print('*'+'-'*(N+2)+'*')
            print('| '+textToDisplay+' |')
            print('*'+'-'*(N+2)+'*')

            print("*** Choose a point and close the figure")

            plt.connect('button_press_event', Graph.on_click)
            plt.show()

            value = input("*** Do you want to continue? [Y/n]")
            if value == 'Y':
                x_incl_i=np.array([points[-1][0],points[-1][1]])
            else: 
                input("*** END")
                sys.exit()
        
          
        fig.savefig(globalPrm['subfolder_rsa_iter_path'].joinpath(f'Inclusion_Placement_{GraphLabel}_{Iter}.png'),dpi=300, bbox_inches='tight') 
            
        plt.close(fig)
        #---
        #  
        if assists_RSA:
            return x_incl_i
    
    #------
    # IP_Figures
    @staticmethod
    def RVE_Figures(logger, rveImageData, ip_path, RegCenters=False,InclCenters=False):
        
        logger.info('RVE_Figures')

        # rveImageData
        pixels= rveImageData.genImage.pixels
        x_incl_Pxls=rveImageData.genImage.x_incl_Pxls
        N_Regions=rveImageData.N_Regions
        x0=rveImageData.centroidRegions[:,0]
        y0=rveImageData.centroidRegions[:,1]
        
        auxString=''

        #---
        fig, ax = plt.subplots() 
        ax.imshow(rveImageData.genImageArrayFlip, cmap=plt.cm.gray) 
        ax.axis((0*pixels, 1*pixels,0*pixels,1*pixels))
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_xlabel(r'$\mathrm{pixels}$', fontsize=20)
        ax.set_ylabel(r'$\mathrm{pixels}$', fontsize=20)

        ax.set_title(r'$\mathrm{RVE}$', fontsize=20)
        
        if RegCenters:
            for I in range(N_Regions):
                ax.annotate(f"$R_{{{I+1}}}$", (x0[I], y0[I]), color='k',fontsize= 15)
            auxString=auxString+'RegCenters_'
        
        if InclCenters:
            for I in range(x_incl_Pxls.shape[0]):
                ax.plot(x_incl_Pxls[I,0], x_incl_Pxls[I,1], '.b', markersize=8)
            auxString=auxString+'InclCenters'
        
        fig.savefig(ip_path.joinpath(f'RVE_Figure_'+auxString+'.png'),dpi=300, bbox_inches='tight') 
    
        plt.close( )
    
    @staticmethod
    def RandomColor(): 
        
        rgb = [np.random.rand(),np.random.rand(),np.random.rand()]
        return tuple(rgb)


    @staticmethod
    def Cloned_Rve_And_Vd(logger, rveImage,VD, ip_path, Seeds_in_the_Rve=False, RVE_Mark=False,\
        Vd_in_the_RVE=False, Vd_outside_the_RVE=False, show_Incl=False, GrayScale_VD=False):
       

        logger.info('Cloned_Rve_And_Vd')

        # rveImage
        pixels= rveImage.pixels
        N_incl=rveImage.N_incl
        theta_incl=rveImage.theta_incl
        R_incl_Pxls=rveImage.R_incl_Pxls
        a2_incl_Pxls=rveImage.a2_incl_Pxls
        x_incl_Pxls=rveImage.x_incl_Pxls
        seedPoints=rveImage.seedPoints
        # VD
        allPolygons=VD.allPolygons
        vdPolygons=VD.vdPolygons

        auxString=''

        #-----
        # Figure 1
        fig1, ax1 = plt.subplots() 
        ax1.axis((-pixels, 2*pixels,-pixels, 2*pixels))
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax1.set_aspect('equal', adjustable='box')
        ax1.set_title(r'$\mathrm{Cloned\; RVE\; (}$ '+r'$3\times3$'+r' $\mathrm{grid\;)\; + \; Voronoi\; diagram}$',fontsize=20)
        ax1.set_xlabel(r'$3\;\times$ $\mathrm{pixels}$', fontsize=20)
        ax1.set_ylabel(r'$3\;\times$ $\mathrm{pixels}$', fontsize=20)
        
        #-----
        if Seeds_in_the_Rve:
            for point in x_incl_Pxls:
                ax1.plot(point[0], point[1], '.b', markersize=5) 
            auxString=auxString+'Seeds_in_the_Rve_'

        else:
            ax1.plot(seedPoints[:,0], seedPoints[:,1], '.b', markersize=5)
        

        #-----
        if RVE_Mark:
            squareX=(0,pixels,pixels,0,0)
            squareY=(pixels,pixels,0,0,pixels)
            ax1.plot(squareX,squareY, color='black', linewidth=0.5)
            auxString=auxString+'RVE_Mark_'
        
        #-----
        if Vd_in_the_RVE and Vd_outside_the_RVE:
            for poly in allPolygons:   
                ax1.add_patch(plt.Polygon(poly, alpha=alpha_value,facecolor='0.8',\
                    edgecolor="black",linewidth=linewidth_value))
                
            auxString=auxString+'Vd_outside_the_RVE_'+'Vd_in_the_RVE_'

        elif Vd_in_the_RVE and not Vd_outside_the_RVE:
            for poly in vdPolygons:   
                ax1.add_patch(plt.Polygon(poly,alpha=alpha_value,facecolor=Graph.RandomColor(),\
                    edgecolor="black",linewidth=linewidth_value))
        
            auxString=auxString+'Vd_in_the_RVE_'

        elif not Vd_in_the_RVE and Vd_outside_the_RVE:
            for poly in allPolygons:
                if  not poly in vdPolygons: 
                    ax1.add_patch(plt.Polygon(poly,alpha=alpha_value,facecolor=Graph.RandomColor(),\
                    edgecolor="black",linewidth=linewidth_value))
                
            auxString=auxString+'Vd_outside_the_RVE_'

        else: pass
    
          
        #-----
        if show_Incl:
            for MM in range(N_incl):
                ax1.plot(x_incl_Pxls[MM,0],x_incl_Pxls[MM,1],'.b',markersize=5)
                ellip = Ellipse((x_incl_Pxls[MM,0],x_incl_Pxls[MM,1]), 2*R_incl_Pxls[MM], 2*a2_incl_Pxls[MM],color='k', angle=np.degrees(theta_incl[MM]),fill=False,linewidth=1)
                ax1.add_patch(ellip)
            auxString=auxString+'Incl_'

        fig1.savefig(ip_path.joinpath(f'Cloned_Rve_And_Vd_'+auxString+'.png'),dpi=300, bbox_inches='tight')

        plt.close()
        
        #-----
        #-----
        # Figure 2
        if GrayScale_VD:

            logger.info('GrayScale_VD')
            
            fig2, ax2 = plt.subplots()
            ax2.set_xticks([]) # Remove ticks
            ax2.set_yticks([])
            ax2.set_aspect('equal', adjustable='box')
            ax2.set_facecolor("black")
            ax2.axis((-1/2*pixels, 3/2*pixels,-1/2*pixels,3/2*pixels)) 
            

            for poly in vdPolygons:
                ax2.add_patch(plt.Polygon(poly,alpha=alpha_value,facecolor="white",\
                    edgecolor="black",linewidth=linewidth_value))
            
            if show_Incl:
                for MM in range(N_incl):
                    ax2.plot(x_incl_Pxls[MM,0],x_incl_Pxls[MM,1],'.k',markersize=5)
                    ellip = Ellipse((x_incl_Pxls[MM,0],x_incl_Pxls[MM,1]), 2*R_incl_Pxls[MM], 2*a2_incl_Pxls[MM],color='r', angle=np.degrees(theta_incl[MM]),fill=False,linewidth=1)
                    ax2.add_patch(ellip)
                    
                    # Constructing the axis of the ellipse
                    x1 = x_incl_Pxls[MM,0] + np.cos(theta_incl[MM]) * R_incl_Pxls[MM]
                    y1 = x_incl_Pxls[MM,1] + np.sin(theta_incl[MM]) * R_incl_Pxls[MM]
                    x2 = x_incl_Pxls[MM,0] - np.cos(np.pi/2-theta_incl[MM]) * a2_incl_Pxls[MM]
                    y2 = x_incl_Pxls[MM,1] + np.sin(np.pi/2-theta_incl[MM]) * a2_incl_Pxls[MM]
                    
                    ax2.plot(x1,y1,'.k',markersize=5)
                    ax2.plot((x_incl_Pxls[MM,0], x1[0]), (x_incl_Pxls[MM,1], y1[0]), '--k', linewidth=1)
                    ax2.plot(x2,y2,'.k',markersize=5)
                    ax2.plot((x_incl_Pxls[MM,0], x2[0]), (x_incl_Pxls[MM,1], y2[0]), '-.k', linewidth=1)
            
            fig2.savefig(ip_path.joinpath(f'GrayScale_VD_and_Incl.png'),dpi=300, bbox_inches='tight',facecolor='black')
        
        plt.close() 
        
            
    @staticmethod
    def Vd_And_Ellips(logger, rveImage,VD,vdImage, ip_path):
        """
        """

        logger.info('Vd_And_Ellips')

        # rveImage
        rvePixels=rveImage.pixels # Inclusions
        theta_incl=rveImage.theta_incl
        R_incl_Pxls=rveImage.R_incl_Pxls
        a2_incl_Pxls=rveImage.a2_incl_Pxls
        x_incl_Pxls=rveImage.x_incl_Pxls 
        # VD 
        vdPolygons=VD.vdPolygons
        # vdImage
        theta_cell_VD=vdImage.theta_cell_VD  
        R_cell_VD_Pxls=vdImage.R_cell_VD_Pxls
        a2_cell_VD_Pxls=vdImage.a2_cell_VD_Pxls
        x_cell_VD_Pxls=vdImage.x_cell_VD_Pxls
        
        #---
        fig, ax = plt.subplots()
        ax.set_xticks([]) # Remove ticks
        ax.set_yticks([])
        #ax.imshow(vdImageData.genImageArrayFlip, cmap=plt.cm.gray)
        #ax.axis((0*rvePixels, 2*rvePixels,0*rvePixels,2*rvePixels))
        ax.set_aspect('equal', adjustable='box')
        ax.set_facecolor("black")
        # Set limits
        #ax.axis((-1/2*rvePixels, 3/2*rvePixels,-1/2*rvePixels,3/2*rvePixels))
        ax.axis((-1/4*rvePixels, 5/4*rvePixels,-1/4*rvePixels,5/4*rvePixels))
        
        MM=0
        for poly in vdPolygons:
            
            # Graphing the VD
            polygon=Polygon(poly,alpha=alpha_value,facecolor="white",\
                edgecolor="black",linewidth=1)
            polygon.set_zorder(1)
            ax.add_patch(polygon)
       
            # Graphing the elliptical cells
            ellip = Ellipse((x_cell_VD_Pxls[MM,0],x_cell_VD_Pxls[MM,1]), 2*R_cell_VD_Pxls[MM,0], 2*a2_cell_VD_Pxls[MM,0],color='b', angle=np.degrees(theta_cell_VD[MM,0]),fill=False,linewidth=1.5)
            ellip.set_zorder(2)
            ax.add_patch(ellip)
        
            # Graphing the inclusions
            incl = Ellipse((x_incl_Pxls[MM,0],x_incl_Pxls[MM,1]), 2*R_incl_Pxls[MM], 2*a2_incl_Pxls[MM],color='r', angle=np.degrees(theta_incl[MM]),fill=False,linewidth=1)
            incl.set_zorder(3)
            ax.add_patch(incl)
            MM=MM+1

        # Legend
        legend_elements = [Line2D([0], [0], color='r', lw=4, label=r'$\mathrm{inclusions}$'),
                             Line2D([0], [0], color='b', lw=4, label=r'$\mathrm{cells}$')]
        ax.legend(handles=legend_elements, fontsize=20, loc='lower center',bbox_to_anchor=(0.75, -0.2),fancybox=True, shadow=True)
        
        # if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3:
        ax.set_title(r'$\mathrm{Voronoi\; diagram}$',fontsize=20)
        
        fig.savefig(ip_path.joinpath(f'Vd_And_Ellips.png'),dpi=300, bbox_inches='tight') 
    
        plt.close( )

    
    @staticmethod
    def Hist_e_cell_VD(logger,vdImage, ip_path):
        
        logger.info('Hist_e_cell_VD')

        intervals=np.arange(0.05,1,0.1)
        intervals=np.append(intervals,1)
        intervals=np.insert(intervals,0,0,axis=0)
        N_intervals=intervals.shape[0]

        interCounter=np.zeros([N_intervals-1])

        for II in range(N_intervals-1):
            if not II==N_intervals-2:
                interCounter[II]=np.count_nonzero(np.array([intervals[II] <= X < intervals[II+1] for X in vdImage.e_cell_VD]))
            else:
                interCounter[II]=np.count_nonzero(np.array([intervals[II] <= X <= intervals[II+1] for X in vdImage.e_cell_VD]))
        
        countMax=max(interCounter)
        
        #---
        fig, ax = plt.subplots()            
        ax.bar(np.arange(0,1.1,0.1), interCounter, width=0.1, align='center',edgecolor='k')
        ax.set_ylabel(r'$\mathrm{Number\; of\; cases}$',fontsize=20)
        #ax.yaxis.set_label_coords(-.18, .48)
        ax.set_xlabel(r'$\mathrm{Aspect\; ratio\;}$ $e^{(\mathrm{cell})}$',fontsize=20)
        ax.set(xticks=np.arange(0,1.1,0.1), xlim=[0, 1])
        ax.set(yticks=np.arange(0,countMax+1,1), ylim=[0, countMax*1.15])
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_aspect(0.5/countMax, adjustable='box')
        
        e_vals = np.arange(0.2, 1.2, 0.4)
        xPos=np.linspace(0.25,0.87, e_vals.shape[0]) # the position of the small windows have been adjusted manually
        for II, EE  in enumerate(e_vals):
            
            ax.axvline(x=EE, ymin=0, ymax=0.9, linewidth=0.5, linestyle='--', color='lightgray') # vertical lines
            
            ax_smallWind = fig.add_axes([xPos[II], 0.8, 0.05, 0.05]) # creates small windows
            ax_smallWind.set_aspect(1, adjustable='box')
            ax_smallWind.set_xlim(0,1); ax_smallWind.set_ylim(0,1)
            ax_smallWind.set_xticks([]); ax_smallWind.set_yticks([])
            
            #---
            # Square cell prototype
            Area = 1
            c_incl = 0.1
            e_incl = EE
            theta_incl = 0*np.pi/180
            R_incl = np.sqrt(c_incl*Area/(e_incl*np.pi))
            a2_incl = R_incl*e_incl
            ellip = Ellipse(((0.5,0.5)), 2*R_incl, 2*a2_incl, color='k', angle=np.degrees(theta_incl), fill=False,linewidth=1.5)
            #---
            ax_smallWind.add_patch(ellip)

        fig.savefig(ip_path.joinpath(f'Hist_e_cell_VD.png'),dpi=300, bbox_inches='tight') 
        
        plt.close( )
    
    @staticmethod
    def Hist_theta_cell_VD(logger,vdImage, ip_path):
        """
        """
        
        logger.info('Hist_theta_cell_VD')
        intervals=np.arange(-85,95,10)
        intervals=np.append(intervals,95)
        intervals=np.insert(intervals,0,-95,axis=0)
        N_intervals=intervals.shape[0]

        interCounter=np.zeros([N_intervals-1])
        
        for II in range(N_intervals-1):
            if not II==N_intervals-2:
                interCounter[II]=np.count_nonzero(np.array([intervals[II] <= X < intervals[II+1] for X in np.degrees(vdImage.theta_cell_VD)]))
            else:
                interCounter[II]=np.count_nonzero(np.array([intervals[II] <= X <= intervals[II+1] for X in np.degrees(vdImage.theta_cell_VD)]))

        countMax=max(interCounter)
        
        #---
        fig, ax = plt.subplots()
        ax.bar(np.arange(-90,100,10), interCounter, width=10, align='center',edgecolor='k')
        ax.set_ylabel(r'$\mathrm{Number\; of\; cases}$',fontsize=20)
        #ax.yaxis.set_label_coords(-.14, .48)
        ax.set_xlabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{cell})}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
        ax.set(xticks=np.arange(-90,100,10), xlim=[-90, 90])
        ax.set(yticks=np.arange(0,countMax+1,1), ylim=[0, countMax+0.15*countMax])
        plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='center')
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_aspect(0.5/(1*countMax)*180, adjustable='box')
        
        theta_vals = np.arange(-80,100,40) 
        xPos=np.linspace(0.14,0.83, theta_vals.shape[0])
        for II, TH in enumerate(theta_vals):
            
            ax.axvline(x=TH, ymin=0, ymax=0.9, linewidth=0.5,linestyle='--', color='lightgray') # vertical lines

            ax_smallWind = fig.add_axes([xPos[II], 0.8, 0.05, 0.05]) # creates small windows
            ax_smallWind.set_aspect(1, adjustable='box')
            ax_smallWind.set_xlim(0,1); ax_smallWind.set_ylim(0,1)
            ax_smallWind.set_xticks([]); ax_smallWind.set_yticks([])
            
            #---
            # Square cell prototype
            Area = 1
            c_incl = 0.2
            e_incl = 0.5
            theta_incl = TH
            R_incl = np.sqrt(c_incl*Area/(e_incl*np.pi))
            a2_incl = R_incl*e_incl
            ellip = Ellipse(((0.5,0.5)), 2*R_incl, 2*a2_incl,color='k', angle=theta_incl, fill=False,linewidth=1.5)
            #---
            ax_smallWind.add_patch(ellip)
            

        fig.savefig(ip_path.joinpath(f'Hist_theta_cell_VD.png'),dpi=300, bbox_inches='tight') 
        
        plt.close( )
    
    @staticmethod
    def ScatterPlot_theta_e(logger,rveImage, vdImage, ip_path, e_cell_PCW=None,theta_cell_PCW=None):
        """We show a scatter plot between orientations and aspect ratios of
        the elliptical cells """
        
        logger.info('ScatterPlot_theta_e')
        #---
        fig, ax = plt.subplots()
        ax.set_ylabel(r'$\mathrm{Aspect\; ratio\;}$ $e$',fontsize=20)
        ax.set_xlabel(r'$\mathrm{Orientation\;}$ $\theta$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
        ax.yaxis.set_label_coords(-.1, .48)
        ax.set(xticks=np.arange(-90,100,10), xlim=[-90, 90])
        ax.set(yticks=np.arange(0,1.1,0.1), ylim=[0, 1.1])
        plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='center')
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)

        theta_vals=np.arange(-90,100,45)
        xPos=np.linspace(0.11,0.87,theta_vals.shape[0])

        e_vals = np.arange(0.2, 1.2, 0.4)
        yPos=np.linspace(0.2252,0.81,e_vals.shape[0])

        for II, TH in enumerate(theta_vals): 
            #------
            # theta_cell_VD
            #------
            ax.axvline(x=TH, ymin=0, ymax=0.95, linewidth=0.5,linestyle='--', color='lightgray')

            ax_smallWind1 = fig.add_axes([xPos[II], 0.225, 0.05, 0.05]) # creates small windows
            ax_smallWind1.set_xlim(0,1); ax_smallWind1.set_ylim(0,1)
            ax_smallWind1.set_xticks([]); ax_smallWind1.set_yticks([])
            
            #---
            # Square cell prototype 1
            Area = 1
            c_incl = 0.1
            e_incl = 0.2
            theta_incl = TH
            R_incl = np.sqrt(c_incl*Area/(e_incl*np.pi))
            a2_incl = R_incl*e_incl
            ellip1 = Ellipse(((0.5,0.5)), 2*R_incl, 2*a2_incl,color='k', angle=theta_incl,fill=False,linewidth=1.5)
            ellip1.set_zorder(1)
            ax_smallWind1.add_patch(ellip1)
            #---
            ax_smallWind1.set_aspect(1, adjustable='box')
            #------
            #------
            
            if II<3:    
                #------
                # e_cell_VD
                #------
                ax.axhline(y=e_vals[II], xmin=0, xmax=0.95, linewidth=0.5,linestyle='--', color='lightgray')
                
                ax_smallWind2 = fig.add_axes([0.87,yPos[II], 0.05, 0.05]) # creates small windows
                ax_smallWind2.set_aspect(1, adjustable='box')
                ax_smallWind2.set_xlim(0,1); ax_smallWind2.set_ylim(0,1)
                ax_smallWind2.set_xticks([]);ax_smallWind2.set_yticks([])

                #---
                # Square cell prototype 2
                Area = 1
                c_incl = 0.1
                e_incl = e_vals[II]
                theta_incl = 90*np.pi/190
                R_incl = np.sqrt(c_incl*Area/(e_incl*np.pi))
                a2_incl = R_incl*e_incl
                ellip2 = Ellipse(((0.5,0.5)), 2*R_incl, 2*a2_incl,color='k', angle=np.degrees(theta_incl),fill=False,linewidth=1.5)
                ellip2.set_zorder(1)
                ax_smallWind2.add_patch(ellip2)
                #------
                #------

        
        theta_incl_Degr=np.degrees(rveImage.theta_incl)
        e_incl=rveImage.e_incl

        theta_cell_VD_Degr=np.degrees(vdImage.theta_cell_VD)
        e_cell_VD=vdImage.e_cell_VD

        ax.scatter(theta_incl_Degr, e_incl, c='r', zorder=2, marker='o', label=r'$\mathrm{inclusions}$') # inclusions
        ax.scatter(theta_cell_VD_Degr, e_cell_VD, c='b', zorder=2, marker='o', label=r'$\mathrm{cells}$') # cells
        ax.scatter(np.mean(theta_cell_VD_Degr), np.mean(e_cell_VD),c='k', zorder=3, marker='*', label=r'$\mathrm{mean\; value}$') # cell - Mean value
        
        if e_cell_PCW is not None:
            ax.scatter(np.degrees(float(theta_cell_PCW[0,0])),float(e_cell_PCW[0,0]), c='purple', zorder=4, marker='s', label=r'$\mathrm{cell-PCW}$') # cell - PCW value
            #ax.scatter(-90,0.93, c='purple', zorder=4, marker='s', label=r'$\mathrm{cell-PCW}$') # cell - PCW value

        ax.legend(loc='upper center',bbox_to_anchor=(1.275, 1),fancybox=True, shadow=True,fontsize= 20)
        fig.savefig(ip_path.joinpath(f'ScatterPlot_theta_e.png'),dpi=300, bbox_inches='tight') 
        
        plt.close( )
    
    #------
    # Numerical_Comparisons
    @staticmethod
    def Appr_Comparison(comparison_path, rveImage, meanField,fullField,c_inclValue=None,e_inclValue=None,theta_inclValue=None,gammaValue=None, tS_hom=None):
        

        # logger.info('Appr_Comparison')

        fig,ax=plt.subplots()
        
        # rveImage
        dir=rveImage.dir
        showMFApproach=rveImage.showMFApproach
        showFFApproach=rveImage.showFFApproach
        varyParamName=rveImage.varyParamName
        varyParamValue_FF=rveImage.varyParamValue_FF
        varyParamValue_MF=rveImage.varyParamValue_MF
        c_incl=rveImage.c_incl
        e_incl=rveImage.e_incl
        theta_incl=rveImage.theta_incl
        
        if varyParamName=='gamma':

            if showMFApproach:

                if meanField.symmetry['MT']:
                    ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[0,0,:],'-', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[1,1,:],'--', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")
                    
                if meanField.symmetry['IDD']:
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[0,0,:],'-', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[1,1,:],'--', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD})}$")
                
                if tS_hom: # Two step homogenization
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_Voigt_EVa[0,0,:],'-', c='#DC143C', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD-Voigt})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_Voigt_EVa[1,1,:],'--', c='#DC143C', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD-Voigt})}$")
                
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_Reuss_EVa[0,0,:],'-', c='#7f7f7f', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD-Reuss})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_Reuss_EVa[1,1,:],'--', c='#7f7f7f', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD-Reuss})}$")
                

                # if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3 and rveImage.labelNumber!=7 and rveImage.labelNumber!=8:
                    # ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[0,0,:], '-',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
                    # ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[1,1,:], '--',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")

            if showFFApproach:

                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
                
            
            ax.set_xlabel(r'$\mathrm{Conductivity\; contrast\;}$ $\gamma$',fontsize=20)
            ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_incl[0, 0]}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_incl[0,0]}$',fontsize=20, multialignment='center')
        
            # ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_incl[0, 0]}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_incl[0,0]}$, '\
            #      +f'$\\theta^{{\mathrm{{(incl)}}}} = {round(np.degrees(theta_incl[0,0]))}$'+r'$^{\circ}$',fontsize=20, multialignment='center')
        
            
        elif varyParamName== 'e_incl':
            
            if showMFApproach:

                ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[0,0,:],'-', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
                ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[1,1,:],'--', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")
                
                ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[0,0,:],'-', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD})}$")
                ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[1,1,:],'--', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD})}$")
                
                if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3 and rveImage.labelNumber!=7 and rveImage.labelNumber!=8:
                    ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[0,0,:],'-',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[1,1,:],'--',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")
            
            if showFFApproach:

                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
                
            ax.set_xlabel(r'$\mathrm{Aspect\; ratio\;}$ $e^{(\mathrm{incl})}$',fontsize=20)
            
            #ax.set(xticks=np.arange(0.4,1.4,0.1), xlim=[0.35, 1.45])
            #ax.set(xticks=np.arange(0.1,1,0.1), xlim=[0.05, 1.05])
            
            ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_inclValue[0,0]}$, '+f'$\\gamma = {gammaValue[0,0]}$, '\
                +f'$\\theta^{{\mathrm{{(incl)}}}} = {round(np.degrees(theta_inclValue[0,0]))}$'+r'$^{\circ}$',fontsize=20)
            
        
        elif varyParamName== 'theta_incl':

            if showMFApproach:

                ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffMt_EVa[0,0,0:],'-', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
                ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffMt_EVa[1,1,0:],'--', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")
                
                ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffIdd_EVa[0,0,0:],'-', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD})}$")
                ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffIdd_EVa[1,1,0:],'--', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD})}$")
                
                if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3 and rveImage.labelNumber!=4 and rveImage.labelNumber!=5 and rveImage.labelNumber!=6 and rveImage.labelNumber!=7 and rveImage.labelNumber!=8:
                    ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffPcw_EVa[0,0,0:],'-',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
                    ax.plot(np.degrees(varyParamValue_MF[0,:]), meanField.keffPcw_EVa[1,1,0:],'--',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")
            
            if showFFApproach:

                ax.plot(np.degrees(varyParamValue_FF[0,:]), fullField.keffNum_EVa[0,0,0:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
                ax.plot(np.degrees(varyParamValue_FF[0,:]), fullField.keffNum_EVa[1,1,0:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
                
            ax.set_xlabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{incl})}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
            
            tmin = np.degrees(varyParamValue_FF)[0,0]
            tmax = np.degrees(varyParamValue_FF)[0,-1]+5
            ax.set(xticks=np.arange(tmin,tmax,15), xlim=[tmin-1, tmax])
        
            ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_inclValue[0,0]}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_inclValue[0,0]}$, '+f'$\\gamma = {gammaValue[0,0]}$',fontsize=20)
            

            #---
            if showFFApproach:
                # Polar plot

                fig1,ax1=plt.subplots()
                ax1 = plt.subplot(projection='polar')
                

                if showMFApproach:
                    ax1.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[0,0,0:],'-', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
                    ax1.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[1,1,0:],'--', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")

                    ax1.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[0,0,0:],'-', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD})}$")
                    ax1.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[1,1,0:],'--', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD})}$")

                    if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3 and rveImage.labelNumber!=4 and rveImage.labelNumber!=5 and rveImage.labelNumber!=6 and rveImage.labelNumber!=7 and rveImage.labelNumber!=8:
                        ax1.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[0,0,0:],'-',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
                        ax1.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[1,1,0:],'--',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")
                    
                
                ax1.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[0,0,0:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
                ax1.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[1,1,0:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
            
                
                rmin1=0
                maxNum11=max(fullField.keffNum_EVa[0,0,:])
                maxNum22=max(fullField.keffNum_EVa[1,1,:])
                if maxNum11>maxNum22:
                    rmax1=maxNum11+0.1
                else:
                    rmax1=maxNum22+0.1

                tmin1 = np.degrees(varyParamValue_FF)[0,0]
                tmax1 = np.degrees(varyParamValue_FF)[0,-1]
                
                ax1.set_rmin(rmin1); ax1.set_rmax(rmax1)
                ax1.set_thetamin(tmin1);ax1.set_thetamax(tmax1)
                ax1.set_rorigin(0)
                
                theta_ticks = np.arange(tmin1, tmax1+10, 10)
                radial_ticks = np.arange(rmin1, rmax1, 0.3)
                ax1.set_thetagrids(theta_ticks)
                ax1.set_rticks(radial_ticks)

                ax1.tick_params(axis='both', labelsize=18)
                
                ax1.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_inclValue[0,0]}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_inclValue[0,0]}$, '+f'$\\gamma = {gammaValue[0,0]}$',fontsize=20)
                ax1.title.set_position((0.5, 0.5))
                ax1.set_ylabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{incl})}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
                #ax1.yaxis.set_label_coords(-0.05, 0.5)
                ax1.set_xlabel(r'$\mathrm{Normalized\; Effective\; Conductivity}$',fontsize=20)
                ax1.xaxis.set_label_coords(0.5, -0.1)
                ax1.grid(False)


                ax1.legend(loc='upper center',bbox_to_anchor=(1.4, 1),fancybox=True, shadow=True,fontsize= 20)
                fig1.savefig(str(Path(comparison_path+f'/Appr_Comparison_varyParam_'+varyParamName+'_polar'+'.png').resolve()),dpi=300, bbox_inches='tight')

        
        else: #'c_incl'
            
            if showMFApproach:
                ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[0,0,:],'-', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
                ax.plot(varyParamValue_MF[0,:], meanField.keffMt_EVa[1,1,:],'--', c = 'orange', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")
                
                ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[0,0,:],'-', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD})}$")
                ax.plot(varyParamValue_MF[0,:], meanField.keffIdd_EVa[1,1,:],'--', c= 'r', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD})}$")
                
                if rveImage.labelNumber!=1 and rveImage.labelNumber!=2 and rveImage.labelNumber!=3 and rveImage.labelNumber!=4 and rveImage.labelNumber!=5 and rveImage.labelNumber!=6 and rveImage.labelNumber!=7 and rveImage.labelNumber!=8:
                    ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[0,0,:], '-',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
                    ax.plot(varyParamValue_MF[0,:], meanField.keffPcw_EVa[1,1,:], '--',c = 'b', lw=1.5, ms=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")

            if showFFApproach:
                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
                ax.plot(varyParamValue_FF[0,:], fullField.keffNum_EVa[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")

            ax.set_xlabel(r'$\mathrm{Concentration\; of\; inclusions\;}$ '+r'$\mathsf{c}$',fontsize=20)

            ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$e^{{\mathrm{{(incl)}}}} = {e_incl[0,0]}$, '\
                +f'$\\theta^{{\mathrm{{(incl)}}}} = {round(np.degrees(theta_incl[0,0]))}$'+r'$^{\circ}$, '+f'$\\gamma = {gammaValue[0,0]}$',fontsize=20)
        
        
        ax.set_ylabel(r'$\mathrm{Normalized\; Effective\; Conductivity}$',fontsize=20)
        #ax.yaxis.set_label_coords(-.19, .48)
        ax.tick_params(axis='both', labelsize=18)
        ax.legend(loc='upper center',bbox_to_anchor=(1.20, 1.05),fancybox=True, shadow=True,fontsize= 15)
        ax.grid()
        
        
        fig.savefig(comparison_path.joinpath(f'Appr_Comparison_varyParam_'+varyParamName+'.png'),dpi=300, bbox_inches='tight') 
        
        plt.close( )

    @staticmethod
    def Rve_And_EVe(rveImage,keff_EVe,name,gammaValue,gammaIndex):
        
        logger.info('Rve_And_EVe')
        
        #rveImage
        N_incl=rveImage.N_incl
        x_incl_Pxls=rveImage.x_incl_Pxls
        R_incl_Pxls=rveImage.R_incl_Pxls
        a2_incl_Pxls=rveImage.a2_incl_Pxls
        theta_incl=rveImage.theta_incl
        if N_incl==1:
            vscale=8
        else:
            vscale=16


        #---
        fig, ax = plt.subplots() 

        auxString=r'$\mathsf{c}$'+f' = {rveImage.c_incl[0,0]}, '+r'$e^{\mathrm{(incl)}}$'+f' = {rveImage.e_incl[0,0]},\
                '+r'$\theta^{\mathrm{(incl)}}$'+f' = {np.degrees(rveImage.theta_incl[0,0])}'+r'$^{\circ}$'+', '+r'$\gamma$'+f' = {gammaValue}'

        if name=='Mt':
            ax.set_title(r'$\mathrm{Eigenvectors\; of\;}$ '+r"$\boldsymbol{k}_{\mathrm{eff}}^{(\mathrm{MT})}$\\"+auxString,fontsize=20)
        elif name=='Idd':
            ax.set_title(r'$\mathrm{Eigenvectors\; of\;}$ '+r"$\boldsymbol{k}_{\mathrm{eff}}^{(\mathrm{IDD})}$\\"+auxString,fontsize=20)
        elif name=='Pcw':
            ax.set_title(r'$\mathrm{Eigenvectors\; of\;}$ '+r"$\boldsymbol{k}_{\mathrm{eff}}^{(\mathrm{PCW})}$\\"+auxString,fontsize=20)
        else:
            ax.set_title(r'$\mathrm{Eigenvectors\; of\;}$ '+r"$\boldsymbol{k}_{\mathrm{eff}}^{(\mathrm{Num})}$\\"+auxString,fontsize=20)

        ax.axis((0*rveImage.pixels, 1*rveImage.pixels,0*rveImage.pixels,1*rveImage.pixels))
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_xlabel('pixels', fontsize=20)
        ax.set_ylabel('pixels', fontsize=20)
        #ax.yaxis.set_label_coords(-.15, .48)
        ax.set_aspect('equal', adjustable='box')

        for I in range(N_incl):

            # Graphing inclusions
            auxAngle=theta_incl[I,0]
            incl = Ellipse((x_incl_Pxls[I,0],x_incl_Pxls[I,1]), 2*R_incl_Pxls[I,0], 2*a2_incl_Pxls[I,0],\
                color='r',linestyle='-', angle=np.degrees(auxAngle),fill=False,linewidth=1)

            ax.add_patch(incl)

            # Semi-axes of ellipses
            xCentroid=x_incl_Pxls[I,0]
            yCentroid=x_incl_Pxls[I,1]
            major_axis_EllipRegions=2*R_incl_Pxls[I,0]
            minor_axis_EllipRegions=2*a2_incl_Pxls[I,0]
            x1 = xCentroid + np.cos(auxAngle) * 0.5 * major_axis_EllipRegions
            y1 = yCentroid + np.sin(auxAngle) * 0.5 * major_axis_EllipRegions
            x2 = xCentroid - np.cos(np.pi/2-auxAngle) * 0.5 * minor_axis_EllipRegions
            y2 = yCentroid + np.sin(np.pi/2-auxAngle) * 0.5 * minor_axis_EllipRegions
            
            ax.plot(x1,y1,'.k',markersize=5)
            ax.plot((xCentroid, x1), (yCentroid, y1), '--k', linewidth=1)
            ax.plot(x2,y2,'.k',markersize=5)
            ax.plot((xCentroid, x2), (yCentroid, y2), ':k', linewidth=1)
            ax.plot(xCentroid,yCentroid, '.k', markersize=5)
        

            # Graphing eigenvectors
            unit_vector_x= np.array([[1],[0]])
            unit_vector_y= np.array([[0],[1]])

            origin = np.array([[xCentroid],[yCentroid]])

            eig_vec1 = keff_EVe[:,0,gammaIndex,np.newaxis] # eigenvector corresponding to the greatest eigenvalue
            eig_vec2 = keff_EVe[:,1,gammaIndex,np.newaxis]
            
            dot_product1=np.dot(eig_vec1.T, unit_vector_x)
            angle1= np.arccos(dot_product1) 

            dot_product2=np.dot(eig_vec2.T, unit_vector_y)
            angle2= np.arccos(dot_product2) 
            
            if I==0:
                ax.quiver(*origin, *eig_vec1, color=['k'], scale=vscale,label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}$")
                ax.quiver(*origin, *eig_vec2, color=['gray'], scale=vscale,label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}$")
            else:
                ax.quiver(*origin, *eig_vec1, color=['k'], scale=vscale)
                ax.quiver(*origin, *eig_vec2, color=['gray'], scale=vscale)
            
            ax.legend(loc='upper center',bbox_to_anchor=(1.10, 1),fancybox=True, shadow=True,fontsize=20)
        
        fig.savefig(rveImage.dir+f'/Results/Numerical_Comparisons/Rve_And_EVe_{name}.png',dpi=300, bbox_inches='tight') 
        
        plt.close( )
        

    @staticmethod
    def ThetaEff_ThetaIncl(rveImage,meanField,fullField,c_inclValue=None,e_inclValue=None,theta_inclValue=None,gammaValue=None):
        
        logger.info('ThetaEff_ThetaIncl')

        # rveImage
        dir=rveImage.dir
        varyParamValue_FF=rveImage.varyParamValue_FF
        varyParamValue_MF=rveImage.varyParamValue_MF

        N_varyParamValue_FF=varyParamValue_FF.shape[1]
        N_varyParamValue_MF=varyParamValue_MF.shape[1]
        unit_vector_x = np.array([[1],[0]])

        dot_product_Mt=np.zeros((N_varyParamValue_MF))
        dot_product_Idd=np.zeros((N_varyParamValue_MF))
        dot_product_Num=np.zeros((N_varyParamValue_FF))


        #-----
        # Plot eigenvectors
        if rveImage.showMFApproach:
            eig_vec1_Mt = meanField.keffMt_EVe[:,0,:] # eigenvector corresponding to the greatest eigenvalue 
            eig_vec1_Idd = meanField.keffIdd_EVe[:,0,:]
            
        
            for II in range(N_varyParamValue_MF):
                if np.all(np.sign(eig_vec1_Mt[:,II,np.newaxis])==-1): 
                    dot_product_Mt[II]=np.dot(-eig_vec1_Mt[:,II,np.newaxis].T, unit_vector_x) # correcting eigenvector direction
                else:
                    dot_product_Mt[II]=np.dot(eig_vec1_Mt[:,II,np.newaxis].T, unit_vector_x)
                    
                if np.all(np.sign(eig_vec1_Idd[:,II,np.newaxis])==-1): 
                    dot_product_Idd[II]=np.dot(-eig_vec1_Idd[:,II,np.newaxis].T, unit_vector_x) # correcting eigenvector direction
                else:
                    dot_product_Idd[II]=np.dot(eig_vec1_Idd[:,II,np.newaxis].T, unit_vector_x)
            
            angle_Mt = np.arccos(dot_product_Mt)
            angle_Idd = np.arccos(dot_product_Idd)
            

        if rveImage.showFFApproach:
            eig_vec1_Num = fullField.keffNum_EVe[:,0,:]

            for JJ in range(N_varyParamValue_FF):
                if np.all(np.sign(eig_vec1_Num[:,JJ,np.newaxis])==-1): 
                    dot_product_Num[JJ]=np.dot(-eig_vec1_Num[:,JJ,np.newaxis].T, unit_vector_x)  # correcting eigenvector direction
                else:
                    dot_product_Num[JJ]=np.dot(eig_vec1_Num[:,JJ,np.newaxis].T, unit_vector_x)
            
            angle_Num = np.arccos(dot_product_Num)
        
    
        fig,ax=plt.subplots()
        if rveImage.showMFApproach:
            ax.plot(np.degrees(varyParamValue_MF)[0,:], np.ravel(np.degrees(angle_Mt)),'-', c = 'orange', lw=1.5, ms=5, label=r"$\mathrm{MT}$") # label=r"$\bar{k}_{\mathrm{eff}}^{(\mathrm{MT})}$"
            ax.plot(np.degrees(varyParamValue_MF)[0,:], np.ravel(np.degrees(angle_Idd)),'-', c= 'r', lw=1.5, ms=5, label=r"$\mathrm{IDD}$") # label=r"$\bar{k}_{\mathrm{eff}}^{(\mathrm{IDD})}$"
            
        if rveImage.showFFApproach:
            ax.plot(np.degrees(varyParamValue_FF)[0,:], np.ravel(np.degrees(angle_Num)), 'o:', c='k', lw=1.5, ms=5, label=r"$\mathrm{Num}$") # label=r"$\bar{k}_{\mathrm{eff}}^{(\mathrm{Num})}$"
        
        ax.set_xlabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{incl})}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
        t_incl_min = 0
        t_incl_max = np.degrees(varyParamValue_FF)[0,-1]
        ax.set(xticks=np.arange(t_incl_min,t_incl_max+15,15), xlim=[t_incl_min, t_incl_max+10])

        ax.set_ylabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{Appr})}_{\mathrm{eff}}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
        t_eff_min = 0
        t_eff_max = t_incl_max
        ax.set(yticks=np.arange(t_eff_min,t_eff_max+15,15), xlim=[t_eff_min, t_eff_max+10])

        ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_inclValue[0,0]}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_inclValue[0,0]}$, '+f'$\\gamma = {gammaValue[0,0]}$',fontsize=20)
        ax.legend(loc='upper center',fontsize=20,bbox_to_anchor=(1.25, 1),fancybox=True, shadow=True)
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.grid()
        ax.set_aspect('equal', adjustable='box')
        
        
        
        fig.savefig(dir+f'/Results/Numerical_Comparisons/ThetaEff_ThetaIncl.png',dpi=300, bbox_inches='tight') 
        
        plt.close( )
    
    # Two-step homogenization
    @staticmethod
    def Hist_numb_grains_orient(ip_path,N_Groups,theta_inclGroups):
        
        logger.info('Hist_numb_grains_orient')
        intervals=np.arange(-85,95,10)
        intervals=np.append(intervals,95)
        intervals=np.insert(intervals,0,-95,axis=0)
        N_intervals=intervals.shape[0]

        interCounter=np.zeros([N_intervals-1])
        
        for II in range(N_intervals-1):
            for JJ in range(N_Groups):
                if not II==N_intervals-2:
                    interCounter[II]+=np.count_nonzero(np.array([intervals[II] <= X < intervals[II+1] for X in np.degrees(theta_inclGroups[f'{JJ}'])]))
                else:
                    interCounter[II]+=np.count_nonzero(np.array([intervals[II] <= X <= intervals[II+1] for X in np.degrees(theta_inclGroups[f'{JJ}'])]))

        countMax=max(interCounter)
         
        #---
        fig, ax = plt.subplots()
        ax.bar(np.arange(-90,100,10), interCounter, width=10, align='center',color='#FF8080',edgecolor='k')
        ax.set_ylabel(r'$\mathrm{Number\; of\; occurrences}$',fontsize=20)
        #ax.yaxis.set_label_coords(-.14, .48)
        ax.set_xlabel(r'$\mathrm{Orientation\;}$ $\theta^{(\mathrm{incl})}$'+'\n'+r'$\mathrm{(degrees)}$',fontsize=20, multialignment='center')
        ax.set(xticks=np.arange(-90,100,10), xlim=[-90, 90])
        ax.set(yticks=np.arange(0,countMax+1,1), ylim=[0, countMax+0.15*countMax])
        plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='center')
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.set_aspect(0.5/(1*countMax)*180, adjustable='box')
        
        theta_vals = np.arange(-80,100,40) 
        #xPos=np.linspace(0.265,0.71, theta_vals.shape[0])
        xPos=np.linspace(0.14,0.83, theta_vals.shape[0])
        for II, TH in enumerate(theta_vals):
            
            ax.axvline(x=TH, ymin=0, ymax=0.9, linewidth=0.5,linestyle='--', color='lightgray') # vertical lines

            ax_smallWind = fig.add_axes([xPos[II], 0.8, 0.05, 0.05]) # creates small windows
            ax_smallWind.set_aspect(1, adjustable='box')
            ax_smallWind.set_xlim(0,1); ax_smallWind.set_ylim(0,1)
            ax_smallWind.set_xticks([]); ax_smallWind.set_yticks([])
            
            #---
            # Square cell prototype
            Area = 1
            c_incl = 0.2
            e_incl = 0.5
            theta_incl = TH
            R_incl = np.sqrt(c_incl*Area/(e_incl*np.pi))
            a2_incl = R_incl*e_incl
            ellip = Ellipse(((0.5,0.5)), 2*R_incl, 2*a2_incl,color='k', angle=theta_incl, fill=False,linewidth=1.5)
            #---
            ax_smallWind.add_patch(ellip)
            

        fig.savefig(ip_path.joinpath(f'Hist_numb_grains_orient.png'),dpi=300, bbox_inches='tight') 
        
        plt.close( )
    

    #------
    # RVE Analysis
    @staticmethod
    def Plot_RVE_Convergence_study(dir,N_Rve,keffNum_EVa_CumMean,index=None):
        
        logger.info('Plot_RVE_Convergence_study')
        fig,ax=plt.subplots()
        
        
        if index=='1':
            ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean, 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
            # ax.legend(loc='upper center',bbox_to_anchor=(0.9, 0.25),fancybox=True, shadow=True,fontsize= 20)
            ax.set_ylabel(r'$\frac{\lvert ^{i}\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})} - \mu_{10} \rvert}{\mu_{10}}$',fontsize=22)
            plt.ylim((0,0.025))

        elif index=='2':
            ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean, 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
            # ax.legend(loc='upper center',bbox_to_anchor=(0.9, 1),fancybox=True, shadow=True,fontsize= 20)
            ax.set_ylabel(r'$\frac{\lvert ^{i}\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})} - \mu_{10} \rvert}{\mu_{10}}$',fontsize=22)
            plt.ylim((0,0.003))

        else:
            ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
            ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
            ax.legend(loc='upper center',bbox_to_anchor=(1.2, 1),fancybox=True, shadow=True,fontsize= 20)
            ax.set_ylabel(r'$\frac{\lvert ^{i}\bar{k}_{\mathrm{eff}}^{(\mathrm{Num})} - \mu_{10} \rvert}{\mu_{10}}$',fontsize=20)

        ax.set_xlabel(r'$\mathrm{RVE\; (i\text{-}th)\;}$',fontsize=20)

        ax.set(xticks=np.arange(1,N_Rve+1,1), xlim=[1, N_Rve])
        #plt.ylim((0,0.005))
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.grid()
        
        fig.canvas.start_event_loop(sys.float_info.min)

        if index=='1':
            path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study-kI.png'
        elif index=='2':
            path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study-kII.png'
        else:
            path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study.png'

        fig.savefig(path,dpi=300, bbox_inches='tight')

        plt.close( )
        return ax
    
    # @staticmethod
    # def Plot_RVE_Convergence_study(dir,N_Rve,keffNum_EVa_CumMean,index=None):
        
    #     logger.info('Plot_RVE_Convergence_study')
    #     fig,ax=plt.subplots()
        
        
    #     if index=='1':
    #         ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
    #         ax.legend(loc='upper center',bbox_to_anchor=(0.8, 1),fancybox=True, shadow=True,fontsize= 20)

    #     elif index=='2':
    #         ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
    #         ax.legend(loc='upper center',bbox_to_anchor=(0.8, 0.25),fancybox=True, shadow=True,fontsize= 20)

    #     else:
    #         ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[0,0,:], 'o:', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
    #         ax.plot(np.arange(1,N_Rve+1,1), keffNum_EVa_CumMean[1,1,:], 'o:',markerfacecolor='none', c='k', lw=1.5, ms=5, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
    #         ax.legend(loc='upper center',bbox_to_anchor=(1.2, 1),fancybox=True, shadow=True,fontsize= 20)

    #     ax.set_xlabel(r'$\mathrm{Number\; of\; RVE\; analyzed\; (Iter)}$',fontsize=20)

    #     ax.set_ylabel(r'$\frac{1}{\mathrm{Iter}}\sum_{i=1}^{\mathrm{Iter}}(^{i}\bar{k}_{\mathrm{eff}}^{(\mathrm{Num})})$',fontsize=20)
    #     ax.set(xticks=np.arange(1,N_Rve+1,1), xlim=[1, N_Rve])
    #     plt.xticks(fontsize= 18)
    #     plt.yticks(fontsize= 18)
    #     ax.grid()
        
    #     fig.canvas.start_event_loop(sys.float_info.min)

    #     if index=='1':
    #         path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study-kI.png'
    #     elif index=='2':
    #         path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study-kII.png'
    #     else:
    #         path=dir+f'/Results/Numerical_Comparisons/RVE_Convergence_study.png'

    #     fig.savefig(path,dpi=300, bbox_inches='tight')

    #     plt.close( )
    #     return ax

    #----------------------
    # Advani_Tucker
    @staticmethod
    def Plot_RVE_Advani_Tucker(rveImage,meanFieldDict,fullFieldDict,AT_Param_m,N_Rve):
        
        logger.info('Plot_RVE_Advani_Tucker')
        # rveImage
        dir=rveImage.dir
        showMFApproach=rveImage.showMFApproach
        showFFApproach=rveImage.showFFApproach
        c_incl=rveImage.c_incl[0,0]
        e_incl=rveImage.e_incl[0,0]
        gammaIndex=-1
        gammaValue=rveImage.varyParamValue_MF[0,gammaIndex]

        varyParam=AT_Param_m
        N_varyParam=AT_Param_m.size
        keffMt_EVa=np.zeros([2,2,N_Rve,N_varyParam])
        keffIdd_Voigt_EVa=np.zeros([2,2,N_Rve,N_varyParam])
        keffIdd_Reuss_EVa=np.zeros([2,2,N_Rve,N_varyParam])
        keffPcw_EVa=np.zeros([2,2,N_Rve,N_varyParam])
        keffNum_EVa=np.zeros([2,2,N_Rve,N_varyParam])
        
        keffMt_EVa_Mean=np.zeros([2,2,N_varyParam])
        keffIdd_Voigt_EVa_Mean=np.zeros([2,2,N_varyParam])
        keffIdd_Reuss_EVa_Mean=np.zeros([2,2,N_varyParam])
        keffPcw_EVa_Mean=np.zeros([2,2,N_varyParam])
        keffNum_EVa_Mean=np.zeros([2,2,N_varyParam])
        
        keffMt_EVa_Std=np.zeros([2,2,N_varyParam])
        keffIdd_Voigt_EVa_Std=np.zeros([2,2,N_varyParam])
        keffIdd_Reuss_EVa_Std=np.zeros([2,2,N_varyParam])
        keffPcw_EVa_Std=np.zeros([2,2,N_varyParam])
        keffNum_EVa_Std=np.zeros([2,2,N_varyParam])

        for II in range(N_varyParam):
            
            for JJ in range(N_Rve):

                if showMFApproach:
                    keffMt_EVa[:,:,JJ,II]=meanFieldDict[f'{II}'][JJ].keffMt_EVa[:,:,gammaIndex]
                    keffIdd_Voigt_EVa[:,:,JJ,II]=meanFieldDict[f'{II}'][JJ].keffIdd_Voigt_EVa[:,:,gammaIndex]
                    keffIdd_Reuss_EVa[:,:,JJ,II]=meanFieldDict[f'{II}'][JJ].keffIdd_Reuss_EVa[:,:,gammaIndex]
                    keffPcw_EVa[:,:,JJ,II]=meanFieldDict[f'{II}'][JJ].keffPcw_EVa[:,:,gammaIndex]
                
                if showFFApproach: 
                    keffNum_EVa[:,:,JJ,II]=fullFieldDict[f'{II}'][JJ].keffNum_EVa[:,:,gammaIndex]
            
            if showMFApproach:
                keffMt_EVa_Mean[:,:,II]=np.mean(keffMt_EVa[:,:,:,II],axis=2,keepdims=0)
                keffMt_EVa_Std[:,:,II]=np.std(keffMt_EVa[:,:,:,II],axis=2,keepdims=0)
                
                keffIdd_Voigt_EVa_Mean[:,:,II]=np.mean(keffIdd_Voigt_EVa[:,:,:,II],axis=2,keepdims=0)
                keffIdd_Voigt_EVa_Std[:,:,II]=np.std(keffIdd_Voigt_EVa[:,:,:,II],axis=2,keepdims=0)
                
                keffIdd_Reuss_EVa_Mean[:,:,II]=np.mean(keffIdd_Reuss_EVa[:,:,:,II],axis=2,keepdims=0)
                keffIdd_Reuss_EVa_Std[:,:,II]=np.std(keffIdd_Reuss_EVa[:,:,:,II],axis=2,keepdims=0)
                
                keffPcw_EVa_Mean[:,:,II]=np.mean(keffPcw_EVa[:,:,:,II],axis=2,keepdims=0)
                keffPcw_EVa_Std[:,:,II]=np.std(keffPcw_EVa[:,:,:,II],axis=2,keepdims=0)
            
            if showFFApproach: 
                keffNum_EVa_Mean[:,:,II]=np.mean(keffNum_EVa[:,:,:,II],axis=2,keepdims=0)
                keffNum_EVa_Std[:,:,II]=np.std(keffNum_EVa[:,:,:,II],axis=2,keepdims=0)
            
        fig,ax=plt.subplots()
        
        if showMFApproach:
            #---
            #'MT'
            ax.errorbar(varyParam[:], keffMt_EVa_Mean[0,0,:], keffMt_EVa_Std[0,0,:] ,fmt='o-', c = 'orange', lw=1.5, ms=5, zorder=3, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{MT})}$")
            ax.errorbar(varyParam[:], keffMt_EVa_Mean[1,1,:], keffMt_EVa_Std[1,1,:],fmt='o--',markerfacecolor='none', c = 'orange', lw=1.5, ms=5, zorder=3, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{MT})}$")
            
            # ax.fill_between(varyParam[:],  keffMt_EVa_Mean[0,0,:]- keffMt_EVa_Std[0,0,:],  keffMt_EVa_Mean[0,0,:]+ keffMt_EVa_Std[0,0,:], color='orange',alpha=0.2)
            # ax.fill_between(varyParam[:],  keffMt_EVa_Mean[1,1,:]- keffMt_EVa_Std[1,1,:],  keffMt_EVa_Mean[1,1,:]+ keffMt_EVa_Std[1,1,:], color='orange',alpha=0.2)
            
            #'IDD-Voigt' and 'IDD-Reuss'
            ax.errorbar(varyParam[:], keffIdd_Voigt_EVa_Mean[0,0,:], keffIdd_Voigt_EVa_Std[0,0,:],fmt='o-', c= '#DC143C', lw=1.5, ms=5, zorder=6, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD-Voigt})}$")
            ax.errorbar(varyParam[:], keffIdd_Voigt_EVa_Mean[1,1,:], keffIdd_Voigt_EVa_Std[1,1,:],fmt='o--',markerfacecolor='none', c= '#DC143C', lw=1.5, ms=5, zorder=6, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD-Voigt})}$")

            # ax.fill_between(varyParam[:],  keffIdd_Voigt_EVa_Mean[0,0,:]- keffIdd_Voigt_EVa_Std[0,0,:],  keffIdd_Voigt_EVa_Mean[0,0,:]+ keffIdd_Voigt_EVa_Std[0,0,:], color='#DC143C',alpha=0.2)
            # ax.fill_between(varyParam[:],  keffIdd_Voigt_EVa_Mean[1,1,:]- keffIdd_Voigt_EVa_Std[1,1,:],  keffIdd_Voigt_EVa_Mean[1,1,:]+ keffIdd_Voigt_EVa_Std[1,1,:], color='#DC143C',alpha=0.2)


            ax.errorbar(varyParam[:], keffIdd_Reuss_EVa_Mean[0,0,:], keffIdd_Reuss_EVa_Std[0,0,:],fmt='o-', c= '#7f7f7f', lw=1.5, ms=5, zorder=4, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{IDD-Reuss})}$")
            ax.errorbar(varyParam[:], keffIdd_Reuss_EVa_Mean[1,1,:], keffIdd_Reuss_EVa_Std[1,1,:],fmt='o--',markerfacecolor='none', c= '#7f7f7f', lw=1.5, ms=5, zorder=4, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{IDD-Reuss})}$")
            
            # ax.fill_between(varyParam[:],  keffIdd_Reuss_EVa_Mean[0,0,:]- keffIdd_Reuss_EVa_Std[0,0,:],  keffIdd_Reuss_EVa_Mean[0,0,:]+ keffIdd_Reuss_EVa_Std[0,0,:], color='#7f7f7f',alpha=0.2)
            # ax.fill_between(varyParam[:],  keffIdd_Reuss_EVa_Mean[1,1,:]- keffIdd_Reuss_EVa_Std[1,1,:],  keffIdd_Reuss_EVa_Mean[1,1,:]+ keffIdd_Reuss_EVa_Std[1,1,:], color='#7f7f7f',alpha=0.2)
            

            #'PCW'
            ax.errorbar(varyParam[:], keffPcw_EVa_Mean[0,0,:], keffPcw_EVa_Std[0,0,:], fmt='o-',c = 'b', lw=1.5, ms=5, zorder=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{PCW})}$")
            ax.errorbar(varyParam[:], keffPcw_EVa_Mean[1,1,:], keffPcw_EVa_Std[1,1,:], fmt='o--',markerfacecolor='none',c = 'b', lw=1.5, ms=5, zorder=5,  label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{PCW})}$")

            # ax.fill_between(varyParam[:],  keffPcw_EVa_Mean[0,0,:]- keffPcw_EVa_Std[0,0,:],  keffPcw_EVa_Mean[0,0,:]+ keffPcw_EVa_Std[0,0,:], color='b',alpha=0.2)
            # ax.fill_between(varyParam[:],  keffPcw_EVa_Mean[1,1,:]- keffPcw_EVa_Std[1,1,:],  keffPcw_EVa_Mean[1,1,:]+ keffPcw_EVa_Std[1,1,:], color='b',alpha=0.2)

        if showFFApproach:   
            #'FF'
            ax.errorbar(varyParam[:], keffNum_EVa_Mean[0,0,:], keffNum_EVa_Std[0,0,:], fmt='o:', c='k', lw=1.5, ms=5, zorder=2, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{I}}^{(\mathrm{Num})}$")
            ax.errorbar(varyParam[:], keffNum_EVa_Mean[1,1,:], keffNum_EVa_Std[1,1,:], fmt='o:',markerfacecolor='none', c='k', lw=1.5, ms=5, zorder=2, label=r"$\bar{k}_{\mathrm{eff}\textrm{--}\mathrm{II}}^{(\mathrm{Num})}$")
            
            # ax.fill_between(varyParam[:],  keffNum_EVa_Mean[0,0,:]- keffNum_EVa_Std[0,0,:],  keffNum_EVa_Mean[0,0,:]+ keffNum_EVa_Std[0,0,:], color='k',alpha=0.2)
            # ax.fill_between(varyParam[:],  keffNum_EVa_Mean[1,1,:]- keffNum_EVa_Std[1,1,:],  keffNum_EVa_Mean[1,1,:]+ keffNum_EVa_Std[1,1,:], color='k',alpha=0.2)
            # #---
        
        ax.set_xlabel(r'$\mathrm{Advani-Tucker\; orientation\; parameter\;}$ '+f'$m_{{\mathrm{{AT}}}}$',fontsize=20)
        ax.set_title(r'$\mathrm{Fixed\; parameters}$'+'\n'+f'$\mathsf{{c}} = {c_incl}$, '+f'$e^{{\mathrm{{(incl)}}}} = {e_incl}$, '+f'$\\gamma = {round(gammaValue)}$',fontsize=20, multialignment='center')
        
        ax.set_ylabel(r'$\mathrm{Normalized\; Effective\; Conductivity}$',fontsize=20)
        #ax.yaxis.set_label_coords(-.19, .48)
        plt.xticks(fontsize= 18)
        plt.yticks(fontsize= 18)
        ax.legend(loc='upper center',bbox_to_anchor=(1.20, 1.05),fancybox=True, shadow=True,fontsize= 15)
        ax.grid()
        

        fig.savefig(dir+f'/Results/Numerical_Comparisons/Appr_Comparison_RVE_Advani_Tucker.png',dpi=300, bbox_inches='tight') 
        
        plt.close( )
        



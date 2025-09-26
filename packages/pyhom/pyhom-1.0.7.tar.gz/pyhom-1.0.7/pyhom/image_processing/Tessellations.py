"""Tessellations
   Description
"""

import os
import numpy as np
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
from matplotlib.path import Path as matplotlib_path
import cv2
from shapely.geometry import Polygon as shapely_Polygon
import logging
from pathlib import Path


from pyhom.image_processing.Graph_Tools import Graph



class Voronoi_Diagram:
   
    def __init__(self, rveImage, vd_image_path):
        
        self.vd_image_path = vd_image_path 
        self.logger = rveImage.logger
        self.rveImage = rveImage
        
        for attr in ["allPolygons","vdPolygons","areaVdPolygons"]:
            setattr(self,attr,None) # Definition of attributes


    def All_Polygons(self):
        """_summary_
        """
        self.logger.info('All_Polygons') 
        vor = Voronoi(self.rveImage.seedPoints) # x-y perspective
        regions, vertices = vor.regions, vor.vertices

        allPolygons = []
        for reg in regions:
            if -1 not in reg and len(reg) !=0:  # We can simply ignore any regions containing -1.
                poly = vertices[reg]
                allPolygons.append(poly)

        self.allPolygons=allPolygons

    def VD_Polygons(self,tol=10**(-5)):
      

        self.logger.info('VD_Polygons') 
        
        allPolygons=self.allPolygons
        x_incl_Pxls=self.rveImage.x_incl_Pxls
        N_incl=x_incl_Pxls.shape[0]

        vdPolygons_Aux = []
        totalArea=0

        JJ=0
        poly_indices = []
        for poly in allPolygons:
            if not JJ==N_incl:
                inside = matplotlib_path(poly).contains_points(x_incl_Pxls)
                for index in np.where(inside)[0]:
                    vdPolygons_Aux.append(poly)
                    poly_indices.append(index)
                    totalArea += shapely_Polygon(poly).area
                    JJ+=1
            else:
                break
        
        vdPolygons= [vdPolygons_Aux[poly_indices.index(i)] for i in range(N_incl)] 
                    
        if abs(totalArea-self.rveImage.pixels**2)<=tol:
            self.logger.info('Checked: area of VD cells')
        else:
            self.logger.error('Error in VD_Polygons. Unmatched area of the image and VD cells')
            os._exit(0) 

        self.vdPolygons= vdPolygons # x-y perspective
        self.areaVdPolygons=totalArea

    def Export_GrayScale_VD(self):
        """This function returns the image of the Voronoi diagram in grayscale. 
        """
        
        self.logger.info('Export_GrayScale_VD')

        vdPolygons = self.vdPolygons
        dir=self.rveImage.dir
        pixels=self.rveImage.pixels

        fig, ax = plt.subplots()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal', adjustable='box')
        ax.set_facecolor("black")
        #---
        # Set limits
        ax.axis((-1/2*pixels, 3/2*pixels,-1/2*pixels,3/2*pixels)) 
       
        #---
        
        alpha=1; linewidth=1 
        for poly in vdPolygons:
            ax.add_patch(plt.Polygon(poly, alpha=alpha, facecolor='white',\
                 edgecolor='black',linewidth=linewidth))

        if True:
            vdLabelName=f'VD'
            vdImagePath=self.vd_image_path.joinpath(f'{vdLabelName}.png')
            fig.savefig(vdImagePath, dpi=300, bbox_inches='tight', pad_inches=0, facecolor='black') # x-y perspective
            
            
            vdImageArray = cv2.imread(str(vdImagePath), cv2.IMREAD_GRAYSCALE)
            assert(vdImageArray.dtype==np.dtype('uint8'))

            unique_values = np.unique(vdImageArray)
            if unique_values.shape[0] !=2:
                vdImageArray[np.where(vdImageArray<255)]=0 
                
            
            vdImageArray = cv2.resize(vdImageArray, (2*pixels, 2*pixels), cv2.INTER_AREA,fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
            cv2.imwrite(str(vdImagePath), vdImageArray)

            self.logger.info('The VD image has been saved')

        plt.close(fig)

        return vdLabelName, vdImagePath






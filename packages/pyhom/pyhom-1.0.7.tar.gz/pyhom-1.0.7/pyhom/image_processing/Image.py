
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon, Ellipse
from skimage import io
from skimage.measure import label as Label
from skimage.measure import  regionprops as RegionProps


import pyhom.image_processing.Graph_Tools as ipgt


class General_Image:

    def __init__(self, globalPrm):
        
        # globalPrm
        self.logger = globalPrm['logger']
        self.dir = globalPrm['dir']
        # self.aim = globalPrm['aim']
        # self.jumpTo = globalPrm['jumpTo']
        # self.labelNumber = globalPrm['labelNumber']
        self.showFFApproach= globalPrm['showFFApproach']
        self.showMFApproach= globalPrm['showMFApproach']

   
    def To_Array(self,ID_Image,imagePath):
        
        self.logger.info('To_Array')

        #Read the image using skimage.io.imread and convert the image to grayscale (the image is loaded as a numpy array)
        genImageArray = io.imread(imagePath,as_gray=True) # x-y perspective

        try:
            assert(genImageArray.dtype==np.dtype('uint8'))
        except:
            # Convert the image to uint8. The range of values for uint8 is from 0 to 255
            genImageArray= (genImageArray * 255).astype(np.uint8)

        #To correct pixels color if necessary
        if ID_Image=='rveImage':
            unique_values = np.unique(genImageArray)
            if unique_values.shape[0] !=2:
                genImageArray[np.where(genImageArray>0)]=255 # More pixels for the inclusions
                
        #To correct pixels color if necessary
        if ID_Image=='vdImage':
            unique_values = np.unique(genImageArray)
            if unique_values.shape[0] !=2:
                genImageArray[np.where(genImageArray<255)]=0 # More pixels for the boundaries in VD
        
        if ID_Image is None:
            self.logger.error("Error in General_Image.To_Array. You must add ID_Image at the Image_Processing definition. You can use either: 'rveImage' or 'vDImage'")
            os._exit(0)
        
        genImageArrayFlip=np.flipud(genImageArray) # x-flip(y) perspective -> Useful for plotting graphs.
        genImageArrayFlipTransp=genImageArrayFlip.T # row-column perspective
        
        return genImageArray,genImageArrayFlip,genImageArrayFlipTransp


class RVE_Image (General_Image):
    
    def __init__(self, globalPrm, setPrm, inclPrm, ID_Image= None):
        
        super().__init__(globalPrm)

        # setPrm
        self.pixels=setPrm.pixels
        self.k0=setPrm.k0
        self.gamma=setPrm.gamma
        self.varyParamName=setPrm.varyParamName
        self.varyParamValue_FF=setPrm.varyParamValue_FF
        self.varyParamValue_MF=setPrm.varyParamValue_MF
        self.labelName=setPrm.rveLabelName
        self.imagePath = setPrm.rveImagePath

        # inclPrm
        self.N_incl=inclPrm.N_incl
        self.c_incl=inclPrm.c_incl
        self.e_incl=inclPrm.e_incl
        self.theta_incl=inclPrm.theta_incl
        self.R_incl_Pxls=inclPrm.R_incl_Pxls
        self.a2_incl_Pxls=inclPrm.a2_incl_Pxls
        self.x_incl_Pxls=inclPrm.x_incl_Pxls
        
        self.ID_Image=ID_Image
        
        for attr in ["c_incl_Ind","seedPoints","clonedRve"]:
            setattr(self,attr,None) # Definition of attributes
        
    
        

class VD_Image (General_Image):

    def __init__(self, logger, vdLabelName, vdImagePath, ID_Image=None):
        
        self.logger = logger
        self.labelName = vdLabelName
        self.imagePath = vdImagePath
        self.ID_Image=ID_Image

        for attr in ["pixels","e_cell_VD","theta_cell_VD","R_cell_VD_Pxls","a2_cell_VD_Pxls","x_cell_VD_Pxls"]:
            setattr(self,attr,None) # Definition of attributes
        

    


class Image_Processing:

    def __init__(self, genImage):

        self.logger = genImage.logger
        self.genImage = genImage  # Object from General_Image class
        self.genImageArray,self.genImageArrayFlip,self.genImageArrayFlipTransp\
            =genImage.To_Array(self.genImage.ID_Image,self.genImage.imagePath)
        
      
        for attr in ["regionsData","N_Regions","centroidRegions","areasRegions","axis_EllipRegions",\
            "theta_EllipRegions","e_EllipRegions","totalAreaRegions"]:
            setattr(self,attr,None) # Definition of attributes


   
        
                     
    def Reorder_And_Compare(self,a, b, valLabel, tol):
       
        self.logger.info(f'Reorder_And_Compare: {valLabel}')
        a_indices = np.zeros(a.shape[0], dtype=int)

        if valLabel == 'x_incl_Pxls':

            for i, val in enumerate(b):

                closest_index = np.argmin(np.linalg.norm(a - val, ord=2, axis=1)) 
                
                if np.all(np.isclose(a[closest_index], b[i], atol=tol)): 
                    a_indices[i] = closest_index

                else:
                    return np.array([])
            
            return a_indices
        
        else:

            for i, val in enumerate(b):

                closest_index = np.argmin(np.abs(a - val)) 
                
                if np.isclose(a[closest_index], b[i], atol=tol): 
                    a_indices[i] = closest_index

                else:
                    return np.array([])
            
            return a_indices

    def Set_Or_Check_Pxls(self):
        
        self.logger.info('Set_Or_Check_Pxls')
        widthImage, heightImage = self.genImageArray.shape
        
        if self.genImage.pixels is None:
            try:
                1/(widthImage-heightImage)
                self.logger.error('Error in Set_Or_Check_Pxls. Non-square image.')
                os._exit(0)
            except:
                self.logger.info('Checked: Square image') 
                self.genImage.pixels=widthImage
        else: # Already has input pixels.
            if self.genImage.pixels== widthImage and widthImage==heightImage:
                self.logger.info('Checked: pixels')
            else:
                self.logger.warning(f'Warning in Set_Or_Check_Pxls. The value of the variable pixels = {self.genImage.pixels} you'+\
                        f' have entered does not correspond to the value of pixels = {widthImage} automatically calculated from the microstructure image.'+\
                        f' You can leave it as None or update it. Here, the calculations will continue with pixels = {widthImage}')
                self.genImage.pixels=widthImage

    def Set_Or_Check_rank_0(self,valToCheck,newVal,valLabel, tol=2*10**(-2)):
        """Set the concentration of the inclusions in the square RVE image or check its value if we already have it.
        'N_incl','c_incl'"""
        
        self.logger.info(f'Set_Or_Check_rank_0: {valLabel}')

        if valToCheck is None:
            setattr(self.genImage, valLabel, newVal)
        
        else: # Already has input 'valLabel'.
            if np.abs(valToCheck-newVal)<=tol:
                self.logger.info(f'Checked: {valLabel} of regions')  
            else:
                self.logger.warning(f'Warning in Set_Or_Check for attribute {valLabel}. The value of the variable'+\
                    f'\n {valLabel} = {valToCheck}'+\
                    f'\n you have entered does not correspond to the value of variable'+\
                    f'\n {valLabel} = {newVal}'+\
                    f'\n automatically calculated from the microstructure image with a tolerance of {tol}.'+\
                    f' You can leave {valLabel} as None or update it. Here, the calculations will continue with'+\
                    f'\n {valLabel} = {valToCheck}.') #{newVal}
                           
    
    def Set_Or_Check_rank_1(self,valToCheck,newVal,valLabel, tol=2*10**(-2)):
        """Set the concentration of the inclusions in the square RVE image or check its value if we already have it.
        'e_incl', 'theta_incl', 'R_incl_Pxls', 'a2_incl_Pxls'"""
        
        self.logger.info(f'Set_Or_Check_rank_1: {valLabel}')

        if valToCheck is None:

            setattr(self.genImage, valLabel, newVal)
        
        else: # Already has input 'valLabel'.

            if np.all( np.abs(valToCheck-newVal) <= tol * np.ones( [valToCheck.shape[0],1] ) ):

                self.logger.info(f'Checked: {valLabel} of regions')

            else:
                # Reorder and compare
                correctIndices=self.Reorder_And_Compare(valToCheck, newVal,valLabel, tol)

                if correctIndices.size!=0:
                    setattr(self.genImage, valLabel, valToCheck[correctIndices])
                    self.logger.info(f'Checked: {valLabel} of regions')  
                else:
                    self.logger.warning(f'Warning in Set_Or_Check for attribute {valLabel}. The value of the variable'+\
                        f'\n {valLabel} = {valToCheck}'+\
                        f'\n you have entered does not correspond to the value of variable'+\
                        f'\n {valLabel} = {newVal}'+\
                        f'\n automatically calculated from the microstructure image with a tolerance of {tol}.'+\
                        f' You can leave {valLabel} as None or update it. Here, the calculations will continue with'+\
                        f'\n {valLabel} = {valToCheck}.') #{newVal}
                        
    
    def Set_Or_Check_rank_2(self,valToCheck,newVal,valLabel, tol=2*10**(-2)):
        """Set the concentration of the inclusions in the square RVE image or check its value if we already have it.
        'x_incl_Pxls'  rank = np.linalg.matrix_rank(a)"""
        
        self.logger.info(f'Set_Or_Check_rank_2: x_incl_Pxls')

        if valToCheck is None:
            setattr(self.genImage, valLabel, newVal)
        else: # Already has input 'valLabel'.

                       
            if np.all( np.linalg.norm(a - val, ord=2, axis=1)  <= tol * np.ones( [valToCheck.shape[0],1] ) ):
                self.logger.info(f'Checked: x_incl_Pxls of regions')
            else:
                # Reorder and compare
                correctIndices=self.Reorder_And_Compare(valToCheck, newVal,valLabel, tol)

                if correctIndices.size!=0:
                    setattr(self.genImage, valLabel, valToCheck[correctIndices])
                    self.logger.info(f'Checked: x_incl_Pxls of regions')  
                else:
                    self.logger.warning(f'Warning in Set_Or_Check for attribute x_incl_Pxls. The value of the variable'+\
                        f'\n x_incl_Pxls = {valToCheck}'+\
                        f'\n you have entered does not correspond to the value of variable'+\
                        f'\n x_incl_Pxls = {newVal}'+\
                        f'\n automatically calculated from the microstructure image with a tolerance of {tol}.'+\
                        f' You can leave x_incl_Pxls as None or update it. Here, the calculations will continue with'+\
                        f'\n x_incl_Pxls = {valToCheck}.') #{newVal}
                    
            
    def Clone_RVE(self):
        """Clone the RVE in a 3x3 grid formation""" 
        
        self.logger.info('Clone_RVE') 
        RveArray=self.genImageArrayFlipTransp # row-column perspective
        
        clonedRve=np.tile(RveArray, (3,3)) # Return the tiled image with dimension 3*pixels by 3*pixels

        self.genImage.clonedRve=clonedRve

    def Region_properties(self,ID_Image,rveImage=None, VD=None):
        """
        Connect similar regions of an image and return their properties.
        """
        
        self.logger.info(f'Region_properties: {ID_Image}')

        #------
        # (*) Notice that the skimage.measure modulus operates with a row-column perspective instead a x-y perspective.
        #------
        if ID_Image=='clonedRve': # The clonedRve image is 3*pixels by 3*pixels in dimension
            
            # We use the attribute "self.genImage.clonedRve" that was previously built by means of
            # the attribute "self.genImageArrayFlipTransp".
            labelArray = Label(self.genImage.clonedRve) # (*) row-column perspective

        if ID_Image=='rveImage' or ID_Image=='vdImage': # The vdImage has a dimension of 2*pixels by 2*pixels
            
            # We use the attribute "self.genImageArrayFlipTransp".
            labelArray = Label(self.genImageArrayFlipTransp) # (*) row-column perspective


        regionsData = RegionProps(labelArray) # Intensity value 0 are ignored.
        regionsData=np.array(regionsData)
        N_regions=regionsData.shape[0]
        pixels=self.genImage.pixels

        centroidRegions=np.zeros((N_regions,2))
        areasRegions=np.zeros((N_regions,1))
        totalAreaRegions=0

        axis_EllipRegions=np.zeros((N_regions,2)) 
        e_EllipRegions=np.zeros((N_regions,1))
        theta_EllipRegions=np.zeros((N_regions,1))
        
        if ID_Image=='clonedRve':
            e_incl=[]
            theta_incl=[]
            R_incl_Pxls=[]
            a2_incl_Pxls=[]
            x_incl_Pxls=[]

        MM=0
        KK=0
        for region in regionsData: 

            x0, y0 = region.centroid
            centroidRegions[MM]=np.array([x0,y0])
    
            areasRegions[MM]=region.area
            totalAreaRegions+=region.area

            major_axis_EllipRegions,minor_axis_EllipRegions=region.major_axis_length,region.minor_axis_length
            axis_EllipRegions[MM]=np.array([major_axis_EllipRegions,minor_axis_EllipRegions])
            e_EllipRegions[MM]=minor_axis_EllipRegions/major_axis_EllipRegions
            
            # This code is to correct the orientation given automatically by scikit-image for circular regions. 
            if e_EllipRegions[MM]==1:
                theta_EllipRegions[MM]=0
            else:
                theta_EllipRegions[MM]=region.orientation
            
            if ID_Image=='clonedRve':
                if pixels <= x0 < 2*pixels and pixels <= y0 < 2*pixels:
                    e_incl.append(e_EllipRegions[MM])
                    theta_incl.append(theta_EllipRegions[MM])
                    R_incl_Pxls.append(major_axis_EllipRegions/2)
                    a2_incl_Pxls.append(minor_axis_EllipRegions/2)
                    x_incl_Pxls.append(centroidRegions[MM])
                    KK=KK+1

            MM=MM+1
        
        if ID_Image=='clonedRve':
            e_incl=np.array(e_incl,dtype=float)
            theta_incl=np.array(theta_incl,dtype=float)
            R_incl_Pxls=np.array(R_incl_Pxls,dtype=float)[:,np.newaxis]
            a2_incl_Pxls=np.array(a2_incl_Pxls,dtype=float)[:,np.newaxis]
            x_incl_Pxls=np.array(x_incl_Pxls,dtype=float)

            # self.genImage.N_incl
            self.Set_Or_Check_rank_0(self.genImage.N_incl,KK,'N_incl')
            # self.genImage.c_incl
            self.Set_Or_Check_rank_0(self.genImage.c_incl,np.array([[totalAreaRegions/(3*pixels)**2]]),'c_incl')
            # self.genImage.e_incl
            self.Set_Or_Check_rank_1(self.genImage.e_incl,e_incl,'e_incl')
            # self.genImage.theta_incl
            self.Set_Or_Check_rank_1(self.genImage.theta_incl,theta_incl,'theta_incl')
            # self.genImage.R_incl_Pxls
            self.Set_Or_Check_rank_1(self.genImage.R_incl_Pxls,R_incl_Pxls,'R_incl_Pxls')
            # self.genImage.a2_incl_Pxls
            self.Set_Or_Check_rank_1(self.genImage.a2_incl_Pxls,a2_incl_Pxls,'a2_incl_Pxls')
            # self.genImage.x_incl_Pxls
            self.Set_Or_Check_rank_2(self.genImage.x_incl_Pxls,x_incl_Pxls - pixels,'x_incl_Pxls') 
                
        if ID_Image=='rveImage':
            # self.genImage.c_incl
            self.Set_Or_Check_rank_0(self.genImage.c_incl,np.array([[totalAreaRegions/pixels**2]]),'c_incl')

            
        if ID_Image=='vdImage': 

            x_cell_VD_Pxls=np.zeros((N_regions,2))

            regionsData_VD=np.zeros((N_regions))
            centroidRegions_VD=np.zeros((N_regions,2))
            areasRegions_VD=np.zeros((N_regions,1))
            axis_EllipRegions_VD=np.zeros((N_regions,2)) 
            e_EllipRegions_VD=np.zeros((N_regions,1))
            theta_EllipRegions_VD=np.zeros((N_regions,1))
            
            R_cell_VD_Pxls=np.zeros((N_regions,1))
            a2_cell_VD_Pxls=np.zeros((N_regions,1))
            
            correctPos=np.zeros((N_regions,1))
        
            #---
            
            rvePixels=rveImage.pixels # Inclusions
            x_incl_Pxls=rveImage.x_incl_Pxls
            #---
            
            x_cell_VD_Pxls_Aux= (centroidRegions-rvePixels/2) 
            
            #---
           
            dist=np.linalg.norm(x_cell_VD_Pxls_Aux[:, np.newaxis]-x_incl_Pxls, axis=2) 
            correctPos=np.argmin(dist, axis=1) 
            
            x_cell_VD_Pxls[correctPos]=x_cell_VD_Pxls_Aux

            regionsData_VD=np.array([regionsData[np.where(correctPos==i)][0] for i in range(N_regions)])
            centroidRegions_VD[correctPos]=centroidRegions
            areasRegions_VD[correctPos]=areasRegions
            axis_EllipRegions_VD[correctPos]=axis_EllipRegions
            e_EllipRegions_VD[correctPos]=e_EllipRegions
            theta_EllipRegions_VD[correctPos]=theta_EllipRegions

            self.genImage.e_cell_VD = e_EllipRegions_VD
            self.genImage.theta_cell_VD = theta_EllipRegions_VD
            self.genImage.R_cell_VD_Pxls = axis_EllipRegions_VD[:,0,np.newaxis]/2
            self.genImage.a2_cell_VD_Pxls = axis_EllipRegions_VD[:,1,np.newaxis]/2
            self.genImage.x_cell_VD_Pxls = x_cell_VD_Pxls

        self.N_Regions=N_regions
        self.totalAreaRegions=totalAreaRegions
        
        if ID_Image=='vdImage':
            self.regionsData=regionsData_VD
            self.centroidRegions=centroidRegions_VD
            self.areasRegions=areasRegions_VD
            self.axis_EllipRegions=axis_EllipRegions_VD
            self.e_EllipRegions=e_EllipRegions_VD
            self.theta_EllipRegions=theta_EllipRegions_VD
        
        else: # ID_Image=='clonedRve' or ID_Image=='rveImage':
            self.regionsData=regionsData
            self.centroidRegions=centroidRegions
            self.areasRegions=areasRegions
            self.axis_EllipRegions=axis_EllipRegions
            self.e_EllipRegions=e_EllipRegions
            self.theta_EllipRegions=theta_EllipRegions

       

    def Clone_x_incl_Pxls(self):
        """Clone the true centers within the RVE in a 3x3 grid formation"""
        
        self.logger.info('Clone_x_incl_Pxls') 
        N_incl=self.genImage.N_incl
        pixels=self.genImage.pixels
        x_incl_Pxls=self.genImage.x_incl_Pxls
        seedPoints=np.zeros((9*N_incl,2))
    
        Points = np.repeat(x_incl_Pxls, 9, axis=0).reshape(N_incl,9,2)
        
        Aux = np.array([0,-pixels, pixels])
        X = np.repeat(Aux, 3, axis=0)
        Y = np.squeeze(np.tile(Aux, (1,3)))
        
        Points[:,:, 0] += X
        Points[:,:, 1] += Y
        
        Points = np.reshape(Points, (9*N_incl, 2))

        self.genImage.seedPoints=Points

        

    
    
    
    
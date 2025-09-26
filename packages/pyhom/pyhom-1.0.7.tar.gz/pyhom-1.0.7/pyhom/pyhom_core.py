import os
from pathlib import Path
import datetime
import shutil
import logging
import time
import copy
import pickle
import zipfile
import requests
import io as standard_io
import warnings
# To ignore all warnings
warnings.filterwarnings("ignore")
# # To ignore a specific warning
# warnings.filterwarnings("ignore", category=DeprecationWarning)
# # To display warnings as errors
# warnings.filterwarnings("error")
from collections import namedtuple


from ruamel.yaml import YAML
import numpy as np
from skimage import io
from tqdm import tqdm


# RSA
from pyhom.rsa.Build_RVE import RSA_Alg

# Image_Processing
import pyhom.image_processing.Image as ipi
import pyhom.image_processing.Tessellations as ipt
import pyhom.image_processing.Graph_Tools as ipgt

# Full_Field
import pyhom.full_field.FF_Hom as ff
import pyhom.full_field.Cell_Problem as ffcp

# Mean_Field
import pyhom.mean_field.MF_Hom as mf


class Core:
   
    
    def __init__(self):

        self.globalPrm = {}

        # Default
        self.globalPrm['pixels'] = 256 # Number of image pixels.
        self.globalPrm['k0'] = 1 # Matrix conductivity property.
        self.globalPrm['N_MF'] = 100 # Number of points to be calculated for the Mean-Field estimates.

        # To control the data is saved.
        self.globalPrm['saveFigures'] = True
        self.globalPrm['saveData'] = True

        # To control which approaches are used.
        self.globalPrm['showFFApproach'] = True
        self.globalPrm['showMFApproach'] = True
        
        self.globalPrm['labelNumber'] = -1 # In case to be unused

        self.logger = None

        for attr in ["rsaPrm","fullField","meanField"]:
            setattr(self,attr,None)

        self.Collection_setP=namedtuple('Collection_setP',['pixels','k0','gamma','varyParamName','varyParamValue_FF',\
            'varyParamValue_MF','N_MF','rveLabelName','rveImagePath'])
        self.setPrm = self.Collection_setP(* [None] * len(self.Collection_setP._fields))


        self.Collection_inclP=namedtuple('Collection_inclP',['N_incl','c_incl','e_incl','theta_incl',\
            'R_incl_Pxls','a2_incl_Pxls','x_incl_Pxls'])
        self.inclPrm = self.Collection_inclP(* [None] * len(self.Collection_inclP._fields))

    def _find_groups(self,e,theta,Pos=None,Act=None):
        """
        """

        eShape=e.shape[0]
        thetaShape=theta.shape[0]
        if Pos is None: Pos=0
        Act=False
        eGroups={}
        thetaGroups={}

        eSet=np.array([x for x in set(e.flatten())])
        thetaSet=np.array([x for x in set(theta.flatten())])

        eSetShape=eSet.shape[0]
        thetaSetShape=thetaSet.shape[0]

        if eSetShape==1 and thetaSetShape==1:  # eShape==thetaShape is implicit
            Act=True
            return e,theta,Act,Pos
        else:
            if eSetShape!=1:
                for I in range(eSetShape):
                    index=np.argwhere(e==eSet[I])

                    eAux=e[index[:,0],index[:,1],np.newaxis]
                    thetaAux=theta[index[:,0],index[:,1],np.newaxis]
                    eReduced,thetaReduced,Act,Pos=self._find_groups(eAux,thetaAux,Pos)
                    if Act:
                        eGroups[f'{Pos}']=eReduced
                        thetaGroups[f'{Pos}']=thetaReduced
                    else:
                        eGroups.update(eReduced)
                        thetaGroups.update(thetaReduced)
                    Pos+=1

                Act=False
                return eGroups,thetaGroups,Act,Pos-1

            else: #thetaSetShape!=1
                for J in range(thetaSetShape):
                    index=np.argwhere(theta==thetaSet[J])

                    eAux=e[index[:,0],index[:,1],np.newaxis]
                    thetaAux=theta[index[:,0],index[:,1],np.newaxis]
                    eReduced,thetaReduced,Act,Pos=self._find_groups(eAux,thetaAux,Pos)
                    if Act:
                        eGroups[f'{Pos}']=eReduced
                        thetaGroups[f'{Pos}']=thetaReduced
                    else:
                        eGroups.update(eReduced)
                        thetaGroups.update(thetaReduced)
                    Pos+=1

                Act=False
                return eGroups,thetaGroups,Act,Pos-1

    def _find_index(self,e,theta,eGroups,thetaGroups):
        """
        """

        indexGroup={}

        for I in range(len(eGroups)):

            arr1=np.argwhere(eGroups[f'{I}'][0]==e)
            arr2=np.argwhere(thetaGroups[f'{I}'][0]==theta)
            arr1Set=set([tuple(x) for x in arr1])
            arr2Set=set([tuple(x) for x in arr2])
            inters=np.array([x for x in arr1Set & arr2Set])
            indexGroup[f'{I}']=inters

        return indexGroup

    def _update_groups(self,rveImage,vdImage,indexGroups,Iter):

        #---
        rveImageCopy=copy.deepcopy(rveImage)

        for attr in rveImage.__dict__.keys():
            setattr(rveImageCopy,attr,None)

        rveImageCopy.pixels=rveImage.pixels
        rveImageCopy.k0=rveImage.k0
        rveImageCopy.gamma=rveImage.gamma
        rveImageCopy.varyParamName=rveImage.varyParamName
        rveImageCopy.varyParamValue_FF=rveImage.varyParamValue_FF
        rveImageCopy.varyParamValue_MF=rveImage.varyParamValue_MF

        rveImageCopy.N_incl=indexGroups[f'{Iter}'].shape[0]
        rveImageCopy.c_incl=rveImage.c_incl
        rveImageCopy.e_incl=rveImage.e_incl[indexGroups[f'{Iter}'][:,0]]
        rveImageCopy.theta_incl=rveImage.theta_incl[indexGroups[f'{Iter}'][:,0]]
        rveImageCopy.R_incl_Pxls=rveImage.R_incl_Pxls[indexGroups[f'{Iter}'][:,0]]
        rveImageCopy.a2_incl_Pxls=rveImage.a2_incl_Pxls[indexGroups[f'{Iter}'][:,0]]
        rveImageCopy.x_incl_Pxls=rveImage.x_incl_Pxls[indexGroups[f'{Iter}'][:,0]]


        #---
        vdImageCopy=copy.deepcopy(vdImage)

        for attr in rveImage.__dict__.keys():
            setattr(vdImageCopy,attr,None)

        vdImageCopy.pixels=vdImage.pixels
        vdImageCopy.e_cell_VD=vdImage.e_cell_VD[indexGroups[f'{Iter}'][:,0]]
        vdImageCopy.theta_cell_VD=vdImage.theta_cell_VD[indexGroups[f'{Iter}'][:,0]]
        vdImageCopy.R_cell_VD_Pxls=vdImage.R_cell_VD_Pxls[indexGroups[f'{Iter}'][:,0]]
        vdImageCopy.a2_cell_VD_Pxls=vdImage.a2_cell_VD_Pxls[indexGroups[f'{Iter}'][:,0]]
        vdImageCopy.x_cell_VD_Pxls=vdImage.x_cell_VD_Pxls[indexGroups[f'{Iter}'][:,0]]

        return rveImageCopy,vdImageCopy

    def _check_symmetry(self,rveImage,meanField,fullField):
       

        self.logger.info('_check_symmetry')

        symmetry={'Num':True,'MT':True,'IDD':True,'PCW':True}
        N_varyParamValue_FF=rveImage.varyParamValue_FF.shape[1]
        N_varyParamValue_MF=rveImage.varyParamValue_MF.shape[1]

        if rveImage.showFFApproach:
            if not all([np.abs(fullField.keffNum[:,:,i][0,1] - fullField.keffNum[:,:,i][1,0]) <1E-8 for i in range(N_varyParamValue_FF)]):
                symmetry['Num']=False
                self.logger.warning('*** No symmetry is fulfilled in keffNum')

        if rveImage.showMFApproach:
            if not all([np.abs(meanField.keffMt[:,:,i][0,1] - meanField.keffMt[:,:,i][1,0]) <1E-8 for i in range(N_varyParamValue_MF)]):
                symmetry['MT']=False
                self.logger.warning('*** No symmetry is fulfilled in keffMt')

            if not all([np.abs(meanField.keffIdd[:,:,i][0,1] - meanField.keffIdd[:,:,i][1,0]) <1E-8 for i in range(N_varyParamValue_MF)]):
                symmetry['IDD']=False
                self.logger.info('*** No symmetry is fulfilled in keffIdd')


            if not all([np.abs(meanField.keffPcw[:,:,i][0,1] - meanField.keffPcw[:,:,i][1,0]) <1E-8 for i in range(N_varyParamValue_MF)]):
                symmetry['PCW']=False
                self.logger.warning('*** No symmetry is fulfilled in keffPcw')


        return symmetry

    def _ip_rve_image(self):

        # global globalPrm
        # global setPrm
        # global inclPrm
        # global fullField
        # global logger

        # Object definition
        self.logger.info('Object definition: RVE Image')
        rveImage=ipi.RVE_Image(self.globalPrm, self.setPrm, self.inclPrm, ID_Image='rveImage')

        #RVE Image Data
        # Object definition
        self.logger.info('Object definition: RVE Image Data')
        rveImageData=ipi.Image_Processing(rveImage)
        rveImageData.Set_Or_Check_Pxls()

        if not self.globalPrm['meta_image']['value']:
            rveImageData.Region_properties('rveImage')
            rveImageData.Clone_x_incl_Pxls()

        else: 
            rveImageData.Clone_RVE()
            rveImageData.Region_properties('clonedRve')
            rveImageData.Clone_x_incl_Pxls()

        if self.globalPrm['showFFApproach']:
            matPixels = rveImageData.genImageArrayFlipTransp # row-column perspective
            # Convert from uint8 array to float64 array
            matPixels = matPixels.astype(np.float64)
            # Normalize the float64 array
            matPixels /= 255
            assert(matPixels.dtype==np.dtype('float64'))
            self.fullField.matPixels=matPixels

        return rveImage, rveImageData

    def _ip_voronoi_diagram(self,rveImage):

        # global logger

        # Object definition
        self.logger.info('Object definition: Voronoi Diagram')
        VD=ipt.Voronoi_Diagram(rveImage, self.globalPrm['subfolder_vd_image_path'])

        VD.All_Polygons()
        VD.VD_Polygons()
        vdLabelName, vdImagePath = VD.Export_GrayScale_VD()

        return VD, vdLabelName, vdImagePath

    def _ip_vd_image(self,rveImage, VD, vdLabelName, vdImagePath):

        # global logger

        # Object definition
        self.logger.info('Object definition: VD Image')
        vdImage=ipi.VD_Image(rveImage.logger, vdLabelName, vdImagePath, ID_Image='vdImage')

        # VD Image Data
        # Object definition
        self.logger.info('Object definition: VD Image Data')
        vdImageData=ipi.Image_Processing(vdImage)


        vdImageData.Set_Or_Check_Pxls()
        vdImageData.Region_properties("vdImage",rveImage,VD)

        return vdImage, vdImageData

    def _wf_set_parameters(self,Iter=None, m_AT=None):
        

        
        chosenParam = 'gamma' # default
        self.globalPrm['chosenParam'] = chosenParam
        self.logger.info(f'The parameter {chosenParam} is the varying one.')

        
        # Parameters
        k0=self.globalPrm['k0'] 
        N_MF=self.globalPrm['N_MF']
        pixels=self.globalPrm['pixels']  
        N_incl=self.globalPrm['N_incl'] 
        
        
        # Varying parameter
        gamma = np.array([self.globalPrm['gamma']])
        varyParamName='gamma' 
        varyParamValue_FF=gamma 
        varyParamValue_MF=np.linspace(gamma[0,0],gamma[0,-1],N_MF).reshape(1,N_MF) 

        # Fixed parameters
        if self.globalPrm['c_incl']:
            c_incl = np.array([self.globalPrm['c_incl']])
        else:
            c_incl = None

        if self.globalPrm['e_incl']:
            e_incl=np.tile(self.globalPrm['e_incl'], (N_incl ,1)) 
        else:
            e_incl = None


        if self.globalPrm['theta_incl']:
            theta_incl = np.tile(eval(self.globalPrm['theta_incl']), (N_incl ,1))
        else:
            theta_incl = None

        if self.globalPrm['e_cell_RSA']:
            e_cell_RSA = np.tile(self.globalPrm['e_cell_RSA'], (N_incl ,1))
        else: 
            e_cell_RSA = None

        if self.globalPrm['theta_cell_RSA']:
            theta_cell_RSA = np.tile(eval(self.globalPrm['theta_cell_RSA']), (N_incl ,1))
        else:
            theta_cell_RSA = None

        if self.globalPrm['size_factor']:
            size_factor = np.array([self.globalPrm['size_factor']])
        else: 
            size_factor = None
        
        security_factor = self.globalPrm['security_factor']

        # Path to save or reach the microstructure image
        if not self.globalPrm['meta_image']['value']:

            rveLabelName=f'Microstructure_Pxls_{pixels}_N_incl_{N_incl}_c_incl_{c_incl[0,0]}_e_incl_{e_incl[0,0]}_theta_incl_{np.degrees(theta_incl[0,0])}_e_cell_RSA_{e_cell_RSA[0,0]}_theta_cell_RSA_{np.degrees(theta_cell_RSA[0,0])}_size_factor_{size_factor[0,0]}_security_factor_{security_factor}'.replace('.', '_')
            rveImagePath = self.globalPrm['subfolder_img_path'].joinpath(rveLabelName+'.png')
            
            
        else: 
            rveLabelName=self.globalPrm['meta_image']['path'].split('/')[2]
            rveImagePath = self.globalPrm['subfolder_img_path'].joinpath(rveLabelName)

            size_factor=None
            security_factor=None
            
            size_factor=None
            security_factor=None
            

        if self.globalPrm['meta_x_incl']['value']:
            #---
            # Built-in example. If True, the code leverages previously obtained inclusion centers.
            # New centers will be generated by means of the RSA algorithm, otherwise.
            posIncl = np.load(self.globalPrm['dir'].joinpath(self.globalPrm['meta_x_incl']['path']),allow_pickle=True)
            x_incl=posIncl['x_incl']
            for i in range(2):
                x_incl[:,i] = x_incl[:,i] - 0.5 # Positions in the unitary cell [-0.5,0.5] x [-0.5,0.5]
            #---



        # Update collections and attributes
        self.setPrm=self.Collection_setP(pixels,k0,gamma,varyParamName,varyParamValue_FF,varyParamValue_MF,N_MF,rveLabelName,rveImagePath)
        self.inclPrm=self.Collection_inclP(N_incl,c_incl,e_incl,theta_incl,*[None]*3)

        if not self.globalPrm['meta_image']['value']:
            self.rsaPrm.e_cell_RSA=e_cell_RSA
            self.rsaPrm.theta_cell_RSA=theta_cell_RSA
            self.rsaPrm.security_factor=security_factor
            self.rsaPrm.size_factor=size_factor
            try:
                x_incl # x_incl is defined
                self.rsaPrm.x_incl=x_incl
            except NameError:
                pass # x_incl is not defined

    def _wf_rsa(self,Iter=None):
        

        # global globalPrm
        # global setPrm
        # global inclPrm
        # global rsaPrm
        # global fullField

        #setPrm
        pixels=self.setPrm.pixels
        rveLabelName=self.setPrm.rveLabelName
        # inclPrm
        N_incl=self.inclPrm.N_incl
        self.logger.info('_wf_rsa')

        # Check the input parameters for the RSA algorithm
        self.rsaPrm.Check_Input_Parameters_For_RSA(self.globalPrm['dir'],self.inclPrm)

        if self.rsaPrm.x_incl is None:
            # Place centers if you dont have them yet
            print(f"### Refer to {self.globalPrm['output_dir_name']}/RSA_Iter_Figures for monitoring the RSA Algorithm ###")
            self.logger.info(f"### Refer to {self.globalPrm['output_dir_name']}/RSA_Iter_Figures for monitoring the RSA Algorithm ###")
            self.rsaPrm.RSA_Place_Centers(self.globalPrm,self.inclPrm)

        # Duplicate inclusions intersecting the borders
        self.rsaPrm.X_Per_From_X_Incl(self.inclPrm)

        # Determine the remaining RSA attributes
        self.rsaPrm.Determine_Remaining_RSA_Attr(self.globalPrm,self.inclPrm,Iter)

        # Update namedtuple inclPrm
        self.inclPrm=self.inclPrm._replace(x_incl_Pxls=self.rsaPrm.x_tot_Pxls[0:N_incl,:])
        self.inclPrm=self.inclPrm._replace(R_incl_Pxls=self.rsaPrm.R_incl_tot_Pxls[0:N_incl,:])
        self.inclPrm=self.inclPrm._replace(a2_incl_Pxls=self.rsaPrm.a2_incl_tot_Pxls[0:N_incl,:])

        # Mesh and build RVE image
        rveImageArray=self.rsaPrm.Mesh_Elliptic_Inclusions(self.globalPrm['pixels'],0,1) # x-y perspective
        # rveImageArray.dtype -> dtype('float64'). The range of values is from 0 to 1.

        # Convert the image to uint8. The range of values for uint8 is from 0 to 255
        rveImageArray= (rveImageArray * 255).astype(np.uint8)

        #---
        # Save the RVE image.

        if True:
            io.imsave(self.setPrm.rveImagePath, rveImageArray, plugin='imageio') # x-y perspective
            self.logger.info('The RVE image has been saved')
        #---

    def _wf_image_processing(self):
        
        #------------
        # (a) RVE Image
        #------------
        rveImage, rveImageData = self._ip_rve_image()

        #------------
        # (b) Voronoi Diagram
        #------------
        VD, vdLabelName, vdImagePath = self._ip_voronoi_diagram(rveImage)

        #------------
        # (c) VD Image
        #------------
        vdImage, vdImageData = self._ip_vd_image(rveImage, VD, vdLabelName, vdImagePath)

        #------------
        if self.globalPrm['saveFigures']:
            ip_path = self.globalPrm['subfolder_ip_figures_path']
            # RVE Image
            ipgt.Graph.RVE_Figures(self.logger, rveImageData, ip_path)

            # Voronoi Diagram
            ipgt.Graph.Cloned_Rve_And_Vd(self.logger, rveImage,VD, ip_path, Seeds_in_the_Rve=False,RVE_Mark=True,\
                Vd_in_the_RVE=True,Vd_outside_the_RVE=False,show_Incl=True,GrayScale_VD=True)

            # VD Image
            ipgt.Graph.Vd_And_Ellips(self.logger, rveImage,VD,vdImage, ip_path)
            ipgt.Graph.Hist_e_cell_VD(self.logger,vdImage, ip_path)
            ipgt.Graph.Hist_theta_cell_VD(self.logger,vdImage, ip_path)
            ipgt.Graph.ScatterPlot_theta_e(self.logger,rveImage,vdImage, ip_path)
        #------------

        return rveImage,VD,vdImage

    def _wf_full_field(self,tol_FFT = 1e-5,Nit_FFT = 2000 ):
       
        # global setPrm
        # global fullField

        # setPrm
        gamma=self.setPrm.gamma
        k0=self.setPrm.k0
        # fullField
        matPixels=self.fullField.matPixels

        N_gamma=gamma.shape[1]
        k_matrix = k0
        k_inclusion = gamma* k_matrix

        self.logger.info('FFT-based full-field solver')

        u_fin=np.array([], dtype=float)
        Du_fin=np.array([], dtype=float)
        Q_fin=np.array([], dtype=float)
        erru_fin=np.array([], dtype=float)
        keff_fin=np.array([], dtype=float)

        for I in range(N_gamma):
            k = k_matrix + matPixels*(k_inclusion[0,I] - k_matrix)  # Conductivity property for each pixel of the image
            u, Du, Q, erru, keff = ffcp.Compute_P_mu0(k,Nit=Nit_FFT,tol=tol_FFT)
            u_fin=np.append(u_fin,u)
            Du_fin=np.append(Du_fin,Du)
            Q_fin=np.append(Q_fin,Q)
            erru_fin=np.append(erru_fin,erru)
            keff_fin=np.append(keff_fin,keff)

        self.logger.info(f'Number of iterations to reach the tolerance : Nit = {erru.size}')

        keff=np.reshape(keff_fin,[N_gamma,4])

        keffNum = np.zeros([2,2,N_gamma])
        keffNum_EVa=np.zeros([2,2,N_gamma])
        keffNum_EVe=np.zeros([2,2,N_gamma])
        keffNum[0,0,:]=keff[:,0]
        keffNum[0,1,:]=keff[:,1]
        keffNum[1,0,:]=keff[:,2]
        keffNum[1,1,:]=keff[:,3]

        for J in range(N_gamma):
            keffNum_EVa[:,:,J], keffNum_EVe[:,:,J]=mf.Mean_Field_Approaches.keff_EVa_EVe(keffNum[:,:,J], self.logger)

        # Object update
        self.fullField.keffNum=keffNum
        self.fullField.keffNum_EVa=keffNum_EVa
        self.fullField.keffNum_EVe=keffNum_EVe

        # return self.fullField

    def _wf_mean_field(self,rveImage,vdImage, saveFigures, fullField=None):
        

        #global logger
        # global meanField

        # rveImage
        e_incl=rveImage.e_incl
        theta_incl=rveImage.theta_incl

        e_inclGroups={}
        theta_inclGroups={}
        N_Groups=0

        eReduced,thetaReduced,Act,Pos=self._find_groups(e_incl,theta_incl)

        N_Groups=Pos+1
        if Act:
            e_inclGroups[f'{Pos}']=eReduced
            theta_inclGroups[f'{Pos}']=thetaReduced
        else:
            e_inclGroups.update(eReduced)
            theta_inclGroups.update(thetaReduced)


        indexGroups=self._find_index(e_incl,theta_incl,e_inclGroups,theta_inclGroups)

        #---------
        # Standard homogenization
        #---------
        # Object definition
        mfCalc=mf.Mean_Field_Calculations(self.meanField, self.logger)
        mfCalc.All_Calc(rveImage,vdImage)


        symmetry=self._check_symmetry(rveImage,self.meanField,fullField)
        self.meanField.symmetry=symmetry

        #---------
        # Two step homogenization
        #---------
        if N_Groups!=1:

            if saveFigures:
                ipgt.Graph.Hist_numb_grains_orient(self.globalPrm['subfolder_ip_figures_path'],N_Groups,theta_inclGroups)

            self.meanField.twoStep=True
            rveImageGroups={}
            vdImageGroups={}
            meanFieldGroups={}


            for II in range(N_Groups):

                rveImageAux,vdImageAux=self._update_groups(rveImage,vdImage,indexGroups,Iter=II)

                rveImageGroups[f'{II}']=rveImageAux
                vdImageGroups[f'{II}']=vdImageAux

                # Object definition
                meanFieldAux=mf.Mean_Field_Approaches(self.logger)
                meanFieldAux.twoStep=True

                # Object definition
                mfCalcAux=mf.Mean_Field_Calculations(meanFieldAux, self.logger)
                mfCalcAux.All_Calc(rveImageAux,vdImageAux)

                meanFieldGroups[f'{II}']=meanFieldAux

                symmetryAux=self._check_symmetry(rveImageAux,meanFieldAux,fullField)
                meanFieldGroups[f'{II}'].symmetry=symmetryAux


        if N_Groups!=1:
            ssHom=mf.Second_Step_Homogenization(self.logger, self.meanField,meanFieldGroups)
            ssHom.Sec_Step_Calc(rveImage,rveImageGroups)

        # return self.meanField

    def _build_folders(self, output_dir:  str) -> None:

        #----------------------------------
        # Folder structure
        #----------------------------------
        # (1) Folder
        # Date and time for log
        now = datetime.datetime.now()
        log = now.strftime("log%Y%m%d%H%M%S")
        results = "run_" + log

        folder_results_path = output_dir.joinpath(results)

        # Create the folder
        folder_results_path.mkdir(parents=True, exist_ok=True)
        print(f"Folder '{results}' has been created inside results folder.")
        
        #----------------------------------
        # |_(a) Subfolder
        
        img = 'RVE_Image'

        subfolder_img_path  = folder_results_path.joinpath(img)

        # Create the folder
        subfolder_img_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{img}' has been created inside '{results}'.")
        #----------------------------------
        # |_(b) Subfolder
        
        rsa_iter = 'RSA_Iter_Figures'

        subfolder_rsa_iter_path = folder_results_path.joinpath(rsa_iter)

        # Create the folder
        subfolder_rsa_iter_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{rsa_iter}' has been created inside '{results}'.")
        #----------------------------------
        # |_(c) Subfolder
        
        vd_image = 'VD_Image'

        subfolder_vd_image_path = folder_results_path.joinpath(vd_image)

        # Create the folder
        subfolder_vd_image_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{vd_image}' has been created inside '{results}'.")
        #----------------------------------
        # |_(d) Subfolder
        
        ip_figures = 'IP_Figures'

        subfolder_ip_figures_path = folder_results_path.joinpath(ip_figures)

        # Create the folder
        subfolder_ip_figures_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{ip_figures}' has been created inside '{results}'.")
        
        #----------------------------------
        # |_(e) Subfolder
        
        saved_data = 'Saved_Data'

        subfolder_saved_data_path = folder_results_path.joinpath(saved_data)

        # Create the folder
        subfolder_saved_data_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{saved_data}' has been created inside '{results}'.")
        #----------------------------------
        # |_(f) Subfolder
        
        num_comp = 'Numerical_Comparisons'

        subfolder_num_comp_path = folder_results_path.joinpath(num_comp)

        # Create the folder
        subfolder_num_comp_path.mkdir(parents=True, exist_ok=True)
        print(f"Subfolder '{num_comp}' has been created inside '{results}'.")
        
        return folder_results_path, subfolder_img_path, subfolder_rsa_iter_path, subfolder_vd_image_path, subfolder_ip_figures_path, subfolder_saved_data_path, subfolder_num_comp_path

    def get_built_in_dataset(self, labelNumber: str) -> None:
        # The URL to the RAW dataset.zip file on GitHub 
        zip_url = "https://raw.githubusercontent.com/olcruzgonzalez/pyhom/main/pyhom/built-in/dataset.zip"

        cwd = Path(os.getcwd())
        destination_dir = cwd.joinpath("built-in_input")
        # Create the folder
        destination_dir.mkdir(parents=True, exist_ok=True)

        try:
            print(f"Downloading dataset from GitHub...")
            response = requests.get(zip_url)
            response.raise_for_status()

            zip_file_bytes = standard_io.BytesIO(response.content)

            with zipfile.ZipFile(zip_file_bytes, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    if member.startswith(f'labelNumber_{labelNumber}' + '/'):
                        zip_ref.extract(member, destination_dir)

            print(f'### Retrieved files from built-in dataset: labelNumber_{labelNumber} ###')

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the file: {e}")
        except zipfile.BadZipFile:
            print("Error: The downloaded file is not a valid zip file.")

    def input_data(self, output_dir: str, input_file_path:  str) -> None:
        
        self.globalPrm['dir']=Path(os.getcwd())  # Project directory.
        self.globalPrm['output_dir_name'] = output_dir
        output_dir = self.globalPrm['dir'].joinpath(output_dir)
        
        print('### Building necessary folders ... ###')
        self.globalPrm['folder_results_path'], self.globalPrm['subfolder_img_path'],\
              self.globalPrm['subfolder_rsa_iter_path'], self.globalPrm['subfolder_vd_image_path'],\
                self.globalPrm['subfolder_ip_figures_path'],  self.globalPrm['subfolder_saved_data_path'],\
                    self.globalPrm['subfolder_num_comp_path'] = self._build_folders(output_dir)
        print('### See results/run_logID/log.log file for log details ###')

        # -----
        logging.basicConfig(
            format='%(levelname)s: %(filename)s, line %(lineno)d -> %(message)s', filename= self.globalPrm['folder_results_path'].joinpath('log.log'), level=logging.INFO)
        self.globalPrm['logger'] = logging.getLogger(__name__)
        self.logger = self.globalPrm['logger']
        # -----

        self.logger.info("### LOGGER START ###")

        
        #----------------------------------------------
        input_file_path = self.globalPrm['dir'].joinpath(input_file_path)
        yaml = YAML(typ='rt')  
        with open(input_file_path, 'r') as f:
            self.globalPrm.update(yaml.load(f))

        #----------------------------------------------
        # Object definitions
        if not self.globalPrm['meta_image']['value'] : # If true, we do not have a RVE image and we use RSA algorithm to build it.
            self.logger.info('Instance of the class RSA.Build_RVE.RSA_Alg')
            self.rsaPrm=RSA_Alg(self.logger)
        
        

        if self.globalPrm['showFFApproach']: # If true, we perform the calculations based on the FFT based full-field approach.
            self.logger.info('Instance of the class Full_Field.FF_Hom.Full_Field_Approach')
            self.fullField=ff.Full_Field_Approach(self.logger)
       

        if self.globalPrm['showMFApproach']: # If true, we perform the calculations based on the mean-field approaches.
            self.logger.info('Instance of the class Full_Field.FF_Hom.Full_Field_Approach')
            self.meanField=mf.Mean_Field_Approaches(self.logger)
       

        # ----
        # Random seed for reproducibility
        if self.globalPrm['hasReproducibility']['value']:
            np.random.seed(self.globalPrm['hasReproducibility']['seed'])

        #----------------------------------------------
        # Save the YAML content to the file
        path = Path(self.globalPrm['folder_results_path'])
        path.mkdir(parents=True, exist_ok=True)
        path = path.joinpath('input.yaml')
        shutil.copy2(str(input_file_path), str(path))

        # Save image 
        if self.globalPrm['meta_image']['value']:
            shutil.copy(self.globalPrm['meta_image']['path'], self.globalPrm['subfolder_img_path'])

    def run(self):
    
        start_GlobalTime = time.time() # To control the execution time.

        # Total checkpoints (adjust this based on how many updates you expect)
        total_checkpoints = 7

        # Create a tqdm progress bar
        with tqdm(total=total_checkpoints, desc="Progress", unit="checkpoint") as pbar:
        
            #--------------
            #  (i) Workflow stage: Set parameters
            #--------------
            self.logger.info('(i) Set parameters')

            self._wf_set_parameters( )
            pbar.update(1)


            #--------------
            #  (ii) Workflow stage: RSA
            #--------------
            if self.globalPrm['meta_image']['value']:
                
                #  RSA - Does NOT apply
                self.logger.info('(ii) RSA algorithm - Does NOT apply')
        
            else:
                self.logger.info('(ii) RSA algorithm')

                self._wf_rsa( )
            pbar.update(1)


            #--------------
            #  (iii) Workflow stage: Image Processing
            #--------------
            self.logger.info('(iii) Image Processing')

            rveImage,VD,vdImage = self._wf_image_processing( )
            pbar.update(1)

            #--------------
            #  (iv) Workflow stage: Full-Field
            #--------------
            if self.globalPrm['showFFApproach']:
                self.logger.info('(iv) Full-Field')
                self._wf_full_field( )
            pbar.update(1)


            #--------------
            #  (v) Workflow stage: Mean-Field
            #--------------
            if self.globalPrm['showMFApproach']:
                self.logger.info('(v) Mean-Field')
                self._wf_mean_field(rveImage,vdImage,self.globalPrm['saveFigures'],self.fullField)
            pbar.update(1)

            #--------------
            #  Results comparison 
            #--------------
            comparison_path = self.globalPrm['subfolder_num_comp_path']
            if True:
                ipgt.Graph.Appr_Comparison(comparison_path, rveImage,self.meanField,self.fullField,tS_hom=self.meanField.twoStep)

            if self.globalPrm['saveFigures']:
                #-------
                #Image
                ipgt.Graph.ScatterPlot_theta_e(self.logger,rveImage,vdImage,comparison_path,e_cell_PCW=self.meanField.e_cell_PCW,theta_cell_PCW=self.meanField.theta_cell_PCW)

                # gammaIndex=-1
                # gammaValue=setPrm.gamma[0,gammaIndex] # the biggest value of gamma

                # if self.globalPrm['showMFApproach']:
                #     ipgt.Graph.Rve_And_EVe(rveImage,meanField.keffMt_EVe,'Mt',gammaValue,gammaIndex)
                #     ipgt.Graph.Rve_And_EVe(rveImage,meanField.keffIdd_EVe,'Idd',gammaValue,gammaIndex)
                #     ipgt.Graph.Rve_And_EVe(rveImage,meanField.keffPcw_EVe,'Pcw',gammaValue,gammaIndex)
                # if self.globalPrm['showFFApproach']:
                #     ipgt.Graph.Rve_And_EVe(rveImage,fullField.keffNum_EVe,'Num',gammaValue,gammaIndex)
            pbar.update(1)
            #------------

            #-------------
            # Save data
            #-------------
            saved_data_path = self.globalPrm['subfolder_saved_data_path']
            self.logger.info('Save Data')
            
            if self.globalPrm['saveData']: 
                
                try:
                    np.savez(saved_data_path.joinpath('x_incl'), x_incl=self.rsaPrm.x_incl)
                except:
                    np.savez(saved_data_path.joinpath('x_incl'), x_incl=rveImage.x_incl_Pxls/rveImage.pixels)
            
                with open(saved_data_path.joinpath('VD'+'.pkl'), 'wb') as outp:
                    pickle.dump(VD, outp, pickle.HIGHEST_PROTOCOL)
                with open(saved_data_path.joinpath('vdImage'+'.pkl'), 'wb') as outp:
                    pickle.dump(vdImage, outp, pickle.HIGHEST_PROTOCOL)
            pbar.update(1)

        globalTime=time.time() - start_GlobalTime
        print(f'### EXECUTION TIME : {globalTime} seconds ###')
        print(f'### END ###')

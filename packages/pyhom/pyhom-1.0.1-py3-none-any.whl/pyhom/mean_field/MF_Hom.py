
import os
import numpy as np
import sympy as sp
from scipy.linalg import eig
import matplotlib.pyplot as plt
# import logging


class Mean_Field_Approaches:
 

    def __init__(self, LOGGER):
        
        self.LOGGER = LOGGER
        self.twoStep= False

        for attr in ["S_cA", "S_cAP","TensorP_PCW","e_cell_PCW",\
            "theta_cell_PCW", "symmetry","Area_total_per_grains",\
            "keffDil","keffDil_EVa","keffDil_EVe","keffMt","keffMt_EVa","keffMt_EVe",\
            "keffIdd","keffIdd_EVa","keffIdd_EVe","keffPcw","keffPcw_EVa","keffPcw_EVe",\
            "keffIdd_Voigt","keffIdd_Voigt_EVa","keffIdd_Voigt_EVe",\
            "keffIdd_Reuss","keffIdd_Reuss_EVa","keffIdd_Reuss_EVe"]:
            setattr(self,attr,None) # Definition of attributes
        
    
    #----------------------
    @staticmethod
    def P_Cell(e_cell,k0): 
        """VECTORIAL: Hill tensor for elliptical cells"""
        N_incl=e_cell.shape[0]
        P = np.zeros((2,2,N_incl))
        
        P[0,0,:] = e_cell[:,0]/(k0 + k0*e_cell[:,0])
        P[1,1,:] = 1/(k0 + k0*e_cell[:,0])

        return P

    @staticmethod
    def A_Incl(gamma, e_incl):
    
        N_incl=e_incl.shape[0]
        A = np.zeros((2,2,N_incl))
        
        A[0,0,:] = (1 + e_incl[:,0])/(1 + gamma*e_incl[:,0])
        A[1,1,:] = (1 + e_incl[:,0])/(gamma + e_incl[:,0])
        
        return A
    
    @staticmethod
    def Rotate(M,theta):
        
        N_incl=theta.shape[0]
        R = np.zeros((2,2,N_incl))
        M_rot = np.zeros((2,2,N_incl))
        
        R[0,0,:] = np.cos(theta[:,0])
        R[0,1,:] = -np.sin(theta[:,0])
        R[1,0,:] = np.sin(theta[:,0])
        R[1,1,:] = np.cos(theta[:,0])

        M_rot=np.einsum('ijn,jkn,lkn->iln', R, M, R)

        return M_rot
    
    @staticmethod
    def Sum_cAP(N_incl,gamma,c_incl_Ind,e_incl,theta_incl,e_cell_VD,theta_cell_VD,k0): # 
       
        
        # S_cAP_Aux=np.zeros((2,2,N_incl))
        S_cAP=np.zeros((2,2))
        
        TensorP=Mean_Field_Approaches.Rotate(Mean_Field_Approaches.P_Cell(e_cell_VD,k0),theta_cell_VD) 
        TensorA=Mean_Field_Approaches.Rotate(Mean_Field_Approaches.A_Incl(gamma, e_incl),theta_incl) 
        
        S_cAP= np.einsum('n, ijn,jkn->ik', c_incl_Ind, TensorA, TensorP)

        # S_cAP_Aux= np.einsum('n, ijn,jkn->ikn', c_incl_Ind, TensorA, TensorP)
        # S_cAP= np.sum(S_cAP_Aux, axis=2)
      
        return S_cAP

    @staticmethod
    def Sum_cA(N_incl,gamma,c_incl_Ind,e_incl,theta_incl):

        # S_cA_Aux=np.zeros((2,2,N_incl))
        S_cA=np.zeros((2,2))

        TensorA=Mean_Field_Approaches.Rotate(Mean_Field_Approaches.A_Incl(gamma, e_incl),theta_incl) 
        
        S_cA= np.einsum('n, ijn->ij', c_incl_Ind, TensorA)
        
        # S_cA_Aux= np.einsum('n, ijn->ijn', c_incl_Ind, TensorA)
        # S_cA= np.sum(S_cA_Aux, axis=2)

        return S_cA
    
    @staticmethod
    def P_TensorMean(e_cell_VD,theta_cell_VD,k0,c_incl_Ind,c_incl): # 
        
        N_incl=e_cell_VD.shape[0]
        # TensorP_PCW_Aux=np.zeros((2,2,N_incl))
        TensorP_PCW=np.zeros((2,2))

        TensorP=Mean_Field_Approaches.Rotate(Mean_Field_Approaches.P_Cell(e_cell_VD,k0),theta_cell_VD)
        
        TensorP_PCW=np.einsum('n, ijn -> ij',c_incl_Ind,TensorP)/c_incl
        
        # TensorP_PCW_Aux=np.einsum('n, ijn -> ijn',c_incl_Ind,TensorP)
        # TensorP_PCW=np.sum(TensorP_PCW_Aux,axis=2)/c_incl
        
        return TensorP_PCW
    
    #----------------------   
    @staticmethod
    def Dil(gamma, S_cA):
        I = np.identity(2)
        keffDil = I + (gamma - 1)*S_cA
        return keffDil
    
    @staticmethod
    def MT(gamma, c_incl, S_cA):
        I = np.identity(2)
        keffMt = I + (gamma - 1) * S_cA @ np.linalg.inv( (1-c_incl) * I + S_cA)
        return keffMt
    
    @staticmethod
    def IDD(gamma, k0, S_cAP,S_cA):
        """
        """
        I = np.identity(2)        
        keffIdd= I + (gamma - 1) * np.linalg.inv( I - k0 * (gamma-1) * S_cAP ) @ S_cA
        return keffIdd
    
    @staticmethod
    def PCW(gamma, k0, S_cA, TensorP_PCW):
        """ 
        """
        I = np.identity(2)          
        keffPcw= I + (gamma-1) * S_cA @ np.linalg.inv( I- k0 * (gamma-1) * TensorP_PCW @ S_cA)
        return keffPcw
   
     
    #----------------------   
    @staticmethod
    def keff_EVa_EVe(keff, logger):
        
        logger.info('keff_EVa_EVe')

        EVa_Aux,EVe_Aux=eig(keff) #eigenvalues and normalized eigenvectors

        EVa_ArgSort=np.argsort(EVa_Aux) # ascending order
        k_I=EVa_Aux[EVa_ArgSort[1]] #k_I=max(k_I, k_II)
        k_II=EVa_Aux[EVa_ArgSort[0]]
        EVa=np.array([k_I,k_II])

        EVe=np.zeros([2,2])
        EVe[:,0]=EVe_Aux[:,EVa_ArgSort[1]]
        EVe[:,1]=EVe_Aux[:,EVa_ArgSort[0]]
        
        try:
            assert(np.all(np.imag(EVa))==0)
        except:
            logger.warning('Warning in keff_EVa_EVe. Note that if e_incl=1.0, the orientation of theta_incl has to be 0 degrees.')

        keff_EVa=np.diag(np.real(EVa))
        keff_EVe=EVe
        return keff_EVa,keff_EVe

    @staticmethod
    def Cell_Props_From_TensorP_PCW(TensorP_PCW,k0): 
        """Determine the properties e_cell_PCW and theta_cell_PCW from the Hill tensor of the PCW approach"""

        # logger.info('Cell_Props_From_TensorP_PCW')
        
        e_cell,theta_cell=sp.symbols('e_cell, theta_cell')
        
        R=np.array([
            [sp.cos(theta_cell),sp.sin(theta_cell)],
            [sp.sin(theta_cell),sp.cos(theta_cell)]
            ])

        P=np.array([
            [e_cell/(k0*(1 + e_cell)), 0],
            [0, 1/(k0*(1 + e_cell))]
            ])

        TensorP= R @ P @ R.T

        eq1=sp.Eq(TensorP[0,0]-TensorP_PCW[0,0],0)
        eq2=sp.Eq(TensorP[1,1]-TensorP_PCW[1,1],0)
        eq3=sp.Eq(TensorP[0,1]-TensorP_PCW[0,1],0)

        results = sp.nsolve([eq1,eq2,eq3],(e_cell,theta_cell),(1,0))
        
        e_cell_PCW=results[0,0]
        theta_cell_PCW=results[1,0]
    
        return e_cell_PCW, theta_cell_PCW
    

   
class Mean_Field_Calculations:

    def __init__(self, meanField,logger):
        self.logger = logger
        self.meanField = meanField
     
    
    def All_Calc(self,rveImage,vdImage):


        self.logger.info('All_Calc')

        #rveImage
        N_incl=rveImage.N_incl
        k0=rveImage.k0
        pixels=rveImage.pixels
        varyParamName=rveImage.varyParamName
        varyParamValue_MF=rveImage.varyParamValue_MF
        if varyParamName=='c_incl':
            c_incl=varyParamValue_MF
        else:
            c_incl= rveImage.c_incl # OJO Este hay que cambiarlo
        N_varyParamValue_MF=varyParamValue_MF.shape[1]

        #vdImage
        theta_cell_VD=vdImage.theta_cell_VD
        e_cell_VD=vdImage.e_cell_VD

        # Initializations
        c_incl_Ind=np.zeros([N_incl,N_varyParamValue_MF])
        Area_incl=np.zeros([N_varyParamValue_MF])
        Area_total=np.zeros([N_varyParamValue_MF])

        TensorP_PCW=np.zeros([2,2])
        S_cAP=np.zeros([2,2,N_varyParamValue_MF])
        S_cA=np.zeros([2,2,N_varyParamValue_MF])

        keffDil=np.zeros([2,2,N_varyParamValue_MF])
        keffMt=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd =np.zeros([2,2,N_varyParamValue_MF])
        keffPcw =np.zeros([2,2,N_varyParamValue_MF])
        #---
        keffDil_EVa=np.zeros([2,2,N_varyParamValue_MF])
        keffMt_EVa=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_EVa =np.zeros([2,2,N_varyParamValue_MF])
        keffPcw_EVa =np.zeros([2,2,N_varyParamValue_MF])

        keffDil_EVe=np.zeros([2,2,N_varyParamValue_MF])
        keffMt_EVe=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_EVe =np.zeros([2,2,N_varyParamValue_MF])
        keffPcw_EVe =np.zeros([2,2,N_varyParamValue_MF])
        
        if varyParamName=='gamma': # Standard varying parameter
            
            if self.meanField.twoStep==True:

                R_incl_Pxls = rveImage.R_incl_Pxls
                a2_incl_Pxls = rveImage.a2_incl_Pxls

            else:

                R_incl_Pxls = np.tile(rveImage.R_incl_Pxls, (1,N_varyParamValue_MF))
                a2_incl_Pxls = np.tile(rveImage.a2_incl_Pxls, (1,N_varyParamValue_MF))  
        
        else:
            gamma=rveImage.gamma

        if varyParamName=='c_incl':
            
            # 'Varying_Parameters':
            R_incl_Pxls = rveImage.R_incl_Pxls
            a2_incl_Pxls = rveImage.a2_incl_Pxls
        
        else:
            c_incl=rveImage.c_incl

        if varyParamName=='e_incl':

            # 'Varying_Parameters':
            R_incl_Pxls = rveImage.R_incl_Pxls
            a2_incl_Pxls = rveImage.a2_incl_Pxls
        
        else:
            e_incl=rveImage.e_incl 
            
        if varyParamName=='theta_incl':
            
            # 'Varying_Parameters':
            R_incl_Pxls = rveImage.R_incl_Pxls
            a2_incl_Pxls = rveImage.a2_incl_Pxls
        
        else:
            theta_incl=rveImage.theta_incl 

        #---------------
        #  Calculation of c_incl_Ind
        Area_incl=np.sum(R_incl_Pxls*a2_incl_Pxls*np.pi,axis=0)
        Area_total=Area_incl/c_incl
        c_incl_Ind=R_incl_Pxls*a2_incl_Pxls*np.pi/Area_total
        
        if varyParamName=='c_incl':
            if np.all(np.abs(np.sum(c_incl_Ind,axis=0)-varyParamValue_MF)<1e-8):
                pass
            else:
                self.logger.error(' Check calculation of c_incl_Ind')
                os._exit(0) 

            self.logger.info('Calculation of c_incl_Ind') 
        else:
            if np.all(np.abs(np.sum(c_incl_Ind,axis=0)-c_incl)<1e-8):
                self.logger.info('Calculation of c_incl_Ind')
            else:
                self.logger.error(' Check calculation of c_incl_Ind')
                os._exit(0) 
        #---------------

        if not varyParamName=='c_incl':
            TensorP_PCW=self.meanField.P_TensorMean(e_cell_VD,theta_cell_VD,k0,c_incl_Ind[:,0],c_incl)
        else:
            pass
        
        for JJ in range(N_varyParamValue_MF):
            if varyParamName=='gamma':
                S_cAP[:,:,JJ]=self.meanField.Sum_cAP(N_incl,varyParamValue_MF[0,JJ],c_incl_Ind[:,0],e_incl,theta_incl,e_cell_VD,theta_cell_VD,k0)
                S_cA[:,:,JJ]=self.meanField.Sum_cA(N_incl,varyParamValue_MF[0,JJ],c_incl_Ind[:,0],e_incl,theta_incl)

                keffDil[:,:,JJ]=self.meanField.Dil(varyParamValue_MF[0,JJ], S_cA[:,:,JJ])
                keffMt[:,:,JJ]=self.meanField.MT(varyParamValue_MF[0,JJ], c_incl, S_cA[:,:,JJ])
                keffIdd[:,:,JJ] =self.meanField.IDD(varyParamValue_MF[0,JJ],k0,S_cAP[:,:,JJ], S_cA[:,:,JJ])
                keffPcw[:,:,JJ] =self.meanField.PCW(varyParamValue_MF[0,JJ],k0,S_cA[:,:,JJ],TensorP_PCW)
            
            elif varyParamName=='c_incl':
                S_cAP[:,:,JJ]=self.meanField.Sum_cAP(N_incl,gamma,c_incl_Ind[:,JJ],e_incl,theta_incl,e_cell_VD,theta_cell_VD,k0)
                S_cA[:,:,JJ]=self.meanField.Sum_cA(N_incl,gamma,c_incl_Ind[:,JJ],e_incl,theta_incl)

                keffDil[:,:,JJ]=self.meanField.Dil(gamma, S_cA[:,:,JJ])
                keffMt[:,:,JJ]=self.meanField.MT(gamma, c_incl[0,JJ], S_cA[:,:,JJ])
                keffIdd[:,:,JJ] =self.meanField.IDD(gamma,k0,S_cAP[:,:,JJ], S_cA[:,:,JJ])
                #keffPcw[:,:,JJ] =self.meanField.PCW(gamma,k0,S_cA[:,:,JJ],TensorP_PCW)
            
            elif varyParamName=='e_incl':
                S_cAP[:,:,JJ]=self.meanField.Sum_cAP(N_incl,gamma,c_incl_Ind[:,0],varyParamValue_MF[:,JJ,np.newaxis],theta_incl,e_cell_VD,theta_cell_VD,k0)
                S_cA[:,:,JJ]=self.meanField.Sum_cA(N_incl,gamma,c_incl_Ind[:,0],varyParamValue_MF[:,JJ,np.newaxis],theta_incl)

                keffDil[:,:,JJ]=self.meanField.Dil(gamma, S_cA[:,:,JJ])
                keffMt[:,:,JJ]=self.meanField.MT(gamma, c_incl, S_cA[:,:,JJ])
                keffIdd[:,:,JJ] =self.meanField.IDD(gamma,k0,S_cAP[:,:,JJ], S_cA[:,:,JJ])
                keffPcw[:,:,JJ] =self.meanField.PCW(gamma,k0,S_cA[:,:,JJ],TensorP_PCW)
            
            else: #'theta_incl'
                S_cAP[:,:,JJ]=self.meanField.Sum_cAP(N_incl,gamma,c_incl_Ind[:,0],e_incl,varyParamValue_MF[:,JJ,np.newaxis],e_cell_VD,theta_cell_VD,k0)
                S_cA[:,:,JJ]=self.meanField.Sum_cA(N_incl,gamma,c_incl_Ind[:,0],e_incl,varyParamValue_MF[:,JJ,np.newaxis])

                keffDil[:,:,JJ]=self.meanField.Dil(gamma, S_cA[:,:,JJ])
                keffMt[:,:,JJ]=self.meanField.MT(gamma, c_incl, S_cA[:,:,JJ])
                keffIdd[:,:,JJ] =self.meanField.IDD(gamma,k0,S_cAP[:,:,JJ], S_cA[:,:,JJ])
                keffPcw[:,:,JJ] =self.meanField.PCW(gamma,k0,S_cA[:,:,JJ],TensorP_PCW)
            
            keffDil_EVa[:,:,JJ], keffDil_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffDil[:,:,JJ], self.logger)
            keffMt_EVa[:,:,JJ], keffMt_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffMt[:,:,JJ],self.logger)
            keffIdd_EVa[:,:,JJ], keffIdd_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffIdd[:,:,JJ],self.logger)
            keffPcw_EVa[:,:,JJ], keffPcw_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffPcw[:,:,JJ],self.logger)
        
        if not varyParamName=='c_incl':
            if not self.meanField.twoStep:
            #---   
                # Cell properties from the Hill tensor in PCW
                e_cell_PCW,theta_cell_PCW=Mean_Field_Approaches.Cell_Props_From_TensorP_PCW(TensorP_PCW,k0)
                e_cell_PCW=np.array([[e_cell_PCW]])
                theta_cell_PCW=np.array([[theta_cell_PCW]])

                self.meanField.e_cell_PCW=e_cell_PCW
                self.meanField.theta_cell_PCW=theta_cell_PCW
        
        #---
        # Update parameters
        rveImage.R_incl_Pxls=R_incl_Pxls
        rveImage.a2_incl_Pxls=a2_incl_Pxls
        rveImage.c_incl_Ind=c_incl_Ind

        self.meanField.Area_total_per_grains=Area_total

        self.meanField.TensorP_PCW=TensorP_PCW
        self.meanField.S_cAP=S_cAP
        self.meanField.S_cA=S_cA

        self.meanField.keffDil=keffDil
        self.meanField.keffMt=keffMt
        self.meanField.keffIdd =keffIdd
        self.meanField.keffPcw =keffPcw
        
        self.meanField.keffDil_EVa=keffDil_EVa
        self.meanField.keffMt_EVa=keffMt_EVa
        self.meanField.keffIdd_EVa =keffIdd_EVa
        self.meanField.keffPcw_EVa =keffPcw_EVa

        self.meanField.keffDil_EVe=keffDil_EVe
        self.meanField.keffMt_EVe=keffMt_EVe
        self.meanField.keffIdd_EVe =keffIdd_EVe
        self.meanField.keffPcw_EVe =keffPcw_EVe
        #---
        


class Second_Step_Homogenization:

    def __init__(self, logger, meanField, meanFieldGroups):
        
        self.logger = logger
        self.meanField = meanField
        self.meanFieldGroups=meanFieldGroups
      
    
    
    @staticmethod
    def Voigt(N_Groups,kProps, c_grains):
        """Homogenization of multi-phase grains. Voigt method is used in a two-step homogenization procedure.""" 
        keffVoigt=np.zeros((2,2))
        for II in range(N_Groups):
            keffVoigt+=kProps[:,:,II]*c_grains[II]

        return keffVoigt

    @staticmethod
    def Reuss(N_Groups,kProps, c_grains):
        """Homogenization of multi-phase grains. Reuss method is used in a two-step homogenization procedure.""" 
        
        keffReuss=np.zeros((2,2))
        for II in range(N_Groups):
            keffReuss+=c_grains[II]*np.linalg.inv(kProps[:,:,II])

        keffReuss=np.linalg.inv(keffReuss)

        return keffReuss
    
    
    def Sec_Step_Calc(self,rveImage,rveImageGroups):
      
        self.logger.info('All_Calc') 
        
        # rveImage
        pixels=rveImage.pixels
        c_incl=rveImage.c_incl
        varyParamName=rveImage.varyParamName
        varyParamValue_MF=rveImage.varyParamValue_MF
        
        N_varyParamValue_MF=varyParamValue_MF.shape[1]

        N_Groups=len(self.meanFieldGroups)
        N_incl_per_group=np.array([rveImageGroups[f'{X}'].N_incl for X in range(N_Groups)])

        kProps=np.zeros([2,2,N_Groups,N_varyParamValue_MF])
        c_grains=np.zeros([N_Groups,N_varyParamValue_MF])
        Area_total_per_grains=np.zeros([N_Groups,N_varyParamValue_MF])

        keffIdd_Voigt=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_Reuss=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_Voigt_EVa=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_Reuss_EVa=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_Voigt_EVe=np.zeros([2,2,N_varyParamValue_MF])
        keffIdd_Reuss_EVe=np.zeros([2,2,N_varyParamValue_MF])

        for II in range(N_Groups):
            kProps[:,:,II,:]=self.meanFieldGroups[f'{II}'].keffIdd
            Area_total_per_grains[II,:]=self.meanFieldGroups[f'{II}'].Area_total_per_grains
        
        # # Determine c_grains
        # Area_incl_per_grains=np.zeros([N_Groups,N_varyParamValue_MF])
        # Area_total_per_grains=np.zeros([N_Groups,N_varyParamValue_MF])

        # for KK in range(N_Groups):
        #     Aux=0
        #     for MM in range(N_incl_per_group[KK]):
        #         Aux+=rveImage.R_incl_Pxls[MM,:]*rveImage.a2_incl_Pxls[MM,:]*np.pi
            
        #     Area_incl_per_grains[KK,:]=Aux
        #     Area_total_per_grains[KK,:]=Aux/c_incl

        
        for JJ in range(N_varyParamValue_MF):
            c_grains[:,JJ]=Area_total_per_grains[:,JJ]/pixels**2
            if varyParamName=='gamma':
                keffIdd_Voigt[:,:,JJ]=Second_Step_Homogenization.Voigt(N_Groups,kProps[:,:,:,JJ], c_grains[:,JJ])
                keffIdd_Reuss[:,:,JJ]=Second_Step_Homogenization.Reuss(N_Groups,kProps[:,:,:,JJ], c_grains[:,JJ])
        
            keffIdd_Voigt_EVa[:,:,JJ], keffIdd_Voigt_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffIdd_Voigt[:,:,JJ],self.logger)
            keffIdd_Reuss_EVa[:,:,JJ], keffIdd_Reuss_EVe[:,:,JJ]=Mean_Field_Approaches.keff_EVa_EVe(keffIdd_Reuss[:,:,JJ],self.logger)



        self.meanField.keffIdd_Voigt=keffIdd_Voigt
        self.meanField.keffIdd_Reuss=keffIdd_Reuss
        self.meanField.keffIdd_Voigt_EVa=keffIdd_Voigt_EVa
        self.meanField.keffIdd_Reuss_EVa=keffIdd_Reuss_EVa
        self.meanField.keffIdd_Voigt_EVe=keffIdd_Voigt_EVe
        self.meanField.keffIdd_Reuss_EVe=keffIdd_Reuss_EVe




    










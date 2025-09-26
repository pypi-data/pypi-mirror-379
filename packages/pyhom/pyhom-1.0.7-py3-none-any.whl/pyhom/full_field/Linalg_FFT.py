# -*- coding: utf-8 -*-
"""Linalg_FFT
Some functions of linear algebra and definition of wavenumber arrays

Contains:
   
    - Wavenumbers : main function, returns arrays of wavenumbers for computations
                    in the Fourier space
    - vT : vector field . tensor field (contraction on the first tensorial index)                    
    - Grad_Fourier : gradient of a tensor field in Fourier space (ik (x) T)    

@author: R. Cornaggia
"""


import numpy as np
import matplotlib.pyplot as plt
import logging


logger = logging.getLogger(__name__)



# Vectors for wavenumbers
def Wavenumbers(N,plot=False):
    """ Computes 2D wavenumbers associated with a Fourier discretisation 
    of a NxN regular square grid
    
    Inputs:
        N : size of the grid
        plot : to plot the wavenumbers (optional, default = False)
        
    Outputs:
        k : 1D-array of wavenumbers
        kv : 2D-array of wavevectors (reciprocal grid)
        kv2 : 2D-array of wavevector norms |k|^2
        ikv2 : 2D array of inverses 1/|k|^2 (and ikv2=0 for k=0)
        K : 2D array of "Green" vector k/|k|^2 (and K=0 for k=0)
    """
    
    logger.info('Wavenumbers')

    k = 2*np.pi*np.fft.fftfreq(N,1/N) # discrete values in Fourier space
                                      # Multiplication by 2 pi for differentiation
    kv = np.zeros((2,N,N))  # wavevector k
    kv2 = np.zeros((N,N))   # norm |k|^2
    ikv2 = np.zeros((N,N))  # inverse 1/|k|^2 (and =0 for k=0)
    K = np.zeros((2,N,N))   # Green vector k/|k|^2 (and =0 for k=0)
    
    for i1 in range(N):
        for i2 in range(N):
            kv[0,i1,i2] = k[i1] 
            kv[1,i1,i2] = k[i2] 
            nk = (k[i1]**2 + k[i2]**2)
            kv2[i1,i2] = nk
            if nk == 0:
                ikv2[i1,i2] = 0
                K[0,0,0] = 0.
                K[1,0,0] = 0.
            else:    
                ikv2[i1,i2] = 1. / nk
                K[0,i1,i2] = k[i1] / nk 
                K[1,i1,i2] = k[i2] / nk 
                
    #Plot wavenumbers                
    if plot:            
        plt.figure(plot,figsize=(10,8),clear=True)
        plt.subplot(221)
        plt.imshow(kv[0,:,:])
        plt.colorbar()
        plt.title('Wavevector component k_1')
        plt.subplot(222)
        plt.imshow(kv[1,:,:])
        plt.colorbar()
        plt.title('Wavevector component k_2')
        plt.subplot(223)
        plt.imshow(K[0,:,:])
        plt.colorbar()
        plt.title('Green vector in Fourier K_1')
        plt.subplot(224)
        plt.imshow(K[1,:,:])
        plt.colorbar()
        plt.title('Green vector in Fourier K_2')
        
    return k, kv, kv2, ikv2, K        
    
# Multiplication vector x tensor 
def vT(v,T):
    """ Vector-tensor scalar product on 2D grids : returns the product
    S_jk... (x,y) = v_i (x,y) T_ikj... (x,y)
    
    Typically used to compute divergence in Fourier domain:
        F(div Du) = ik . Duh        
    
    Inputs:
        v : vector (2xNxN array)
        T : tensor (2x ... xNxN array)
    Output:
        S : tensor (... xNxN array)
    """        
    
    logger.info('vT')

    shape = T.shape
    order = len(shape) - 2 #order of the tensor T
    vT = np.zeros(shape[1:],dtype=complex)
    
    if order == 1:
        vT[:,:] = v[0,:,:]*T[0,:,:] + v[1,:,:]*T[1,:,:]
    elif order == 2: #May be a pseudo stress corresponding to symmetrized cell solutions
        NbComp = shape[1]
        for i in range(NbComp):
            vT[i,:,:] = v[0,:,:]*T[0,i,:,:] + v[1,:,:]*T[1,i,:,:]
    elif order == 3:
        for i in range(2):
            for j in range(2):
                vT[i,j,:,:] = v[0,:,:]*T[0,i,j,:,:] + v[1,:,:]*T[1,i,j,:,:]
    elif order == 4:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    vT[i,j,k,:,:] = v[0,:,:]*T[0,i,j,k,:,:] + v[1,:,:]*T[1,i,j,k,:,:]
    return vT
            
# Grad_Fourier and Div_Fourier
def Grad_Fourier(u,kv):
    """ Gradient of a tensor field in Fourier space
    F(grad V) = ik x Vh 
    (differentiation on first index)
    Inputs:
        u : tensor field (...xNxN array) of order 0 to 3
        kv : wavenumbers (2xNxN array, see function Wavenumbers)
    Output:
        Gu : tensor field (2x...xNxN array)
    """
    
    logger.info('Grad_Fourier')

    N = u.shape[-1]
    order = len(u.shape) - 2
    
    if order == 0:
        Gu = 1j*kv*u
        
    elif order == 1: # includes vectors and "pseudo-vector" of symmetrized tensors
        NbComp = u.shape[0]
        Gu = np.zeros((2,NbComp,N,N),dtype=complex)
        for i in range(2):
            for j in range(NbComp):
                Gu[i,j,:,:] = 1j*kv[i,:,:]*u[j,:,:] 
                
    elif order == 2:
        Gu = np.zeros((2,2,2,N,N),dtype=complex)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    Gu[i,j,k,:,:] = 1j*kv[i,:,:]*u[j,k,:,:] 
                    
    elif order == 3:
        Gu = np.zeros((2,2,2,2,N,N),dtype=complex)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        Gu[i,j,k,l,:,:] = 1j*kv[i,:,:]*u[j,k,l,:,:]                     
        
    return Gu    


# -*- coding: utf-8 -*-
"""
@author R. Cornaggia
@date 10/2018   
"""

import numpy as np
import logging

import pyhom.full_field.Linalg_FFT as fflin


logger = logging.getLogger(__name__)




# Main function to compute an arbitrary cell problem
def cell_problem(mu,muc,P0,S0,F,Nit=100,tol=1e-8):
    """ 
    Look for the (tensor-valued) cell solution P satisfying
        div (S0 + mu * grad(P)) + F = 0 in Y (unit cell)
        P has zero mean and is Y-periodic   
        
    using the FFT-based algorithm by Moulinec and Suquet (1998).       
    
    Inputs: 
        - mu : shear modulus, (N,N) array 
        - muc : reference shear modulus, usually (min(mu) + max(mu))/2
        - P0 : initial guess, (...,N,N) array, usually zero
        - S0 : prestress, (2,...,N,N) array
        - F : surfacic force, (...,N,N) array
        - Nit : maximum number of iterations (default: 100)
        - tol : tolerance on residual relative error to stop iterations
                (default: 1e-8)
        
    Outputs:
        - P :  final solution
        - S = S0 + mu grad(P), associated stress
        - err : values of the error criterion
    """
    

    logger.info('cell_problem')

    N = mu.shape[0]
    k, kv, kv2, ikv2, K = fflin.Wavenumbers(N)
    
    err = np.zeros(Nit)
    Ph = np.fft.fft2(P0)
    Sh = np.fft.fft2(S0)
    Fh = np.fft.fft2(F)
    
    def mynorm(v):
        return np.sqrt(np.sum(np.abs(v)**2))
    
    for n in range(Nit):
        # Lippman-Schwinger resolution in Fourier domain (in P)
        GPh = (1j * fflin.vT(K,Sh) + Fh * ikv2) / muc
        Ph = Ph + GPh
    
        # Grad(P) in Fourier domain, and back to real domain
        DPh = fflin.Grad_Fourier(Ph,kv)
        DP = np.fft.ifft2(DPh)
    
        # Stress computation in real domain, then Fourier transform
        S = S0 + DP * mu
        Sh = np.fft.fft2(S)
        
        # Error computation |Pn - Pn+1|_L2 / |Pn+1|_L2
        err[n] = mynorm(GPh)/ mynorm(Ph)
        if err[n] < tol: break        
    
    # Final inverse Fourier transform to retrieve P    
    P = np.fft.ifft2(Ph)  
    
    # Returns only the real parts : fields are real
    return P.real, S.real, err[0:n+1]


# Function to compute P, its gradient and mu0
def Compute_P_mu0(mu,Nit=100,tol=1e-8):
    """ 
    Solves the cell problem for antiplane elasticity
    for a square unit cell, using the FFT-based algorithm by Moulinec 
    and Suquet (1998)
    
    Inputs: 
        - mu : shear modulus (NxN array, intervenes in div(mu grad u))
        - Nit : number of iterations for fixed point method (defaut = 100)
        - tol : tolerance on residual relative error to stop iterations
                (default: 1e-8)
        
    Outputs:        
        - P : cell solutions P
        - DP : gradient of P
        - SP : cell stresses S = mu(Id + DP)
        - errP : criterion for the fixed points iterations
        - mu0 : homogenized coefficient mu_0
    """
    
    logger.info('Compute_P_mu0')

    N = mu.shape[0] # size of the grid : NxN
    muc = (np.min(mu) + np.max(mu))/2 # Reference medium
    NitP = Nit
        
    # First cell problem : P 
    P0 = np.zeros((2,N,N))
    SP0 = np.einsum('ij,kl -> ijkl', np.eye(2), mu) # mu Id
    FP = np.zeros((2,N,N))
    
    P, SP, errP = cell_problem(mu,muc,P0,SP0,FP,NitP,tol) 

    # Grad(P)    
    muId = np.einsum('ij,kl->ijkl',np.eye(2),mu) # mu * Id en notation 3
    DP = (SP - muId)/mu
    
    # 0th-order coefficients    
    mu_0 = np.mean(SP,(-2,-1))
    
    return P, DP, SP, errP, mu_0



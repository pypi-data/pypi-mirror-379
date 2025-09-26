
import os
import sympy as sp
import numpy as np


import pyhom.image_processing.Ellipses_Builder as ipeb
import pyhom.image_processing.Graph_Tools  as ipgt


class RSA_Alg:

    instance = [] # To access an externally created instance from inside the class

    def __init__(self, logger):

        self.__class__.instance.append(self) # To access an externally created instance from inside the class

        self.logger = logger
        for attr in ["e_incl_per","e_incl_tot","e_cell_RSA","e_cell_RSA_per","e_cell_RSA_tot",\
                    "theta_incl_per","theta_incl_tot","theta_cell_RSA","theta_cell_RSA_per","theta_cell_RSA_tot",\
                    "R_incl","R_incl_per","R_incl_tot","R_incl_tot_Pxls","R_cell_RSA","R_cell_RSA_per","R_cell_RSA_tot","R_cell_RSA_Pxls","R_cell_RSA_tot_Pxls",\
                    "a2_incl","a2_incl_per","a2_incl_tot","a2_incl_tot_Pxls","a2_cell_RSA","a2_cell_RSA_per","a2_cell_RSA_tot","a2_cell_RSA_Pxls","a2_cell_RSA_tot_Pxls",\
                    "N_incl_tot","x_incl","x_per","x_tot","x_tot_Pxls","security_factor","size_factor","index_Dupl_Incl"]:
            setattr(self,attr,None) # Definition of attributes

        """Attributes
            e_incl_per (array): Aspect ratio of duplicated inclusions outside the square RVE
            e_incl_tot (array): Aspect ratio of all inclusions, i.e. inside or outside the square RVE
            e_cell_RSA (float array): Aspect ratio of the RSA cells.
            e_cell_RSA_per (array): Aspect ratio of duplicated RSA cells outside the square RVE
            e_cell_RSA_tot (array): Aspect ratio of all RSA cells, i.e. inside or outside the square RVE
            theta_incl_per (array): Counter clock-wise rotation of duplicated inclusions outside the square RVE
            theta_incl_tot (array): Counter clock-wise rotation of all inclusions, i.e. inside or outside the square RVE
            theta_cell_RSA (float array): Counter clock-wise orientation of the RSA cells.
            theta_cell_RSA_per (array): Counter clock-wise rotation of duplicated RSA cells outside the square RVE
            theta_cell_RSA_tot (array): Counter clock-wise rotation of all RSA cells, i.e. inside or outside the square RVE
            R_incl_per (array): Major semi-axis of duplicated inclusions outside the square RVE
            R_incl_tot (array): Major semi-axis of all inclusions, i.e. inside or outside the square RVE
            R_cell_RSA (float array): Major semi-axis of the RSA cells.
            R_cell_RSA_Pxls
            R_cell_RSA_per (array): Major semi-axis of duplicated RSA cells outside the square RVE.
            R_cell_RSA_tot (array): Major semi-axis of all RSA cells, i.e. inside or outside the square RVE
            R_incl_tot_Pxls
            R_cell_RSA_tot_Pxls
            R_incl (float array): Major semi-axis of the inclusions inside the unitary RVE (see (*)).
            a2_cell_RSA (float array): Minor semi-axis of the RSA cells.
            a2_cell_RSA_Pxls
            a2_incl_per (array): Minor semi-axis of duplicated inclusions outside the square RVE
            a2_incl_tot (array): Minor semi-axis of all inclusions, i.e. inside or outside the square RVE
            a2_cell_RSA_per (array): Minor semi-axis of duplicated RSA cells outside the square RVE
            a2_cell_RSA_tot (array): Minor semi-axis of all RSA cell, i.e. inside or outside the square RVE
            a2_incl_tot_Pxls
            a2_cell_RSA_tot_Pxls
            a2_incl (float array): Minor semi-axis of the inclusions inside the unitary RVE.
            N_incl_tot (int): Number of inclusions inside the square RVE + the number of duplicate inclusions outside the square RVE
            x_incl (float array): Center point of the inclusions inside the unitary RVE.
            x_per (array): Center point of duplicated inclusions outside the square RVE
            x_tot (array): Center point of all inclusions,i.e. inside or outside the square RVE
            x_tot_Pxls
            security_factor (float): Sets a safety threshold for the intersection of inclusions
            based on the major semi-axis of them.
            size_factor (float array): Represents the ratio between the major semi-axis of the inclusion
            and the major semi-axis of the respective RSA cell.
            index_Dupl_Incl ():
            (*) The unitary RVE has dimensions [0, 1]x[0, 1].
        """


    def Check_Input_Parameters_For_RSA(self,DIR,inclPrm):
       

        self.logger.info('Check_Input_Parameters_For_RSA')
        # inclPrm
        N_incl=inclPrm.N_incl
        c_incl=inclPrm.c_incl
        e_incl=inclPrm.e_incl
        theta_incl=inclPrm.theta_incl
        #---
        e_cell_RSA=self.e_cell_RSA
        theta_cell_RSA=self.theta_cell_RSA
        size_factor=self.size_factor


        R_incl_Max=np.sqrt(c_incl/(np.pi*np.sum(size_factor**2*e_incl,axis=0)))
        R_cell_RSA=R_incl_Max*np.ones((N_incl,1))
        a2_cell_RSA=R_cell_RSA*e_cell_RSA
        R_incl=size_factor*R_cell_RSA
        a2_incl=R_incl*e_incl

        for I in range(N_incl): # To check if each inclusion fits within the RSA cell, respectively.
            Ellip_cell_RSA=ipeb.Ellipse_Object((0,0),2*R_cell_RSA[I,0],2*a2_cell_RSA[I,0],theta_cell_RSA[I,0])
            Ellip_incl=ipeb.Ellipse_Object((0,0),2*R_incl[I,0],2*a2_incl[I,0],theta_incl[I,0])
            
            detected_diff=ipeb.Ellipse_Object.Difference_Region(Ellip_incl,Ellip_cell_RSA)

            if detected_diff:
                ipgt.Graph.Non_Adjusted_Incl(DIR,Ellip_cell_RSA,Ellip_incl)
                self.logger.error(f'Error in Check_Input_Parameters_For_RSA. The inclusion {I} doesn\'t fit within the corresponding RSA cell. Check input parameters.')
                os._exit(0) 

        # Update attributes
        self.R_incl=R_incl
        self.a2_incl=a2_incl
        self.R_cell_RSA=R_cell_RSA
        self.a2_cell_RSA=a2_cell_RSA

    @staticmethod
    def Generate_First_Pos(labelNumber, inclPrm, logger):
        

        logger.info('Generate_First_Pos')
        vert_dist_center_border=None
        vert_dist_betw_incl=None
        N_incl=inclPrm.N_incl
        x_incl = np.zeros((N_incl,2))

        if labelNumber==1:
            #x_incl[0,:] = np.array([0,-0.25]) # Center point
            x_incl[0,:] = np.array([0,0]) # Center point
            #x_incl[0,:] = np.array([0,-0.5]) # Bottom point

        elif labelNumber==2:
            x_incl[0,:] = np.array([0,-0.5])

        elif labelNumber==3:
            e_incl=inclPrm.e_incl
            theta_incl=inclPrm.theta_incl
            R_incl=RSA_Alg.instance[0].R_incl

            E1=ipeb.Ellipse_Object([0,0],2*R_incl[0][0], 2*R_incl[0][0]*e_incl[0][0],theta_incl[0][0])
            eq1=E1.Equation()
            x, y = sp.symbols('x, y')
            eq2=sp.Eq(x,0)
            sol = sp.solve([eq1, eq2], [x, y])
            vert_dist_center_border=[(a,b) for (a,b) in sol if b>0][0][1]

            vert_dist_betw_incl=(1-6*vert_dist_center_border)/3
            x_incl[0,:] = np.array([0,-0.5])

        elif labelNumber==4:
            x_incl[0,:] = np.array([0,0])

        elif labelNumber==5:
            e_incl=inclPrm.e_incl
            theta_incl=inclPrm.theta_incl
            R_incl=RSA_Alg.instance[0].R_incl

            E1=ipeb.Ellipse_Object([0,0],2*R_incl[0][0], 2*R_incl[0][0]*e_incl[0][0],theta_incl[0][0])
            eq1=E1.Equation()
            x, y = sp.symbols('x, y')
            eq2=sp.Eq(x,0)
            sol = sp.solve([eq1, eq2], [x, y])
            vert_dist_center_border=[(a,b) for (a,b) in sol if b>0][0][1]

            vert_dist_betw_incl=(1-4*vert_dist_center_border)/2
            x_incl[0,:] = np.array([0,-0.5]) # First point

        elif labelNumber==6:
            e_incl=inclPrm.e_incl
            theta_incl=inclPrm.theta_incl
            R_incl=RSA_Alg.instance[0].R_incl

            E1=ipeb.Ellipse_Object([0,0],2*R_incl[0][0], 2*R_incl[0][0]*e_incl[0][0],theta_incl[0][0])
            eq1=E1.Equation()
            x, y = sp.symbols('x, y')
            eq2=sp.Eq(x,0)
            sol = sp.solve([eq1, eq2], [x, y])
            vert_dist_center_border=[(a,b) for (a,b) in sol if b>0][0][1]

            vert_dist_betw_incl=(1-6*vert_dist_center_border)/3
            x_incl[0,:] = np.array([0,-0.5])
        else:
            # General case (uniform distribution)
            x_incl[0,:] = np.random.rand(2) - np.array([0.5,0.5])

        return x_incl, vert_dist_center_border, vert_dist_betw_incl

    @staticmethod
    def Generate_Other_Pos(labelNumber, N_iter, vert_dist_center_border, vert_dist_betw_incl, logger):
       
        
        logger.info('Generate_Other_Pos')

        if labelNumber==1:
                pass

        elif labelNumber==2:
            x_incl_i = np.array([0,0]) # Second point

        elif labelNumber==3:
            if N_iter==1:
                x_incl_i = np.array([0,-0.5+vert_dist_betw_incl+2*vert_dist_center_border],dtype=float) # Second point
            elif N_iter==2:
                x_incl_i = np.array([0,0.5-vert_dist_betw_incl-2*vert_dist_center_border],dtype=float) # Third point

        elif labelNumber==4:
            x_incl_i = np.array([-0.5,-0.5]) # Second point

        elif labelNumber==5:
            if N_iter==1:
                x_incl_i = np.array([0,0]) # Second point
            elif N_iter==2:
                x_incl_i = np.array([0.5,-0.5+vert_dist_center_border+vert_dist_betw_incl/2],dtype=float) # Third point
            elif N_iter==3:
                x_incl_i = np.array([0.5,0.5-vert_dist_center_border-vert_dist_betw_incl/2],dtype=float) # Fourth point

        elif labelNumber==6:
            if N_iter==1:
                x_incl_i = np.array([0,-0.5+vert_dist_betw_incl+2*vert_dist_center_border],dtype=float) # Second point
            elif N_iter==2:
                x_incl_i = np.array([0,0.5-vert_dist_betw_incl-2*vert_dist_center_border],dtype=float) # Third point
            elif N_iter==3:
                x_incl_i = np.array([0.499,-0.5+vert_dist_center_border+vert_dist_betw_incl/2],dtype=float) # Fourth point
            elif N_iter==4:
                x_incl_i = np.array([0.499,0.5-vert_dist_center_border-vert_dist_betw_incl/2],dtype=float) # Fifth point
            elif N_iter==5:
                x_incl_i = np.array([0.499,-0.5+3*vert_dist_center_border+3*vert_dist_betw_incl/2],dtype=float) # Sixth point

        else:
            # Non-periodic case (uniform distribution)
            x_incl_i = np.random.rand(2) - np.array([0.5,0.5])

        return x_incl_i


    def RSA_Place_Centers(self,globalPrm,inclPrm,N_iter_max=2000):

       

        # globalPrm
        labelNumber=globalPrm['labelNumber']
        self.logger.info('RSA_Place_Centers')
        # inclPrm
        N_incl=inclPrm.N_incl
        # rsaPrm
        rsaPrm=RSA_Alg.instance[0]

        theta_cell_RSA=self.theta_cell_RSA
        R_cell_RSA=self.R_cell_RSA
        a2_cell_RSA=self.a2_cell_RSA
        security_factor=self.security_factor

        dmin = security_factor*R_cell_RSA              # Major-semi axis of the RSA cell assuming the security threshold.
        dirs = np.array([[1,0],[0,1],[1,1],[1,-1]])    # Direct lattice vectors.
        N_iter=0                                       # Iteration counter.
        i = 1                                          # ith inclusion placed.
        p=1                                            # Iterations to placed the ith inclusion.
        #---------
        p0=13
        """In cases where the number of inclusions is small, and you prefer to assist the RSA algorithm for purely
        geometric purposes, you can assign small values to the p0 parameter, for instance, p0=0 or p0=3.
        However, be aware that by doing this you are biasing the randomness when placing the inclusion i>1.
        """
        #---------
        self.logger.info(f'Placing N_incl = {N_incl} inclusions')

        #---------
        # Generate first inclusion position
        x_incl, vert_dist_center_border, vert_dist_betw_incl=RSA_Alg.Generate_First_Pos(labelNumber, inclPrm, self.logger)

        #---------
        # Generate the position of the other inclusions and check that there is no contact with the previously placed inclusions.
        while N_iter < N_iter_max and i < N_incl:
            N_iter = N_iter+1
            contact = 0         # Contact indicator between inclusions.

            if i>1:
                if p > p0:      # To assist the RSA process.

                    self.logger.info(f'As you reach {p0}, the RSA process starts being assisted.')
                    x_incl_i=ipgt.Graph.RSA_Figures(globalPrm,inclPrm,rsaPrm,x_incl[0:i,:],x_incl_i,GraphLabel='Iter', Iter=N_iter,assists_RSA=True)
                    self.logger.info('RSA process was successfully assisted.')

                else:
                    x_incl_i=RSA_Alg.Generate_Other_Pos(labelNumber, N_iter, vert_dist_center_border, vert_dist_betw_incl, self.logger)
            else:
                x_incl_i=RSA_Alg.Generate_Other_Pos(labelNumber, N_iter, vert_dist_center_border, vert_dist_betw_incl, self.logger)

            if globalPrm['saveFigures']:
                # Figures of the RSA iteration, except the last one.
                ipgt.Graph.RSA_Figures(globalPrm,inclPrm,rsaPrm,x_incl[0:i,:],x_incl_i,GraphLabel='Iter',Iter=N_iter)

            for k in range(i): # Check contact with previously placed inclusions.
                x_incl_k = x_incl[k,:]

                # First, check the distance with the inclusions inside the RVE.
                r = x_incl_i - x_incl_k

                if np.linalg.norm(r) < dmin[i,0]+dmin[k,0]:

                        E_i=ipeb.Ellipse_Object(x_incl_i,2*security_factor*R_cell_RSA[i,0], 2*security_factor*a2_cell_RSA[i,0],theta_cell_RSA[i,0])
                        E_k=ipeb.Ellipse_Object(x_incl_k,2*security_factor*R_cell_RSA[k,0], 2*security_factor*a2_cell_RSA[k,0],theta_cell_RSA[k,0])

                        detected_inters=ipeb.Ellipse_Object.Intersection_Region(E_i,E_k)
                        
                        if detected_inters:
                            contact = 1
                            break

                # Then, check the inclusions outside the RVE, obtained by periodicity.
                for nd in range(4):
                    x_incl_kper = x_incl_k - np.sign(np.dot(x_incl_k,dirs[nd,:]))*dirs[nd,:]
                    r = x_incl_i - x_incl_kper

                    if np.linalg.norm(r) < dmin[i,0]+dmin[k,0]:

                        E_i=ipeb.Ellipse_Object(x_incl_i,2*security_factor*R_cell_RSA[i,0], 2*security_factor*a2_cell_RSA[i,0],theta_cell_RSA[i,0])
                        E_kper=ipeb.Ellipse_Object(x_incl_kper,2*security_factor*R_cell_RSA[k,0], 2*security_factor*a2_cell_RSA[k,0],theta_cell_RSA[k,0])

                        detected_inters=ipeb.Ellipse_Object.Intersection_Region(E_i,E_kper)
                        
                        if detected_inters:
                            contact = 1
                            break

                if contact: break

            if contact:
                p = p+1
            else:
                x_incl[i,:] = x_incl_i
                self.logger.info(f'{i+1}th inclusion placed in {p} iterations')
                i = i+1
                p = 1
        #---------

        if globalPrm['saveFigures']:
            # Last figure of the RSA iteration
            ipgt.Graph.RSA_Figures(globalPrm,inclPrm,rsaPrm,x_incl[0:N_incl,:],np.array([]),GraphLabel='Iter',Iter=N_iter+1)

        if N_incl==1: self.logger.info(f'{i}th inclusion placed in {p} iterations')

        self.x_incl=x_incl


    def X_Per_From_X_Incl(self, inclPrm, a1=-0.5,a2=-0.5):
        


        self.logger.info('X_Per_From_X_Incl')
        # inclPrm
        N_incl=inclPrm.N_incl
        e_incl=inclPrm.e_incl
        theta_incl=inclPrm.theta_incl

        e_cell_RSA=self.e_cell_RSA
        theta_cell_RSA=self.theta_cell_RSA
        R_incl=self.R_incl
        R_cell_RSA=self.R_cell_RSA
        x_incl=self.x_incl
        #---------

        b1 = a1 + 1
        b2 = a2 + 1

        e_incl_per = np.zeros((2*N_incl,1))
        e_cell_RSA_per = np.zeros((2*N_incl,1))
        theta_incl_per = np.zeros((2*N_incl,1))
        theta_cell_RSA_per = np.zeros((2*N_incl,1))
        R_incl_per = np.zeros((2*N_incl,1))
        R_cell_RSA_per = np.zeros((2*N_incl,1))
        x_per = np.zeros((2*N_incl ,2))


        n = 0 # Number of duplicated inclusions
        index_Dupl_Incl=[] # Index of duplicated inclusions

        # Maximum horizontal and vertical distance for ellipses
        for i in range(N_incl):

            if np.abs(theta_incl[i,0]) < 1e-5: # to avoid error from 1 / tan(theta)
                d1 = R_incl[i,0]
                d2 = e_incl[i,0]*R_incl[i,0]

            else: # TO CHECK: Formula obtained by computing the position of inflection points
                  # when the ellipse is parametrized by an angle phi
                  # then [x1, x2] = R * R(theta) * [cos(phi), e*sin(phi)]
                ct = np.cos(theta_incl[i,0])
                st = np.sin(theta_incl[i,0])

                p1 = np.arctan(- e_incl[i,0]*np.tan(theta_incl[i,0])) # Inflection point for horizontal direction
                d1 = np.abs( R_incl[i,0]*(ct*np.cos(p1) - e_incl[i,0]*st*np.sin(p1)))

                p2 = np.arctan(e_incl[i,0] / np.tan(theta_incl[i,0]))
                d2 = np.abs(R_incl[i,0]*(st*np.cos(p2) + e_incl[i,0]*ct*np.sin(p2)))


            nper = 0  # "periodicity" counter : 1 for borders, 3 for corners

            x1 = x_incl[i,0]
            x2 = x_incl[i,1]

            x1per = x1
            x2per = x2
            if x1-d1 < a1:
                nper = nper+1
                x1per = x1+1
            if x1+d1 > b1:
                nper = nper+1
                x1per = x1-1
            if x2-d2 < a2:
                nper = nper+1
                x2per = x2+1
            if x2+d2 > b2:
                nper = nper+1
                x2per = x2-1

            if nper == 1: # intersection with border : one duplicate
                x_per[n,:] = np.array([x1per,x2per])
                R_incl_per[n,0] = R_incl[i,0]
                theta_incl_per[n,0] = theta_incl[i,0]
                e_incl_per[n,0] = e_incl[i,0]

                R_cell_RSA_per[n,0] = R_cell_RSA[i,0]
                theta_cell_RSA_per[n,0] = theta_cell_RSA[i,0]
                e_cell_RSA_per[n,0] = e_cell_RSA[i,0]

                n = n+1
                index_Dupl_Incl.append(i)

            elif nper == 2: # intersection with corner : three duplicates
                x_per[n,:] = np.array([x1per,x2per])
                x_per[n+1,:] = np.array([x1,x2per])
                x_per[n+2,:] = np.array([x1per,x2])
                R_incl_per[n,0] = R_incl[i,0]
                R_incl_per[n+1,0] = R_incl[i,0]
                R_incl_per[n+2,0] = R_incl[i,0]
                theta_incl_per[n,0] = theta_incl[i,0]
                theta_incl_per[n+1,0] = theta_incl[i,0]
                theta_incl_per[n+2,0] = theta_incl[i,0]
                e_incl_per[n,0] = e_incl[i,0]
                e_incl_per[n+1,0] = e_incl[i,0]
                e_incl_per[n+2,0] = e_incl[i,0]

                R_cell_RSA_per[n,0] = R_cell_RSA[i,0]
                R_cell_RSA_per[n+1,0] = R_cell_RSA[i,0]
                R_cell_RSA_per[n+2,0] = R_cell_RSA[i,0]
                theta_cell_RSA_per[n,0] = theta_cell_RSA[i,0]
                theta_cell_RSA_per[n+1,0] = theta_cell_RSA[i,0]
                theta_cell_RSA_per[n+2,0] = theta_cell_RSA[i,0]
                e_cell_RSA_per[n,0] = e_cell_RSA[i,0]
                e_cell_RSA_per[n+1,0] = e_cell_RSA[i,0]
                e_cell_RSA_per[n+2,0] = e_cell_RSA[i,0]

                n = n+3
                index_Dupl_Incl.append(i)
                index_Dupl_Incl.append(i)
                index_Dupl_Incl.append(i)

        if n==0:
            x_per = np.array([])
            R_incl_per = np.array([])
            theta_incl_per = np.array([])
            e_incl_per = np.array([])

            R_cell_RSA_per = np.array([])
            theta_cell_RSA_per = np.array([])
            e_cell_RSA_per = np.array([])
        else:
            x_per = x_per[:n]
            R_incl_per = R_incl_per[:n]
            theta_incl_per = theta_incl_per[:n]
            e_incl_per = e_incl_per[:n]

            R_cell_RSA_per = R_cell_RSA_per[:n]
            theta_cell_RSA_per = theta_cell_RSA_per[:n]
            e_cell_RSA_per = e_cell_RSA_per[:n]

        self.x_per=x_per
        self.e_incl_per=e_incl_per
        self.e_cell_RSA_per=e_cell_RSA_per
        self.theta_incl_per=theta_incl_per
        self.theta_cell_RSA_per=theta_cell_RSA_per
        self.R_incl_per=R_incl_per
        self.R_cell_RSA_per=R_cell_RSA_per
        self.index_Dupl_Incl=index_Dupl_Incl


    def Determine_Remaining_RSA_Attr (self, globalPrm, inclPrm, Iter=None):

        self.logger.info('Determine_Remaining_RSA_Attr')
        pixels = globalPrm['pixels']
        saveFigures = globalPrm['saveFigures']
        # inclPrm
        e_incl=inclPrm.e_incl
        theta_incl=inclPrm.theta_incl
        N_incl=inclPrm.N_incl
        # rsaPrm
        rsaPrm=RSA_Alg.instance[0]

        if self.x_per.size==0: # There are not duplicated inclusions

            # Positions at the unitary cell [0,1]x[0,1]
            for i in range(2):
                self.x_incl[:,i] = self.x_incl[:,i] + 0.5

            self.e_incl_tot= e_incl
            self.e_cell_RSA_tot= self.e_cell_RSA
            self.theta_incl_tot= theta_incl
            self.theta_cell_RSA_tot= self.theta_cell_RSA
            self.R_incl_tot= self.R_incl
            self.R_cell_RSA_tot= self.R_cell_RSA
            self.a2_incl_per= np.array([])
            self.a2_incl_tot= self.a2_incl
            self.a2_cell_RSA_per = np.array([])
            self.a2_cell_RSA_tot= self.a2_cell_RSA
            self.x_tot = self.x_incl
            self.N_incl_tot= self.x_tot.shape[0]


        else: # There are duplicated inclusions

            # Positions at the unitary cell
            for i in range(2):
                self.x_incl[:,i] = self.x_incl[:,i] + 0.5
                self.x_per[:,i] = self.x_per[:,i] + 0.5

            self.e_incl_tot=np.concatenate((e_incl,self.e_incl_per),axis=0)
            self.e_cell_RSA_tot=np.concatenate((self.e_cell_RSA,self.e_cell_RSA_per),axis=0)
            self.theta_incl_tot=np.concatenate((theta_incl,self.theta_incl_per),axis=0)
            self.theta_cell_RSA_tot=np.concatenate((self.theta_cell_RSA,self.theta_cell_RSA_per),axis=0)
            self.R_incl_tot=np.concatenate((self.R_incl,self.R_incl_per),axis=0)
            self.R_cell_RSA_tot=np.concatenate((self.R_cell_RSA,self.R_cell_RSA_per),axis=0)
            self.a2_incl_per = self.R_incl_per*self.e_incl_per
            self.a2_incl_tot=np.concatenate((self.a2_incl,self.a2_incl_per),axis=0)
            self.a2_cell_RSA_per = self.R_cell_RSA_per*self.e_cell_RSA_per
            self.a2_cell_RSA_tot=np.concatenate((self.a2_cell_RSA,self.a2_cell_RSA_per),axis=0)
            self.x_tot = np.concatenate((self.x_incl,self.x_per),axis=0)
            self.N_incl_tot=self.x_tot.shape[0]


        #RVE_0_1_To_Pxls
        #We map the properties from the square unit cell [0, 1]^2 to [0, pixels]^2.
        self.R_cell_RSA_Pxls=pixels*self.R_cell_RSA
        self.a2_cell_RSA_Pxls=pixels*self.a2_cell_RSA
        self.R_incl_tot_Pxls=pixels*self.R_incl_tot
        self.R_cell_RSA_tot_Pxls=pixels*self.R_cell_RSA_tot
        self.a2_incl_tot_Pxls=pixels*self.a2_incl_tot
        self.a2_cell_RSA_tot_Pxls=pixels*self.a2_cell_RSA_tot
        self.x_tot_Pxls=pixels*self.x_tot


        if saveFigures:
            X=self.x_tot[0:N_incl,:]
            Y=self.x_tot[N_incl:self.N_incl_tot,:]
            if Iter is None:
                ipgt.Graph.RSA_Figures(globalPrm,inclPrm,rsaPrm,X, Y,GraphLabel='Final')
            else:
                ipgt.Graph.RSA_Figures(globalPrm,inclPrm,rsaPrm,X, Y,GraphLabel='Final',Iter=Iter)


    def Mesh_Elliptic_Inclusions(self,pixels,pv_matrix,pv_incl):
      
        
        self.logger.info('Mesh_Elliptic_Inclusions')

        theta_incl_tot=self.theta_incl_tot
        R_incl_tot=self.R_incl_tot
        a2_incl_tot=self.a2_incl_tot
        x_tot=self.x_tot

        matPixels = pv_matrix*np.ones((pixels, pixels))
        p_x1 = np.arange(pixels)/pixels # pixel positions on the rows in normal order
        p_x2 = np.flip(np.arange(pixels))/pixels # pixel positions on the columns in reverse order
        N_incl_tot = x_tot.shape[0]    # number of inclusions

        R = [] # rotational matrix
        for n in range(N_incl_tot):
            # Angles and rotation matrix
            ct = np.cos(theta_incl_tot[n,0])
            st = np.sin(theta_incl_tot[n,0])
            R.append(np.array([[ct, st],\
                        [-st, ct]]))

        for i in range(pixels): # in normal order
            for j in reversed(range(pixels)): # in reverse order
                p = np.array([p_x1[i],p_x2[j]]) # pixel position
                for n in range(N_incl_tot):
                    y = p - x_tot[n,:]   # relative position to center
                    Ry = R[n].dot(y)       # coordinates in ellipse referential
                    d = (Ry[0]/R_incl_tot[n,0])**2 + (Ry[1]/a2_incl_tot[n,0])**2
                    if (d < 1.):
                        matPixels[j,i] = pv_incl # indexes exchanged

        # Notice that the "matPixels" array has a x-y perspective instead of row-column perspective.
        return matPixels



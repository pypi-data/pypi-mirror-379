
import numpy as np
import sympy as sp
from shapely.geometry import Polygon as shapely_Polygon
import logging

logger = logging.getLogger(__name__) 


class Ellipse_Object:
    
    def __init__(self, center, majorAxis, minorAxis, theta, polyNum=300):
        
        self.center = center
        self.majorAxis = majorAxis
        self.minorAxis = minorAxis
        self.theta = theta
        self.polyNum=polyNum
    
    if True:
       
        @property 
        def center(self): 
            logger.info("Getter center") 
            return self._center
        
        
        @center.setter 
        def center(self, value): 
            logger.info("Setter center") 
            self._center = value 
       
        @property 
        def majorAxis(self): 
            logger.info("Getter majorAxis") 
            return self._majorAxis
        
        
        @majorAxis.setter 
        def majorAxis(self, value): 
            logger.info("Setter majorAxis") 
            self._majorAxis = value 
       
        @property 
        def minorAxis(self): 
            logger.info("Getter minorAxis") 
            return self._minorAxis
        
        
        @minorAxis.setter 
        def minorAxis(self, value): 
            logger.info("Setter minorAxis") 
            self._minorAxis = value 
       
        @property 
        def theta(self): 
            logger.info("Getter theta") 
            return self._theta
        
        
        @theta.setter 
        def theta(self, value): 
            logger.info("Setter theta") 
            self._theta = value 
       
        @property 
        def polyNum(self): 
            logger.info("Getter polyNum") 
            return self._polyNum
        
       
        @polyNum.setter 
        def polyNum(self, value): 
            logger.info("Setter polyNum") 
            self._polyNum = value 
        #---

    def Equation(self):
        
        logger.info('Equation') 

        x,y=sp.symbols('x, y')
        v=np.array([x-self.center[0],y-self.center[1]])
        R=np.array([
            [np.cos(self.theta),np.sin(self.theta)],
            [np.sin(self.theta),np.cos(self.theta)]
            ])
        A=np.array([
            [1/(self.majorAxis/2)**2,0],
            [0,1/(self.minorAxis/2)**2]
            ])
        eq=sp.Eq(v @ R @ A @ R.T @ v.T,1)
        return eq

    def Polyline(self):
        
        logger.info('Polyline')

        t = np.linspace(0, 2*np.pi, self.polyNum, endpoint=False)
        p = np.zeros((self.polyNum, 2))
       
        p[:, 0] = self.center[0] + self.majorAxis/2 * np.cos(self.theta) * np.cos(t) - self.minorAxis/2 * np.sin(self.theta) * np.sin(t)
        p[:, 1] = self.center[1] + self.majorAxis/2 * np.sin(self.theta) * np.cos(t) + self.minorAxis/2 * np.cos(self.theta) * np.sin(t)
        return p

        
    @staticmethod
    def Difference_Region(*ellips):
       

        logger.info('Difference_Region')

        e1 = shapely_Polygon(ellips[0].Polyline()) 
        e2 = shapely_Polygon(ellips[1].Polyline()) 
        differRegion = e1.difference(e2)

        if differRegion.area<=1e-8:
            
            return False
        else:
            
            return True


    @staticmethod
    def Intersection_Region(*ellips):
        
        logger.info('Intersection_Region')

        e1 = shapely_Polygon(ellips[0].Polyline())
        e2 = shapely_Polygon(ellips[1].Polyline())
        intersRegion = e1.intersection(e2)

        # Note that the intersection of the two ellipses can be an empty geometry, which causes a 'RuntimeWarning' in the shapely version 2.0.1
        # RuntimeWarning: invalid value encountered in intersection return lib.intersection(a, b, **kwargs)
        # https://github.com/shapely/shapely/issues/1709           
        
        if intersRegion.is_empty:
           
            return False
        else:
            
            return True



"""
Forward problem (dimensionless, exclude the initial conditions from the final 
obseravtions).

Author:
    Panagiotis Tsilifis
Date:
    06/09/2014

"""


import numpy as np
from model_1 import *
from model_2 import *
import sys
sys.path.insert(0,'../')
from vuq import Model
from vuq import view_as_column



class CatalysisModelDMNLY0(Model):
    """
    A class representing the forward model of the catalysis problem.
    """

    def __init__(self, name='Catalysis model (dimensionless)'):
        """
        Initialize the object
        """
        #self._kappa = x
        super(CatalysisModelDMNLY0, self).__init__(5, 30, name=name)

    def _eval(self, x):
        """
        Solves the dynamical system for given parameters x.
        """
        x = view_as_column(x)
        # Points where the solution will be evaluated
        t = np.array([0., 1./6, 1./3, 1./2, 2./3, 5./6, 1.])
        t = view_as_column(t)
        # Initial condition
        y0 = np.array([1., 0., 0., 0., 0., 0.])
        y0 = view_as_column(y0)
        assert x.shape[0] == 5
        sol = f(x[:,0], y0[:,0], t[:,0])
        J = df(x[:,0], y0[:,0], t[:,0])
        H = df2(x[:,0], y0[:,0], t[:,0])
        y = np.delete(sol.reshape((7,6)), 2, 1).flatten() # The 3rd species is unobservable
        sol_y = np.delete(y.reshape((7,5)), 0, 0).reshape(30) # Delete the initial conditions from the data  
        dy = np.array([np.delete(J[:,i].reshape((7,6)), 2, 1).reshape(35) for i in range(J.shape[1])]) # Delete the 3rd species
        sol_dy = np.array([np.delete(dy[i,:].reshape((7,5)), 0, 0).flatten() for i in range(dy.shape[0])]) # Delete the initial cond. 
        sol_d2y = np.zeros((30, H.shape[1], H.shape[2]))
        for i in range(H.shape[1]):
            for j in range(H.shape[2]):
                d2y = np.delete(H[:,i,j].reshape((7,6)), 2, 1).reshape(35) # Delete the 3rd species
                sol_d2y[:,i,j] = np.delete(d2y.reshape((7,5)), 0, 0).flatten()
        state = {}
        state['f'] = sol_y
        state['f_grad'] = sol_dy.T
        state['f_grad_2'] = sol_d2y
        return state

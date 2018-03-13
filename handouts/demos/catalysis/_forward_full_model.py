"""
Forward problem (dimensionless - full matrix)

Author:
    Panagiotis Tsilifis
Date:
    06/12/2014

"""


import numpy as np
from model_1 import *
from model_2 import *
import sys
sys.path.insert(0,'../')
from vuq import Model
from vuq import view_as_column



class CatalysisFullModelDMNLESS(Model):
    """
    A class representing the forward model of the catalysis problem
    using a full matrix.
    """

    def __init__(self, name='Catalysis model (dimensionless, full matrix)'):
        """
        Initialize the object
        """
        #self._kappa = x
        super(CatalysisFullModelDMNLESS, self).__init__(36, 35, name=name)

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
        assert x.shape[0] == 36
        sol = f_full(x[:,0], y0[:,0], t[:,0])
        J = df_full(x[:,0], y0[:,0], t[:,0])
        H = df2_full(x[:,0], y0[:,0], t[:,0])
        y = np.delete(sol.reshape((7,6)), 2, 1).flatten() # The 3rd species is unobservable
        dy = np.array([np.delete(J[:,i].reshape((7,6)), 2, 1).reshape(35) for i in range(J.shape[1])]) # Delete the 3rd species
        d2y = np.zeros((35, H.shape[1], H.shape[2]))
        for i in range(H.shape[1]):
            for j in range(H.shape[2]):
                d2y[:,i,j]= np.delete(H[:,i,j].reshape((7,6)), 2, 1).reshape(35) # Delete the 3rd species
        state = {}
        state['f'] = y
        state['f_grad'] = dy.T
        state['f_grad_2'] = d2y
        return state

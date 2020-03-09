"""
Forward problem

Author:
    Panagiotis Tsilifis
    Ilias Bilionis
Date:
    05/22/2014
    03/13/2018
"""


import numpy as np
from .model_1 import *
from .model_2 import *
import sys
from .. import Model
from .. import view_as_column



class CatalysisModel(Model):
    """
    A class representing the forward model of the catalysis problem.
    """

    def __init__(self, name='Catalysis model'):
        """
        Initialize the object
        """
        #self._kappa = x
        super(CatalysisModel, self).__init__(5, 35, name=name)

    def _eval(self, x):
        """
        Solves the dynamical system for given parameters x.
        """
        x = view_as_column(x)
        # Points where the solution will be evaluated
        t = np.array([0., 30., 60., 90., 120., 150., 180.])
        t = view_as_column(t)
        # Initial condition
        y0 = np.array([500., 0., 0., 0., 0., 0.])
        y0 = view_as_column(y0)
        assert x.shape[0] == 5
        sol = f(x[:,0], y0[:,0], t[:,0])
        J = df(x[:,0], y0[:,0], t[:,0])
        H = df2(x[:,0], y0[:,0], t[:,0])
        y = np.delete(sol.reshape((7,6)), 2, 1).flatten() # The 3rd species is unobserved
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

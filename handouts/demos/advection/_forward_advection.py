"""
Forward problem with one source. 

Author:
    Panagiotis Tsilifis
Date:
    10/15/2014

"""


import numpy as np
import fipy as fp
from transport_model import *
import sys
sys.path.insert(0,'../')
from vuq import Model
from vuq import view_as_column

class ContaminantAdvectionModel(Model):
    """
    A class representing the forward model of the contaminant transport problem
    using a advection equation.
    """
    
    def __init__(self, name='Transport model'):
        """
        Initialize the object
        """
        super(ContaminantAdvectionModel, self).__init__(2, 40, name=name)

    def _eval(self, xs):
        """
        Solves the advection equation for u and its derivatives for a given 
        source location xs. 
        """
        xs = view_as_column(xs)
        assert xs.shape[0] == 2
        nx = 50
        ny = nx
        dx = 0.1
        dy = dx
        mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
        vx, vy = make_V_field(mesh)
        u = f(xs[:,0], mesh, vx, vy)
        du1 = df(xs[:,0], mesh, vx, vy, 1)
        du2 = df(xs[:,0], mesh, vx, vy, 2)
        d2u11 = df2(xs[:,0], mesh, vx, vy, 1, 1)
        d2u22 = df2(xs[:,0], mesh, vx, vy, 1, 1)
        d2u12 = df2(xs[:,0], mesh, vx, vy, 1, 2)
        dU = np.hstack([view_as_column(du1), view_as_column(du2)])
        d2U = np.hstack([view_as_column(d2u11), view_as_column(d2u12), view_as_column(d2u12), view_as_column(d2u22)])
        d2U = d2U.reshape((d2U.shape[0], 2, 2))
        state = {}
        state['f'] = u #view_as_column(u)
        state['f_grad'] = dU
        state['f_grad_2'] = d2U
        return state
    
    def _eval_u(self, xs):
        """
        Solves only the diffusion equation for u for a given 
        source location xs. 
        """
        xs = view_as_column(xs)
        assert xs.shape[0] == 2
        nx = 50
        ny = nx
        dx = 0.1
        dy = dx
        mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
        vx, vy = make_V_field(mesh)
        u = f(xs[:,0], mesh, vx, vy)
        return u
    
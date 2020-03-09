"""
Solve numerically the diffusion equation using the fipy package

Author:
    Panagiotis Tsilifis

Date:
    6/16/2014
"""

import numpy as np 
import fipy as fp
import matplotlib.pyplot as plt 



def make_source(xs, mesh, time):
    """
    Makes the source term of the diffusion equation 
    """
    #assert xs.shape[0] == 2
    sourceTerm = fp.CellVariable(name = "Source term", mesh=mesh, value = 0.)
    rho = 0.05
    q0 = 1 / (np.pi * rho ** 2)
    T = 0.3
    for i in range(sourceTerm().shape[0]):
        sourceTerm()[i] = q0 * np.exp( - ((mesh.cellCenters[0]()[i] - xs[0]) ** 2
                                       + (mesh.cellCenters[1]()[i] - xs[1]) ** 2 ) / (2 * rho **2)) * (time() < T)
    return sourceTerm

def make_source_der(xs, mesh, time, i):
    """
    Make the source term of the diffusion equation for the derivatives of u.
    """
    #assert xs.shape[0] == 2
    rho = 0.05
    sourceTerm = make_source(xs, mesh, time)
    for j in range(sourceTerm().shape[0]):
        sourceTerm()[j] = sourceTerm()[j] * (mesh.cellCenters[i-1]()[j] - xs[i-1]) / rho ** 2
    return sourceTerm

def make_source_der_2(xs, mesh, time, i, j):
    """
    Make the source term of the diffusion equation for the 2nd derivatives of u.
    """
    #assert xs.shape[0] == 2
    rho = 0.05
    sourceTerm = make_source(xs, mesh, time)
    for k in range(sourceTerm().shape[0]):
        sourceTerm()[k] = sourceTerm()[k] * ( (mesh.cellCenters[i-1]()[k] - xs[i-1]) * (mesh.cellCenters[j-1]()[k] - xs[j-1]) / rho **2
                    - (i == j)) / rho **2
    return sourceTerm

def f(xs, mesh):
    """
    Evaluate the model for the concentration at the four corners of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_4(t_1)
    ...
    y_1(t_4)
    ...
    y_4(t_4)
    """
    time = fp.Variable()
    q = make_source(xs, mesh, time)
    D = 1.
    # Define the equation
    eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=D) + q
    # Boundary conditions 
    
    # The solution variable
    phi = fp.CellVariable(name = "Concentraion", mesh=mesh, value=0.)
    
    # Solve
    dt = 0.005
    steps = 60
    U_sol = []
    for step in range(steps):
        eq.solve(var=phi, dt=dt)
        if step == 14 or step == 29 or step == 44 or  step == 59:
            #dl = phi()[0]
            #dr = phi()[24]
            ul = phi()[600]
            #ur = phi()[624]
            #U_sol = np.hstack([U_sol, np.array([dl, dr, ul, ur])])
            U_sol = np.hstack([U_sol, np.array([ul])])
    
    return U_sol

def df(xs, mesh, i):
    """
    Evaluate the model for the derivatives at the four corners of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_4(t_1)
    ...
    y_1(t_4)
    ...
    y_4(t_4)
    """
    assert i == 1 or i == 2
    time = fp.Variable()
    q0 = make_source_der(xs, mesh, time, i)
    D = 1.
    # Define the equation
    eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=D) + q0
    # Boundary conditions 
    
    # The solution variable
    phi = fp.CellVariable(name = "Concentraion", mesh=mesh, value=0.)
    
    # Solve
    dt = 0.005
    steps = 60
    dU = []
    for step in range(steps):
        eq.solve(var=phi, dt=dt)
        if step == 14 or step == 29 or step == 44 or  step == 59:
            #dl = phi()[0]
            #dr = phi()[24]
            ul = phi()[600]
            #ur = phi()[624]
            #dU = np.hstack([dU, np.array([dl, dr, ul, ur])])
            dU = np.hstack([dU, np.array([ul])])
    
    return dU

def df2(xs, mesh, i, j):
    """
    Evaluate the model for the 2nd derivatives at the four corners of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_4(t_1)
    ...
    y_1(t_4)
    ...
    y_4(t_4)
    """
    assert i == 1 or i == 2
    assert j == 1 or j == 2
    nx = 25
    ny = nx
    dx = 0.04
    dy = dx
    mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
    time = fp.Variable()
    q0 = make_source_der_2(xs, mesh, time, i, j)
    D = 1.
    # Define the equation
    eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=D) + q0
    # Boundary conditions 
    
    # The solution variable
    phi = fp.CellVariable(name = "Concentraion", mesh=mesh, value=0.)
    
    # Solve
    dt = 0.005
    steps = 60
    d2U = []
    for step in range(steps):
        eq.solve(var=phi, dt=dt)
        if step == 14 or step == 29 or step == 44 or  step == 59:
            #dl = phi()[0]
            #dr = phi()[24]
            ul = phi()[600]
            #ur = phi()[624]
            #d2U = np.hstack([d2U, np.array([dl, dr, ul, ur])])
            d2U = np.hstack([d2U, np.array([ul])])
    
    return d2U
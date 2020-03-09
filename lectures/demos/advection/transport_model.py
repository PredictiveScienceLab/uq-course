"""
Solve numerically the transport equation using the fipy package.
The velocity field is obtained after solving first the Richard's equation 
in steady state.

Author:
    Panagiotis Tsilifis

Date:
    10/15/2014
"""

import numpy as np
import fipy as fp
from random import *
import matplotlib.pyplot as plt



def make_source(xs, mesh, time):
    """
    Makes the source term of the transport equation 
    """
    #assert xs.shape[0] == 2
    sourceTerm = fp.CellVariable(name = "Source term", mesh=mesh, value = 0.)
    rho = 0.35
    q0 = 1 / (np.pi * rho ** 2)
    T = 0.3
    for i in range(sourceTerm().shape[0]):
        sourceTerm()[i] = q0 * np.exp( - ((mesh.cellCenters[0]()[i] - xs[0]) ** 2
                                       + (mesh.cellCenters[1]()[i] - xs[1]) ** 2 ) / (2 * rho **2)) * (time() < T)
    return sourceTerm

def make_source_der(xs, mesh, time, i):
    """
    Make the source term of the transport equation for the derivatives of u.
    """
    #assert xs.shape[0] == 2
    rho = 0.35
    sourceTerm = make_source(xs, mesh, time)
    for j in range(sourceTerm().shape[0]):
        sourceTerm()[j] = sourceTerm()[j] * (mesh.cellCenters[i-1]()[j] - xs[i-1]) / rho ** 2
    return sourceTerm

def make_source_der_2(xs, mesh, time, i, j):
    """
    Make the source term of the transport equation for the 2nd derivatives of u.
    """
    #assert xs.shape[0] == 2
    rho = 0.35
    sourceTerm = make_source(xs, mesh, time)
    for k in range(sourceTerm().shape[0]):
        sourceTerm()[k] = sourceTerm()[k] * ( (mesh.cellCenters[i-1]()[k] - xs[i-1]) * (mesh.cellCenters[j-1]()[k] - xs[j-1]) / rho **2
                    - (i == j)) / rho **2
    return sourceTerm

def make_V_field(mesh):
    """
    Solves Richards equation at steady state and uses head solution to calculate
    the velocity field.
    """
    ############################################################################
    ######## --------- Make the hydraulic conductivity field --------- #########
    ############################################################################

    A = np.load('covarMatrix50.npy')
    # Perform Cholesky decomposition of cov
    U = np.linalg.cholesky(A)
    # 

    y = np.zeros((2500,1))
    e = np.zeros((2500,1))
    mu = -1.106 # normal random field mean 
    for i in range(0,2500):
        e[i] = gauss(0,1)
    
    y = mu + np.dot(U,e)
    K = np.exp(y)

    ############################################################################
    ############################################################################
    ########## ---------- Steady state equation for head ----------- ###########
    ############################################################################
    ############################################################################

    phi = fp.CellVariable(name = "solution variable", mesh=mesh, value=0.)

    D = fp.CellVariable(mesh=mesh, value = 1.)
    for i in range(0,2500):
        D()[i] = K[i]

    coeffD = D()*fp.numerix.exp(0.01*phi)

    # --- Assign boundary conditions
    valueTop = -1.5
    valueGradBottom = 0.

    phi.constrain(valueTop, where=mesh.facesTop)
    phi.constrain(valueGradBottom, where=mesh.facesBottom)

    # --- Solve steady state groundwater flow equation
    eqSteady = (fp.DiffusionTerm(coeff=D()*fp.numerix.exp(0.01*phi)) + np.gradient(coeffD())[0])
    eqSteady.solve(var=phi) 
    
    theta = 0.4 # Effective porosity
    Rd = 2 # Retardation factor
    
    head = phi().reshape(50,50)
    Dhead = np.gradient(head)
    qx = Dhead[1]
    vx = qx.reshape(2500)
    for i in range(0,2500):
        vx[i] = -coeffD[i]*vx[i]/theta
    
    qy = Dhead[0] + 1.
    vy = qy.reshape(2500)
    for i in range(0,2500):
        vy[i] = -coeffD[i]*vy[i]/theta
    
    return vx, vy

def f(xs, mesh, vx, vy):
    """
    Evaluate the model for the concentration at the 10 locations of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_10(t_1)
    ...
    y_1(t_4)
    ...
    y_10(t_4)
    """
    ############################################################################
    ############################################################################
    ##### ------------------ Solve the transport equation ---------------- #####
    ############################################################################
    
    Rd = 2. # Retardation factor
    
    convCoeff = fp.CellVariable(mesh=mesh, rank=1)
    convCoeff()[0,:] = vx
    convCoeff()[1,:] = vy
    time = fp.Variable()
    # --- Make Source ---
    q = make_source(xs, mesh, time)
    # The solution variable
    var = fp.CellVariable(name = "variable", mesh=mesh, value=0.)
    # Define the equation
    eqC = fp.TransientTerm(Rd) == -fp.ConvectionTerm(coeff=convCoeff) + q
    
    # Solve
    U_sol = []
    timeStepDuration = 0.005
    steps = 400
    for step in range(steps):
        time.setValue(time() + timeStepDuration)
        eqC.solve(var=var, dt=timeStepDuration)
        if step == 99 or step == 199 or step == 299 or  step == 399:
            U_sol = np.hstack([U_sol, np.array([var()[8*50+14], var()[8*50+34],
                                            var()[18*50+14], var()[18*50+34],
                                            var()[28*50+14], var()[28*50+34],
                                            var()[38*50+14], var()[38*50+34],
                                            var()[48*50+14], var()[48*50+34]])])
    
    return U_sol
        
    ##############################    END    ###################################
def df(xs, mesh, vx, vy, i):
    """
    Evaluate the model for the derivatives at the 10 locations of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_10(t_1)
    ...
    y_1(t_4)
    ...
    y_10(t_4)
    """
    assert i == 1 or i == 2
    ############################################################################
    ############################################################################
    ##### ------------------ Solve the transport equation ---------------- #####
    ############################################################################
    
    Rd = 2. # Retardation factor
    
    convCoeff = fp.CellVariable(mesh=mesh, rank=1)
    convCoeff()[0,:] = vx
    convCoeff()[1,:] = vy
    time = fp.Variable()
    # --- Make Source ---
    q0 = make_source_der(xs, mesh, time, i)
    # The solution variable
    var = fp.CellVariable(name = "variable", mesh=mesh, value=0.)
    # Define the equation
    eqC = fp.TransientTerm(Rd) == -fp.ConvectionTerm(coeff=convCoeff) + q0
    
    # Solve
    dU = []
    timeStepDuration = 0.005
    steps = 400
    for step in range(steps):
        time.setValue(time() + timeStepDuration)
        eqC.solve(var=var, dt=timeStepDuration)
        if step == 99 or step == 199 or step == 299 or  step == 399:
            dU = np.hstack([dU, np.array([var()[8*50+14], var()[8*50+34],
                                            var()[18*50+14], var()[18*50+34],
                                            var()[28*50+14], var()[28*50+34],
                                            var()[38*50+14], var()[38*50+34],
                                            var()[48*50+14], var()[48*50+34]])])
    
    return dU
        
    ##############################    END    ###################################
    
def df2(xs, mesh, vx, vy, i, j):
    """
    Evaluate the model for the 2nd derivatives at the 10 locations of the domain
    at times ``t``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_10(t_1)
    ...
    y_1(t_4)
    ...
    y_10(t_4)
    """
    assert i == 1 or i == 2
    assert j == 1 or j == 2
    ############################################################################
    ############################################################################
    ##### ------------------ Solve the transport equation ---------------- #####
    ############################################################################
    
    Rd = 2. # Retardation factor
    
    convCoeff = fp.CellVariable(mesh=mesh, rank=1)
    convCoeff()[0,:] = vx
    convCoeff()[1,:] = vy
    time = fp.Variable()
    # --- Make Source ---
    q0 = make_source_der_2(xs, mesh, time, i, j)
    # The solution variable
    var = fp.CellVariable(name = "variable", mesh=mesh, value=0.)
    # Define the equation
    eqC = fp.TransientTerm(Rd) == -fp.ConvectionTerm(coeff=convCoeff) + q0
    
    # Solve
    d2U = []
    timeStepDuration = 0.005
    steps = 400
    for step in range(steps):
        time.setValue(time() + timeStepDuration)
        eqC.solve(var=var, dt=timeStepDuration)
        if step == 99 or step == 199 or step == 299 or  step == 399:
            d2U = np.hstack([d2U, np.array([var()[8*50+14], var()[8*50+34],
                                            var()[18*50+14], var()[18*50+34],
                                            var()[28*50+14], var()[28*50+34],
                                            var()[38*50+14], var()[38*50+34],
                                            var()[48*50+14], var()[48*50+34]])])
    
    return d2U
        
    ##############################    END    ###################################
"""
Generate data for the advection forward model.

Author:
    Panagiotis Tsilifis

Date:
    10/15/2014

"""

import numpy as np
import fipy as fp
from random import *
import matplotlib.pyplot as plt

################################################################################
######## --------- Make the hydraulic conductivity field ------------ ##########
################################################################################

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

################################################################################
################################################################################
###### ----- Initialization and steady state equation for head ---------- ######
################################################################################
################################################################################

nx = 50
ny = nx 
dx = 0.05
dy = dx
L = dx * nx
mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)

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

if __name__ == '__main__':
    viewer = fp.Viewer(vars=phi)#, datamin=-1.5, datamax=0.)
    viewer.plot()

# --- Solve steady state groundwater flow equation
eqSteady = (fp.DiffusionTerm(coeff=D()*fp.numerix.exp(0.01*phi)) + np.gradient(coeffD())[0])
eqSteady.solve(var=phi) 
print phi()
if __name__ == '__main__':
    viewer.plot()

if __name__ == '__main__':
    raw_input("Implicit steady-state diffusion. Press <return> to proceed...")

################################################################################
################################################################################
##### -------------------- Solve the transport equation ------------------ #####
################################################################################


theta = 0.4 # Effective porosity
Rd = 2 # Retardation factor

head = phi().reshape(50,50)
Dhead = np.gradient(head)
qx = Dhead[1]
Vx = qx.reshape(2500)
for i in range(0,2500):
    Vx[i] = -coeffD[i]*Vx[i]/theta
print Vx

qy = Dhead[0] + 1.
Vy = qy.reshape(2500)
for i in range(0,2500):
    Vy[i] = -coeffD[i]*Vy[i]/theta
print Vy

    
vx = fp.CellVariable(name="x-component velocity", mesh=mesh, value=Vx)
vy = fp.CellVariable(name="y-component velocity", mesh=mesh, value=Vy)
viewerVx = fp.Viewer(vars=vx, datamin=-0.1, datamax=0.1)
viewerVx.plot()
viewerVy = fp.Viewer(vars=vy, datamin=-4., datamax=0.)
viewerVy.plot()

if __name__ == '__main__':
    raw_input("Velocity field. Press <return> to proceed")

convCoeff = fp.CellVariable(mesh=mesh, rank=1)
convCoeff()[0,:] = Vx
convCoeff()[1,:] = Vy
time = fp.Variable()


var = fp.CellVariable(name = "variable", mesh=mesh)

# --- Make source term
rho = 0.35
q0 = 1. / (np.pi * rho ** 2)
T = 0.3
xs_1 = np.array([1.25, 2.])
sourceTerm_1 = fp.CellVariable(name = "Source term", mesh=mesh, value = 0.)
for i in range(sourceTerm_1().shape[0]):
    sourceTerm_1()[i] = q0 * np.exp( - ((mesh.cellCenters[0]()[i] - xs_1[0]) ** 2 
                                    + (mesh.cellCenters[1]()[i] - xs_1[1]) ** 2 ) / (2 * rho **2)) * (time() < T)



eqC = fp.TransientTerm(Rd) == -fp.ConvectionTerm(coeff=convCoeff) + sourceTerm_1

if __name__ == '__main__':
    viewer = fp.Viewer(vars=var, datamin = 0., datamax = 2.5)
    viewer.plot()

data = []
timeStepDuration = 0.005
steps = 400
for step in range(steps):
    time.setValue(time() + timeStepDuration)
    eqC.solve(var=var, dt=timeStepDuration)
    if step == 99 or step == 199 or step == 299 or  step == 399:
        data = np.hstack([data, np.array([var()[8*50+14], var()[8*50+34],
                                          var()[18*50+14], var()[18*50+34],
                                          var()[28*50+14], var()[28*50+34],
                                          var()[38*50+14], var()[38*50+34],
                                          var()[48*50+14], var()[48*50+34]])])
    #    data = np.hstack([data, np.array([dc, uc])])
    if __name__ == '__main__':
        viewer.plot()
        
if __name__ == '__main__':
    raw_input("Steady-state convection-diffusion equation. Press <return> to continue...")

np.save('data_concentrations_advection.npy',data)
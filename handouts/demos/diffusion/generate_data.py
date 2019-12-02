"""
Generate data for the diffusion forward model.

Author:
    Panagiotis Tsilifis

Date:
    6/12/2014

"""

import numpy as np
import fipy as fp
import os
import matplotlib.pyplot as plt


# Make the source 

nx = 101
ny = nx
dx = 1./101 
dy = dx
rho = 0.05
q0 = 1. / (np.pi * rho ** 2)
T = 0.3
mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
xs_1 = np.array([0.91, 0.23])
#xs_2 = np.array([0.89, 0.75])
time = fp.Variable()
sourceTerm_1 = fp.CellVariable(name = "Source term", mesh=mesh, value = 0.)
#sourceTerm_2 = fp.CellVariable(name = "Source term", mesh=mesh, value = 0.)
for i in range(sourceTerm_1().shape[0]):
    sourceTerm_1()[i] = q0 * np.exp( - ((mesh.cellCenters[0]()[i] - xs_1[0]) ** 2 
                                  + (mesh.cellCenters[1]()[i] - xs_1[1]) ** 2 ) / (2 * rho **2)) * (time() < T)
    #sourceTerm_2()[i] = q0 * np.exp( - ((mesh.cellCenters[0]()[i] - xs_2[0]) ** 2 
    #                              + (mesh.cellCenters[1]()[i] - xs_2[1]) ** 2 ) / (2 * rho **2)) * (time() < T)

# The equation
eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=1.) + sourceTerm_1# + sourceTerm_2

# The solution variable
phi = fp.CellVariable(name = "Concentration", mesh=mesh, value=0.)


#if __name__ == '__main__':
#    viewer = fp.Viewer(vars=phi, datamin=0., datamax=3.)
#    viewer.plot()

x = np.arange(0,101.)/101
y = x

data = []
dt = 0.005
steps = 60
for step in range(steps):
    time.setValue(time() + dt)
    eq.solve(var=phi, dt=dt)
#    if __name__ == '__main__':
#        viewer.plot()
    if step == 14 or step == 29 or step == 44 or  step == 59:
        dc = phi()[50]
        #dr = phi()[109]
        uc = phi()[10150]
        #ur = phi()[12099]
        #data = np.hstack([data, np.array([dl, dr, ul, ur])])
        data = np.hstack([data, np.array([dc, uc])])
        
        fig = plt.figure()
        plt.contourf(x, y, phi().reshape(101,101),200)
        plt.colorbar()
#        fig.suptitle('Concentration at t = ' + str(time()))
        plt.xlabel('x')
        plt.ylabel('y')
        #png_file = os.path.join('figures', 'concentration'+'t.png')
        #plt.savefig(png_file)
        plt.show()
        

        
#if __name__ == '__main__':
#    raw_input("Transient diffusion with source term. Press <return> to proceed")

#np.save('data_concentrations_upperlowercenters.npy',data)
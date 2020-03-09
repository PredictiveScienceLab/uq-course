"""
Implementation of a generic adjoint solver for linear dynamical systems.

Author:
    Ilias Bilionis

Date:
    4/23/2014
"""


import numpy as np
from scipy.integrate import ode


def f0(t, y, A):
    """
    The nomral dynamics.
    """
    return np.dot(A, y)

def f1(t, y, A):
    """
    The normal dynamics and of the 1st derivatives wrt A.
    """
    d = A.shape[0]
    y_0 = y[:d]
    f_y_0 = f0(t, y_0, A)
    y_1 = y[d:d + d**3].reshape((d, d, d))
    f_y_1 = np.einsum('ij,jkl->ikl', A, y_1)
    for i in range(d):
        f_y_1[i, i, :] += y_0
    return np.hstack([f_y_0, f_y_1.flatten()])

def f2(t, y, A):
    """
    The normal dynamics and of the 2st derivatives wrt A.
    """
    d = A.shape[0]
    y_0 = y[:d]
    f_y_0 = f0(t, y_0, A)
    y_1 = y[d:d + d**3].reshape((d, d, d))
    f_y_1 = np.einsum('ij,jkl->ikl', A, y_1)
    for i in range(d):
        f_y_1[i, i, :] += y_0
    #return np.hstack([f_y_0, f_y_1.flatten()])
    y_2 = y[d+d**3:d+d**3+d**5].reshape((d,d**2,d**2))
    f_y_2 = np.einsum('ij,jkl->ikl',A, y_2)
    for i in range(d):
        for j in range(i*d,(i+1)*d):
            f_y_2[i,j,:] += y_1[j-i*d,:,:].flatten()
    for i in range(d):
        for j in range(i*d,(i+1)*d):
            f_y_2[i,:,j] += y_1[j-i*d,:,:].flatten()
    return np.hstack([f_y_0, f_y_1.flatten(), f_y_2.flatten()])
    

def loss(A, t, y):
    r = ode(f0)
    r.set_initial_value(y[0, :], t[0]).set_f_params(A)
    y_m = np.zeros((t.shape[0], r.y.shape[0]))
    y_m[0, :] = r.y
    for i in range(1, t.shape[0]):
        r.integrate(t[i])
        y_m[i, :] = r.y
    tmp = y_m - y
    return np.dot([1, 1, 0, 1, 1, 1], np.linalg.norm(tmp, axis=0) ** 2)


def dloss(A, t, y):
    r = ode(f1)
    d = A.shape[0]
    r.set_initial_value(np.hstack([y[0, :], np.zeros((d ** 3, ))])).set_f_params(A)
    y_m = np.zeros((t.shape[0], r.y.shape[0]))
    y_m[0, :] = r.y
    for i in range(1, t.shape[0]):
        r.integrate(t[i])
        y_m[i, :] = r.y
    y_m0 = y_m[:, :d]
    y_m1 = y_m[:, d:d + d**3].reshape((t.shape[0], d, d, d))
    tmp = y_m0 - y
    return 2. * np.einsum('ij,j,ijkl->kl', tmp, np.array([1, 1, 0, 1, 1, 1]), y_m1)

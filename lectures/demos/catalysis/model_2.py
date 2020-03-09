"""
Implements the catalysis model as found in Yiannis paper.

"""

from .system import *


def make_A(kappa):
    """
    Make the matrix of the dynamical system from ``kappa``.
    """
    A = np.array([[-kappa[0], 0, 0, 0, 0, 0],
              [kappa[0], -kappa[1]-kappa[3]-kappa[4], 0, 0, 0, 0],
              [0, kappa[1], -kappa[2], 0, 0, 0],
              [0, 0, kappa[2], 0, 0, 0],
              [0, kappa[4], 0, 0, 0, 0],
              [0, kappa[3], 0, 0, 0, 0]])
    # The derivative of A with respect to kappa
    d = A.shape[0]
    s = kappa.shape[0]
    dA = np.zeros((d, d, s))
    dA[0, 0, 0] = -1.
    dA[1, 0, 0] = 1.
    dA[1, 1, 1] = -1.
    dA[1, 1, 4] = -1.
    dA[1, 1, 3] = -1.
    dA[2, 1, 1] = 1.
    dA[2, 2, 2] = -1.
    dA[3, 2, 2] = 1.
    dA[4, 1, 4] = 1.
    dA[5, 1, 3] = 1.
    return A, dA

def make_full_A(kappa):
    """
    Make the matrix of the dynamical system from ``kappa``.
    """
    assert kappa.shape[0] == 36
    A = kappa.reshape((6,6))
    dA = np.zeros((36,36))
    for i in range(36):
        dA[i,i] = 1
    dA = dA.reshape((6,6,36))
    return A, dA

def f(kappa, y0, t):
    """
    Evaluate the model at ``kappa`` and at times ``t`` with initial
    conditions ``y0``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_d(t_1)
    ...
    y_1(t_K)
    ...
    y_d(t_K)
    """
    A = make_A(kappa)[0]
    r = ode(f0)
    r.set_initial_value(y0, 0).set_f_params(A)
    y_m = [y0[None, :]]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    return y_m.flatten()

def f_full(kappa, y0, t):
    """
    Evaluate the model at ``kappa`` and at times ``t`` with initial
    conditions ``y0``.

    It returns a flatten version of the system, i.e.:
    y_1(t_1)
    ...
    y_d(t_1)
    ...
    y_1(t_K)
    ...
    y_d(t_K)
    """
    A = make_full_A(kappa)[0]
    r = ode(f0)
    r.set_initial_value(y0, 0).set_f_params(A)
    y_m = [y0[None, :]]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    return y_m.flatten()


def df2(kappa, y0, t):
    """
    Evaluate the derivative of the model derivatives at ``kappa`` and at times ``t``
    with initial conditions ``y0``.

    This returns a matrix of the following form:
    dy_1(t_1) / dkappa_1 ... dy_1(t_1) / dkappa_s
    ...
    dy_d(t_1) / dkappa_1 ... dy_d(t_1) / dkappa_s
    ...
    dy_1(t_K) / dkappa_1 ... dy_d(t_K) / dkappa_s
    ...
    dy_d(t_K) / dkappa_1 ... dy_d(t_K) / dkappa_s
    """
    A, dA = make_A(kappa)
    d = A.shape[0]
    r = ode(f2) # Look at system.py: this should be the f of the adjoint
    r.set_initial_value(np.hstack([y0, np.zeros((d ** 3 + d ** 5, ))])).set_f_params(A)
    y_m = [r.y]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    # This is the Jacobian with respect to the full matrix A
    J = y_m[:, d:d+d**3].reshape((t.shape[0], d, d, d))
    # Now we apply the chain rule to compute the jacobian wrt kappa
    J_kappa = np.einsum('ijkl,klr', J, dA)
    
    J2 = y_m[:,d+d**3:d+d**3+d**5].reshape((t.shape[0], d, d**2, d**2))
    #print len(J2[0,0,0,:])
    ## Trying something New
    JJ = np.zeros((t.shape[0],d,kappa.shape[0],d**2))
    for j in range(t.shape[0]):
        for k in range(d):
            for i in range(d**2):
                JJ[j,k,:,i] = np.einsum('kl,klr',J2[j,k,i,:].reshape(d,d), dA)
    J_kappa2 = np.einsum('ijklr,lrs', JJ.reshape(t.shape[0],d,kappa.shape[0],d,d), dA)
    return J_kappa2.reshape((d * t.shape[0], kappa.shape[0], kappa.shape[0]))

def df2_full(kappa, y0, t):
    """
    Evaluate the derivative of the model derivatives at ``kappa`` and at times ``t``
    with initial conditions ``y0``.

    This returns a matrix of the following form:
    dy_1(t_1) / dkappa_1 ... dy_1(t_1) / dkappa_s
    ...
    dy_d(t_1) / dkappa_1 ... dy_d(t_1) / dkappa_s
    ...
    dy_1(t_K) / dkappa_1 ... dy_d(t_K) / dkappa_s
    ...
    dy_d(t_K) / dkappa_1 ... dy_d(t_K) / dkappa_s
    """
    A, dA = make_full_A(kappa)
    d = A.shape[0]
    r = ode(f2) # Look at system.py: this should be the f of the adjoint
    r.set_initial_value(np.hstack([y0, np.zeros((d ** 3 + d ** 5, ))])).set_f_params(A)
    y_m = [r.y]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    # This is the Jacobian with respect to the full matrix A
    J = y_m[:, d:d+d**3].reshape((t.shape[0], d, d, d))
    # Now we apply the chain rule to compute the jacobian wrt kappa
    J_kappa = np.einsum('ijkl,klr', J, dA)
    
    J2 = y_m[:,d+d**3:d+d**3+d**5].reshape((t.shape[0], d, d**2, d**2))
    #print len(J2[0,0,0,:])
    ## Trying something New
    JJ = np.zeros((t.shape[0],d,kappa.shape[0],d**2))
    for j in range(t.shape[0]):
        for k in range(d):
            for i in range(d**2):
                JJ[j,k,:,i] = np.einsum('kl,klr',J2[j,k,i,:].reshape(d,d), dA)
    J_kappa2 = np.einsum('ijklr,lrs', JJ.reshape(t.shape[0],d,kappa.shape[0],d,d), dA)
    return J_kappa2.reshape((d * t.shape[0], kappa.shape[0], kappa.shape[0]))

def ndf2(kappa0, y0 ,t, h=1e-3):
    
    y = f(kappa0, y0, t)
    kappa = kappa0.copy()
    J = np.zeros((y.shape[0], kappa0.shape[0], kappa0.shape[0]))
    for i in range(kappa0.shape[0]):
        for j in range(kappa0.shape[0]):
            kappa[i] += h
            kappa[j] += h
            py1 = f(kappa, y0, t)
            kappa[j] -= 2*h
            py2 = f(kappa, y0 ,t)
            kappa[j] += 2*h
            kappa[i] -= 2*h
            py3 = f(kappa, y0, t)
            kappa[j] -= 2*h
            py4 = f(kappa, y0, t)
            kappa[i] += h
            kappa[j] += h 
            J[:, i, j] = (py1 - py2 - py3 + py4) / (4*h**2)
    return J

if __name__ == '__main__':
    # Test if what we are doing make sense
    import matplotlib.pyplot as plt
    # Some kappas to evaluate the model at:
    kappa = np.array([0.0216, 0.0292, 0.0219, 0.0021, 0.0048])
    # The observed data (to read the initial conditions):
    obs_data = np.loadtxt('obs_data.txt')
    # Remember that the column of the data that has all zeros contains X
    # which is not observed. This is the 4th column.
    # The observed times
    t = obs_data[:, 0]
    # The intial points
    y0 = obs_data[0, 1:]
    # Here is how we evaluate the model
    y = f(kappa, y0, t)
    # Here is how we evaluate the derivatives of the model
    ddy = df2(kappa, y0, t)
    # Now evaluate the numerical derivatives at kappa
    J = ndf2(kappa, y0, t)
    for i in range(kappa.shape[0]):
        for j in range(kappa.shape[0]):
            plt.plot(ddy[:, i, j], 'r', linewidth=2)
            plt.plot(J[:, i, j], '--g', linewidth=2)
            plt.legend(['Adjoint derivative', 'Numerical Derivative'])
            plt.show()

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

def df(kappa, y0, t):
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
    r = ode(f1) # Look at system.py: this should be the f of the adjoint
    r.set_initial_value(np.hstack([y0, np.zeros((d ** 3, ))])).set_f_params(A)
    y_m = [r.y]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    # This is the Jacobian with respect to the full matrix A
    J = y_m[:, d:].reshape((t.shape[0], d, d, d))
    # Now we apply the chain rule to compute the jacobian wrt kappa
    J_kappa = np.einsum('ijkl,klr', J, dA)
    return J_kappa.reshape((d * t.shape[0], kappa.shape[0]))

def df_full(kappa, y0, t):
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
    r = ode(f1) # Look at system.py: this should be the f of the adjoint
    r.set_initial_value(np.hstack([y0, np.zeros((d ** 3, ))])).set_f_params(A)
    y_m = [r.y]
    for tt in t[1:]:
        r.integrate(tt)
        y_m.append(r.y[None, :])
    y_m = np.vstack(y_m)
    # This is the Jacobian with respect to the full matrix A
    J = y_m[:, d:].reshape((t.shape[0], d, d, d))
    # Now we apply the chain rule to compute the jacobian wrt kappa
    J_kappa = np.einsum('ijkl,klr', J, dA)
    return J_kappa.reshape((d * t.shape[0], kappa.shape[0]))

def ndf(kappa0, y0, t, h=1e-3):
    """
    Numerically compute the Jacobian of f at x0.
    """
    y = f(kappa0, y0, t)
    kappa = kappa0.copy()
    J = np.zeros((y.shape[0], kappa0.shape[0]))
    for i in range(kappa0.shape[0]):
        kappa[i] += h
        py = f(kappa, y0, t)
        kappa[i] -= h
        J[:, i] = (py - y) / h
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
    dy = df(kappa, y0, t)
    # Now evaluate the numerical derivatives at kappa
    J = ndf(kappa, y0, t)
    for i in range(kappa.shape[0]):
        plt.plot(dy[:, i], 'r', linewidth=2)
        plt.plot(J[:, i], '--g', linewidth=2)
        plt.legend(['Adjoint derivative', 'Numerical Derivative'])
        plt.show()

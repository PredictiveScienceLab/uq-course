"""
Test the multivariate Gamma class.

Author:
    Panagiotis Tsilifis

Date:
    5/22/2014

"""

import numpy as np
from catalysis import CatalysisModel
from catalysis import CatalysisModelDMNLESS
from catalysis import CatalysisModelDMNLY0
from matplotlib.pyplot import *


x = np.array([0.0216, 0.0292, 0.0219, 0.0021, 0.0048])

# Test first the original model 
solution = CatalysisModel()

print str(solution) + '\n'

state = solution._eval(x)
y = state['f']
J = state['f_grad']
H = state['f_grad_2']
print 'Solution'
print '-' * 80
print y.reshape((7, y.shape[0]/7))
print '\n'
print 'Jacobian'
print '-' * 80
print J
print '\n'
print 'Second derivatives'
print '-' * 80
print H
t = np.array([0.0, 30., 60., 90., 120., 150., 180.])
plot(t, y.reshape((t.shape[0], y.shape[0]/t.shape[0])))
show()



#print 'Test the evaluation at many inputs simultaneously'
#kappa = 0.1*np.random.rand(x.shape[0],5)
#state2 = solution(kappa)
#print 'Solution'
#print '-' * 80
#print str(state['f']) + '\n'
#print 'First derivates'
#print '-' * 80
#print str(state['f_grad']) + '\n'
#print 'Second derivatives'
#print '-' * 80
#print str(state['f_grad_2']) + '\n'

# Now test the dimensionless version of the model
solution = CatalysisModelDMNLY0()

print str(solution) + '\n'

state = solution._eval(x * 180)
y = state['f']
J = state['f_grad']
H = state['f_grad_2']
print 'Solution'
print '-' * 80
print y.reshape((6, y.shape[0]/6))
print '\n'
print 'Jacobian'
print '-' * 80
print J
print '\n'
print 'Second derivatives'
print '-' * 80
print H
t = np.array([1./6, 1./3, 1./2, 2./3, 5./6, 1.])
plot(t, y.reshape((t.shape[0], y.shape[0]/t.shape[0])))
show()
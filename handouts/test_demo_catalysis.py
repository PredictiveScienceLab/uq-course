"""
Test the multivariate Gamma class.

Author:
    Panagiotis Tsilifis
    Ilias Bilionis

Date:
    5/22/2014
    3/18/2018

"""

import numpy as np
import demos
from demos.catalysis import CatalysisModel
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


"""
A trivial test model.

Author:
    Ilias Bilionis

Date:
    6/16/2014

"""


__all__ = ['TestModel0']


import numpy as np
from vuq import Model


class TestModel0(Model):

    def __init__(self, name='Test Model 0'):
        super(TestModel0, self).__init__(1, 1, name=name)

    def _eval(self, x):
        state = {}
        state['f'] = x
        state['f_grad'] = np.ones((1, 1))
        state['f_grad_2'] = np.zeros((1, 1, 1))
        return state

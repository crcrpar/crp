#!/usr/bin/env python

import os
import json

import numpy as np
import scipy as sp


class OnlineCRP:
    """Online Chinese Restaurant Process

    KDD 2014"""

    def __init__(self, n, alpha, G_0):
        self._n = n
        self._alpha = alpha
        self._g0 = G_0
        self._results = []

    @property
    def result(self):
        return self._results

    def __call__(self):
        # TODO:


def relaxing(gamma_1, gamma_2, e_j, f_j):
    """relaxing function

    corrector for prior distribution of online CRP
    Args:
        gamma_1: regret rates
        gamma_2: regret rates
        e_j:     for tracer of allocation of previous i-1 customers at table j
        f_j:     for tracer of allocation of previous i-1 customers at table j
    """
    return pow(1+gamma_1, f_j) * pow(1-gamma_2, e_j)

def error_j(y_results, z_results, j):

    return np.sum(np.where(z_results == j and y_results != j, 1, 0))

def false_j(y_results, z_results, j):

    return np.sum(np.where(y_results == j and z_results != j, 1, 0))

def p_z:
    #TODO:


def main():
    import datetime
    o_crp = OnlineCRP(n=1e5, alpha=10, G_0='normal')
    o_crp()
    o_crp_result = o_crp.result
    dict_result = dict(enumerate(o_crp_result))
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    f_name = 'online_crp_{}.json'.format(time)
    with open(f_name, 'w') as f:
        json.dump(dict_result, f)

if __name__ == '__main__':
    main()

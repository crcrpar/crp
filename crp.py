#!/usr/bin/env python

import json

import numpy as np
import scipy as sp


class CRP:
    """Chinese Restaurant Process

    ref: chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#uri=https://www.cs.princeton.edu/courses/archive/fall07/cos597C/scribe/20070921.pdf
    """

    def __init__(self, n, alpha=3, G_0='normal', name=None):
        self._n = n
        self._alpha = alpha
        self._results = []
        self._results.append(np.random.normal(1))

    def __call__(self):
        for i in range(self._n):
            probability = self._alpha / float(self._alpha + i - 1)
            tmp = np.random.uniform(size=(1,))
            if tmp < probability:
                self._results.append(np.random.normal(1))
            else:
                self._results.append(np.random.choice(self._results[:i-1], 1)[0])

    @property
    def results(self):
        return self._results

    @property
    def name(self):
        return self._name


if __name__ == '__main__':

    crp = CRP(n=10000)
    crp()
    crp_results = crp.results
    results_dic = dict(enumerate(crp_results, start=0))
    with open('./resutls.json', 'w') as f:
        json.dump(results_dic, f)

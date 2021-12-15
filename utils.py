# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:25:46 2020

@author: Adam.Comelio
"""

import time
from itertools import product

def time_me(func):
    def inner1(*args, **kwargs):
        st = time.perf_counter_ns()
        r = func(*args, **kwargs)
        print('Function done in {} seconds real time'.format(
                                            (time.perf_counter_ns()-st)/1e9))
        return r
    return inner1

def tokenise_input_file(filepath, seperator='\n', func=None):
    with open(filepath, 'r') as f:
        text = f.read()
    if func is None:
        return text.split(seperator)
    return list(map(func, text.split(seperator)))

def run_tests(func, io_pairs):
    print(f'Running {len(io_pairs)} test(s)')
    for i, (func_input, correct_output) in enumerate(io_pairs):
        result = func(func_input)
        if result == correct_output:
            print(f'Test {i+1} passed')
        else:
            print(f'Test {i+1} failed, output was {result}')
    print('Tests done')

def get_adjacent_coords(coord, include_self=False):
    difs = (-1,0,1)
    ranges = tuple(tuple(map(lambda x: x + v, difs)) for v in coord)
    if include_self:
        return tuple(product(*ranges))
    return tuple(p for p in product(*ranges) if p != coord)

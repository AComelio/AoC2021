# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:25:46 2020

@author: Adam.Comelio
"""

import time

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
    print(f'Running {len(io_pairs)} tests')
    for i, (func_input, correct_output) in enumerate(io_pairs):
        if func(func_input) == correct_output:
            print(f'Test {i+1} passed')
        else:
            print(f'Test {i+1} failed')
    print('Tests done')

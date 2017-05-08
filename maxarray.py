#!/usr/bin/env python3

import os, sys
import time
import random
import itertools

max_sum = lambda x,y: max(y, x+y)

def accum(a, func):
  t = 0
  for i in a:
    t = func(t,i)
    yield t

def max_subarray(a):
  return max(accum(a, max_sum))

def max_subarray_fast(a):
  return max(itertools.accumulate(a, max_sum))

def run_tests(func):
  print("running tests")
  for i in range(6):
    n = 10**i
    t1 = time.time()
    m = func(A[:n])
    t2 = time.time()
    print("  time for", n, "elements:", round(t2-t1,6))

A = [-2, -4, 3, -1, 5, 6, -7, -2, 4, -3, 2]
print(max_subarray(A))
print(max_subarray_fast(A))

print("generating array")
A = [random.randint(-10,10) for i in range(10**5)]

run_tests(max_subarray)
run_tests(max_subarray_fast)

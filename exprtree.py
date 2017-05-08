#!/usr/bin/env python3

################################################################################
#
# Written by Huki, file inception on 2016-11-25.
# Adapted and extended from: 
#   http://openbookproject.net/thinkcs/python/english3e/trees.html
#
################################################################################

import sys

def get_token(expr, c=None):
  if len(expr) == 0:
    return None
  if c and expr[-1] not in c:
    return None
  if expr[-1] == ')':
    expr.pop()
    x = get_sum(expr)
    expr.pop()
    return x
  return expr.pop()

def get_power(expr, a=None):
  if not a:
    a = get_token(expr)
  op = get_token(expr, '^')
  if op:
    b = get_token(expr)
    return get_power(expr, [op, a, b])
  return a

def get_product(expr):
  a = get_power(expr)
  op = get_token(expr, '*/')
  if op:
    b = get_product(expr)
    return [op, a, b]
  return a

def get_sum(expr):
  a = get_product(expr)
  op = get_token(expr, '+-')
  if op:
    b = get_sum(expr)
    return [op, a, b]
  return a

################################################################################

operations = {
  '+': lambda x,y: x+y,
  '-': lambda x,y: x-y,
  '*': lambda x,y: x*y,
  '/': lambda x,y: x/y,
  '^': lambda x,y: x**y
}

def print_tree(node, level=0):
  if type(node) is list:
    print_tree(node[1], level+1)
    print('\t' * level + node[0])
    print_tree(node[2], level+1)
  else:
    print('\t' * level + node)

def eval_tree(node):
  if type(node) is list:
    a = eval_tree(node[2])
    b = eval_tree(node[1])
    return operations[node[0]](a, b)
  else:
    return float(node)

def build_tree(expr):
  return get_sum(expr)

def is_digit(c):
  return c.isdigit() or '.' in c or 'e' in c

def parse_expr(expr):
  l = []
  for e in expr:
    if is_digit(e):
      if len(l) and is_digit(l[-1]):
        l[-1] += e
      else:
        l.append(e)
    elif e != ' ':
      l.append(e)
  return l

def main():
  expr = '3 + 4 * 2 / (1 - 5) ^ 2 ^ 3'
  if len(sys.argv) > 1:
    expr = sys.argv[1]

  expr = parse_expr(expr)
  print(expr)
  expr = build_tree(expr)
  print(expr)
  print('syntax tree:')
  print_tree(expr)

  print('result:')
  val = eval_tree(expr)
  if val == int(val):
    val = int(val)
  print(val)

################################################################################

if __name__ == '__main__':
  main()

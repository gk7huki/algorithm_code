#!/usr/bin/env python3

import sys

operations = {
  '+': lambda x,y: x+y,
  '-': lambda x,y: x-y,
  '*': lambda x,y: x*y,
  '/': lambda x,y: x/y,
  '^': lambda x,y: x**y
}

precedence = {
  '+': lambda op: op in '+-*/^',
  '-': lambda op: op in '+-*/^',
  '*': lambda op: op in '*/^',
  '/': lambda op: op in '*/^',
  '^': lambda op: op in ''
}

def is_digit(c):
  return c.isdigit() or '.' in c or 'e' in c

def get_rpn(expr):
  l = []
  op = []
  for c in expr:
    if is_digit(c):
      l.append(c)
    elif c == '(':
      op.append(c)
    elif c == ')':
      t = op.pop()
      while t != '(':
        l.append(t)
        t = op.pop()
    else:
      while len(op) and precedence[c](op[-1]):
        l.append(op.pop())
      op.append(c)
  while len(op):
    l.append(op.pop())
  return l

def eval_stack(expr):
  op = []
  for c in expr:
    if is_digit(c):
      op.append(float(c))
    else:
      b = op.pop()
      a = op.pop()
      op.append(operations[c](a, b))
  return op.pop()

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
  expr = get_rpn(expr)
  print(expr)

  val = eval_stack(expr)
  if val == int(val):
    val = int(val)
  print(val)

if __name__ == '__main__':
  main()

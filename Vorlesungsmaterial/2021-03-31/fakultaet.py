from functools import reduce
from math import prod

def fakultaet(n: int):
  '''Berechnet die Fakultät von n, also das Produkt der Zahlen von 1 bis n.'''
  
  ergebnis = 1

  for i in range(2,n+1):
    ergebnis *= i
  
  return ergebnis

def fak(n):
  if n == 0:
    return 1
  return n * fak(n-1)
#fak = lambda n: 1 if n == 0 else n * fak(n - 1)
#f3 = lambda n: 1 if n == 0 else reduce(lambda x, y: x*y, [x for x in range(1, n+1)])
def fak2(n):
  return prod(list(range(1,n+1)))

def fak3(n):
  return reduce(lambda x,y: x * y, list(range(1,n+1)), 1)

def fak4(n):
  def mult(x,y):
    return x * y

  return reduce(mult, list(range(1,n+1)), 1)

#print(fakultaet(0))
#print(fakultaet(5))
#print(fakultaet(10))

print(fak2(5))
print(fak3(5))
print(fak4(5))
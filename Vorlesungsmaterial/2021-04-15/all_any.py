#def any_of(a, f):
#  ''' Erwartet ein Array a und eine Funktion f.
#      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
#  '''
#  for el in a:
#    if f(el) == True:
#      return True
#  return False

#def any_of(a, f):
#  ''' Erwartet ein Array a und eine Funktion f.
#      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
#  '''
#  results = [f(el) for el in a]  # Liste mit Funktionsergebnissen von f
#  return any(results) # any liefert True, wenn irgendeiner der Werte in der Liste True ist.

#def any_of(a, f):
#  ''' Erwartet ein Array a und eine Funktion f.
#      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
#  '''
#  return any(map(f,a))

def any_of(a, f):
  ''' Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  from functools import reduce
  return reduce(lambda x,y : x or y, map(f,a), False)



a1 = [1,3,5,7,9]
a2 = [1,2,3,4,5]

def even(x):
  '''Liefert True, falls x eine gerade Zahl ist.'''
  return x % 2 == 0

assert(any_of(a1,even) == False)
assert(any_of(a2,even) == True)
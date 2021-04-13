l1 = [3,5,2,7,25]

#print(sum(l1))

#def summe(l):
#  ergebnis = 0
#  for element in l:
#    ergebnis += element
#  return ergebnis

#def summe(l):
#  if l == []:
#    return 0
#  return l[0] + summe(l[1:])

def summe(l):
  if l == []:
    return 0
  head, *tail = l
  return head + summe(tail)

def add(x,y):
  # x + 0 = x
  # x + sy = s(x+y)
  if y == 0:
    return x
  return 1 + add(x,y-1)

addLambda = lambda x, y: x if x == 0 else 1 + addLambda(x, y-1)

def mult(x,z):
  #( x * 0 = 0 )
  # x * 1 = x
  # x * sy = x + (x*y)
  '''Berechnet x * z rekursiv.'''
  if z == 0:
    return 0
  # Hierher kommen wir nur, wenn z >= 1
  return x + mult(x,z-1)

def pow(x,y):
  '''Berechnet x hoch y rekursiv.'''
  if y == 0:
    return 1 
  return x * pow(x, y - 1)

def find(l,x):
  '''Sucht x in l und liefert die Position. Rekursiv.
     Wenn x nicht enthalten ist, liefern wir die Länge von l.'''
  # Basisfall: l ist leer.
  if l == []:
    return 0 # Länge liefern

  # l ist nicht leer, lässt sich in head und tail zerlegen.
  head, *tail = l
  if x == head:
    return 0 # x an Stelle 0 gefunden.
  return 1 + find(tail,x)


print(summe(l1))
print(add(2,3))
print(mult(2,3))
print(pow(2,3))
print(find(l1,7))
print(find(l1,15))

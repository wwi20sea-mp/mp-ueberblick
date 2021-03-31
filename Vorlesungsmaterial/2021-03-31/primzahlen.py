def teilbar(n,m):
  '''Liefert True, falls n durch m teilbar ist.'''
  return n % m == 0
#lambda m, n: m % n == 0


def teiler(n):
  '''Liefert eine Liste aller Teiler von n.
     Also alle Zahlen, durch die n teilbar ist.
  '''
  result = []
  for i in range(1,n+1):
    if teilbar(n,i):
      result += [i]
  return result

def teiler(n):
  return [i for i in range(1,n+1) if teilbar(n,i)]
#teiler = lambda n: [x for x in range(1, n+1) if teilbar(n, x)]

def teiler(n):
  return filter(lambda i : teilbar(n,i), range(1,n+1))

# t = lambda n: list(filter(lambda i: teilbar(n, i), range(1, n+1)))
#Schade :(

def istPrimzahl(n):
  '''Liefert True, falls n einer Primzahl ist.'''
  return len(list(teiler(n))) == 2
#isPrim = lambda n: len(teiler(n)) == 2

def primzahlen(n):
  '''Liefert eine Liste aller Primzahlen, die kleiner sind als n.'''
  return [i for i in range(1,n+1) if istPrimzahl(i)]
#lambda n: [x for x in range(1, n+1) if isPrim(x)]

print(list(teiler(60)))

# t ist ein Filter-Objekt bzw. ein "Generator"
t = teiler(60)
for i in range(4):
  print(next(t))

print(istPrimzahl(2))

print(primzahlen(100))

def primes():
  '''Liefert einen Generator für alle Primzahlen.'''
  i = 2
  while True:
    if istPrimzahl(i):
      yield i
    i += 1

p = primes()

primzahlen_bis_10 = [next(p) for i in range(10)]

print(primzahlen_bis_10)

print(p)

print(next(p))
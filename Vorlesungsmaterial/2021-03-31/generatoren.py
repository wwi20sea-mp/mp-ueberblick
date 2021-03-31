def verdoppeln(gen):
    '''Nimmt einen Generator und liefert einen neuen Generator,
     bei dem jedes Element des alten verdoppelt wird.

     Beispiel: [1,2,3,4,5] --> [2,4,6,8,10]
  '''
    return (2 * i for i in gen)


#lambda gen: map(lambda n: n*2, gen)


def vernfachen(gen, n):
    '''Ver-n-facht jedes Element aus gen.'''

    return (n * i for i in gen)


print(verdoppeln([1, 2, 3, 4, 5]))

print(list(verdoppeln(verdoppeln([1, 2, 3, 4, 5]))))

## Ziel: Einen unendlichen Generator schreiben, der alle Vielfachen von 17 auflistet.

def zahlen():
    '''Generator für alle Zahlen'''
    i = 1
    while True:
        yield i
        i += 1


# Vielfache von 17
v17 = vernfachen(zahlen(), 17)

print([next(v17) for i in range(10)])


# Das Ganze als eine einzige Funktion
# - Wirkt auf den ersten Blick kompakter.
# - Ist aber weniger flexibel, wenn man Ähnliches mehrfach braucht.
def g17():
  n = 17
  while True:
    yield n
    n += 17

def g15():
  n = 15
  while True:
    yield n
    n += 15

def vielfacheVonN(n):
  i = n
  while True:
    yield i
    i += n
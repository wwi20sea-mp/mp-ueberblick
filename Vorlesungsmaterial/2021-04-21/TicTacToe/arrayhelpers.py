def any_of(a, f):
  ''' Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  return any(map(f,a))

def contains_only(l, c):
  '''Prüft, ob die Liste l ausschließlich das Zeichen c enthält.
     Liefert False, wenn l irgendetwas anderes als c enthält.
  '''
  ## Basisfall: Leere Liste.
  if l == []:
    return True
  
  head, *tail = l
  return head == c and contains_only(tail,c)

def get_row(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Zeile aus a.
  '''
  return a[i]


def get_column(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Spalte aus a.
  '''
#  return [a[0][i], a[1][i], a[2][i]]
  return [a[j][i] for j in range(len(a))]

def get_diag1(a):
  '''Liefert die Diagonale in a, die von links oben nach rechts unten geht.'''
  return [a[i][i] for i in range(len(a))]

def get_diag2(a):
  '''Liefert die Diagonale in a, die von links unten nach rechts oben geht.'''
  return [a[i][-i-1] for i in range(len(a))]


def row_contains_only(a,i,c):
  '''Erwartet ein zweidimensionales Array a, eine Zahl i
     und ein Zeichen c.
     Liefert True, wenn die i-te Zeile nur das Zeichen c enthält.
  '''
  return contains_only(get_row(a,i),c)

def column_contains_only(a,i,c):
  '''Erwartet ein zweidimensionales Array a, eine Zahl i
     und ein Zeichen c.
     Liefert True, wenn die i-te Zeile nur das Zeichen c enthält.
  '''
  return contains_only(get_column(a,i),c)

def diag1_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links oben nach rechts unten geht, nur das Zeichen c enthält.'''
  return contains_only(get_diag1(a), c)

def diag2_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links unten nach rechts oben geht, nur das Zeichen c enthält.'''
  return contains_only(get_diag2(a), c)
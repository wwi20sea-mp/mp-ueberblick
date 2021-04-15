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

def test_contains_only():
  l1 = ['X', 'X', 'X']
  assert(contains_only(l1,'X'))
  assert(not contains_only(l1,'O'))

  l2 = ['X', 'X', 'O']
  assert(not contains_only(l2,'X'))
  assert(not contains_only(l2,'O'))

  # Forderung, dass die leere Liste sozusagen voll mit
  # jedem Buchstaben ist.
  # Macht die rekursive Implementierung einfacher.
  assert(contains_only([], 'X'))
  assert(contains_only([], 'O'))


def get_row(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Zeile aus a.
  '''
  return a[i]


def test_get_row():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_row(a1,0) == [1,2,3])


def get_column(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Spalte aus a.
  '''
#  return [a[0][i], a[1][i], a[2][i]]
  return [a[j][i] for j in range(len(a))]

def test_get_column():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_column(a1,0) == [1,4,7])


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

def test_row_contains_only():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  assert(row_contains_only(a1,0,'X'))
  assert(not row_contains_only(a1,1,'X'))
  assert(not row_contains_only(a1,2,'X'))

def diag1_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links oben nach rechts unten geht, nur das Zeichen c enthält.'''
  return contains_only(get_diag1(a), c)

def diag2_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links unten nach rechts oben geht, nur das Zeichen c enthält.'''
  return contains_only(get_diag2(a), c)

def player_wins(a,c):
  '''Erwartet ein zweidimensionales Array a.
     Liefert True, wenn eine Zeile, Spalte oder Diagonale nur c enthält.
  '''
  rows = [get_row(a,i) for i in range(len(a))]
  cols = [get_column(a,i) for i in range(len(a))]
  diags = [get_diag1(a), get_diag2(a)]

  contains_only_c = lambda l: contains_only(l,c)
  return any_of(rows + cols + diags, contains_only_c)
  

def player_X_wins(a):
  return player_wins(a,'X')

def player_O_wins(a):
  return player_wins(a,'O')


def test_player_X_wins():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  # [TODO] Mehr Tests für Diagonalen und Spalten hinzufügen.
  assert(player_X_wins(a1))

  a2 = [['X',' ',' '],['X','O','O'],['X','O',' ']]
  assert(player_X_wins(a2))

  a3 = [['X',' ',' '],['X','X','O'],[' ','O','X']]
  assert(player_X_wins(a3))

  a4 = [[' ',' ','X'],['X','X','O'],['X','O',' ']]
  assert(player_X_wins(a4))

def test_player_O_wins():
  #[TODO]
  pass # Platzhalter: Statement, das nichts macht


test_contains_only()
test_get_row()
test_get_column()
test_row_contains_only()
test_player_X_wins()
test_player_O_wins()

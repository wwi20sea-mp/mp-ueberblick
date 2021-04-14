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

def row_contains_only(a,i,c):
  '''Erwartet ein zweidimensionales Array a, eine Zahl i
     und ein Zeichen c.
     Liefert True, wenn die i-te Zeile nur das Zeichen c enthält.
  '''
  return contains_only(get_row(a,i),c)

def test_row_contains_only():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  assert(row_contains_only(a1,0,'X'))
  assert(not row_contains_only(a1,1,'X'))
  assert(not row_contains_only(a1,2,'X'))

def player_X_wins(a):
  '''Erwartet ein zweidimensionales Array a.
     Liefert True, wenn eine Zeile nur 'X' enthält.
     [TODO]: Spalten und Diagonalen nachrüsten.
  '''
  return row_contains_only(a,0,'X') or row_contains_only(a,1,'X') or row_contains_only(a,2,'X')

def test_player_X_wins():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  # [TODO] Mehr Tests für Diagonalen und Spalten hinzufügen.
  assert(player_X_wins(a1))


test_contains_only()
test_get_row()
test_row_contains_only()

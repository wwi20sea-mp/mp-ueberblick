from arrayhelpers import contains_only, get_row, get_column, row_contains_only

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


def test_get_row():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_row(a1,0) == [1,2,3])


def test_get_column():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_column(a1,0) == [1,4,7])


def test_row_contains_only():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  assert(row_contains_only(a1,0,'X'))
  assert(not row_contains_only(a1,1,'X'))
  assert(not row_contains_only(a1,2,'X'))




def run_arrayhelpers_tests():
  test_contains_only()
  test_get_row()
  test_get_column()
  test_row_contains_only()

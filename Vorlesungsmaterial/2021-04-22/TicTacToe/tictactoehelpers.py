from arrayhelpers import any_of, contains_only, get_row, get_column, get_diag1, get_diag2

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

def draw(a):
  '''Liefert True, falls das Spiel beendet und unentschieden ist.'''
  #[TODO] Prüfen, ob das Spielfeld voll ist (nur noch 'X' oder 'O').
  return False

def board_to_string(b):
  lines = [" | ".join(line) for line in b]
  return "\n--+---+--\n".join(lines)

def move_allowed(spielfeld, row, col):
  '''Prüft, ob an Stelle (row,col) ein Zug gemacht werden darf.'''
  return row in range(len(spielfeld)) and col in range(len(spielfeld[row])) and spielfeld[row][col] == ' '

def game_finished(spielfeld):
  '''Liefert True, falls das Spiel zu Ende ist.'''
  return player_X_wins(spielfeld) or player_O_wins(spielfeld) or draw(spielfeld)
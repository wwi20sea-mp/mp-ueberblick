from tictactoehelpers import board_to_string

def set_char(a,row,col,c):
  '''Schreibt das Zeichen c in die angegebene Zeile und Spalte in a und liefert das neue Spielfeld zurück.'''
  # [TODO]
  return a

def get_human_player_input(a, spieler):
  '''Liest die Eingabe vom Spieler'''
  # [TODO]
  # - Eingabe überprüfen
  print("Spieler",spieler + ", Du bist am Zug.")
  row = int(input("Bitte eine Zeile wählen: "))
  col = int(input("Bitte eine Spalte wählen: "))

  return row,col

def game_round(a, spieler, get_next_player_input):
  ''' Führt eine einzelne Spielrunde durch.
      Erwartet ein Spielfeld und den Spieler, der am Zug ist.
      Liefert das neue Spielfeld zurück und den Spieler, der als nächstes am Zug ist.

      Spielfeld: 2D-Array.
      Spieler: String, 'X' oder 'O' '''

  # [TODO]
  # - Spielfeld anzeigen.
  print(board_to_string(a))
  # - Spielereingabe einlesen.
  row, col = get_next_player_input(a,spieler)
  # - Spielzug durchführen.
  new_board = set_char(a,row,col,spieler) # TODO
  
  return new_board, 'O' if spieler == 'X' else 'X'

def game_loop(a):
  ''' Führt so lange Spielrunden aus, bis das Spiel beendet ist. '''
  # [TODO]
  spieler = 'X'
  
  # Wiederholen, bis das Spiel zu Ende ist.
  a,spieler = game_round(a, spieler, get_human_player_input) 

def run_tictactoe():
  # [TODO]
  a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  game_loop(a)

if __name__ == '__main__':
  run_tictactoe()


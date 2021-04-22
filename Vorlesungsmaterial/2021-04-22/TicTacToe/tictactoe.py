from tictactoehelpers import board_to_string, move_allowed, game_finished
from arrayhelpers import set_char

def get_ai_input(spielfeld, spieler):
  '''Liefert den nächsten Zug des KI-Spielers.'''
  # [TODO]

  # 1. Möglichkeit: Zufällige Koordinaten generieren und prüfen, ob sie gültig sind.
  #                 So lange, bis sie gültig sind.

  # 2. Möglichkeit:
  # - Prüfen, ob wir selbst gewinnen können und das ggf. tun.
  # - Prüfen, ob der Gegenspieler gewinnen kann und das mit dem
  #   eigenen Zug möglichst verhindern.

  # 3. Möglichkeit:
  # - Alle gültigen Züge aufzählen, die man jetzt machen könnte.
  # - Das Spiel ab dort simulieren.
  
  return 0,0



def get_human_player_input(spielfeld, spieler):
  '''Liest die Eingabe vom Spieler'''
  # [TODO]
  # - Eingabe überprüfen
  print("Spieler",spieler + ", Du bist am Zug.")
  row = int(input("Bitte eine Zeile wählen: "))
  col = int(input("Bitte eine Spalte wählen: "))

  if move_allowed(spielfeld, row, col):
    return row,col
  
  print("Die Eingabe war ungültig.")
  print("Bitte noch einmal versuchen.")
  print()

  return get_human_player_input(spielfeld, spieler)

def game_round(spielfeld, spieler, get_next_player_input):
  ''' Führt eine einzelne Spielrunde durch.
      Erwartet ein Spielfeld und den Spieler, der am Zug ist.
      Liefert das neue Spielfeld zurück und den Spieler, der als nächstes am Zug ist.

      Spielfeld: 2D-Array.
      Spieler: String, 'X' oder 'O' '''

  # - Spielfeld anzeigen.
  print(board_to_string(spielfeld))
  # - Spielereingabe einlesen.
  row, col = get_next_player_input(spielfeld,spieler)
  # - Spielzug durchführen.
  new_board = set_char(spielfeld,row,col,spieler) # TODO
  
  return new_board, 'O' if spieler == 'X' else 'X'

def game_loop(spielfeld, get_player_X_input, get_player_O_input, spieler = 'X'):
  ''' Führt so lange Spielrunden aus, bis das Spiel beendet ist. '''  
  # Wiederholen, bis das Spiel zu Ende ist.

  get_player_input = get_player_X_input if spieler == 'X' else get_player_O_input
  spielfeld, spieler = game_round(spielfeld, spieler, get_player_input)

  if game_finished(spielfeld):
    print(board_to_string(spielfeld))
    return spielfeld
  
  return game_loop(spielfeld, get_player_X_input, get_player_O_input, spieler)

def run_tictactoe():
  spielfeld = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

  # Variante mit zwei menschlichen Spielern.
  #spielfeld = game_loop(spielfeld, get_human_player_input, get_human_player_input)

  # Variante mit Spieler O als Computerspieler
  spielfeld = game_loop(spielfeld, get_human_player_input, get_ai_input)


if __name__ == '__main__':
  run_tictactoe()


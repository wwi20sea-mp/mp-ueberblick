from tictactoe import game_loop

def test_game_loop():
  spielfeld = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  
  moves_x = [(1,1),(2,2),(0,0)]
  moves_x = iter(moves_x)
  moves_o = [(0,1),(1,2),(2,0)]
  moves_o = iter(moves_o)

  spielfeld = game_loop(spielfeld, lambda s,x : next(moves_x), lambda s,o : next(moves_o))

def run_tictactoe_tests():
  test_game_loop()
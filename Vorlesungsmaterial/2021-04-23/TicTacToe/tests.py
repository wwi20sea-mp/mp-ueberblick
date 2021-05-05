from test_arrayhelpers import run_arrayhelpers_tests
from test_tictactoehelpers import run_tictactoehelpers_tests
from test_tictactoe import run_tictactoe_tests

def run_tests():
  run_arrayhelpers_tests()
  run_tictactoehelpers_tests()
  run_tictactoe_tests()

if __name__ == '__main__':
  run_tests()
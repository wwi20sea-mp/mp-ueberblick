

a1 = [["1","2","3"],["4","5","6"],["7","8","9"]]

a2 = ["1","2","3"]

print(a2)

line = " | ".join(a2)

print(line)

lines = [" | ".join(line) for line in a1]

print(lines)

board = "\n--+---+--\n".join(lines)

print(board)

def board_to_string(b):
  lines = [" | ".join(line) for line in b]
  return "\n--+---+--\n".join(lines)

print(board_to_string(a1))
print(board_to_string([[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]))
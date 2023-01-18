class Sudoku:

  def __init__(self, board):
    self.board = board

  def print_board(self):
    return self.board

  def get_row(self, row):
    return self.board[row]

  def get_col(self, col):
    col = []
    for i in self.board:
      col.append(i[col])
    return col

  def get2x2(self, row, col):
    if row <= 1 and col <= 1:
      maximum = 1
      table2x2 = []

      for i in range(2):
        table2x2.append([self.board[i][:maximum]])

      return table2x2

    if row <= 1 and col > 1:
      maximum = 1
      table2x2 = []

      for i in range(2, 4):
        table2x2.append([self.board[i][:maximum]])

      return table2x2
    
    if row > 1 and col > 1:
      minimum = 2
      maximum = 4
      table2x2 = []

      for i in range(2, 4):
        table2x2.append([self.board[i][minimum:maximum]])

      return table2x2

    if row > 1 and col <= 1:
      minimum = 2
      maximum = 4
      table2x2 = []

      for i in range(2):
        table2x2.append([self.board[i][minimum:maximum]])

      return table2x2

  def is_allowed(self, row, col, value):

    row = self.get_row(row)
    col = self.get_row(col)
    table2x2 = self.get2x2(row, col)

    print(row)
    print(col)
    print(table2x2)


  # helper method - is sudoku solved?
  def is_filled(self):
    pass

  # alternative to the above method - find the first empty cell if exists
  # useful for automatic solver
  def find_first_empty_cell(self):
    pass

  def get_dead_cell(self):
    pass

  def add_player_number(self):
    pass

  def play(self):
    user_input = input("Zadej hodnoty: radek, sloupec a cislo k zapsani, oddelene mezerou, napr. 2 4 3: ")
    user_input = user_input.split(' ')
    
    self.is_allowed(int(user_input[0]), int(user_input[1]), int(user_input[2]))

  def solve_board(self):
    pass

if __name__ == "__main__":

  # Test 1. Let the user solve an "easy" sudoku
  sudoku1 = Sudoku(
   [[0, 2, 1, 0],
    [0, 4, 2, 3],
    [2, 3, 4, 0],
    [4, 0, 3, 2]]
  )
  sudoku1.play()

  # # Test 2. Let the user solve a "very hard" sudoku
  # sudoku2 = Sudoku(
  #  [[0, 0, 4, 0],
  #   [3, 0, 0, 0],
  #   [0, 0, 3, 1],
  #   [0, 3, 0, 4]]
  # )
  # sudoku2.play()

  # # Test 3. Automatically solves a "very hard" sudoku
  # sudoku3 = Sudoku(
  #  [[0, 0, 4, 0],
  #   [3, 0, 0, 0],
  #   [0, 0, 3, 1],
  #   [0, 3, 0, 4]]
  # )
  # sudoku3.solve_board()

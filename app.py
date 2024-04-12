from game import TicTacToe

class TicTacToeApp:
    def __init__(self):
        self.game = None

    def start(self):
        num_players = int(input("Enter the number of players (2-4): "))
        player_names = [input(f"Enter player {i + 1} name: ") for i in range(num_players)]
        grid_size = int(input("Enter grid size (5-25): "))
        player_symbols = input("Enter player symbols separated by space: ").split()

    def game_loop(self):
        while True:
            # Display the current board state
            self.display_board()
            # Current player makes a move
            print(f"{self.game.current_player}'s turn ({self.game.player_symbols[self.game.current_player]}).")
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1

            result, winner, winning_cells = self.game.make_move(row, col)

    def display_board(self):
        for row in self.game.board:
            print(' | '.join([cell if cell else ' ' for cell in row]))
          #  print('-' * (self.game.grid_size * 4 - 1))


#app = TicTacToeApp()
#app.start()

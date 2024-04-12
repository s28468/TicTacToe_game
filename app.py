from game import TicTacToe

class TicTacToeApp:
    def __init__(self):
        self.game = None

    def start(self):
        num_players = int(input("Enter the number of players (2-4): "))
        player_names = [input(f"Enter player {i + 1} name: ") for i in range(num_players)]
        grid_size = int(input("Enter grid size (5-25): "))
        player_symbols = input("Enter player symbols separated by space: ").split()

        if len(player_symbols) != num_players:
            print("The number of symbols does not match the number of players. Assigning default symbols.")
            player_symbols = None

        self.game = TicTacToe(num_players, player_names, grid_size, player_symbols)


        self.game_loop()

    def game_loop(self):
        while True:

            self.display_board()

            print(f"{self.game.current_player}'s turn ({self.game.player_symbols[self.game.current_player]}).")
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1

            result, winner, winning_cells = self.game.make_move(row, col)

            if result == 'win':
                self.display_board()
                print(f"Congratulations {winner}, you have won the game!")
                break
            elif result == 'draw':
                self.display_board()
                print("The game is a draw.")
                break
            elif result == 'occupied':
                print("That cell is already occupied, try a different move.")
            else:
                print("Move made successfully.")

    def display_board(self):
        for row in self.game.board:
            print(' | '.join([cell if cell else ' ' for cell in row]))
            print('-' * (self.game.grid_size * 4 - 1))


app = TicTacToeApp()
app.start()
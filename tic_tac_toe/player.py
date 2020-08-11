from colorama import init, Fore, Style
init(autoreset=True)


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def input_mark(self):
        """Handles the players inputting their mark"""
        while True:
            position = input(Fore.LIGHTGREEN_EX + f"{self.symbol}'s turn:")
            if position in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return position, self.symbol  # Return the position, player symbol
            else:
                print(Fore.LIGHTRED_EX + "You tried to enter a position not indicated in the board!")
                continue  # If a player enters a wrong board  position,  allow them to enter a again

    @staticmethod
    def place_mark(player_input, board=None):
        """Finds the index of a position in the board matrix and inserts the player symbol
        Args:
            board: This is the board matrix of the Game Class
            player_input: This is a tuple returned by the input_mark class of the Player Class.e.g (8,'X').
                  8 indicates the board position and 'X' the player symbol.

        Returns:
            board.index(sublist): The index of the sublist(within the board matrix) where the player symbol is placed.
            i: The index of the symbol within the above sublist.
            False: If the position in the mark argument is already taken

        """
        if board is None:
            board = []
        for sublist in board:
            for i, num in enumerate(sublist):
                if sublist[i] == player_input[0]:
                    sublist[i] = player_input[1]
                    return board.index(sublist), i
            else:
                continue
        else:  # If player tries to enter a position already taken previously they are allowed  to enter again
            print(Fore.LIGHTRED_EX + "You tried  to take a position already taken  previously!")
            return False





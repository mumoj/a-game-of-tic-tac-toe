"""This module defines the Game class"""

from colorama import init, Style


init(autoreset=True) # Initializes the colorama class


class Game:
    def __init__(self, board=None):
        if board is None:
            board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.board = board

    def show_board(self):
        """Displays the board from the board matrix"""
        print(Style.DIM + "\n {0:^5}|{1:^5}|{2:^5}\n\n".format(self.board[0][0], self.board[0][1], self.board[0][2]),
              Style.DIM + "{0:^5}|{1:^5}|{2:^5}\n\n".format(self.board[1][0], self.board[1][1], self.board[1][2]),
              Style.DIM + "{0:^5}|{1:^5}|{2:^5}".format(self.board[2][0], self.board[2][1], self.board[2][2])
              )

    def determine_win(self, mark_indices):
        """Determines whether there is a win or not after a move
        Args:
             mark_indices:A tuple indicating the sublist in which a player symbol is placed, and the index of that
             symbol within the sublist.
        Returns:
            True: A win is found
            False: A win is not found
        """
        sublist_index = mark_indices[0]
        marker_index = mark_indices[1]
        sublist_len = len(self.board[sublist_index])

        if len(set(self.board[sublist_index])) == 1:  # Check for an horizontal win
            return True

        elif len(set([sublist[marker_index] for sublist in self.board])) == 1:  # Check for a vertical win
            return True

        elif marker_index == sublist_index:
            if len(set([self.board[i][i] for i in range(sublist_len)])) == 1:  # Check for a diagonal win
                return True
            else:
                return False

        elif marker_index == (sublist_len - 1 - sublist_index):  # Check for reverse diagonal win
            if len(set([self.board[sublist_len - 1 - i][i] for i in range(sublist_len - 1, -1, -1)])) == 1:
                return True
            else:
                return False

        else:
            return False

    def determine_draw(self):
        """ Determines whether there is draw or not after a move.It checks fot a blank position in all sublists
        of the board matrix.
        Returns:
            True: A draw found.
            False: A draw not found
        """
        for sublist in self.board:

            for item in sublist:
                if item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return False
                else:
                    continue
        else:
            return True

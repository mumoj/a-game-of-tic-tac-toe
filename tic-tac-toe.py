# *********************A PYTHON SCRIPT FOR PLAYING TIC TAC TOE ON COMMAND LINE *****************************************


def show_board(board):  # A function to display the board from the board matrix
    print("\n {0:^5}|{1:^5}|{2:^5}\n".format(board[0][0], board[0][1], board[0][2]),
          "{0:^5}|{1:^5}|{2:^5}\n".format(board[1][0], board[1][1], board[1][2]),
          "{0:^5}|{1:^5}|{2:^5}".format(board[2][0], board[2][1], board[2][2]))


def initial_player():  # Determine the first player
    first_player = input("Play as either 'X' or 'O':")
    if first_player in ('X', 'O'):
        if first_player == 'X':
            return True
        if first_player == 'O':
            return False
    else:
        print("Please enter either 'X' or 'O'.")
        return initial_player()  # Recursively run the function until users enter appropriate symbol


def change_turns(player):  # Change players after a move
    players = ('X', 'O')

    def input_mark(player_on_turn):  # Handle input of board places
        position = input(f"{player_on_turn}'s turn:")
        if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return position, player_on_turn, player  # Return the position, the player symbol, and the player  boolean
        else:
            print("You tried to enter a position not indicated in the board!")
            return change_turns(player)  # If player enters a wrong board  position allow them to enter a again

    while player:  # Determine player symbol from the the player boolean
        player_name = players[0]
        return input_mark(player_name)
    while not player:
        player_name = players[1]
        return input_mark(player_name)


def place_mark(board, mark):  # Find the index of the symbol position in the board matrix and insert the player symbol
    for sublist in board:
        for i, num in enumerate(sublist):
            if sublist[i] == mark[0]:
                sublist[i] = mark[1]
                return board.index(sublist), i
        else:
            continue
    else:  # If player tries to enter a position already taken previously they are allowed  to enter again
        print("You tried  to take a position already taken  previously!")
        mark = change_turns(mark[2])
        return place_mark(board, mark)


def determine_win(board, mark_position):  # Determine whether there is a win or not after a move
    sublist_index = mark_position[0]
    marker_index = mark_position[1]
    sublist_len = len(board[sublist_index])
    if len(set(board[sublist_index])) == 1:  # Check for an horizontal win
        return True
    elif len(set([sublist[marker_index] for sublist in board])) == 1:  # Check for a vertical win
        return True
    elif marker_index == sublist_index:
        if len(set([board[i][i] for i in range(sublist_len)])) == 1:  # Check for a diagonal win
            return True
        else:
            return False
    elif marker_index == (sublist_len - 1 - sublist_index):  # Check for reverse diagonal win
        if len(set([board[sublist_len - 1 - i][i] for i in range(sublist_len - 1, -1, -1)])) == 1:
            return True
        else:
            return False
    else:
        return False


def determine_draw(board):  # Determine whether there is draw or not after a move
    for sublist in board:
        for item in sublist:
            if item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
            else:
                continue  # Check all lists in the board matrix for a position, if there is, a draw has not happened.
        else:
            return True  # In case a win didn't happen, and there are no more numbered positions,  it is a draw


def play(board, player):  # Play the game by running the relevant functions
    show_board(board)
    mark = change_turns(player)
    mark_position = place_mark(board, mark)
    result = determine_win(board, mark_position)
    draw = determine_draw(board)
    if draw:
        print("A DRAW.Game over.")
        show_board(board)  # On draw, show the final board
    else:
        if not result:  # If a win or a draw hasn't occurred, the player boolean changes and the next player moves
            player = not player
            return play(board, player)
        else:
            print("CHECKMATE! Game Over.")
            show_board(board)  # On win, show the final board


print("\n *********************A PYTHON SCRIPT FOR PLAYING TIC TAC TOE ON COMMAND LINE ******************************\n"
      "To play, the first player must first choose their playing symbol('X' or 'O'), then\n"
      "proceed to enter a position indicated on the board using the respective keyboard key to place their symbol.\n"
      "The game shall then turn to the next player after such a move.Welcome.\n")

play(board=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], player=initial_player())

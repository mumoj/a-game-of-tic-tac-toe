"""This is  module runs the game"""
import sys
from colorama import init, Fore, Style
from tic_tac_toe.player import Player
from tic_tac_toe.game import Game


init(autoreset=True)


def initial_player():
    """Determines the first player

    first_player: First player inputs their symbol
    Returns:
        [True,X]:If the first player choose 'X'
        [True,O]: If the second player chooses 'Y'

    """
    while True:
        first_player = input("Play as either 'X' or 'O':").upper()
        if first_player in ('X', 'O'):
            if first_player == 'X':
                return [True, 'X']
            if first_player == 'O':
                return [True, 'O']
        else:
            print(Fore.YELLOW + "Please enter either 'X' or 'O'.")
            continue


def change_turns(the_player):
    """ switches players after a move.
    Args:
        the_player:This is the  player  whose turn it currently is.
    Returns:
        A False boolean is also returned to help switch players in a while loop.
        '[False, X]: The player symbol and   a False boolean returned if the argument was player '0'
        '[False, O]':  The player symbol and a False boolean returned if the argument was player 'X'

    """

    if the_player == 'X':
        return [False, 'O']
    if the_player == 'O':
        return [False, 'X']


def exit_condition():
    """Evaluates weather the user wants to restart game or exit
     exit_game = Prompts the user to restart or exit
     Returns:
         True:If the user input indicates restart
         False:If the use input indicates exit

    """
    while True:
        exit_game_option = input(Fore.LIGHTGREEN_EX + "Press Y to restart game or N to exit:").upper()
        if exit_game_option in ("Y", "N"):
            if exit_game_option == 'Y':
                return True

            if exit_game_option == 'N':
                return False
        else:
            continue


if __name__ == '__main__':
    NEW_GAME = True
    while NEW_GAME:

        print(Fore.LIGHTYELLOW_EX +
              "\n ***************A PYTHON SCRIPT FOR PLAYING TIC TAC TOE ON COMMAND LINE ************\n"
              "To play, the first player must first choose their playing symbol('X' or 'O') .\n"
              "They must then proceed to enter a number position as indicated on the game board \n"
              "in order to place their symbol .\n"
              "The game shall then turn to the next player after such a move.Welcome Mates!\n"
              "\n ************************************************************************************\n")

        the_game = Game()  # Initialize the Game

        player_on_turn = initial_player()  # Allow the first user to choose their symbol
        while player_on_turn[0]:

            the_game.show_board()  # After a move show the game board

            player = Player(symbol=player_on_turn[1])  # Allow a player to place their mark in a board position
            player_input = player.input_mark()
            mark_indices = player.place_mark(player_input, board=the_game.board)

            while not mark_indices:
                # In case a player  enters an already taken position,lin allow them to take another position
                player_input = player.input_mark()
                mark_indices = player.place_mark(player_input, board=the_game.board)

            if the_game.determine_win(mark_indices):  # In case of a win, end game.
                print(Fore.LIGHTGREEN_EX, Style.BRIGHT+"\nGet in there! You Win!")
                the_game.show_board()
                break

            if the_game.determine_draw():  # If a draw happens, end game
                print(Fore.LIGHTGREEN_EX, Style.BRIGHT+"\n Keep up mates, A Draw")
                the_game.show_board()
                break

            player = change_turns(player_on_turn[1])  # Switch players after a move is made
            player_on_turn = player
            player_on_turn[0] = True

        print(Fore.LIGHTYELLOW_EX +
              "\n****************************************************************************")
        NEW_GAME = False

        print(Style.BRIGHT+"Do you want to restart game?")
        if exit_condition():
            NEW_GAME = True  # Restart game if user so desires
        else:
            sys.exit(Fore.LIGHTYELLOW_EX+"Adios Mates!")  # Exit game if use so desires


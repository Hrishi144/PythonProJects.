"""
Tic-Tac-Toe Game in Python

This is a simple implementation of the classic Tic-Tac-Toe game.
The game is played on a 3x3 grid where two players take turns marking 'X' and 'O'.
The first player to align three marks in a row, column, or diagonal wins.
If the grid is full and no player has won, the game results in a draw.
"""

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|",board[3*i], "|", board[3*i+1], "|", board[3*i+2], "|")
        print("-------------")
def check_win (board,mark):
    win_conditions=[
        (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
    ]       
    for condition in win_conditions:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]==mark:
            return True
    return False
def Tic_tac_toe():
        board=[" "]*9
        current_player="X"
        move=0
        while True:
            print_board(board)
            try:
                move=int(input(f"player{current_player},Enter your move(1-9)"))-1
                if move<0 or move >8:
                    print("Enter a valid move b/w 1-9")
                    continue
                if board[move]!=" ":
                    print("The space is already taken.Try another move")
                    continue
                board[move]=current_player
                move+=1
                

                if check_win(board,current_player):
                    print_board(board)
                    print(f"player {current_player} wins")
                    break

                current_player="O" if current_player=="X" else "X"

            except ValueError:print("Invalid input.Enter a number b\w 1 and 9")

Tic_tac_toe()


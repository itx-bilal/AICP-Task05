def print_board(board):
    for i,row in enumerate(board):
        print(" | ".join(row))
        if i < len(board)-1:
            print("-" * 10)
            
            
def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=' ' or \
            board[0][i]==board[1][i]==board[2][i]!=' ':
                return True
            
    if board[0][0]==board[1][1]==board[2][2]!=' ' or \
        board[0][2]==board[1][1]==board[2][0]!=' ':
            return True
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell==' ':
                return False
    return True


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0,1,2): "))
        col = int(input(f"Player {player}, enter column (0,1,2): "))
        
        if 0 <= row < 3 and 0 <=col < 3 and board[row][col]==' ':
            board[row][col] = player
            
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            player = 'O' if player == 'X' else 'X'
            
        else:
            print("Invalid move. Try again!")
            
if __name__ == "__main__":
    tic_tac_toe()
                
from chessPlayerNew import *
board = genBoard()
while True:
    print("11")
    printBoard()
    print("1")
    anton = chessPlayerA(board, 10)
    board[anton[1][1]] = anton[daniel[1][0]]
    board[anton[1][0]] = 0

    printBoard()
    print("2")
    daniel = chessPlayerA(board, 20)
    board[daniel[1][1]] = board[daniel[1][0]]
    board[daniel[1][0]] = 0

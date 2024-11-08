def solution(N, K, board):
  for i in range(N):
      for _ in range(K):
          for j in range(N):
              print((str(board[i][j]) + " ") * K, end="")
          print()

solution(3, 3, [
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1],
])
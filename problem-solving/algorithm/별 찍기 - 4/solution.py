def solution(n):
  for i in range(0,n):
    for j in range(0, i):
      print(" ",end="")
    for j in range(i, n):
      print("*",end="")
    print("")
    
solution(4)
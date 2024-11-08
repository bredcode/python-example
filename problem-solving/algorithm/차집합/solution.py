nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = sorted(A - B) # sorted(A.difference(B))

if len(result) == 0:
  print(0)
else:
  print(len(result))
  print(result)
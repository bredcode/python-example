# 문제 1번
numbers = [1,2,3,4,5]

ret = list(map(lambda x: x * x, numbers))
print(ret)

# 문제 2번
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ret = list(filter(lambda x: x % 2 == 1, numbers))
print(ret)

# 문제 3번
words =  ["apple", "banana", "cherry", "date"]

ret1 = list(map(lambda x: len(x), words))
ret2 = list(filter(lambda x: len(x) >= 5, words))

print(ret1)
print(ret2)

# 문제 4번
def isPrime(x):
  chk = True
  for i in range(2, x):
    if x % i == 0 and i != x:
      chk = False
  
  return chk

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

ret = list(filter(lambda x: isPrime(x), numbers))

print(ret)
def solution(numbers, k):
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  k = 3

  result = []

  for i in range(0, len(numbers), k):
      part = numbers[i:i+k]
      part.reverse()

      for element in part:
          result.append(element)
      
  print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
solution(numbers, k)
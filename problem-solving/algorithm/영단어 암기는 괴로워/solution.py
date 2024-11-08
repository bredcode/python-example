def solution(N, M):
  wordList = {}

  for i in range(N):
      word = input()
      
      if len(word) < M:
          continue
      else:
          if word in wordList:
              wordList[word] += 1
          else:
              wordList[word] = 1

  wordList = sorted(wordList.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수

  # [('sand', 3), ('apple', 2), ('append', 1)]
  for i in wordList:
      print(i[0])

solution(7, 4)
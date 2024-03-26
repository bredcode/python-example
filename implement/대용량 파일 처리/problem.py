### 문제 풀이에 사용되는 데이터 생성을 위해 해당 부분을 지우지 마세요
import diary

FILE_NAME = "diary.txt"
diary_ans = diary.create_diary(FILE_NAME)
###

def solution():
  ans = {}

  return diary_ans == ans

ret = solution()

print("정답" if ret == True else "오답")
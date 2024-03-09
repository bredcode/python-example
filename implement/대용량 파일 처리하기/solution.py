### 문제 풀이에 사용되는 데이터 생성을 위해 해당 부분을 지우지 마세요
import diary

FILE_NAME = "diary.txt"
diary_ans = diary.create_diary(FILE_NAME)
###

def solution():
  ans = {}

  with open(FILE_NAME, "r", encoding="utf-8") as file:
      for line in file:
          if "행복" in line:
            ans.setdefault("행복", 0)
            ans["행복"] += 1
          elif "슬픔" in line:
            ans.setdefault("슬픔", 0)
            ans["슬픔"] += 1
          elif "기쁨" in line:
            ans.setdefault("기쁨", 0)
            ans["기쁨"] += 1
          elif "분노" in line:
            ans.setdefault("분노", 0)
            ans["분노"] += 1

  return diary_ans == ans

ret = solution()

print("정답" if ret == True else "오답")
"""
 문제를 푸는 동안은 이 코드를 참조하지 마세요.
 실력향상에 도움되지 않습니다.
"""
import random
from datetime import datetime, timedelta

def create_diary(filename = "diary.txt"):
  LINES = 100000

  ans = {}

  start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
  emotions = ["행복", "슬픔", "기쁨", "분노"]
  with open(filename, "w", encoding="utf-8") as file:
    for i in range(LINES):
      date = start_date + timedelta(days=i)
      emotion = random.choice(emotions)

      ans.setdefault(emotion, 0)
      ans[emotion] += 1

      entry = f"{date} 오늘은 {emotion}한 하루였다.\n"
      file.write(entry)

  return ans


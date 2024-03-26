def solution(arr):
  arr = list(filter(lambda x: x["type"] == "planet", arr))
  arr = list(map(lambda x: x["dist"], arr))
  arr = sorted(arr, key=lambda x: abs(x))
  return arr[:3]

arr = [
  {"type": "planet", "dist": 10},
  {"type": "star", "dist": -3},
  {"type": "milkyway", "dist": 2},
  {"type": "planet", "dist": 5},
  {"type": "planet", "dist": -7},
  {"type": "star", "dist": 4},
  {"type": "planet", "dist": 6},
  {"type": "planet", "dist": -1},
  {"type": "star", "dist": 8},
  {"type": "milkyway", "dist": -9}
]

print(solution(arr))
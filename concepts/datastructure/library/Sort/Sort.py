# 1. 기본 정렬
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # 오름차순 정렬
print(numbers)  # [1, 2, 5, 5, 6, 9]

# 2. 내림차순 정렬
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)  # 내림차순 정렬
print(numbers)  # [9, 6, 5, 5, 2, 1]

# 3. 문자열 정렬
words = ["banana", "apple", "orange", "mango"]
words.sort()  # 알파벳 순으로 정렬
print(words)  # ['apple', 'banana', 'mango', 'orange']

# 4. [lambda] 문자열 길이 기준 정렬
words = ["banana", "apple", "orange", "kiwi"]
words.sort(key=lambda x: len(x))
print(words)  # ['kiwi', 'apple', 'banana', 'orange']

# 5.1. [lambda] 커스텀 튜플 정렬
points = [(1, 3), (4, 1), (5, 1), (5, 0)]
points.sort(key=lambda x: x[1])  # 두 번째 값을 기준으로 정렬
print(points)  # [(5, 0), (4, 1), (2, 2), (1, 3)]

# 5.2. [lambda] 커스텀 리스트 정렬
points = [[1, 3], [4, 1], [5, 1], [5, 0]]
points.sort(key=lambda x: x[1])  # 두 번째 값을 기준으로 정렬
print(points)  # [(5, 0), (4, 1), (2, 2), (1, 3)]

# 5.3. [lambda] 커스텀 튜플 정렬
points = [(1, 3), (4, 1), (5, 1), (5, 0)]
points.sort(key=lambda x: (x[1], -x[0]))  # 두 번째 값을 기준으로 오름차순 정렬, 만약 같다면 첫 번째 값을 기준으로 내림차순 정렬
print(points)  # [(5, 0), (4, 1), (2, 2), (1, 3)]

# 5.4. [lambda] 커스텀 튜플 정렬 
"""
Q. 첫 번째 값을 기준으로 오름차순 정렬, 
만약 같다면 세 번째 값을 기준으로 내림차순 정렬, 
만약 같다면 두 번째 값을 기준으로 내림차순 정렬
"""

points = [(1, 2, 3), (2, 3, 4), (1, 4, 5), (4, 3, 6), (1, 7, 5)]
points.sort(key=lambda x: (x[0], -x[2], -x[1])) 
print(points)  # [(5, 0), (4, 1), (2, 2), (1, 3)]

# 6. [lambda] 대소문자 구분 없이 정렬
words = ["banana", "Apple", "orange", "Mango"]
words.sort(key=lambda x: x.lower())  # 소문자로 변환하여 정렬
print(words)  # ['Apple', 'banana', 'Mango', 'orange']

# 6.1. [lambda] sorted를 이용한 대소문자 구분 없이 정렬
words = ["banana", "Apple", "orange", "Mango"]
sorted_words = sorted(words, key=lambda x: x.lower())  # numbers는 그대로 두고 정렬된 복사본 반환
print(words)  # [1, 2, 5, 5, 6, 9]
print(sorted_words)  # [5, 2, 9, 1, 5, 6] (원본 리스트는 그대로)

# 7. [lambda] 여러 기준으로 정렬
items = [("apple", 5), ("banana", 3), ("cherry", 5), ("date", 1)] # 첫 번째 기준: 수량 (내림차순), 두 번째 기준: 이름의 길이 (오름차순)
items.sort(key=lambda x: (-x[1], len(x[0])))
print(items)  # [('apple', 5), ('cherry', 5), ('banana', 3), ('date', 1)]

# 8. 역순 정렬
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [9, 6, 5, 5, 2, 1]

# 6.1. [lambda] 대소문자 구분 없이 역순 정렬
words = ["banana", "Apple", "orange", "Mango"]
words.sort(key=lambda x: x.lower(), reverse=True)  # 소문자로 변환하여 정렬
print(words)  # ['orange', 'Mango', 'banana', 'Apple']
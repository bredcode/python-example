# 두 집합 정의
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 합집합 (Union)
union_set = set1.union(set2)
print("합집합:", union_set)

# 교집합 (Intersection)
intersection_set = set1.intersection(set2)
print("교집합:", intersection_set)

# 차집합 (Difference)
difference_set = set1.difference(set2)
print("차집합:", difference_set)

# 대칭 차집합 (Symmetric Difference)
symmetric_difference_set = set1.symmetric_difference(set2)
print("대칭 차집합:", symmetric_difference_set)

class MergeSort:
    def merge(self, left, right):
        sorted_arr = []

        # left와 right를 비교하여 작은 값을 sorted_arr에 추가
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))

        # left 또는 right에 남아있는 원소를 모두 추가
        # 한쪽 리스트는 반드시 비어있게 됨
        return sorted_arr + left + right

    def sort(self, data):
        # 배열의 길이가 1이면 그대로 반환
        if len(data) == 1:
            return data

        # 배열을 반으로 나눔
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # 재귀적으로 분할한 후 병합
        return self.merge(self.sort(left), self.sort(right))


# 사용 예제
merge_sort = MergeSort()
arr = [29, 10, 14, 37, 8, 27]
print("Original array:", arr)
sorted_arr = merge_sort.sort(arr)
print("Sorted array:", sorted_arr)

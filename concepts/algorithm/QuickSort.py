class QuickSort:
    def sort(self, data, start, end):
        if start >= end:  # 종료 조건
            return

        left = start
        right = end

        pivot = data[left]

        # 오른쪽 값이 pivot보다 작으면 pivot 왼쪽으로, 왼쪽 값이 pivot보다 크면 pivot 오른쪽으로
        while left < right:
            # 피벗값보다 right 값이 큰 경우에는 right가 왼쪽으로 이동
            while data[right] >= pivot and right > left:
                right -= 1

            # 그렇지 않은 경우에는 left 위치에 right 값을 대입
            data[left] = data[right]

            # 피벗값보다 left 값이 작은 경우에는 left가 오른쪽으로 이동
            while data[left] <= pivot and left < right:
                left += 1

            # 그렇지 않은 경우에는 right 위치에 left 값을 대입
            data[right] = data[left]

        # left와 right가 만나는 지점이 pivot 값이 들어가는 위치
        if left == right:
            data[left] = pivot
            self.sort(data, start, right - 1)
            self.sort(data, left + 1, end)

        return data

# 사용 예시
quick_sort = QuickSort()
arr = [6, 8, 3, 2, 4, 5, 1, 7]
print("원래 배열:", arr)

sorted_arr = quick_sort.sort(arr, 0, len(arr) - 1)
print("정렬된 배열:", sorted_arr)

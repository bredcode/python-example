class BubbleSort:
    def sort(self, data):
        length = len(data)
        # 각 회전을 의미
        for i in range(length):
            for j in range(length - i - 1):
                if data[j] > data[j + 1]:
                    # Swap
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data

"""
  만약 버블 정렬에서 반복문 내에서 swap이 발생하지 않는다면
  모두 정렬된 것이나 마찬가지므로 더이상 버블소트를 진행하지 않아도 된다.
"""
class AdvancedBubbleSort:
    def sort(self, data):
        length = len(data)
        is_swap = False

        for i in range(length):
            is_swap = False
            for j in range(length - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    is_swap = True

            if not is_swap:
                break

        return data

# 기본 버블 정렬 사용 예시
bubble_sort = BubbleSort()
arr = [28, 10, 14, 37, 8, 27]
print("원래 배열:", arr)
sorted_arr = bubble_sort.sort(arr)
print("정렬된 배열:", sorted_arr)

# 고급 버블 정렬 사용 예시
advanced_bubble_sort = AdvancedBubbleSort()
arr = [28, 10, 14, 37, 8, 27]
print("원래 배열:", arr)
sorted_arr = advanced_bubble_sort.sort(arr)
print("정렬된 배열:", sorted_arr)

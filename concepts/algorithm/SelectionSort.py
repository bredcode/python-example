class SelectionSort:
    def sort(self, data):
        length = len(data)

        # 선택 정렬에서 N - 1회전이 종료되면 마지막 데이터도 자동 정렬이 완료되기에 length - 1
        for i in range(length - 1):
            min_idx = i  # i회전에 i번째 원소가 최솟값임을 가정

            for j in range(i + 1, length):
                if data[min_idx] > data[j]:
                    min_idx = j

            # 최솟값이 있는 index를 찾으면 해당 min_idx와 현재 위치 i를 swap
            data[i], data[min_idx] = data[min_idx], data[i]

        return data


selection_sort = SelectionSort()
arr = [28, 10, 14, 37, 8, 27]
print("Original array:", arr)
sorted_arr = selection_sort.sort(arr)
print("Sorted array:", sorted_arr)

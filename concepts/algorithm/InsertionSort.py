class InsertionSort:
    def sort(self, data):
        length = len(data)

        # 삽입 정렬은 두 번째 원소부터 시작
        for i in range(1, length):
            target = data[i]
            target_idx = i

            # 이미 정렬된 0~i-1번 인덱스 사이에서
            # target보다 큰 값을 한칸씩 뒤로 밀기
            # i-1부터 0번 인덱스까지 -1씩 진행
            for j in range(i - 1, -1, -1):
                if data[j] > target:
                    target_idx = j
                    data[j + 1] = data[j]
                else:
                    break

            # target 데이터를 삽입
            data[target_idx] = target

        return data


# 사용 예제
insert_sort = InsertionSort()
arr = [28, 10, 14, 37, 8, 27]
print("Original array:", arr)
sorted_arr = insert_sort.sort(arr)
print("Sorted array:", sorted_arr)
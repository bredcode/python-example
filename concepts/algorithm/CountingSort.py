class CountingSort:
    def sort(self, data):
        # data 배열에서 가장 큰 수를 찾아야 함
        max_value = max(data)
        # countingArr 배열을 0으로 초기화된 배열로 생성 (크기는 max_value + 1)
        counting_arr = [0] * (max_value + 1)

        # 현재 값을 토대로 counting_arr의 인덱스 위치에 값을 +1 해준다
        for num in data:
            counting_arr[num] += 1

        # counting_arr의 값이 1 이상일 때
        # 해당 인덱스 값을 data에 넣어주면 정렬이 완료
        idx = 0
        for i in range(len(counting_arr)):
            if counting_arr[i] > 0:
                for _ in range(counting_arr[i]):
                    data[idx] = i
                    idx += 1

        return data

# 사용 예시
counting_sort = CountingSort()
arr = [1, 2, 2, 3, 2, 8, 7, 9, 7, 9]
print("원래 배열:", arr)
sorted_arr = counting_sort.sort(arr)
print("정렬된 배열:", sorted_arr)

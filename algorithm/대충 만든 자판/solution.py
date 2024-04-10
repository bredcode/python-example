def solution(keymap, targets):
    # 각 키의 최소 이동횟수를 가진 딕셔너리
    min_map = {}

    # 각 문자열을 순회하면서 딕셔너리에 최소 이동횟수를 갱신
    for str in keymap:
        for i, ch in enumerate(str):
            if ch not in min_map:
                min_map[ch] = i + 1
            else:
                min_map[ch] = min(min_map[ch], i + 1)

    # targets의 문자열이 만들어질 수 있는지 min_map을 통해 계산
    answer = []
    for str in targets:
        count = 0
        for ch in str:
            if ch not in min_map:
                count = -1
                break
            else:
                count += min_map[ch]

        answer.append(count)

    return answer

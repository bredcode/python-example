def solution(text, word):
    cnt = 0
    before = text
    cur = text
    while True:
        cur = before.replace(word, "", 1)
        print(before, cur)
        if cur != before:
            cnt += 1
            before = cur
        else:
            break

    return cnt

print(solution("ababababa", "aba"))
print(solution("a a a a a", "a a"))
print(solution("ababababa", "ababa"))
print(solution("aaaaaaa", "aa"))
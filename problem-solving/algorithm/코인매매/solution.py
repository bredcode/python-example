import sys
input = sys.stdin.readline

N = int(input().strip())
prices = list(map(int, input().split()))

# 가장 비싼 날에 한번에 팔 수 있는 전략을 구성
def calc_profit(start, end):
    # 유효하지 않은 구간이면 0원
    if start >= end - 1:
        return 0
    
    # 1) 구간 내에서 '마지막에 등장하는' 최댓값 찾기
    max_price = -1
    max_idx = -1
    for i in range(start, end):
        if prices[i] >= max_price:
            max_price = prices[i]
            max_idx = i
    
    # 2) 매도일을 max_idx 로 잡으면 이전 날은 모두 매도일 보다 저렴한 날
    #    sum_profit 은 그날 팔았을 때의 수익 합
    sum_profit = 0
    buy_count = 0
    for i in range(start, max_idx):
        if prices[i] < max_price:
            sum_profit += (max_price - prices[i])  # (매도가 - 매수가)
            buy_count += 1
    
    # 산 코인이 1개 이상이었다면 수수료 1원 차감
    if buy_count > 0:
        sum_profit -= 1
    
    # 3) max_idx 이후 구간에 대해서도 재귀적으로 반복
    sum_profit += calc_profit(max_idx + 1, end)
    
    return sum_profit

answer = calc_profit(0, N)
print(answer)
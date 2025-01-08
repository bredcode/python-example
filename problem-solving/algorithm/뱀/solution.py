from collections import deque

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
APPLE = 2
SNAKE = 1
LAND = 0

def set_snake():
    global sy, sx, ans, dir, dq, arr
    if not (0 <= sy < n) or not (0 <= sx < n) or arr[sy][sx] == SNAKE:
        print(ans)
        exit(0)

    if arr[sy][sx] == APPLE:
        arr[sy][sx] = SNAKE
        dq.appendleft((sy, sx))
    elif arr[sy][sx] == LAND:
        arr[sy][sx] = SNAKE
        dq.appendleft((sy, sx))
        tail_y, tail_x = dq.pop()
        arr[tail_y][tail_x] = LAND

n = int(input())
k = int(input())
arr = [[LAND] * n for _ in range(n)]
sy, sx = 0, 0 # 뱀은 맨위 맨좌측에 위치
dq = deque()
dq.append((sy, sx)) # 뱀의 길이는 1
arr[sy][sx] = SNAKE
ans = 0
dir = RIGHT # 뱀은 처음에 오른쪽을 향함

for _ in range(k):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = APPLE

m = int(input())
commands = []
for _ in range(m):
    t, pos = input().split()
    commands.append((int(t), pos))

prev = 0

for t, pos in commands:
    move_time = t - prev

    for _ in range(move_time):
        ans += 1
        if dir == UP:
            sy -= 1
            set_snake()
        elif dir == DOWN:
            sy += 1
            set_snake()
        elif dir == LEFT:
            sx -= 1
            set_snake()
        elif dir == RIGHT:
            sx += 1
            set_snake()
    
    # 방향 전환
    if dir == UP and pos == 'L':
        dir = LEFT
    elif dir == UP and pos == 'D':
        dir = RIGHT
    elif dir == DOWN and pos == 'L':
        dir = RIGHT
    elif dir == DOWN and pos == 'D':
        dir = LEFT
    elif dir == LEFT and pos == 'L':
        dir = DOWN
    elif dir == LEFT and pos == 'D':
        dir = UP
    elif dir == RIGHT and pos == 'L':
        dir = UP
    elif dir == RIGHT and pos == 'D':
        dir = DOWN

    prev = t

# 명령이 끝난 후 벽이나 몸에 부딪힐 때까지 이동
while True:
    ans += 1
    if dir == UP:
        sy -= 1
        set_snake()
    elif dir == DOWN:
        sy += 1
        set_snake()
    elif dir == LEFT:
        sx -= 1
        set_snake()
    elif dir == RIGHT:
        sx += 1
        set_snake()

from collections import deque

# 방향 상수
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
APPLE, SNAKE, LAND = 2, 1, 0

def move_snake():
    #뱀을 한 칸 움직이고 게임 상태를 업데이트
    global sy, sx, ans, direction, snake, board

    # 다음 위치로 이동
    sy, sx = sy + dy[direction], sx + dx[direction]

    # 벽 또는 자신의 몸에 부딪히면 게임 종료
    if not (0 <= sy < n and 0 <= sx < n) or board[sy][sx] == SNAKE:
        print(ans)
        exit(0)

    # 사과가 있으면 몸 길이 유지
    if board[sy][sx] == APPLE:
        board[sy][sx] = SNAKE
        snake.appendleft((sy, sx))
    # 빈 칸이면 꼬리를 줄임
    else:
        board[sy][sx] = SNAKE
        snake.appendleft((sy, sx))
        tail_y, tail_x = snake.pop()
        board[tail_y][tail_x] = LAND

def change_direction(curr_dir, turn):
    #현재 방향과 회전 명령('L', 'D')에 따라 새로운 방향 반환
    if curr_dir == UP:
        return LEFT if turn == 'L' else RIGHT
    if curr_dir == DOWN:
        return RIGHT if turn == 'L' else LEFT
    if curr_dir == LEFT:
        return DOWN if turn == 'L' else UP
    if curr_dir == RIGHT:
        return UP if turn == 'L' else DOWN

# 입력 처리
n = int(input())
k = int(input())
board = [[LAND] * n for _ in range(n)]

# 사과 위치 설정
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = APPLE

# 방향 전환 명령 입력
m = int(input())
commands = [input().split() for _ in range(m)]
commands = [(int(t), pos) for t, pos in commands]

# 초기 설정
sy, sx = 0, 0
board[sy][sx] = SNAKE
snake = deque([(sy, sx)])
direction = RIGHT
ans = 0

# 방향 이동 배열 (UP, DOWN, LEFT, RIGHT)
dy = {UP: -1, DOWN: 1, LEFT: 0, RIGHT: 0}
dx = {UP: 0, DOWN: 0, LEFT: -1, RIGHT: 1}

prev_time = 0

# 명령 수행
for t, turn in commands:
    # 이동 시간 동안 뱀 이동
    for _ in range(t - prev_time):
        ans += 1
        move_snake()

    # 방향 전환
    direction = change_direction(direction, turn)
    prev_time = t

# 명령이 끝난 후 계속 이동
while True:
    ans += 1
    move_snake()

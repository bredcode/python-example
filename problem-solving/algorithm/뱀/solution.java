import java.util.*;

public class solution {

    // 방향 상수
    private static final int UP = 1;
    private static final int DOWN = 2;
    private static final int LEFT = 3;
    private static final int RIGHT = 4;
    private static final int APPLE = 2;
    private static final int SNAKE = 1;
    private static final int LAND = 0;

    private static int n, ans = 0, dir = RIGHT, sy = 0, sx = 0;
    private static int[][] arr;
    private static Deque<int[]> dq = new LinkedList<>(); // 뱀의 몸체를 관리
    private static List<int[]> commands;

    public void setSnake() {
        // 벽이나 자기 몸에 부딪힌 경우 게임 종료
        if (!(0 <= sy && sy < n && 0 <= sx && sx < n) || arr[sy][sx] == SNAKE) {
            System.out.println(ans);
            System.exit(0);
        }

        // 사과를 먹으면 뱀의 길이를 늘림
        if (arr[sy][sx] == APPLE) {
            arr[sy][sx] = SNAKE;
            dq.addFirst(new int[]{sy, sx});
        }
        // 빈 땅인 경우 머리를 이동시키고 꼬리를 제거
        else if (arr[sy][sx] == LAND) {
            arr[sy][sx] = SNAKE;
            dq.addFirst(new int[]{sy, sx});
            int[] tail = dq.removeLast();
            arr[tail[0]][tail[1]] = LAND;
        }
    }

    public void solve() {
        int prev = 0;

        // 명령 처리
        for (int[] command : commands) {
            int t = command[0];
            int turn = command[1];
            int moveTime = t - prev;

            // 이동 시간만큼 이동
            for (int i = 0; i < moveTime; i++) {
                ans++;
                if (dir == UP) {
                    sy--;
                } else if (dir == DOWN) {
                    sy++;
                } else if (dir == LEFT) {
                    sx--;
                } else if (dir == RIGHT) {
                    sx++;
                }
                setSnake();
            }

            // 방향 전환
            if (turn == -1) { // 왼쪽
                dir = (dir == UP) ? LEFT : (dir == LEFT) ? DOWN : (dir == DOWN) ? RIGHT : UP;
            } else if (turn == 1) { // 오른쪽
                dir = (dir == UP) ? RIGHT : (dir == RIGHT) ? DOWN : (dir == DOWN) ? LEFT : UP;
            }

            prev = t;
        }

        // 명령이 끝난 후 벽이나 몸에 부딪힐 때까지 이동
        while (true) {
            ans++;
            if (dir == UP) {
                sy--;
            } else if (dir == DOWN) {
                sy++;
            } else if (dir == LEFT) {
                sx--;
            } else if (dir == RIGHT) {
                sx++;
            }
            setSnake();
        }
    }

    public static void main(String[] args) {
        solution sol = new solution();
        Scanner sc = new Scanner(System.in);

        // 입력 처리
        n = sc.nextInt();
        int k = sc.nextInt();
        arr = new int[n][n];

        // 뱀의 초기 위치
        dq.add(new int[]{sy, sx});
        arr[sy][sx] = SNAKE;

        // 사과 위치 입력
        for (int i = 0; i < k; i++) {
            int y = sc.nextInt() - 1;
            int x = sc.nextInt() - 1;
            arr[y][x] = APPLE;
        }

        // 명령 입력
        int m = sc.nextInt();
        commands = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int t = sc.nextInt();
            String pos = sc.next();
            commands.add(new int[]{t, pos.equals("L") ? -1 : 1}); // L = -1, D = 1
        }

        // 게임 시작
        sol.solve();
    }
}

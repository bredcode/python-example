import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class solution {

    private int n, m;
    private List<int[]> house = new ArrayList<>();
    private List<int[]> chicken = new ArrayList<>();
    private int result = Integer.MAX_VALUE;

    // 치킨 거리 계산 함수
    public int calculateChickenDistance(List<int[]> selectedChickens) {
        int totalDistance = 0;

        for (int[] h : house) {
            int hy = h[0], hx = h[1];
            int minDistance = Integer.MAX_VALUE;

            for (int[] c : selectedChickens) {
                int cy = c[0], cx = c[1];
                int distance = Math.abs(hy - cy) + Math.abs(hx - cx);
                minDistance = Math.min(minDistance, distance);
            }
            totalDistance += minDistance;
        }
        return totalDistance;
    }

    // 백트래킹으로 치킨집 조합 선택
    public void dfs(List<int[]> selectedChickens, int pos) {
        // 치킨집 조합이 m개 선택되었으면 거리 계산
        if (selectedChickens.size() == m) {
            result = Math.min(result, calculateChickenDistance(selectedChickens));
            return;
        }

        // 현재 위치부터 치킨집 선택 탐색
        for (int i = pos; i < chicken.size(); i++) {
            selectedChickens.add(chicken.get(i)); // 치킨집 추가
            dfs(selectedChickens, i + 1);        // 다음 치킨집 탐색
            selectedChickens.remove(selectedChickens.size() - 1); // 백트래킹
        }
    }

    // 도시 데이터 초기화
    public void initialize(int n, int m, int[][] city) {
        this.n = n;
        this.m = m;

        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.n; j++) {
                if (city[i][j] == 1) {
                    house.add(new int[]{i, j}); // 집 좌표 저장
                } else if (city[i][j] == 2) {
                    chicken.add(new int[]{i, j}); // 치킨집 좌표 저장
                }
            }
        }
    }

    // 결과 반환
    public int getResult() {
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 처리
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] city = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                city[i][j] = sc.nextInt();
            }
        }

        // Solution 클래스 인스턴스 생성
        solution sol = new solution();

        // 도시 초기화 및 계산 수행
        sol.initialize(n, m, city);
        sol.dfs(new ArrayList<>(), 0);

        // 결과 출력
        System.out.println(sol.getResult());

        sc.close();
    }
}

public class solution {
    public int[] solve(int[][] edges) {
        // 결과 배열: [생성 정점, 도넛, 막대, 8자]
        int[] answer = {0, 0, 0, 0};

        // 최대 노드 번호 계산
        int maxVal = 0;
        for (int[] edge : edges) {
            maxVal = Math.max(maxVal, Math.max(edge[0], edge[1]));
        }
        maxVal++; // 인덱스를 맞추기 위해 1 증가

        // in, out 간선 수를 저장할 배열
        int[] inCnt = new int[maxVal];
        int[] outCnt = new int[maxVal];

        // 간선 정보 저장
        for (int[] edge : edges) {
            int outEdge = edge[0];
            int inEdge = edge[1];
            outCnt[outEdge]++;
            inCnt[inEdge]++;
        }

        // 노드별로 조건 확인
        for (int node = 1; node < maxVal; node++) {
            if (inCnt[node] == 0 && outCnt[node] >= 2) { // 생성 노드
                answer[0] = node;
            } else if (inCnt[node] >= 1 && outCnt[node] == 0) { // 막대 그래프
                answer[2]++;
            } else if (inCnt[node] >= 2 && outCnt[node] == 2) { // 8자 그래프
                answer[3]++;
            }
        }

        // 도넛 그래프 계산
        answer[1] = outCnt[answer[0]] - (answer[2] + answer[3]);

        return answer;
    }

    public static void main(String[] args) {
        solution sol = new solution();
        int[][] edges = {{2, 3}, {4, 3}, {1, 1}, {2, 1}};
        int[] result = sol.solve(edges);

        // 결과 출력
        for (int value : result) {
            System.out.print(value + " ");
        }
    }
}

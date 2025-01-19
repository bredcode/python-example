import java.util.Scanner;

public class solution {

    private static int[] prices;

    // 구간의 최대 수익 계산 (재귀 함수)
    public static int solve(int start, int end) {
        // 유효하지 않은 구간이면 0원 반환
        if (start >= end - 1) {
            return 0;
        }

        // 1) 구간 내에서 '마지막에 등장하는' 최댓값 찾기
        int maxPrice = -1;
        int maxIdx = -1;
        for (int i = start; i < end; i++) {
            if (prices[i] >= maxPrice) {
                maxPrice = prices[i];
                maxIdx = i;
            }
        }

        // 2) 매도일을 maxIdx로 잡고 이전 날의 이익 계산
        int sumProfit = 0;
        int buyCount = 0;
        for (int i = start; i < maxIdx; i++) {
            if (prices[i] < maxPrice) {
                sumProfit += (maxPrice - prices[i]); // 매도가 - 매수가
                buyCount++;
            }
        }

        // 산 코인이 1개 이상이었다면 수수료 1원 차감
        if (buyCount > 0) {
            sumProfit -= 1;
        }

        // 3) maxIdx 이후 구간에 대해서도 재귀적으로 반복
        sumProfit += solve(maxIdx + 1, end);

        return sumProfit;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 처리
        int n = sc.nextInt();
        prices = new int[n];
        for (int i = 0; i < n; i++) {
            prices[i] = sc.nextInt();
        }

        // 계산 및 출력
        int answer = solve(0, n);
        System.out.println(answer);

        sc.close();
    }
}

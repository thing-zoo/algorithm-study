import java.util.Scanner;

public class Main {
    public static int[][] dp = new int[101][100001]; // dp[i][j] : 최대무게 j일때, i개의 아이템까지 봤을때 만들수있는 최대 가치
    public static int[] w = new int[101];
    public static int[] v = new int[101];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }
        sc.close();

        solution(n, k);
        System.out.println(dp[n][k]);
        
    }
    public static void solution(int n, int k) {
        for (int i = 1; i <= n; i++) { // 모든 아이템에 대해
            for (int j = 1; j <= k; j++) { // 무게 k까지
                if (j >= w[i]) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j - w[i]] + v[i]);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
    }
}
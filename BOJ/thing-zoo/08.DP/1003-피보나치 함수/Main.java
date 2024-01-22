import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int[][] dp = new int[2][42]; // dp[i][n]: n번째 호출시 i 출력개수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        solution(40); // 미리 dp 다 구해두고
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            System.out.printf("%d %d\n", dp[0][n], dp[1][n]); // 바로 출력
        }
    }
    
    public static void solution(int n) {
        dp[0][0] = 1; dp[0][1] = 0;
        dp[1][0] = 0; dp[1][1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[0][i] = dp[0][i-1] + dp[0][i-2];
            dp[1][i] = dp[1][i-1] + dp[1][i-2];
        }
    }
}

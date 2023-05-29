import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static boolean[] prime = new boolean[246913];
    public static int[] dp = new int[246913];
    public static void main(String[] args) {
        Arrays.fill(prime, true);
        findPrime();
        countPrime();

        Scanner sc = new Scanner(System.in);
        while(true) {
            int n = sc.nextInt();
            if (n == 0) break;
            System.out.println(dp[2*n]-dp[n]);
        }
        sc.close();
    }
    public static void countPrime() {
        for (int i = 2; i < dp.length; i++) {
            if (prime[i]) {
                dp[i] = dp[i-1] + 1;
            } else {
                dp[i] = dp[i-1];
            }
        }
    }
    public static void findPrime() {
		prime[0] = prime[1] = false;
		
		for(int i = 2; i <= Math.sqrt(prime.length); i++) {
			if(!prime[i]) continue;
			for(int j = i * i; j < prime.length; j += i) {
				prime[j] = false;
			}
		}
	}
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> prime = getPrimeList(n);
        int answer = 0;
        if (n > 1) {
            int end = 0;
            int total = prime.get(0);
            for(int start = 0; start < prime.size(); start++) {
                while(end < prime.size() && total < n) {
                    end++;
                    if(end != prime.size()) total += prime.get(end);
                }
                if(end == prime.size()) break;
                if(total == n) answer += 1;
                total -= prime.get(start);
            }
        }
        System.out.println(answer);
        sc.close();
    }
    
    public static ArrayList<Integer> getPrimeList(int n) {
        ArrayList<Integer> prime = new ArrayList<Integer>();
        boolean[] sieve = new boolean[n+1];
        Arrays.fill(sieve, true);
        sieve[0] = sieve[1] = false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (!sieve[i]) continue;
            for (int j = i*i; j <= n; j += i) {
                sieve[j] = false;
            }
        }
        for (int i = 2; i <= n; i++) {
            if (sieve[i]) prime.add(i);
        }
        return prime;
    }
}

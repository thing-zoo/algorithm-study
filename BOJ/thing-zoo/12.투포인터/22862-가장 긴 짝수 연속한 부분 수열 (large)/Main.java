import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] s = new int[n];
        for (int i = 0; i < n; i++) {
            s[i] = sc.nextInt();
        }
        sc.close();

        int end = 0, count = 0, answer = 0;
        for (int start = 0; start < n; start++) { // 모든 수에 대해
            while (end < n && (count < k || count == k && s[end]%2 == 0)) { // 홀수가 k개이하면서 늘릴수있을때까지
                if (s[end]%2 != 0) count++; // 홀수를 만나면 카운트
                end++;
            }
            answer = Math.max(answer, end - start - count); // 현재 길이 - 홀수 개수
            if (end == n) break; // 끝에 도달하면 종료
            if (s[start]%2 != 0) count--; // 현재값이 홀수면 다시 빼주기
        }
        System.out.println(answer);
    }
}

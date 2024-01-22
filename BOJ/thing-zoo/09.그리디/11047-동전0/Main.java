import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        sc.close();

        int answer = 0; // 필요한 동전의 최소 개수
        for (int i = n-1; i >= 0; i--) { // 큰 수부터
            answer += k/arr[i]; // 나누주고
            k %= arr[i]; // 나머지 저장
        }
        System.out.println(answer);
    }
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int pre = n;
        int now = -1;
        int answer = 0;
        while (now != n) {
            now = (pre%10)*10 + (pre/10 + pre%10)%10;
            pre = now;
            answer++;
        }
        System.out.println(answer);
    }
    
}

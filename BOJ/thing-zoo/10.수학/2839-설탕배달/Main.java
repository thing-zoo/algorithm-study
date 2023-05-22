import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        
        while(true) {
            if (n%5 == 0) {
                System.out.println(n/5 + answer);
                break;
            }
            if (n < 0) {
                System.out.println(-1);
                break;
            }
            n -= 3;
            answer += 1;
        }
        sc.close();
    }
}
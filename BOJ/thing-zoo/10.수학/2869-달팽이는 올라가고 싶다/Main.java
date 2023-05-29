import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int v = sc.nextInt();
        int day = (v-b)/(a-b);
        if ((v-b)%(a-b) == 0) {
            System.out.println(day);
        } else {
            System.out.println(day + 1);
        }
        sc.close();
    }
    
}
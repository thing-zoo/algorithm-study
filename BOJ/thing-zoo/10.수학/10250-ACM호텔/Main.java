import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i = 0; i < t; i++) {
            int h = sc.nextInt();
            int w = sc.nextInt();
            int n = sc.nextInt();
            int floor = n%h;
            int room = n/h+1;
            if (floor == 0) {
                floor = h;
                room = n/h;
            }
            System.out.println(floor*100+room);
        }
        sc.close();
        
    }
    
}
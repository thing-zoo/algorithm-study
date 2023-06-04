import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String site = sc.next();
            String pw = sc.next();
            map.put(site, pw);
        }
        for (int i = 0; i < m; i++) {
            String site = sc.next();
            System.out.println(map.get(site));
        }
        sc.close();
    }
}

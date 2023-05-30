import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            Map<String, Integer> map = new HashMap<>();
            while (n-- > 0) {
                String name = sc.next();
                String type = sc.next();
                map.compute(type, (k, v) -> (v == null) ? 1 : v + 1);
            }
            int answer = 1;
            for (int i : map.values()) {
                answer *= (i + 1); // 해당 종류를 착용하지 않는 경우 추가
            }
            System.out.println(answer - 1); // 모든 종류를 착용하지 않는 경우 제외
        }
        sc.close();
    }
}

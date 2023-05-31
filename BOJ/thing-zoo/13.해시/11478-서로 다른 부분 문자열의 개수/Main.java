import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();

        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            for (int j = i+1; j <= s.length(); j++) {
                map.compute(s.substring(i, j), (k, v) -> (v == null) ? 1: v + 1);
            }
        }
        System.out.println(map.size());
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static long n, p, q; // 1e9
    public static Map<Long, Long> a = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());
        a.put(0L, 1L);
        System.out.println(solution(n));
    }

    public static long solution(long i) {
        if (!a.containsKey(i)) {
            a.put(i, solution(Math.floorDiv(i, p)) + solution(Math.floorDiv(i, q)));
        }
        return a.get(i);
    }
}
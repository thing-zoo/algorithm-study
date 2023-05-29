import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int end = 0;
        int answer = 0;
        Map<Integer, Integer> count = new HashMap<>();
        for (int start = 0; start < n; start++) {
            for (; end < n; end++) {
                Integer end_value = count.get(a[end]);
                if (end_value != null && end_value == k) break;
                count.compute(a[end], (key, value) -> (value == null) ? 1 : value + 1);
            }
            answer = Math.max(answer, end - start);
            if (end == n) break;
            count.compute(a[start], (key, value) -> value - 1);
            if (count.get(a[start]) == 0) count.remove(a[start]);
        }
        System.out.println(answer);
    }
}

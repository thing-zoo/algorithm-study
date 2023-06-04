import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s, e, q;
        s = Integer.parseInt(st.nextToken().replaceAll(":", ""));
        e = Integer.parseInt(st.nextToken().replaceAll(":", ""));
        q = Integer.parseInt(st.nextToken().replaceAll(":", ""));
        
        String line;
        Map<String, Integer> map = new HashMap<>();
        while ((line = br.readLine()) != null) {
            st = new StringTokenizer(line);
            int time = Integer.parseInt(st.nextToken().replaceAll(":", ""));
            String name = st.nextToken();
            if (time <= s) {
                map.put(name, 1);
            } else if (e <= time && time <= q) {
                if (map.containsKey(name)) {
                    map.replace(name, 2);
                }
            }
        }
        int answer = 0;
        for (int v : map.values()) {
            if (v == 2) answer++;
        }
        System.out.println(answer);
    }
}

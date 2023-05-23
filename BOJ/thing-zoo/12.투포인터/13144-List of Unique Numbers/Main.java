import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        
        int[] a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        
        long answer = 0;
        int end = 0;
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int start = 0; start < n; start++) {
            while (end < n && !count.containsKey(a[end])) {
                count.put(a[end++], 1);
            }
            answer += end - start;
            count.remove(a[start]);
        }
        System.out.println(answer);
    }
    
}
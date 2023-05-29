import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Set<String> employee = new HashSet<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String info = st.nextToken();
            if (info.equals("enter")) employee.add(name);
            else employee.remove(name);
        }
        ArrayList<String> result = new ArrayList<>(employee);
        Collections.sort(result, Collections.reverseOrder());
        for (String name: result) {
            System.out.println(name);
        }
    }
}
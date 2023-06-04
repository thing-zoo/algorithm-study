import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Map<String, Integer> dic_name = new HashMap<>();
        Map<Integer, String> dic_no = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            String name = sc.next();
            dic_name.put(name, i);
            dic_no.put(i, name);
        }

        for (int i = 0; i < m; i++) {
            String info = sc.next();
            if (isNumeric(info)) {
                System.out.println(dic_no.get(Integer.parseInt(info)));
            } else {
                System.out.println(dic_name.get(info));
            }
        }
        sc.close();
    }

    public static boolean isNumeric(String str) {
        if (str == null) {
            return false;
        }
        try {
            double d = Double.parseDouble(str);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }
}

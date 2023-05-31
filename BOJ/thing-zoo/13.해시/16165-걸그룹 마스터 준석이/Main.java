import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Map<String, List<String>> mapTeam = new HashMap<>();
        Map<String, String> mapMember = new HashMap<>();
        while (n-- > 0) {
            String team = sc.next();
            int k = sc.nextInt();
            List<String> members = new ArrayList<>();
            while (k-- > 0) {
                String member = sc.next();
                members.add(member);
                mapMember.put(member, team);
            }
            mapTeam.put(team, members);
        }
        while (m-- > 0) {
            String quiz = sc.next();
            int type = sc.nextInt();
            if (type == 1) {
                System.out.println(mapMember.get(quiz));
            } else {
                List<String> temp = mapTeam.get(quiz);
                Collections.sort(temp);
                temp.forEach(e -> System.out.println(e));
            }
        }
        sc.close();
    }
}

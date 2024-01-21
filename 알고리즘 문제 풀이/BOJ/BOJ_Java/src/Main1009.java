import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int i=0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            ArrayList<Integer> lastNums = new ArrayList<>();
            lastNums.append(a);
            int idx = 1;
            while (true) {
                int r = (a * a) % 10;
                if ( r == 0 ){
                    r = 10;
                }
                if (lastNums.get(0) == r) break;
                last_num.append(r);
                idx += 1;
            }
            int cnt = b % idx;
            System.out.println(lastNums.get(cnt-1));
        }
    }
}

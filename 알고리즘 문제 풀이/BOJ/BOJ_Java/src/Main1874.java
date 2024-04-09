import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1874 {
    // 같은 정수가 두번 나오는 일은 없다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
//        int curNum = 1;
        int[] stack = new int[n];
        int top = -1;
        int nxt = Integer.parseInt(br.readLine());
        int i = 0;
        int cnt = 0;
        while (true) {
            // 종료 조건 더 이상 입력할게 없을 때
            if (top != -1 && stack[top] == nxt) {
                nxt = Integer.parseInt(br.readLine());
                sb.append("-\n");
                top -= 1;
                continue;
            }
            top += 1;
            i += 1;
            stack[top] = i+1;
            sb.append("+\n");
            }
    }
}

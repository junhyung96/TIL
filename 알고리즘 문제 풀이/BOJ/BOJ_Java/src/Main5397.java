import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//// 키로거
//// 입력 알파벳 대문자, 소문자, 숫자, 백스페이스(-) 화살표(<>)
//// 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
//// 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.
//// 1. 스택에 넣어서 인덱스 값으로 지우고 추가하기
//// 2. 연결리스트 사용
public class Main5397 {
    // cursor 위치 판별
    static int cursor;
    static int max_cursor;
    static char[] data;
    static int[] pre;
    static int[] nxt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb;
        int testCase = Integer.parseInt(br.readLine());

        for(int tc=0; tc < testCase; tc++){
            cursor = 0;
            max_cursor = 0;
            sb = new StringBuilder();
            data = new char[1_000_100];
            pre = new int[1_000_100];
            nxt = new int[1_000_100];
            data[0] = '-';
            pre[0] = -1;
            nxt[0] = -1;
            String keyLog = br.readLine();
            int lengthOfKeyLog = keyLog.length();
            for (int i=0; i < lengthOfKeyLog; i++) {
                // 키 입력에 대해서 로직 구현
                switch (keyLog.charAt(i)){
                    case '<': {
//                        System.out.println(cursor);
                        if (cursor == 0) break;
//                        System.out.println(pre[cursor]);
                        cursor = pre[cursor];
//                        System.out.println(cursor);
                    } break;
                    case '>': {
//                        System.out.println(cursor);
                        if (nxt[cursor] == -1) break;
                        cursor = nxt[cursor];
                    } break;
                    case '-' : {
//                        System.out.println(cursor);
                        if (cursor == 0) break;
                        nxt[pre[cursor]] = nxt[cursor];
                        if (nxt[cursor] != -1) {
                            pre[nxt[cursor]] = pre[cursor];
                        }
                        cursor = pre[cursor];
                    } break;
                    default: {
//                        System.out.println(keyLog.charAt(i) + " " + cursor + " " + max_cursor);
                        max_cursor += 1;
                        data[max_cursor] = keyLog.charAt(i);
                        pre[max_cursor] = cursor;
//                        System.out.println(max_cursor + "max" + cursor + " cur" + pre[max_cursor]);
                        nxt[max_cursor] = nxt[cursor];

//                        nxt[cursor] = max_cursor;
                        if (nxt[max_cursor] != -1) {
                            pre[nxt[cursor]] = max_cursor;
                        }
                        nxt[cursor] = max_cursor;
                        cursor = max_cursor;
                    }
                }
            }
            int idx = 0;
//            System.out.println(Arrays.toString(data));
            while (true){
                if (nxt[idx] == -1) break;
//                System.out.println(nxt[idx] + " " + data[nxt[idx]]);
                sb.append(data[nxt[idx]]);
//                System.out.println(nxt[idx] + " " + data[nxt[idx]]);
                idx = nxt[idx];
            }
            System.out.println(sb);
        }
    }
}
import org.w3c.dom.ls.LSOutput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main1406 {
    private static char[] dat = new char[600_000];
    private static int[] pre = new int[600_000];
    private static int[] nxt = new int[600_000];
    private static int unused = 1;
    private static int cursor = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dat[0] = '-';
        pre[0] = -1;
        nxt[0] = -1;
        String str = br.readLine();
        for (int i = 0; i < str.length(); i++) {
            add(cursor++, str.charAt(i));
        }
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] command = br.readLine().split(" ");

            switch (command[0].charAt(0)){
                case 'L':
                    if (pre[cursor] != -1){
                        cursor = pre[cursor];
                    }
                    break;
                case 'D':
                    if (nxt[cursor] != -1){
                        cursor = nxt[cursor];
                    }
                    break;
                case 'B':
                    if (pre[cursor] != -1) {
                        remove(cursor);
                        cursor = pre[cursor];
                    }
                    break;
                default:
                    add(cursor, command[1].charAt(0));
                    cursor = nxt[cursor];
                    break;
            }
        }
        System.out.println(search());
    }
    private static String search() {
        StringBuilder sb = new StringBuilder();
        int addr = 0;
        while (nxt[addr] != -1){
            sb.append(dat[nxt[addr]]);
            addr = nxt[addr];
        }
        return sb.toString();
    }
    private static void add(int addr, char ch){
        dat[unused] = ch;
        pre[unused] = addr;
        nxt[unused] = nxt[addr];
        if(nxt[addr]!=-1){
            pre[nxt[addr]] = unused;
        }
        nxt[addr] =unused;
        unused++;
    }
    private static void remove(int addr) {
        nxt[pre[addr]] = nxt[addr];
        if(nxt[addr] != -1) {
            pre[nxt[addr]] = pre[addr];
        }
    }
}

//public class Main1406 {
//    static int cursor;
//    static int myLength;
//    static LinkedList list = new LinkedList();
//    // 한 줄로 된 간단한 에디터를 구현
//    // 영어 소문자만을 기록할 수 있는 편집기 (최대 600,000 글자)
//    // 이 편집기에는 '커서' 라는 것이 있음
//    // 지원 하는 명령어
//    // L : 커서를 왼쪽으로 한 칸 옮김
//    // D : 커서를 오른쪽으로 한 칸 옮김
//    // B : 커서 왼쪽에 있는 문자를 삭제함
//    // P $ : $라는 문자를 커서 왼쪽에 추가함
//    // 연결리스트의 추가, 삭제 로직이 현재 커서 위치를 기준으로 작동하게끔 커스터 마이징 해야 함.
//    static class ListNode {
//        char data;
//        ListNode next;
//
//        ListNode(char data) {
//            this.data = data;
//            this.next = null;
//        }
//    }
//
//    static class LinkedList {
//        ListNode head;
//        LinkedList() {
//            this.head = null;
//        }
//
//        void append(char data) {
//            ListNode newNode = new ListNode(data);
//            if (head == null) {
//                head = newNode;
//            } else {
//                ListNode current = head;
//                while (current.next != null) {
//                    current = current.next;
//                }
//                current.next = newNode;
//            }
//        }
//        void delete(char key) {
//
//        }
//        void display() {
//            ListNode current = head;
//            while (current != null) {
//                System.out.print(current.data + " ");
//                current = current.next;
//            }
//            System.out.println();
//        }
//    }
//
//    static void orderImp (char order) {
//        // case 사용할 수도 있다
//        if (order == 'L') {
//            if (cursor == 0) return;
//            cursor--;
//        }
//        else if (order == 'D') {
//            if (cursor == myLength + 1) return;
//            cursor++;
//        }
//        else if (order == 'B') {
//            if (cursor == 0) return;
//            myLength--;
//        } else {
//
//        }
//
//    }
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        // 편집기에 입력된 최초의 문자열
//        String str = br.readLine();
//
//
//        for (int i=0; i < str.length(); i++) {
//            list.append(str.charAt(i));
//        }
//
//        // 현재 커서의 위치
//        cursor = str.length();
//        myLength = str.length();
//
//        int M = Integer.parseInt(br.readLine());
//        for (int i=0; i<M; i++) {
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            if (st.countTokens() == 1 ) {
//                char order = st.nextToken().charAt(0);
//                orderImp(order);
//            } else {
//                char order = st.nextToken().charAt(0);
//                char element = st.nextToken().charAt(0);
//                orderImp(element);
//            }
//        }
//    }
//}

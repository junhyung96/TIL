import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// 키로거
// 입력 알파벳 대문자, 소문자, 숫자, 백스페이스(-) 화살표(<>)
// 키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.
// 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.
// 1. 스택에 넣어서 인덱스 값으로 지우고 추가하기
// 2. 연결리스트 사용

public class Main5397 {
    // 양방향 연결 리스트 구현
    class Node {
        // 하나의 노드는 값(data), 앞의 노드의 값, 뒤의 노드의 값을 가지고 있다.
        char data;
        Node prev;
        Node next;

        Node(char data) {
            this.data = data;
            this.prev = null;
            this.next = null;
        }
    }

    public class DoublyLinkedList {
        Node head;
        Node tail;

        DoublyLinkedList() {
            head = null;
            tail = null;
        }

        // 연결 리스트 끝에 새로운 노드 추가
        public void append(char data) {
            Node newNode = new Node(data);
            if (head == null) {
                head = newNode;
                tail = newNode;
                return;
            }
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }

        // 연결 리스트 중간에 새로운 노드 추가
        public void insertAfter(Node prevNode, char data) {
            if (prevNode == null) {
                return;
            }
            Node newNode = new Node(data);
            newNode.next = prevNode.next;
            if (prevNode.next != null) {
                prevNode.next.prev = newNode;
            } else {
                tail = newNode;
            }
            prevNode.next = newNode;
            newNode.prev = prevNode;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        String currentNode;

        for (int testcase = 0; testcase < T; testcase++) {
            DoublyLinkedList list = new DoublyLinkedList();
            int currentIndex = 0;
            int lastIndex = 0;
            String keyLog = br.readLine();
            keyLog.chars().forEach(key -> {
                if (currentIndex == 0 && key == '<') return;
                if (currentIndex == lastIndex && key == '>') return;

                if (key != '<' && key != '>' && key != '-') {
                    if (currentIndex == lastIndex) {
                        DoublyLinkedList.append('c');
                    }
                }
            });
        }
    }
}

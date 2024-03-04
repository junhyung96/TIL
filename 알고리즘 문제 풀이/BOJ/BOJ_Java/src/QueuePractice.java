import java.util.LinkedList;
import java.util.Queue;

public class QueuePractice {
    public static void main(String[] args) {
        // 큐 생성
        Queue<LinkedList<Integer>> queue = new LinkedList<>();

        // 리스트 생성
        LinkedList<Integer> list1 = new LinkedList<>();
        list1.add(1);
        list1.add(2);
        list1.add(3);

        LinkedList<Integer> list2 = new LinkedList<>();
        list2.add(4);
        list2.add(5);
        list2.add(6);

        // 큐에 리스트 추가
        queue.offer(list1);
        queue.offer(list2);

        // 큐에서 리스트 꺼내기
        while (!queue.isEmpty()) {
            LinkedList<Integer> currentList = queue.poll();
            System.out.println("List: " + currentList);
        }
    }
}
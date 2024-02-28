import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main1302 {
    static String bestSellerTitle;
    static int bestSellerCount = 0;
    // 가장 많이 팔린 책의 제목을 출력
    // 입력 : 첫째줄 팔린 책의 수, 다음 N 줄 책의 제목
    public static void main(String[] args) throws IOException {
        // 해시맵에 책제목과 책이 팔린 수를 업데이트
        // 책이 팔린 수가 제일 많이 팔린 수보다 크면 출력할 책 제목 업데이트
        HashMap<String, Integer> soldBooks = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String title = br.readLine();
            if (soldBooks.containsKey(title)) {
                soldBooks.put(title, soldBooks.get(title) + 1);
            } else {
                soldBooks.put(title, 1);
            }
            int numOfSold = soldBooks.get(title);
            if (numOfSold > bestSellerCount) {
                bestSellerCount = numOfSold;
                bestSellerTitle = title;
            } else if (numOfSold == bestSellerCount && title != bestSellerTitle) {
                int compareResult = title.compareTo(bestSellerTitle);
                if (compareResult < 0) {
                    bestSellerTitle = title;
                }
            }
        }
        System.out.println(bestSellerTitle);
    }
}

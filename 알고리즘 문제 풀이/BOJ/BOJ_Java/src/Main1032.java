import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main1032 {



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String tmp = br.readLine();

        for (int i=0; i<N-1; i++) {
            String tmp1 = tmp;
            String tmp2 = br.readLine();
            String finalResult = IntStream.range(0, tmp.length())
                    .mapToObj(j -> tmp1.charAt(j) == tmp2.charAt(j) ? String.valueOf(tmp1.charAt(j)) : "?")
                    .collect(Collectors.joining());
            tmp = finalResult;
        }
        System.out.println(tmp);
    }
}

/*
StringBuilder 사용

String str1 = "hello";
String str2 = "helpo";

StringBuilder result = new StringBuilder();
for (int i = 0; i < Math.min(str1.length(), str2.length()); i++) {
    if (str1.charAt(i) != str2.charAt(i)) {
        result.append('*'); // 다른 부분을 '*'로 대체
    } else {
        result.append(str1.charAt(i)); // 동일한 부분은 그대로 유지
    }
}

String finalResult = result.toString();
System.out.println(finalResult);
*/

/*
문자열 변환 메서드 사용

String str1 = "hello";
String str2 = "helpo";

String finalResult = "";
for (int i = 0; i < Math.min(str1.length(), str2.length()); i++) {
    if (str1.charAt(i) != str2.charAt(i)) {
        finalResult += "*"; // 다른 부분을 '*'로 대체
    } else {
        finalResult += str1.charAt(i); // 동일한 부분은 그대로 유지
    }
}

System.out.println(finalResult);
*/
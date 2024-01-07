import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());

        String input = br.readLine();
        String[] numbers = input.split(" ");

        int N = Integer.parseInt(numbers[0]);
        int M = Integer.parseInt(numbers[0]);

        System.out.println(input);
    }
}

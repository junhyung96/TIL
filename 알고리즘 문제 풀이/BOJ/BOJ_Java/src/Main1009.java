import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*  분산처리
    많은 데이터가 있다 각 데이터는 해당 번호에 맞는 컴퓨터가 처리한다
    번호가 1으로 끝나는 데이터는 1번 컴퓨터가
    번호가 2로 끝나는 데이터는 2번 컴퓨터가
    번호가 0으로 끝나는 데이터는 10번 컴퓨터가 처리한다
    a ^ b 인 데이터는 몇번 컴퓨터가 처리하는가?

    같은 숫자를 연속해서 곱하면 1의 자리숫자는 반복되서 나타난다
    1. 각 숫자마다 몇번만에 1의 자리숫자가 반복해서 나타나는지
    2. 어떤 숫자가 반복되는지 저장하고
    b 를 1 사이클에 해당하는 숫자로 나눈 나머지번째에 해당하는 1의 숫자를 출력

    반복문을 통해 각 숫자마다 거듭제곱해서
    1의자리숫자를 저장하고
    거듭제곱시 1의 자리숫자가 a와 같을 때 멈추기

    배열 10개를 만든다
    각 배열의 원소는 가변길이의 배열을 가진다(2차원 배열)

    배운점
    1. ArrayList 길이는 .size()로 알 수 있다.
    2. ArrayList 원소는 .get(index)로 알 수 있다.
    3. ArrayList 선언은 <Type> 과 함께 작성해야 한다.
    4. BufferedReader는 br.readline() 이 호출될때마다 한 줄 씩 읽어온다.
    5. StringTokenizer는 delim 을 기준으로 문자열을 분리한다. (delim 기본값 공백 \t\n\r)
    6. StringTokenizer : nextElement() 는 Object 를 nextToken() 는 String 을 반환한다.

 */

public class Main1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer>[] lastNums = new ArrayList[11];

        for (int i = 1; i < 11; i++) {
            lastNums[i] = new ArrayList<>();
            int num1 = i;
            int num2 = i;
            lastNums[i].add(num1);
            while (true){
                num2 = (num2*num1) % 10;
                if (num2 == 0){
                    break;
                }
                if (num1 == num2) break;
                lastNums[i].add(num2);
            }
        }

        int T = Integer.parseInt(br.readLine());
        for (int tc=0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            a = a % 10;
            if (a == 0) a = 10;
            int b = Integer.parseInt(st.nextToken());
            int c = lastNums[a].size();
            b = b % c;
            if (b > 0) System.out.println(lastNums[a].get(b-1));
            else System.out.println(lastNums[a].get(c-1));

        }
    }
}

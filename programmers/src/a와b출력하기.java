import java.util.Scanner;

public class a와b출력하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int a = sc.nextInt();
        String a = sc.next();
//        int b = sc.nextInt();
        String b = sc.next();

        System.out.println("a = " + a);
        System.out.println("b = " + b);

        sc.close();
    }
}

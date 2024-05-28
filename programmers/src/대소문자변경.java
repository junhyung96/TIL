import java.util.Scanner;

public class 대소문자변경 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";
        for (int i=0; i < a.length(); i++) {
            char tmp =a.charAt(i);
            if (tmp >= 65 && tmp <= 90) {
                result += (char)(tmp + 32);
            }
            else {
                result += (char)(tmp -32);
            }
        }
        System.out.println(result);

        String answer = "";
        for(Character c : a.toCharArray()){
            if(Character.isUpperCase(c)){
                //stack.push(Character.toLowerCase(c));
                answer += Character.toLowerCase(c);
            }
            else if(Character.isLowerCase(c)){
                //stack.push(Character.toUpperCase(c));
                answer += Character.toUpperCase(c);
            }
        }
        System.out.println(answer);
    }
}

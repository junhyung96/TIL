
```java
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/*
 * InputStreamReader 로 입력받는 경우에는 배열을 어떻게 주느냐에 따라 2개 이상의 값을 받을 수 있음
 */
InputStream in = System.in;
InputStreamReader reader = new InputStreamReader(in); // InputStreamReader 사용하기 위해 객체 생성
		
OutputStream out = System.out;
OutputStreamWriter writer = new OutputStreamWriter(out); // OutputStreamWriter 사용하기 위해 객체 생성
		
char cdata[] = new char[2]; // 이제는 char 를 기본형으로 받을 수 있고, 2개 이상의 값을 배열을 통해 받아올수 있다.
reader.read(cdata);
		
int IcData = cdata[0]-'0'; // 배열이기 때문에 char 로 받은 값을 int로 변환하여 계산하고 싶은 경우 이처럼 사용해야한다.
		
writer.write("입력받은 값 : ");
writer.write(cdata);
writer.write("\n");
writer.write("입력받은 첫번째 값 + 10 : ");
writer.write(IcData+10+"\n"); // 입력받은 첫번째 값 +10
		
System.out.println("#######결과#######");
writer.flush(); // 이 매서드를 통해 출력
writer.close();
```

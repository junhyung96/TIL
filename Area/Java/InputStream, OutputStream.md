
자바에서는 처리 단위에 따라 Reader - inputStream / Writer - outputStream 으로 나뉘어 통신한다. 이때 입력 스트림 inputStream 은 스트림을 한 줄 씩 읽고, 출력스트림 outputStream 으로 데이터를 내보내며 해당 공간을 비운다.
InputStream 은 System.in 을 사용하며, OutputStream 은 System.out 을 사용

```java
import java.io.InputStream; // Import 필수
import java.io.OutputStream;		
  
 /*
* InputStream 로 입력받는 경우 맨 앞 문자 1개만 출력됨 && int 형태로 입력받음
 */		
InputStream in = System.in;
OutputStream out = System.out;
        
int idata = in.read(); // input 은 read 와 연결되어있기 때문에 in.read 를 사욯한다.
		
out.write(idata); // output 은 write 와 연결되어있기 때문에 out.write 를 사용한다
out.flush(); // flush 를 써주지 않으면 출력되지 않는다
out.close(); // output 을 끝내는 매서드
```

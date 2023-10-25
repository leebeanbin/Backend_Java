
```java
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;


public class Main {
  public static void main(String args[]) throws IOException {
    Integer[] chess_piece = {1,1,2,2,2,8};
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    StringBuilder text = new StringBuilder();
    int cnt = 0;

    while(st.hasMoreTokens()){
      text.append(chess_piece[cnt]- Integer.parseInt(st.nextToken())).append(" ");
      cnt += 1;
    }
    br.close();
    System.out.println(text);
  }
}
```

```java
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;


public class Main {
  public static void main(String args[]) throws IOException {
    Integer[] chess_piece = {1,1,2,2,2,8};
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    StringBuilder text = new StringBuilder();
    int cnt = 0;

    while(st.hasMoreTokens()){
      text.append(chess_piece[cnt]- Integer.parseInt(st.nextToken())).append(" ");
      cnt += 1;
    }
    br.close();
    System.out.println(text);
  }
}
```
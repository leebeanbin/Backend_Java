
```java
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder result = new StringBuilder();
    List<Integer> db = new ArrayList<>();

    Integer times = Integer.parseInt(br.readLine());
    int multi = 0;
    String argument = "";

    for(int i = 0; i < times ; i++){
      StringTokenizer stm = new StringTokenizer(br.readLine());

      multi = Integer.parseInt(stm.nextToken());
      argument = stm.nextToken();

      char[] charArray = argument.toCharArray(); // it makes 

      for (int j = 0; j < charArray.length; j++) {
        char c = charArray[j];
        for(int k = 0; k < multi; k++){
          result.append(c);
        }
      }
      result.append("\n");
    }
    System.out.println(result);
    br.close();
  }
}

```
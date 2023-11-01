### <font color="#c00000">version 1</font>
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // StringTokenizer를 통해 A(낮에 올라가는 높이),B(자면서 내려오는 길이),V(나무의 총 높이)의 값을 받는다.
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int nNoon = Integer.parseInt(st.nextToken());
    int nNight = Integer.parseInt(st.nextToken());
    int nHeightOfTree = Integer.parseInt(st.nextToken());
    int nDays = 0;

    while (true) {
      nDays++;
      nHeightOfTree = nHeightOfTree - nNoon;
      if (nHeightOfTree <= 0) {
        break;
      }
      nHeightOfTree += nNight;
    }

    System.out.println(nDays);
  }
}
```

### <font color="#c00000">version 2</font>
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int nNoon = Integer.parseInt(st.nextToken());
    int nNight = Integer.parseInt(st.nextToken());
    int nHeightOfTree = Integer.parseInt(st.nextToken());
    
    int days = (nHeightOfTree - nNoon + nNoon - nNight - 1) / (nNoon - nNight) + 1;
    
    System.out.println(days);
  }
}

```


위의 두 코드는 같은 결과를 출력해 낸다. 하지만, 첫번째 코드에서 while은 굳이 쓰일 필요는 없으며 



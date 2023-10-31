
```java
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // 숫자를 입력하기 위해서 char을 기준으로 입력을 받는 .read를 0을 뺌으로서 내가 입력한 숫자 그대로를 입력할 수 있게 한다.
    int nLoops = Integer.parseInt(br.readLine());

    // 문제의 조건에는 최대 거스름돈은 5.00$이다.
    for(int i = 0; i < nLoops; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int nDollars = Integer.parseInt(st.nextToken());

      int nQuater = nDollars / 25;
      int nDime   = (nDollars % 25) / 10;
      int nNickel = ((nDollars % 25) % 10) / 5;
      int nPenny  = ((nDollars % 25) % 10) % 5;
      System.out.println(nQuater + " " + nDime + " " + nNickel + " " + nPenny);
      
    }
  }
}
```

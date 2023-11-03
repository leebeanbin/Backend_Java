
### Divisors Sum
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    while (true) {
      int nTargetValue = Integer.parseInt(br.readLine());
      List<Integer> divisors = new ArrayList<>();
      StringBuilder strOutput = new StringBuilder();
      int sum = 0;

      if (nTargetValue == -1) break;

      for (int i = 1; i <= nTargetValue / 2; i++) {
        if (nTargetValue % i == 0) {
          divisors.add(i);
          sum += i;
        }
      }

      if (sum == nTargetValue) {
        strOutput.append(nTargetValue).append(" = ");
        for (int Inner : divisors) {
          strOutput.append(Inner).append(" + ");
        }
        strOutput.delete(strOutput.length() - 3, strOutput.length());
      } else {
        strOutput.append(nTargetValue).append(" is NOT perfect.");
      }
      System.out.println(strOutput);
    }
  }
}

```

### Relatively prime detector
```java
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int nNumberOfInput = Integer.parseInt(br.readLine());

    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    // String[] numbers = br.readLine().split(" ");
    // If I used this Array to distribute them and classify would be better.
    int nPimerCount = 0;

    for(int i = 0; i < nNumberOfInput; i++){
      int nValueCount = 0;
      
      int nCoprime = Integer.parseInt(st.nextToken());
      if(nCoprime == 1){
        nValueCount -= 1;
      }

      else{
        for(int j = 1; j < nCoprime+1 ; j++){
          if(nCoprime % j == 0){
            nValueCount += 1;
          }
        }
      }
      if(nValueCount == 2){
        nPimerCount += 1;
      }
    }
    System.out.println(nPimerCount);
    
  }
}
```


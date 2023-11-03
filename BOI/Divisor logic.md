
## Version 1
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder strOutput = new StringBuilder();

    while(true){
      StringTokenizer st = new StringTokenizer(br.readLine(), " ");
      int nInputOne = Integer.parseInt(st.nextToken());
      int nInputTwo = Integer.parseInt(st.nextToken());
      if(nInputOne == 0 && nInputTwo == 0){
        break;
      }else if(nInputOne < nInputTwo && nInputTwo % nInputOne == 0){
        strOutput.append("factor\n");
      }else if(nInputOne > nInputTwo && nInputOne % nInputTwo == 0){
        strOutput.append("multiple\n");
      }else{
        strOutput.append("neither\n");
      }
    }
    System.out.println(strOutput);
    br.close();
  }
}

```
As you see, this code looks so simple you are able to understand what this is directly. I just got two Input to judge they're factor or multiple or neither. Shortly, this code is defector is to find out the relationship between two value. 

### version 2
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    

    int nMainValue = Integer.parseInt(st.nextToken());
    int nDivisorOfMainValue = Integer.parseInt(st.nextToken());
    int nDivisorCounter = 0;

    for(int i = 1; i < nMainValue+1; i++){
      if(nMainValue % i == 0){
        nDivisorCounter ++;
        if(nDivisorCounter == nDivisorOfMainValue){
          System.out.println(i);
        }
      }
    }

    if(nDivisorCounter < nDivisorOfMainValue){
      System.out.println(0);
      
    }
    br.close();
  }
}
```




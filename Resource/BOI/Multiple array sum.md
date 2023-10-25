
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int[][] nArray = new int[9][9];
    int prev = 0;
    int nMaxNum = 0;
    int nRow = 0, nCol =0;

    for(int i = 0; i < 9; i ++){
      StringTokenizer st = new StringTokenizer(br.readLine(), " ");
      for(int j = 0; j < 9; j ++){
        int nArrayNum = Integer.parseInt(st.nextToken());
        nArray[i][j] = nArrayNum;
        if(prev <= nArrayNum){
          if(nMaxNum <= nArrayNum){
            nMaxNum = nArrayNum;
            nRow = i+1;
            nCol = j+1;
          }
          prev = nArrayNum;
        }else{
          prev = nArrayNum;
        }
      }
    }
    // System.out.println(Arrays.deepToString(nArray));
    System.out.println(nMaxNum);
    System.out.println(nRow + " " + nCol);
    
    
  }
}

```

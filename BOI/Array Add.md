
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    int nRow = Integer.parseInt(st.nextToken());
    int nCol = Integer.parseInt(st.nextToken());
    int[][] nArray = new int[nRow][nCol];

    for (int k = 0; k < 2; k++) {
      if (k != 0) {
        for (int i = 0; i < nRow; i++) {
          StringTokenizer stm = new StringTokenizer(br.readLine(), " ");
          for (int j = 0; j < nCol; j++) {
            int a = Integer.parseInt(stm.nextToken());
            nArray[i][j] = a + nArray[i][j];
          }
          // 한 줄의 각 col에 대한 반복문
        }
        // 총 줄 수 에 대한 반복문
      } else {
        for (int i = 0; i < nRow; i++) {
          StringTokenizer stm = new StringTokenizer(br.readLine(), " ");
          for (int j = 0; j < nCol; j++) {
            int a = Integer.parseInt(stm.nextToken());
            nArray[i][j] = a;
          }
          // 한 줄의 각 col에 대한 반복문
        }
        // 총 줄 수 에 대한 반복문
      }
    }

    br.close(); // Close the BufferedReader
    for (int k = 0; k < nRow; k++) {
      for (int h = 0; h < nCol; h++) System.out.printf("%d ", nArray[k][h]);
      System.out.println();
    }
  }
}

```


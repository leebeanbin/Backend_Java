

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) throws IOException {
    // 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다.
    // 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String result = "";
    // 배열의 초기화
    char[][] nArray = new char[15][5];
    for (int i = 0; i < 15; i++) {
      for (int j = 0; j < 5; j++) {
        nArray[i][j] = ' ';
      }
    }

    // 내가 초기화한 배열을 문제에 주어진 조건과 같이 최대 5행 15열의 Input을 받을 수 있는 반복문을 구성
    for (int k = 0; k < 5; k++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      String each_line = st.nextToken();
      for (int h = 0; h < each_line.length(); h++) {
        nArray[h][k] = each_line.charAt(h);
      }
    }

    // 조건에 의하면 공백이 발견 될 시에는 바로 다음 줄로 넘어가 프린트를 하기 때문에 조건문을 통하여 break 생성
    for (int l = 0; l < 15; l++) {
      for (int m = 0; m < 5; m++) {
        char chLoc = nArray[l][m];
        result += chLoc;
      }
    }
    System.out.println(result.replace(" ", ""));
    // System.out.println(result.replace(" ", "").length());
    br.close();
    // System.out.println(Arrays.toString(nArray));
  }
}
```

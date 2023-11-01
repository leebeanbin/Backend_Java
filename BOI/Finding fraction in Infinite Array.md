```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // InputValue가 만약 1이면 바로 해당 값의 분수 꼴이 출력되게 만든다.
    int nBelt = Integer.parseInt(br.readLine());

    int nDom = 2;
    int nNumer = 1;

    boolean bCrnt = false;
    boolean bPrev = true;

    if (nBelt == 1) {
      System.out.println("1/1");
    } else {
      for (int i = 1; i < nBelt - 1; i++) {
        if (nDom > nNumer && nNumer == 1) {
          bCrnt = true;
        } else if (nDom < nNumer && nDom == 1) {
          bCrnt = false;
        }

        if (bCrnt == true && bPrev == true) {
          nNumer += 1;
          nDom -= 1;
          bPrev = bCrnt;
        } else if (bCrnt == true && bPrev == false) {
          nDom += 1;
          bPrev = bCrnt;
        } else if (bCrnt == false && bPrev == true) {
          nNumer += 1;
          bPrev = bCrnt;
        } else if (bCrnt == false && bPrev == false) {
          nDom += 1;
          nNumer -= 1;
          bPrev = bCrnt;
        }
      }

      System.out.printf("%d/%d\n", nNumer, nDom);
    }
  }
}

```
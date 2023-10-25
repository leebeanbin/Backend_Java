
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String strInput = br.readLine(); // main input is gonna be changed with words in croatia array instead.
    String[] strCroatiaStrings = {
      "c=",
      "c-",
      "dz=",
      "d-",
      "lj",
      "nj",
      "s=",
      "z=",
    };

    // Keep looping until no more patterns are found
    for (String pattern : strCroatiaStrings) {
      if (strInput.contains(pattern)) {
        strInput = strInput.replaceAll(pattern, "A");
      }
    }

    System.out.println(strInput.length());
  }
}

```
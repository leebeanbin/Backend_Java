
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

  public static void main(String args[]) throws IOException {
    int ch;
    int cnt = 0;
    List<String> alphabet_Strings = new ArrayList<String>() {
      {
        add("ABC");
        add("DEF");
        add("GHI");
        add("JKL");
        add("MNO");
        add("PQRS");
        add("TUV");
        add("WXYZ");
        add("+-/*");
      }
    };

    Character sCharacter;
    while ((ch = System.in.read()) != -1) {
      if (ch == '\n') {
        break;
      }
      char inputChar = (char) ch;
      for (String word : alphabet_Strings) {
        if (word.contains(String.valueOf(inputChar))) {
          cnt += alphabet_Strings.indexOf(word) + 3;
        }
      }
    }
    System.out.println(cnt);
  }
}

```
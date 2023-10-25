
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    List<Integer> db = new ArrayList<>();

    String input = br.readLine();
    String res = "";
    for (int i = 'a'; i <= 'z'; i++) {
      db.add(-1);
    }

    StringBuilder result = new StringBuilder();
    for (int i = 0; i < input.length(); i++) {
      char c = input.charAt(i);
      if (db.get(c - 'a') != -1 && db.get(c - 'a') < i) {
        continue;
      }
      db.set(c - 'a', i);
    }
    
    for (int i = 0; i < 26; i++) {
      result.append(db.get(i)).append(" ");
    }

    System.out.println(result.toString().trim());
  }
}

```
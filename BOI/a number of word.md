
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cnt = 0;
        String argument = br.readLine();

        String[] tokens = argument.split(" ");
        for (String word : tokens) {
            if (!word.isEmpty()) {
                cnt++;
            }
        }

        System.out.println(cnt);
        br.close();
    }
}

```
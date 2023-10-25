
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> res_db = new ArrayList<>();  
        
        int a, b;
        // 첫 번째 인수의 개수 입력
        a = Integer.parseInt(br.readLine());
        // 두 번째 줄 입력 처리
        StringTokenizer stn = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < a ; i++){
            b = Integer.parseInt(stn.nextToken());
            res_db.add(b);
        }

        Collections.sort(res_db);
        int max = Collections.max(res_db);
        int min = Collections.min(res_db);
        
        System.out.println(min + " " + max);
        
        br.close();
    }
}

```

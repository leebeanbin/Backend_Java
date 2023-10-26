
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

        int a, b, cnt = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        
        for(int i = 1; i < a+1; i++){
            res_db.add(i);
        }

        for(int i = 0; i < b; i++){
            StringTokenizer stm = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(stm.nextToken()); // Start from c 
            int d = Integer.parseInt(stm.nextToken()); // to d

            List<Integer> subList = res_db.subList(c-1, d);
            Collections.reverse(subList);
        }

        for(Integer value : res_db){
            System.out.printf("%d ", value);
        }

        br.close();
    }
}


```
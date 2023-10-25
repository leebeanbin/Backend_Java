
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

        int a, b = 0;
        double sum = 0, nMax =0;

        a = Integer.parseInt(br.readLine());

        StringTokenizer stm = new StringTokenizer(br.readLine());
        for(int i = 0; i < a ; i++){
            b = Integer.parseInt(stm.nextToken());
            res_db.add(b);
        }
        
        nMax = Collections.max(res_db);
        for(Integer value : res_db){
            double dNum = (value/nMax)*100;
            sum += dNum;
        }

        System.out.println(sum/(double)a);

        br.close();
    }
}

```
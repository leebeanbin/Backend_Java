
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> res_db = new ArrayList<>();  
        
        // List size, a number of putting ball in the basket
        int a, b, base = 0;
        // 인수 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        
        for(int i = 0; i < a; i++){
            res_db.add(base);
        }
        
        for(int j = 0; j < b ; j++){
            StringTokenizer stn = new StringTokenizer(br.readLine(), " ");
            int c = Integer.parseInt(stn.nextToken()); // From c
            int d = Integer.parseInt(stn.nextToken()); // to d
            int e = Integer.parseInt(stn.nextToken()); // put e num ball

            for(int k = c ; k <= d ; k++){ // 범위 수정
                res_db.set(k-1, e);
            }
        }

        for(Integer value : res_db){
            System.out.printf("%d ", value);
            
        }

        br.close();
    }
}

```

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
        
        for(int i = 1; i < a+1; i++){
            res_db.add(i);
        }
        
        for(int j = 0; j < b ; j++){
            StringTokenizer stn = new StringTokenizer(br.readLine(), " ");
            int c = Integer.parseInt(stn.nextToken())-1; //  c
            int d = Integer.parseInt(stn.nextToken())-1; // to d

            int crnt     = res_db.get(c);
            int node     = res_db.get(d); 

            res_db.set(d, crnt);
            res_db.set(c, node);
            // System.out.println(res_db);

        }

        StringBuilder builder = new StringBuilder();
        for (Integer value : res_db) {
            builder.append(value).append(" ");
        }
        
        String result = builder.toString().trim();
        System.out.println(result);
        

        br.close();
    }
}
```
### Total receipt cost calculator

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
        
        List<Integer> integers = new ArrayList<>(); 

        int sum, coef, a, b, res, tot;
        res = 0; 
        tot = 0;

        sum = Integer.parseInt(br.readLine());
        coef = Integer.parseInt(br.readLine());
        

        for(int i = 1; i < coef+1; i++){
            StringTokenizer stn = new StringTokenizer(br.readLine());
            a = Integer.parseInt(stn.nextToken());
            b = Integer.parseInt(stn.nextToken());

            res = a * b;
            integers.add(res);
            tot += res;
        }

        if(tot == sum){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
```


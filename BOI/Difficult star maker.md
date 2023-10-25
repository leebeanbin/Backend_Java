
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main
{
	public static void main(String[] args) throws IOException {
    		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int times = Integer.parseInt(br.readLine());
    
        String blk = " ";
        String dot = "*";
    
        int cnt = times; // margin
        int rev = 1; // star
    
    
        for(int i = 1; i < times+1 ; i++){
          String margin = blk.repeat(times - i);
          String star = dot.repeat(rev);
          rev += 2;
          cnt --;
          System.out.println(margin+star);
        }
        
        for(int j = times - 1; j > 0; j--){
          String margin2 = blk.repeat(times-j);
          String star2 = dot.repeat(j + (j-1));
          System.out.println(margin2+star2);
        }
	}
}

```
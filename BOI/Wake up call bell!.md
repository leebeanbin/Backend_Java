```java
import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        
        int a,b,c;
        
        a = scanner.nextInt();
        b = scanner.nextInt();
        
        c = b - 45;
        
        if(a == 0 && c <0){
            a = 24;
        }

        if(c > 0){
            System.out.println(a+" "+c);
        }else if(c == 0){
            System.out.println(a+" "+c);
        }else{
            System.out.println((a-1)+" "+(c+60));
        }
    }
}
```

if we put hour and minute we want to put in this, this wake up call automatically will set up on 45 mins later
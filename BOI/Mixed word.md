
```java
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int nInterval_value = Integer.parseInt(br.readLine());
    int sum = nInterval_value;
    char[] node;

    for(int i = 0; i < nInterval_value; i++){
      boolean foundDuplicate = false;
      String ch = br.readLine();
      boolean[] alphabet = new boolean[26];
      int prev = 0;
      for(int j = 0; j < ch.length(); j++) {
        int now = ch.charAt(j);	// i 번째 문자 저장 (현재 문자)
        
        
        // 앞선 문자와 i 번째 문자가 같지 않다면?
        if (prev != now) {		
          
          // 해당 문자가 처음 나오는 경우 (false 인 경우)
          if ( alphabet[now - 'a'] == false ) {
            alphabet[now - 'a'] = true;		// true 로 바꿔준다
            prev = now;					// 다음 턴을 위해 prev 도 바꿔준다 
          }
     
          // 해당 문자가 이미 나온 적이 있는 경우 (그룹단어가 아니게 됨) 
          else {
            sum--;
            break;	//함수 종료
          }
        }
      }
    }
    System.out.println(sum);
  }
}
```


```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
 
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
	public static void main(String[] args) throws IOException{
 
		int count = 0;
		int N = Integer.parseInt(br.readLine());
 
		for (int i = 0; i < N; i++) {
			if (check() == true) {
				count++;
			}
		}
		System.out.println(count);
	}
 
	public static boolean check() throws IOException {
		boolean[] check = new boolean[26];
		int prev = 0;
		String str = br.readLine();
		
		for(int i = 0; i < str.length(); i++) {
			int now = str.charAt(i);	// i 번째 문자 저장 (현재 문자)
			
			
			// 앞선 문자와 i 번째 문자가 같지 않다면?
			if (prev != now) {		
				
				// 해당 문자가 처음 나오는 경우 (false 인 경우)
				if ( check[now - 'a'] == false ) {
					check[now - 'a'] = true;		// true 로 바꿔준다
					prev = now;					// 다음 턴을 위해 prev 도 바꿔준다 
				}
	 
				// 해당 문자가 이미 나온 적이 있는 경우 (그룹단어가 아니게 됨) 
				else {
					return false;	//함수 종료
				}
			}
	        
	        
			// 앞선 문자와 i 번째 문자가 같다면? (연속된 문자)
			// else 문은 없어도 됨
			else {
				continue;
			}
		}    
		return true;
	}
}
```


```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int count = n; // 그룹 단어로 판별되는 단어 수

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            boolean[] alphabet = new boolean[26];

            for (int j = 1; j < word.length(); j++) {
                char prevChar = word.charAt(j - 1);
                char currentChar = word.charAt(j);

                if (prevChar != currentChar) {
                    if (alphabet[currentChar - 'a']) {
                        count--;
                        break;
                    } else {
                        alphabet[prevChar - 'a'] = true;
                    }
                }
            }
        }

        System.out.println(count);
    }
}

```
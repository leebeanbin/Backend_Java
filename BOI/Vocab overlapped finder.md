```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int[] alphabet = new int[26];
    String text = br.readLine().toUpperCase();
    // char[] word = text.toCharArray();

    
    for(int i = 0; i < text.length(); i++){
      int word = text.charAt(i) - 'A';
      alphabet[word] ++;
    }

    int maxNum = 0;
    char maxChar = '?';
    for(int j = 0; j < alphabet.length; j++){
      if(maxNum < alphabet[j]){
        maxNum = alphabet[j];
        maxChar = (char)(j + 'A');
      }else if(maxNum == alphabet[j]){
        maxChar = '?';
      }
    }
    System.out.println(maxChar);
    
  }
}


```
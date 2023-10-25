
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

  static BufferedReader br = new BufferedReader(
    new InputStreamReader(System.in)
  );
  static float cnt = 0;

  public static void main(String[] args) throws IOException {
    int loop = 20;
    float total = 0.0f;
    // Create an instance of the Calculator class
    Calculator calculator = new Calculator();
    for (int i = 0; i < 20; i++) {
      // Calculate and retrieve the sum from the Calculator
      float sum = calculator.calculateGrade();
      total += sum;
    }

    br.close(); // Close the BufferedReader
    System.out.println(total / cnt);
  }

  static class Calculator {

    StringTokenizer st;
    String[] grade = { "A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F" };
    float[] nGrade = { 4.5f, 4.0f, 3.5f, 3.0f, 2.5f, 2.0f, 1.5f, 1.0f, 0.0f };

    float calculateGrade() throws IOException {
      st = new StringTokenizer(br.readLine(), " ");
      String sub = st.nextToken();
      float st_grade = Float.parseFloat(st.nextToken());
      String avg = st.nextToken();
      float sub_grade = 0.0f;
      if (!avg.equals("P")) {
        int index = Arrays.asList(grade).indexOf(avg);
        sub_grade = nGrade[index];
        cnt = cnt + st_grade;
      }

      return st_grade * sub_grade;
    }
  }
}

```


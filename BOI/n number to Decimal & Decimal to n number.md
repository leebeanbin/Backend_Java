1. n number to Decimal 💢
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // BuffuredReader를 통해 받은 값을 공백을 기준으로 나눠 배열로 저장한다.
    String[] strTrans = br.readLine().split(" ");
    String strInputText = strTrans[0];
    int nTrans = Integer.parseInt(strTrans[1]);

    int result = 0;
    // 아스키코드에서 대문자 `A`는 십진수 65와 같다.
    for (int i = strInputText.length() - 1; i >= 0; i--) {
      // 반복문을 뒤부터 반복하여 변환 결과를 구한다.
      char chX = strInputText.charAt(i);
      int nCoef;
	  // 조건문을 통해서 만약 입력받은 값이 문자일 경우(이 문제에서 입력은 대문자로 고정하였기 때문에 부가적인 조건을 붙이지 않아도 된다.)를 통해
	  // 계수를 각기 다르게 조절하면 원하는 값을 얻을 수 있다.
      if (Character.isLetter(strInputText.charAt(i))) {
        nCoef = chX - 'A' + 10;
      } else {
        nCoef = chX - '0';
      }
      int nSquare = strInputText.length() - (i + 1);
      // Math.pow(n,m)이라는 함수는 n을 계수롤 사용하고 m을 지수로 사용해 제곱해주는 함수이다.
      result += (nCoef * (Math.pow(nTrans, nSquare)));
    }

    br.close();
    System.out.println(result);
  }
}

```

2. Decimal to n number
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // BuffuredReader를 통해 받은 값을 공백을 기준으로 나눠 배열로 저장한다.
    String[] strTrans = br.readLine().split(" ");
    int nInputNum = Integer.parseInt(strTrans[0]);
    int nTrans = Integer.parseInt(strTrans[1]);

    String result = "";

    while (true) {
      int nDevision = nInputNum % nTrans;
      char chAddWord;

      if (nDevision >= 10) {
        // 10이 초과하는 변수 같은 경우에는 A가 시작으로 보기 때문에 10을 빼고 문자를 게산한다.
        chAddWord = (char) (nDevision - 10 + 'A');
      } else {
        // 10이 초과하지 않는 변수는 숫자와 문자간의 시작 점이 다르지 않기 때문에 그대로 더한다.
        chAddWord = (char) (nDevision + '0');
      }
      result += chAddWord;

      nInputNum = nInputNum / nTrans; // 점점 깎여가는 정수 값을 의미한다.
      if (nInputNum == 0) {
        break;
      }
    }
    // 반복문을 통해 역순으로 result 안에 있는 문자열을 출력한다.
    for (int i = result.length() - 1; i >= 0; i--) {
      char chPrint = result.charAt(i);
      System.out.printf("%c", chPrint);
    }
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

        // 입력 받은 값을 공백을 기준으로 나눠 배열로 저장
        String[] strTrans = br.readLine().split(" ");
        int nInputNum = Integer.parseInt(strTrans[0]);
        int nTrans = Integer.parseInt(strTrans[1]);

        StringBuilder result = new StringBuilder();

        while (nInputNum > 0) {
            int nDevision = nInputNum % nTrans;
            // 기존의 위의 코드에서는 조건문을 따로 작성하여 chAddWord에 대한 값을 정해 줬으나, Java라는 언어는 이와 같이 변수를 정의하는 단계에서 조건문을 걸어 선언을 할 수 있다.
            char chAddWord = (nDevision >= 10) ? (char) (nDevision - 10 + 'A') : (char) (nDevision + '0');
            
            result.append(chAddWord);

            nInputNum = nInputNum / nTrans;
        }

        // 결과를 역순으로 출력
        String reversedResult = result.reverse().toString();
        System.out.println(reversedResult);
    }
}

```

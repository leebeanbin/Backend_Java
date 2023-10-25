
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> integers = new ArrayList<>();

        String inputLine = reader.readLine();

        // 입력 문자열을 공백으로 분할하여 정수로 변환하고 리스트에 추가
        String[] inputValues = inputLine.split("\\s+");
        for (String value : inputValues) {
            // 입력되고 분할된 변수의 갯수 만큼 반복문을 돌려 변수를 parsing한다.
            int intValue = Integer.parseInt(value);
            integers.add(intValue);
            // parsing한 변수를 저장한다.
        }

        int thirdIntValue = Integer.parseInt(reader.readLine());
        integers.add(thirdIntValue);

        int hour, min, wait;

        hour = integers.get(0);
        min = integers.get(1);
        wait = integers.get(2);

        min += wait;
        
        // 시간과 분을 조정
        hour = (hour +min / 60) %  24;
        min = min % 60;

        // 결과 출력
        System.out.printf("%d %d%n", hour, min);

        // BufferedReader를 닫아줍니다.
        reader.close();
    }
}

```

it showed me times when i can put out my stuff that is in oven.


```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 내가 입력받는 종이의 장수를 말한다.
        int nPapers = Integer.parseInt(br.readLine());

        // 도화지 배열을 생성하고 초기화합니다.
        int[][] canvas = new int[101][101];

		// 종이의 장수만큼 반복문을 돌려서, paperPosition이라는 문자열 배열에 공백을 두고 입력 되는 각각의 값을 집어 넣는다.
        for (int i = 0; i < nPapers; i++) {
            String[] paperPosition = br.readLine().split(" ");
            int left = Integer.parseInt(paperPosition[0]);
            int bottom = Integer.parseInt(paperPosition[1]);
				
            // 색종이를 붙이는 작업 (도화지 배열에 마킹)
            // 그렇게 넣은 배열을 따라서, 각 색종이의 크기가 가로 세로 10이기 때문에 입력 받은 값에 각각 10을 더해준 만큼 반복문을 통해서 canvas라는 배열의 해당 위치의 값을 1로 초기화를 해준다.
            for (int x = left; x < left + 10; x++) {
                for (int y = bottom; y < bottom + 10; y++) {
                    canvas[x][y] = 1;
                }
            }
        }

        int blackArea = 0;
        for (int x = 0; x <= 100; x++) {
            for (int y = 0; y <= 100; y++) {
                if (canvas[x][y] == 1) {
                    blackArea++;
                }
            }
        }

        System.out.println(blackArea);
    }
}

```
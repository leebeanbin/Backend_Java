
### 1. Root
```java
import java.util.ArrayList;
import java.util.List;

public class DivisorsSqrtExample {
    public static List<Integer> findDivisors(int n) {
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                divisors.add(i);
                if (i != n / i) {
                    divisors.add(n / i);
                }
            }
        }
        return divisors;
    }

    public static void main(String[] args) {
        int number = 36;
        List<Integer> divisors = findDivisors(number);
        System.out.println("Divisors of " + number + ": " + divisors);
    }
}

```
: Basically, we can think of this algorithm within an easy. there is no divisor which is over a half of Main Input Number. that's why we made it to Root square and loop it to find divisors are not overlapped.

### 2. Sieve of Eratosthenes
```java
public class SieveOfEratosthenesExample {
    public static boolean[] sieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        return isPrime;
    }

    public static List<Integer> findDivisors(int n) {
        boolean[] isPrime = sieve(n);
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (n % i == 0 && isPrime[i]) {
                divisors.add(i);
            }
        }
        return divisors;
    }

    public static void main(String[] args) {
        int number = 36;
        List<Integer> divisors = findDivisors(number);
        System.out.println("Divisors of " + number + ": " + divisors);
    }
}

```
: Sieve of Eratosthenes is quite similar with Root square. I think all of Algorithm basically sharing it but use different logic to find out and remove how each algorithm pick up overlapped value.
### 3. Algorithm of Euclid 
```java
public class EuclideanAlgorithmExample {
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    public static List<Integer> findDivisors(int n) {
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (n % i == 0 && gcd(n, i) == 1) {
                divisors.add(i);
            }
        }
        return divisors;
    }

    public static void main(String[] args) {
        int number = 36;
        List<Integer> divisors = findDivisors(number);
        System.out.println("Divisors of " + number + ": " + divisors);
    }
}

```

![[Pasted image 20231103110109.png]]

: The `gcd` function is a recursive function to find the GCD of two integers `a` and `b`. If `b` is 0, it returns `a`, which is the GCD. Otherwise, it calls itself with the arguments `b` and `a % b`, effectively applying the Euclidean Algorithm recursively(재귀적으로) until `b` becomes 0.
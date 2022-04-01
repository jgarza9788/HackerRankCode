

## input using scanner
```java
Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);
```


## if then example
```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner scanner = new Scanner(System.in);
        int thisInt = scanner.nextInt();
        
        if (thisInt % 2 == 0)
        {
            System.out.println("Not Weird");
        }
        else
        {
            System.out.println("Weird");
        }
        
    }
}
```

## if then example
```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        if (n % 2 == 1)
        {
            System.out.println("Weird");
        }
        else
        {
            if (n >= 2 & n <= 5)
            {
                System.out.println("Not Weird");
            }
            if (n >= 6 && n <= 20)
            {
                System.out.println("Weird");
            }
            if (n > 20)
            {
                System.out.println("Not Weird");
            }
        }
        
    }
}
```


## 
```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        double y=sc.nextDouble();
        sc.nextLine();
        String s=sc.nextLine();


        System.out.println("String: "+s);
        System.out.println("Double: "+y);
        System.out.println("Int: "+x);
    }
}
```
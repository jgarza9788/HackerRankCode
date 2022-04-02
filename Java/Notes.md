

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

## 
```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++)
        {
            String s1=sc.next();
            int x=sc.nextInt();
            System.out.printf("%-15s%03d%n", s1, x);
        }
        System.out.println("================================");
    }
}
```

## 
```java
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        for(int i=1;i<=10;i++)
        {
            System.out.printf("%d x %d = %d%n", N, i,N*i);
        }
        bufferedReader.close();
    }
}

```

## 
```java
import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc=new Scanner(System.in);
        int q=sc.nextInt();
        for(int i=0;i<q;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            int c = a;
            for(int j=0;j<n;j++){
                c += Math.pow(2, j)*b;
                System.out.printf("%s ",c);
            }
            System.out.println();
        }
        sc.close(); 
        
    }
}

```

## 
```java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int l = sc.nextInt();
        sc.nextLine();
        // // debugging
        // System.out.println(l);
        
        for (int i = 0;i<l;i++)
        {
            // System.out.println(i);
            
            String N = sc.nextLine();
            // System.out.println(N);
            
            int count = 0;
            boolean couldByte = false;
            boolean couldShort = false;
            boolean couldInt = false;
            boolean couldLong = false;
                        
            try {
                byte b = Byte.parseByte(N);
                count += 1;
                couldByte = true;
                // System.out.println("* byte");
            }
            catch(Exception e) {
                //do nothing
            }
            
            try {
                short b = Short.parseShort(N);
                count += 1;
                couldShort = true;
                // System.out.println("* short");
            }
            catch(Exception e) {
                //do nothing
            }
            
            try {
                int b = Integer.parseInt(N);
                count += 1;
                couldInt = true;
                // System.out.println("* int");
            }
            catch(Exception e) {
                //do nothing
            }
            
            try {
                long b = Long.parseLong(N);
                count += 1;
                couldLong = true;
                // System.out.println("* long");
            }
            catch(Exception e) {
                //do nothing
            }
            
            if (count > 0)
            {
                System.out.println(N + " can be fitted in:");
                
                if (couldByte)
                {
                    System.out.println("* byte");
                }
                
                if (couldShort)
                {
                    System.out.println("* short");
                }
                
                if (couldInt)
                {
                    System.out.println("* int");
                }
                
                if (couldLong)
                {
                    System.out.println("* long");
                }
                
            }
            else
            {
                System.out.println(N + " can't be fitted anywhere.");    
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

        Scanner in=new Scanner(System.in);
        String a;
        int i=1;
        while(in.hasNext())
            {
            a=in.nextLine();
            System.out.println(i+" "+a);
            i++;
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

        Scanner sc=new Scanner(System.in);
        int B = sc.nextInt();
        int H = sc.nextInt();
        
        if (B > 0 & H > 0)
        {
            System.out.println(B*H);
        }
        else
        {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }

    }
}
```

## 
```java

```


## 
```java

```

## 
```java

```

## 
```java

```

## 
```java

```
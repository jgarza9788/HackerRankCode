

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
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        String s = Integer.toString(n);
        System.out.println("Good job");
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


import java.util.Calendar;
// import java.time.DayOfWeek;
// import java.time.LocalDate;

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    

    public static String findDay(int month, int day, int year) {
        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.MONTH, month-1);
        cal.set(Calendar.DAY_OF_MONTH, day);
        cal.set(Calendar.YEAR, year);
        return cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.US).toUpperCase();
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);
        System.out.println(res);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

```

## 
```java
import java.io.*;
import java.util.*;

import java.text.NumberFormat;
import java.util.Locale;

public class Solution {

    public static void main(String[] args) {

        // NumberFormat nf = NumberFormat.getInstance();
        Locale indiaLocale = new Locale("en", "IN");
        
        NumberFormat nf_us = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat nf_india = NumberFormat.getCurrencyInstance(indiaLocale);
        NumberFormat nf_china = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat nf_french = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        
        Scanner sc = new Scanner(System.in);

        double d = sc.nextDouble();

        System.out.println("US: " + nf_us.format(d));
        System.out.println("India: " + nf_india.format(d));
        System.out.println("China: " + nf_china.format(d));
        System.out.println("France: " + nf_french.format(d));
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
        
        Scanner sc = new Scanner(System.in);
        
        String a = sc.nextLine();
        String b = sc.nextLine();
               
        
        System.out.println(a.length() + b.length());
        
        if ( a.compareTo(b) > 0 )
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
        
        System.out.println( capitalize(a) + " " + capitalize(b));
    }
    
    public static String capitalize(String str) {
    if(str == null || str.isEmpty()) {
        return str;
    }

    return str.substring(0, 1).toUpperCase() + str.substring(1);
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
        
        
        Scanner sc = new Scanner(System.in);
        
        String s = sc.nextLine();
        int start = sc.nextInt();
        int end = sc.nextInt();
        
        System.out.println(s.substring(start,end));
        
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
        

        Scanner sc = new Scanner(System.in);
        
        String s = sc.nextLine();
        int k = sc.nextInt();
        
        // s = "somethingelse";
        // k = 3;
        
        // System.out.println(s.length());
        // System.out.println(s.length()-4);
        // System.out.println(s.length()-3);
        
        // String[] ss = new String[];
        ArrayList<String> ss = new ArrayList<String>();
        for (int i = 0;i <= s.length()-k ;i++)
        {
            // System.out.println(i);
            // System.out.println(k+i);
            // System.out.println(s.substring(i,k+i));
            ss.add(s.substring(i,k+i));
        }
        
        // System.out.println(ss);
        
        String SL = ss.get(0);
        String EL = ss.get(0);
        
        for(String x: ss)
        {
            // System.out.println(x);
            
            if (SL.compareTo(x) > 0)
            {
                SL = x;
            }
            
            if (EL.compareTo(x) < 0)
            {
                EL = x;
            }
        }
        
        System.out.println(SL + "\n" + EL);
        // System.out.println(EL);

        
        // Scanner scan=new Scanner(System.in);
        // String str=scan.next();
        // int k=scan.nextInt();
        // SortedSet<String> sets=new TreeSet<String>();
        // for(int i=0;i<=str.length()-k;i++)
        // {
        //     sets.add(str.substring(i,i+k));
        // }
        // System.out.println(sets.first());
        // System.out.println(sets.last());

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
    
    
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        
        // System.out.println(s);
        // s = "soemthing";
        
        String b = "Yes";
        
        for (int i =0;i <= s.length()-1;i++)
        {
            
            if (s.substring(i,i+1).equals(s.substring(s.length()-i-1,s.length()-i)))
            {
                //good
            }
            else
            {
                b = "No";
            }
            
        }
    
        System.out.println(b);
    }
}
```

## 
```java
import java.io.*;
import java.util.*;
import org.json.simple.JSONObject;



public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().toLowerCase();
        String b = sc.nextLine().toLowerCase();
        
        if (a.length() == b.length())
        {
            JSONObject a_obj = analyze_string(a);
            JSONObject b_obj = analyze_string(b);
            
            // System.out.println(a_obj.toString());
            // System.out.println(b_obj.toString());
            
            String a_str = a_obj.toString();
            String b_str = b_obj.toString();
            
            if (a_str.equals(b_str))
            {
                System.out.println("Anagrams");
            }
            else
            {
                System.out.println("Not Anagrams");
            }
            
        }
        else
        {
            System.out.println("Not Anagrams");
        }
    }
    
    public static JSONObject analyze_string(String s)
    {
        JSONObject obj = new JSONObject();
        
        // System.out.println(s);
        for (int i = 0; i <= s.length() -1 ;i++)
        {
            String l = s.substring(i,1+i);
            var v0 = obj.get(l);
            int v = 0;
            if (v0 == null)
            {
                v = 0;
            }
            else
            {
                v = (Integer)v0;
            }
            
            obj.put(l,v + 1);
        }
        
        // System.out.println(s);
        // System.out.println((Integer)obj.get("a"));
        // System.out.println(obj.toString());
        
        return obj;
    }
}
```

## 
```java
import java.io.*;
import java.util.*;
import java.util.regex.Pattern;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        
        // s = "                        ";
        s = s.trim().replaceAll("[!,?._'@\\s]+", " ");
        
        // System.out.println("|" + s + "|");
        if (s.isEmpty())
        {
            System.out.println(0);
        }
        else
        {
        
            // s = "           YES      leading spaces        are valid,    problemsetters are         evillllll".replaceAll("[!,?._'@\\s]+", " ");
            
            String REGEX = "\\s+";
            Pattern pattern = Pattern.compile(REGEX);
            String[] result = pattern.split(s);
            
            System.out.println(result.length);
            
            for(String data:result)
            {
                System.out.println(data); 
            }
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
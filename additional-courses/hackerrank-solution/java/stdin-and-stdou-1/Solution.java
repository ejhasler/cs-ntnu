import java.util.Scanner;

/**
 * Most HackerRank challenges require you read input from stdin (standard input)
 * and write output to stdout (standard output).
 * 
 * One popular way to read input from stdin is using the Scanner class and Specifying
 * the Input Stream as System.in. For example:
 * 
 * <code>
 * Scanner scanner = new Scanner(System.in);
 * String myString = scanner.next();
 * int myInt = scanner.nextInt();
 * scanner.close();
 * 
 * System.out.println("myString is: " + myString);
 * System.out.println("myInt is: + myInt");
 * </code>
 * 
 * The code above creates a Scanner object named scanner and uses it to read
 * a String and an int. it then closes the Scanner object because there is no more
 * input to read, and prints to stdout using System.out.println("String").
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

    }
}
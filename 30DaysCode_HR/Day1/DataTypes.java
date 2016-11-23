import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";

        Scanner scan = new Scanner(System.in);
         /* Declare second integer, double, and String variables. */
        /* Read and save an integer, double, and String to your variables.*/
        int i2 = scan.nextInt();
        scan.nextLine();
        double d2 = scan.nextDouble();
        scan.nextLine();
        String s2 = scan.nextLine();

        /* Print the sum of both integer variables on a new line. */
            System.out.println(i+i2);
        /* Print the sum of the double variables on a new line. */

		    System.out.printf("%.1f\n",d+d2);
        /* Concatenate and print the String variables on a new line;
        	the 's' variable above should be printed first. */
            System.out.println(s+s2);
             scan.close();
    }
}
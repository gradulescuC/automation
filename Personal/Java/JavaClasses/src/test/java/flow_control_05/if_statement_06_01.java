package flow_control_05;

import java.util.Scanner;

public class if_statement_06_01  // if statement  = A way through which we can pass the decision responsibility to the system
            // who will need to choose between executing statement x or statement y depending on the result of evaluating a condition

{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Please insert the current hour (a number between 1 and 24)");
        int time = sc.nextInt();

        if (time <= 10) // if it is earlier than 10 am

        {
            System.out.println("Good Morning"); // print in the console "Good Morning"

        }

        else if (time < 20) // else, if it is not earlier than 10 am but earlier than 8 pm

        {

            System.out.println("Good Day");  // print in the console "Good day"

        } else // if none of the above conditions are fulfilled

        {
            System.out.println("Good evening");  // print in the console "Good evening"
        }
    }
}

package basic_java_operations_01;

public class Operators_01_02 {
    public static void main(String[] args) {
        System.out.println("------------------------Arithmetical operators - are used to perform mathematical calculations----------------------------");
        int x=7;
        int y=8;
        int sum = x + y;
        System.out.println("x+y = " + sum);
        int difference = x - y;
        System.out.println("x-y = " + difference);
        int multiplication = x * y;
        System.out.println("x*y = " + multiplication);
        int division = x / y;
        System.out.println("x/y = " + division); // When we do the division between two whole numbers, the result will be a truncated number, in case the it will be a decimal number
        int modulo = y%x;
        System.out.println("y%x = " + modulo); // This is called a modulo operation, which means it will return the remainder of the division between the first and second number
        System.out.println("Current value of x is " + x+ " and the current value of y is:  " + y);
        // -----------------------------------------------------------------------------------

        System.out.println("------------------Assignment operators are used to assign a value to a variable (a.i. storing a value at the address identified by the name of the variable)------------------");
        x=10; // This is the "=" operator with which we can assign a new value to a variable
        System.out.println("Value of x after assigning the value of 10 is: " + x);
        x=x+3;
        System.out.println("Value of x after adding the value of 3 to it is: " + x);
        x+=3; //This is the "+=" operator which is used also to assign a value to a variable, but this time it will not replace the whole content
                    // but increase it with the value specified in the right of the operator
                        // the result will be the same as when applying the operator at line 18
        System.out.println("Value of x after adding again the value of 3 to it is: " + x);

        x=x-3;
        System.out.println("Value of x after decreaseing the value of 3 from it is: " + x);
        x-=3; //This is the "-=" operator which is used also to assign a value to a variable, but this time it will not replace the whole content
                        // but decrease it with the value specified in the right of the operator
                                 // the result will be the same as when applying the operator at line 25
        System.out.println("Value of x after decreaseing again the value of 3 from it is: " + x);


        x=x*3;
        System.out.println("Value of x after multiplying it with the value of 3 from it is: " + x);
        x*=3; //This is the "*=" operator which is used also to assign a value to a variable, but this time it will not replace the whole content
                    // but multiply it with the value specified in the right of the operator
                            // the result will be the same as when applying the operator at line 33
        System.out.println("Value of x after multiplying it again with the value of 3 from it is: " + x);


        x=x/3;
        System.out.println("Value of x after dividing it by 3 from it is: " + x);
        x/=3; //This is the "/=" operator which is used also to assign a value to a variable, but this time it will not replace the whole content
                         // but divide it with the value specified in the right of the operator
                                 // the result will be the same as when applying the operator at line 41
        System.out.println("Value of x after dividing again it by 3 from it is: " + x);

        // -----------------------------------------------------------------------------------

        System.out.println("------------------Comparison operators are used to check whether two variables have the same value or if a variable has a specific value" +
                "Their result will be a boolean result (TRUE or FALSE)------------------");



        boolean condition = y>=6;
        // 1. Check if y is greater or equal than 6
        condition = y>=6;
        System.out.println("y>=6:" + condition);

        // 2. Check is x has the same value as y
        condition = x>y;
        System.out.println("x==y" + condition);

        // 3. Check if x and y are different
        condition = x!=y;
        System.out.println("x!=y" + condition);

        // 4. Check if x is smaller than y
        condition = x<y;
        System.out.println("x<y:" + condition);

        // 5. Check if x is smaller or equal than y
        condition = x<=y;
        System.out.println("x<=y: " +condition);

        // 6. Check if x is greater than y
        condition = x>y;
        System.out.println("x>y: " + condition);

        // -----------------------------------------------------------------------------------

        System.out.println("-----------------Logical operators are used in combination with the comparison operators to evaluate complex conditions------------------");

//         && - means AND - all sub-conditions must be evaluated as TRUE in order for the complex condition to be true
//         || - means OR - at least one of the sub-conditions must be evaluated as TRUE in order for the complex condition to be true
//         ! - means NOT - it will check the oposite of the condition (usually used when we want to check if something is false)


        /*

        Example of using the NOT operator:
        We are on a webpage and we want to check if a button is displayed, but only want to treat the case in which
        it is not, otherwise we want to move on.

        In this case we can do like this:

        if(!isDisplayed()){
        System.put.println("Error: The button is not visible on the webpage. Test execution will be stopped")
        }

        In this case the condition "!isDisplayed()" will do the exact same thing as "isDisplayed() == False", the only
        difference being that it is shorter

         */

        int a = 6;
        condition = !(a<5 || a<10);
        System.out.println("!(a<5 || a<10): " + condition); // first a<5 will be evaluated, and it will return FALSE
                                                // since it returned false it will go to the next condition
                                                    // a<10 will be evaluated, and it will return TRUE
                                                        // the final condition will be evaluated: FALSE or TRUE = TRUE
                                                            // the NOT operator will be applied: NOT TRUE = FALSE
        condition = a<5 && a<10;
        System.out.println("a<5 && a<10: " + condition); // first a<5 will be evaluated, and it will return FALSE
                                             // since it returned false it will NOT go to the next sub-condition
                                                // because the sub-conditions are linked with an && operator, which means
                                                    // both of them need to be true in order for the complex condition to be true

        System.out.println("---------------------------------");

        //Exercise 1: Check if the number stored in the variable n is greater than -2 but smaller than 13

        int n = 5;
        if (n > -2 && n < 13){
            System.out.println("The number is in the right interval. The condition \"n > -2 && n < 13\" was evaluated as true ");
        }

        //Exercise 2: Check if n has 3 or more digits:
        boolean three_or_more_digits = n>=100;
        System.out.println("Is " + n + "  greater or equal than 100? " + three_or_more_digits );

        // Exercise 3: Check if x is greater or equal than y
        boolean x_goe_than_y = x>=y;
        System.out.println("Is " + x + "  greater or equal than " +  y + "? " + x_goe_than_y);


        // -----------------------------------------------------------------------------------

    }
}
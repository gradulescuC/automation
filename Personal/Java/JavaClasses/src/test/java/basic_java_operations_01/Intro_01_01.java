package basic_java_operations_01;/*

NOTIONS TO COVER

- Variables
- Constants
- Primitive data types
- Non-Primitive data types

IDE = Integrated Development Environment
Compiler = Component of any IDE that translates the code that we write from human-readable text into a language understandable by the system
Indentation = A space between the margin of the file and the line of code
 */


// This is a comment, it won’t be interpreted by java. Single line comments can be made with double slash
/* This is a comment block
It is used for commenting multiple lines */


public class Intro_01_01 { // through convention, the name of the class should start with uppercase
                                    // In Java it is mandatory that the name of the class should be the same as the name of the file

    public static void main(String[] args) {
        System.out.println("--------------------VARIABLES-----------------------");
        /*
        A variable is a location in memory to hold data. To indicate the storage area, each variable should be given a unique name.
        In order to use a variable, we must first declare it
        declaration of a variable = reserving memory for it
        The declaration of a variable can be done through specifying its data type and its name
        Data type = propery that tells the system what kind of information can we store inside a variable
        After we declare the variable we need to save some information in it in order to use it. This process is called initialization

        Rules for naming variables:

        Names can contain letters, digits, underscores, and dollar signs
        Names must begin with a letter
        Names should start with a lowercase letter and it cannot contain whitespace
        Names are case sensitive ("myVar" and "myvar" are different variables)
        Reserved words (like Java keywords, such as int or boolean) cannot be used as names
         */
        System.out.println("Let's define a variable and print its content on the screen");
        int age; // here we declared a new variable called age
        age = 7; // here we initialised the variable called age with the value of 7
        System.out.println(age); // accessing the information inside a variable means calling that variable

        System.out.println("Now let's change its value");
        age = 10; // We can also replace the information inside a variable. This process is called overriding
        System.out.println(age);/* We can print the content of a variable on the screen using the line System.out.println(<nameOfTheVariable>);
                                 System.out.println means that we are going to print the information stored in the variable and then move to the next line
                                 System.out.print means that we are going to print the information stored in the variable but stay on the same line
        */
        int days = 7; // We can also declare and initialise a variable in one single line of code


        System.out.println("--------------------CONSTANTS-----------------------");

        /*
        A constant is a reserved memory that contains information which cannot be changed
        In order to define a constant we need to specify the keyword "final" before the data type
        Through convention, the name of a constant must be set in capitals
         */
        final int WEEKS = 4;
//        WEEKS = 3; // this line of code will return syntax error because we cannot change a constant

        System.out.println("Let's define and print a constant storing how many hours there are in a day - there are always 24 hours (or are there?)");
        final int HOURS_IN_A_DAY =24;
        System.out.println(HOURS_IN_A_DAY);


        System.out.println("--------------------PRIMITIVE DATA TYPES (CARE SUNT PREDEFINITE IN JAVA)-----------------------");
        System.out.println(

                "A primitive data type specifies the size and type of variable values, and it has no additional methods. \n" +
                        "There are eight primitive data types in Java:\n" +
                        "byte - stores whole numbers from -127 to 127\n" +
                        "short - stores whole numbers from -32768 and 32767\n" +
                        "int - stores whole numbers from -2147483648 to 2147483647 \n" +
                        "long - stores whole numbers from -9223372036854775808 to 9223372036854775807\n" +
                        "float - stores decimal numbers. It can store up to 6 decimals. If the number has more decimals it either cuts the rest of the decimals or rounds to the closed number\n" +
                        "double - stores decimal numbers. It can store up to 6 decimals.  If the number has more decimals it cuts the rest of the decimals\n" +
                        "boolean - stores true or false values\n" +
                        "char - stores a single character/letter or ASCII values"
        );

        float num = 12.3456789f; // in order to define a float number we need to specify the f at the end of the string so that the system knows we are talking about a float
        double num1 = 12.34567890123456789;
        byte num2 = 36;
        short num3  = 21890;
        int num4 = 123789023;
        long num5 = 9223372036854775807L; // just as with float, we need to specify a capital L at the end of the number
        boolean num6 = true;
        char num7 = 't'; // char values must be inclosed in quotes, not double quotes

        System.out.println(num);
        System.out.println(num1);
        System.out.println(num2);
        System.out.println(num3);
        System.out.println(num4);
        System.out.println(num5);
        System.out.println(num6);
        System.out.println(num7);


        System.out.println("--------------------NON-PRIMITIVE DATA TYPES-----------------------");
        System.out.println("Non-Primitive data types refer to objects and hence they are called reference types. Examples of non-primitive types include Strings, Arrays, Classes, Interface, etc.\n" +
                "Strings: String is a sequence of characters. But in Java, a string is an object that represents a sequence of characters. The java.lang.String class is used to create a string object.\n" +
                "Arrays: Arrays in Java are homogeneous data structures implemented in Java as objects. Arrays store one or more values of a specific data type and provide indexed access to store the same. A specific element in an array is accessed by its index.\n" +
                "Classes: A class in Java is a blueprint which includes all your data. A class contains fields(variables) and methods to describe the behavior of an object.\n" +
                "Interface: Like a class, an interface can have methods and variables, but the methods declared in interface are by default abstract (only method signature, no body)");
        /*Difference between primitive and non-primitive data types
            Primitive types are predefined in Java. Non-primitive types are created by the programmer and is not defined by Java.
            Non Primitive types can be used to call methods to perform certain operations, while primitive types cannot.
            A primitive type always has a value, whereas non-primitive types can be null.
            A primitive type starts with a lowercase letter, while non-primitive types start with an uppercase letter.*/

        System.out.println("-------------------STRINGS-------------------");
        /*Strings, which are widely used in Java programming, are a sequence of characters. In the Java programming language, strings are objects.
        The Java platform provides the String class to create and manipulate strings. String greeting = "Hello world!";
        Strings are concatenated with +
        String object has methods like (.length, .toUpperCase, .contains etc)*/

        String greeting = "Test"; // We defined a variable called greeting in which we stored the text 'Test'
        System.out.println(greeting.length()); // We checked how many characters there are in the text that we stored in the variable
        System.out.println(greeting.contains("Te")); // We checked if the text that we stored contains the letters 'Te'
        System.out.println(greeting.toUpperCase()); // We printed the text in uppercase
        System.out.println(greeting); // The uppercase method was applied only at run-time, but it will not change the value of the variable
                // To find out more methods that can be used with strings, write the name of the variable that stores the string followed by a dot

        System.out.println("---------------TYPE CASTING---------------------");
        /*Type casting is when you assign a value of one primitive data type to another type. In Java, there are two types of casting:
            Widening Casting (automatically) - converting a smaller type to a larger type size byte -> short -> char -> int -> long -> float -> double
            Narrowing Casting (manually) - converting a larger type to a smaller size type double -> float -> long -> int -> char -> short -> byte
         */
        System.out.println("----------------OPERATORS-------------------");
            /*Operators are used to perform operations on variables and values. Java divides the operators into the following groups:
                Arithmetic operators Assignment operators Comparison operators Logical operators
            */
        System.out.println("Arithmetic operators are used to perform common mathematical operations." +
                "The arithmetic perators are:" +
                "+" + // sum
                "-" + // extraction
                "*" + // multiplication
                "/" + // division
                "%" + // modulo (returns the remainder of the division)
                "++" + // incrementing operator -> incresease the value of the variable with 1
                "--"); // incrementing operator -> decresease the value of the variable with 1


        System.out.println("Assignment operators are used to assign values to variables." +
                "The assignment operators are:" +
                "=" +
                "+=" +
                "-=" +
                "*=" +
                "/=");


        System.out.println("Comparison operators are used to compare two values:" +
                "The comparison operators are:" +
                "==" +
                "!=" +
                ">" +
                "<" +
                ">=" +
                "<=");

        System.out.println("Logical operators are used to determine the logic between variables or values:" +
                "The logical operators are:" +
                "&&" +
                "||" +
                "!");
    }
}
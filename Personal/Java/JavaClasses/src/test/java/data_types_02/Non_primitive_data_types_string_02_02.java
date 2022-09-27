package data_types_02;

public class Non_primitive_data_types_string_02_02 {

    public static void main(String[] args) {
        // Non primitive data types: Class, Object, String, Array, Interface
        String hello = ""; // defining a variable with a String data type
        System.out.println(hello); // printing the string on the screen will actually print nothing because the string we defined is empty
        String firstName = "Gabriela"; // declaring and initialising a String storing the value of "Gabriela"
        String lastName = "Mateescu"; // declaring and initialising a String storing the value of "Mateesc"
        System.out.println("-----------String concatenation-------------");
        // string concatenation means connecting two variables containing two different strings into a single one

        System.out.println(firstName + " " + lastName);

        System.out.println("-----------String methods-------------");
        System.out.println("firstName.length(): " + firstName.length());
        System.out.println("firstName.toUpperCase(): " + firstName.toUpperCase());
        System.out.println("firstName.isEmpty()" + firstName.isEmpty());
    }
}

package data_types_02;

public class Type_casting_02_04 {

    public static void main(String[] args) {

        System.out.println("-------------Type casting-------------");

        // Type casting means forcing the type of a variale to another type

        double PI = 3.14; // here we declared a new variable of type double, storing a double value

        System.out.println("------------Manual casting--------------");
        int int_pi = (int) PI; // now we want to force the data type of PI to be int instead of double

        System.out.println("Initial value of PI: " + PI); // it will print 3.14
        System.out.println("Resulting value after casting: " + int_pi + "\n"); // it will print 3, because int does not support coma-separated values

        System.out.println("------------Automatic casting--------------");

        // automatic casting is a type of conversion that is being done without the explicit intervention of the developer
                    // it is usually done from a smaller type to a larger type, but not the other way rounf

        int age = 13;
        float new_age;
        new_age = age; // it will convert the value stored in the variable age from int to float
        System.out.println("Initial value of age: " + age );
        System.out.println("Resulting value after manual casting: " + new_age + "\n");

        float weight = 55.65f;
//        int new_weigt = weight; // this will return error, because you are trying to cast a wider type to a smaller type
        int new_weigt = (int) weight; // this will work, but with the cost of data loss

        System.out.println("Initial value of weight: " + weight);
        System.out.println("Resulting value after manual casting: " + new_weigt);
    }
}

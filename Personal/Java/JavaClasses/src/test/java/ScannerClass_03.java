import java.util.Scanner;

public class ScannerClass_03 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); // I instantiated an obiect of the class Scanner called sc

        System.out.println("Insert the grade of the student");

        int grade = sc.nextInt(); // the method nextInt() is a method from the class Scanner
                                        // in order to access a method of any class we need to instantiate an object of that specific class


//        String studentName = sc.nextLine(); // instructs the systemul the ask a text from the keyboard
//        int studentAge = sc.nextInt(); //  instructs the systemul the ask a number from the keyboard


        if (grade <= 4 && grade >= 1) {
            System.out.println("The student didn't pass");
        } else if (grade > 4 && grade <= 6 )
        {
            System.out.println("The student didn't learn enoguh");
        } else if (grade == 7 || grade == 8) {
            System.out.println("The student has good grades. He learned a lot");
        } else if (grade == 9 || grade == 10 ){
            System.out.println("The student is very diligen");
        } else {
            System.out.println("Insert a grade between 1 and 10");
        }
    }
}


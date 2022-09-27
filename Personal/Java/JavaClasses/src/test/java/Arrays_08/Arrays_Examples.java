package Arrays_08;

public class Arrays_Examples {
    public static void main(String[] args) {
        int[] age = new int[5];
        age[0] = 12;
        age[1] = 4;
        age[2] = 5;

        int[] age1 = {12, 14, 5, 2, 5, 6};
        for (int i = 0; i <= 5; i++) {
            System.out.println(age1[i]);
        }
        System.out.println("Lungimea array-ului este " + age1.length);


        System.out.println("--------------------------------------------");


        // declaram si initializam
        String[] cars = {"Volvo", "BMW", "Ford", "Trabant", "Dacia"};

        // putem suprascrie valorile din sir
        cars[0] = "Opel";

        // aflam dimensiunea sirului
        System.out.println(cars.length);
        // accesam elementele, pornind de la 0
        System.out.println(cars[0].toUpperCase());


        int n = 3;
        int[] newage = new int[n]; // declarare
        newage[0] = 18; // 0 is the index of the array, 18 is the element it holds
        newage[1] = -3; // initializare cu valori
        newage[2] = 200;

        System.out.println(age[age.length - 1]);

        // create an array
        int[] numbers = {3, 7, 5, -5};

        // iterating through the array with for each
        for (String car : cars) {
            System.out.println(car);
        }

        for (int i = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }


    }
}

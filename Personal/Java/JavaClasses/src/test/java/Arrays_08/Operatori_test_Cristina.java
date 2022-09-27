package Arrays_08;

import java.util.Scanner;

public class Operatori_test_Cristina {
    public static void main(String[] args) {
        // Operatori aritmetici
        System.out.println("Restul impartii lui 10 la 3 este: " + 10%3);
        int a = 0;
        System.out.println("Valoarea initiala a lui a este: " + a);
        a++; // echivalent cu a = a + 1
        System.out.println("Dupa incrementare valoarea lui variabilei a a devenit: " + a);
        a--;
        System.out.println("Dupa decrementare valoarea variabilei a a devenit: " + a); //echivalent cu a = a - 1

        //Operatori de asignare
        a = 10;
        System.out.println("Valoarea lui a dupa asignare este: " + a);
        a = a + 5;
        System.out.println("Dupa asignare valoarea lui a a devenit: " + a);
        a+=5; // echivalent cu a = a + 5
        System.out.println("Dupa asignarea cu instructiune echivalenta valoarea lui a a devenit: "+ a );
        a = a - 2;
        System.out.println("Dupa asignare valoarea lui a a devenit: " + a);
        a-=2; // echivalent cu a = a - 2
        System.out.println("Dupa asignarea cu instructiune echivalenta valoarea lui a a devenit: "+ a );

        // Operatori de comparatie

        System.out.println(a == 2);
        System.out.println(a = 2);

        double discount = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Insereaza pretul ");
        double price = sc.nextDouble();
        System.out.println("Insereaza clasa ");
        int c = sc.nextInt();
        System.out.println("Insereaza varsta calatorului ");
        int age = sc.nextInt();
        if (age >=65 && c == 1) {
            discount = 0.10;
        }
        else {
            discount = 0.05;
        }
        System.out.println(discount);

        if (!(age >=65 || c == 1)) {
            discount = 0.10;
        }
        else {
            discount = 0.05;
        }
        System.out.println("Noul discount este: " + discount);
    }
}

package flow_control_exercises_07;

import java.util.Scanner;

public class PachetCalatorie {
    public static void main(String[] args) {

         double discount = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Insereaza pretul");
        double price = sc.nextDouble();
        System.out.println("Insereaza varsta calatorului");
        int age = sc.nextInt();
        System.out.println("Insereaza numarul de copii");
        int nrc = sc.nextInt();
        sc.nextLine();
        System.out.println("Insereaza sezonul");
        String s = sc.nextLine();
        System.out.println("Insereaza clasa");
        int c = sc.nextInt();
        double taxa = 0;

        System.out.println(price);

        if  (age >=65){
            discount = 0.15;
        }
        else {
            if (nrc>=1){
                discount = 0.10;
            }
        }

        if (s == "iarna"){
            discount  = discount + 0.10;
        }

        if(c==1){
            taxa = 0.03;
        }
        else
        {
            taxa = 0.01;
        }

        price = price + price * discount -  price * taxa;
        System.out.println(price);

    }
}
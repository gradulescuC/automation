package RezolvareaTemelor;

import java.util.Scanner;

public class GhicitoareCuSwitch {
    public static void main(String[] args) {

        final String ANIMAL = "pisica";

        System.out.print("introduce-ti numele animalului ");
        Scanner valoareIntrodusa = new Scanner(System.in);
        String animalulAfostGhicit = valoareIntrodusa.nextLine();

        int counter = 1;

        while (!(animalulAfostGhicit.equals(ANIMAL)) && counter != 4) {

            switch (counter) { //caine -> pisica == caine? Nu
                case 1:
                    System.out.println("gresit,este un animal de casa,mai ai 2 incercari");
                    animalulAfostGhicit = valoareIntrodusa.nextLine();
                    counter++;
                    break;

                case 2:
                    System.out.println("gresit,mananca soareci,mai ai o incercare");
                    animalulAfostGhicit = valoareIntrodusa.nextLine();
                    counter++;
                    break;

                case 3:
                    System.out.println("Ai pierdut jocul,incearca din nou");
                    counter++;
                    break;

            }
        }
        if (ANIMAL == animalulAfostGhicit) {
            System.out.println("bravo,esti cel mai tare");
        }

    }
}
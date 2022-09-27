package RezolvareaTemelor;

import java.util.Scanner;

public class GhicitoareCuWhile {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Ghiceste animal mare");

        String corect_answer = "Girafa";

        int counter=0;
        String guess="";

        while (!guess.equals(corect_answer) && counter<=2) {
            counter++;
            if (counter==1) {
                System.out.println("Indiciu: are gatul lung");
            } else if (counter==2) {
                System.out.println("Indiciu: incepe cu litera G");
            } else if (counter==3) {
                System.out.println("Indiciu: e galbena cu pete");
            }
            guess = sc.next();
        }
        String msg = (guess.equals(corect_answer)) ? "You win":"You lose";
        System.out.println(msg);
    }
}
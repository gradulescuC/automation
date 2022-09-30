import java.util.*;

public class Trial {

    public static void main(String args[]) {

    /*
    6. Citim un string de la tastatura. Trebuie sa gasim literele duplicate din string si sa numaram de cate ori apar. Afisam rezultatul.
    Exemplu:
    INPUT: abracadabra
    OUTPUT: a-> 5, b->2; r->2
    Observati ca literele 'c' si 'd' nu apar in output pentru ca nu reprezinta duplicate
    */

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the text:");

        String text = scanner.nextLine();

        int[] count1 = new int[256];

        System.out.println(text.charAt(0));
        System.out.println(count1['t']);
         System.out.println(count1[text.charAt(0)]);
         System.out.println(count1[text.charAt(1)]);

        for (int i = 0; i < text.length(); i++)
        {
            System.out.println(i);
            count1[text.charAt(i)]++;
        }
    }
}
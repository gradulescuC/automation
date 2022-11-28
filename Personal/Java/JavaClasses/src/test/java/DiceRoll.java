import java.util.Random;
import java.util.Scanner;

public class DiceRoll {
    public static void main(String[] args) {
        Random rand = new Random();
        int upperbound = 2;
        int dice_roll = rand.nextInt(upperbound);
        Scanner sc= new Scanner(System.in);
        System.out.println("Introduceti zarul");
        int zar = sc.nextInt();
        if (dice_roll == zar ){
            System.out.println("Ai ghicit. Felicitari! ai ales " + zar + " si a fost " + dice_roll);
        } else if (zar>dice_roll) {
            System.out.println("Ai pierdtu. Ai ales un numar mai mare. Ai ales " + zar + " si a fost "+ dice_roll);
        }else {
            System.out.println("Ai pierdtu. Ai ales un numar mai mic. Ai ales " + zar + " si a fost "+ dice_roll);
        }
    }


}

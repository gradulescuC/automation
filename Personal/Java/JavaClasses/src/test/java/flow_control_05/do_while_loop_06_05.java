package flow_control_05;

public class do_while_loop_06_05 {
    public static void main(String[] args) {
        int a = 0;
        do {
            System.out.println(a);
            a++;
        }
        while (a < 5);

        System.out.println("----------------------");
        int i = 3;
        do {
            System.out.println("i = "+ i);
            System.out.println("a = " + a);
            a = a/i;
            i--;
        }
        while (i>0);

        System.out.println("-----------------------");

        int x = 3;
        do {
            System.out.println("Codul se executa cel putin o data; si continua sa se execute atat tp cat conditia inca e TRUE");
            x++; // nu uitiati sa il incrementati pe x !!!
        }
        while (x <= 3);
    }
}

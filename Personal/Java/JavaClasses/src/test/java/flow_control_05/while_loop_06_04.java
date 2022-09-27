package flow_control_05;

public class while_loop_06_04 {
    public static void main(String[] args) {
        int a = 0;
        while(a<5){
            System.out.println(a);
            a++;
        }
        System.out.println("----------------------");
        int i = 3;
        while(i>0){
            System.out.println("i = "+ i);
            System.out.println("a = " + a);
            a = a/i;
            i--;

        }

        System.out.println("--------------------------");

        //printat 101 dalmatieni
        int nrd=1;
        while (i<=101) {
            if (i==1) {
                System.out.println("Pogo");
            } else {
                System.out.println("dalmatianul no.: "+ nrd);

            }

            i++;

        }

    }
}


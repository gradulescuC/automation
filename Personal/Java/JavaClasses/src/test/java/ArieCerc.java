import java.lang.Math;

public class ArieCerc {

        public static double AriaCercului(double r) {
//            final double PI = 3.14;
            double Aria = Math.PI*r*r;
            return Aria;
        }

        public static void main(String[] args) {
            System.out.println("Aria cercului este: " + AriaCercului(6));
            System.out.println("Aria cercului este: " + AriaCercului(3.1));
            System.out.println("Aria cercului este: " + AriaCercului(32.72));
        }

}

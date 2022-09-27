package Methods_09;

public class MethodScope {
    public static void main(String[] args) {

        // x = x + 1; -> this is not a valid instruction because x is not visible here

        int x = 100;
        System.out.println(x);
    }
}

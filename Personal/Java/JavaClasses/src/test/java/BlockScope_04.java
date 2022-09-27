public class BlockScope_04 {
    public static void main(String[] args) {
        // x = x + 1 -> this is not a valid instruction because x is not visible here
        {
            // x = x + 1 -> this is not a valid instruction because x is not visible here
            int x = 100;
            System.out.println(x);
        }
        // x = x + 1 -> this is not a valid instruction because x is not visible here
    }
}
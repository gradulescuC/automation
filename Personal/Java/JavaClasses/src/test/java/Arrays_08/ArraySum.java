package Arrays_08;

public class ArraySum {

    public static void main(String[] args) {
        // afisati suma elementelor unui array
        int[] numbers = {2, 7, 8};

        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum = sum + numbers[i];
        }
        System.out.println(sum);
    }
}

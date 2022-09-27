package Arrays_08;

public class ArrayMerge {
    public static void main(String[] args) {
        //avand doua array-uri date generati un nou array cu valorile concatenate

        int[] numbers1 = {5, 7, 9};
        int[] numbers2 = {-12, 423};

        int[] numbers = new int[numbers1.length+numbers2.length];

        for (int i=0; i< numbers1.length; i++) {
            numbers[i] = numbers1[i];
        }
        for (int i=0; i< numbers2.length; i++) {
            numbers[i+numbers1.length] = numbers2[i];
        }
        for (int number:numbers) {
            System.out.println(number);
        }
    }
}
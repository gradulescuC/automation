package Arrays_08;

public class ArrayMax {
    public static void main(String[] args) {

        //afisati nr. maxim dintr-un array
        int[] numbers = {2375685, -4, 1000, 5, -23654, 237568500, 1000}; //am declarat si initializat arrayul
        int max = 0; // valoare de pornire pt max, ca tipul de date primitive nu pot fi nule
        if(numbers.length > 0) {
            max = numbers[0]; // daca arrayul are valori, atunci presupunem ca primul element exte max
        }
        for(int i = 0; i < numbers.length; i++) { // parcurgem elementele din array folosidu-ne de indexul lor
            if(numbers[i] > max) {
                max = numbers[i]; //daca nr. curent de max, il salvam in max
            } //inchide if-ul
        } //inchide for-ul
        if(numbers.length == 0) {
            System.err.println("Arrayul e gol"); //daca arrayul e gol, printam o !eroare!
        } else {
            System.out.println(max);// printam nr. maxim dupa ce l-am aflat in for
        }
    } // inchide functia main
} // inchide clasa
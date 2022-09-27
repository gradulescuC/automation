package Arrays_08;

public class RemoveElemArray {

    public static void main(String[] args) {
        // remove x from array
        int x = 3;
        int[] numbers = {3, 3, 8, 3, 3, 5, 8, 3, 7, 3, 9, 3, 10};
        int counter = 0;
        int howManyX = 0;

        // aflam de cate ori apare x ca sa stim dimensiunea noului array
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == x) {
                howManyX++;
            }
        }

        // declaram un array gol de dimensiunea necesara
        int[] result = new int[numbers.length-howManyX];

        // parcurgem array cu for
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == x) {
                counter++; // numaram de cate ori am intalnit x pana acum ca sa stim la ce index punem valoarea in noul array
                continue; // daca il intalnim pe x, nu facem nimic si ne intoarcem la inceput de for cu continue
            }
            // indexul noului array va fi tot tp. i minus de cate ori am intalnit pe x si am crescut
            result[i-counter] = numbers[i];
        }

        // printam cu for each noul array
        for (int nr : result) {
            System.out.println(nr);
        }
    }
}
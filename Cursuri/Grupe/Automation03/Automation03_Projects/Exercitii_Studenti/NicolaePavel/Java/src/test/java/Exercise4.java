import java.util.*;

public class Exercise4 {

    public static void main(String args[]) {

        /*
        4. Scrieti un program care sterge duplicatele dintr-o lista de numere si sorteaza numerele.
        Examplu:
        Original array: [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7]
        After removing duplicates: [1,  2,  3, 4, 5, 6, 7]
        */

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the list:");
        int size = scanner.nextInt();
        Integer[] list = new Integer[size];
        System.out.println("Enter the elements of the list: ");

        for(int i = 0; i < size; i++) {
            list[i] = scanner.nextInt();
        }
        System.out.println("The created list is: " + Arrays.toString(list));

        int min = list[0];
        for (int i = 0; i < list.length; i++) {
            for (int j = i + 1; j < list.length; j++) {
                if (list[i] >= list[j]) {
                    min = list[j];
                    list[j] = list[i];
                    list[i] = min;
                }
            }
        }
        System.out.println("The sorted list is: " + Arrays.toString(list));
        System.out.println("Dimensiunea lui list este " + list.length);

        List<Integer> tmplist = Arrays.asList(list); // aici am creat o lista de la un array prin Array.asList care nu suporta adaugarea si stergerea de elemente pentru ca lista mosteneste automat proprietatile array-ului (care nu este resizable)
        System.out.println("Dimensiunea lui tmplist este " + tmplist.size());

        ArrayList<Integer> newList = new ArrayList<Integer>(); // aici am creat un arrayList pentru a putea rezolva problema de mai sus
        newList.addAll(tmplist);

        System.out.println("The original list is: " + tmplist);
        for (int i = 0; i < newList.size(); i++) {
            System.out.println("i este " + i);
            for (int j = i + 1; j <= newList.size()-1; j++) // aici am pus <=newList.size()-1 pentru ca am nevoie sa parcurg toata lista, dar sa nu imi crape cu outOfBound
            {
                System.out.println("j este " + j);
                if (newList.get(i) == newList.get(j)) {
                    newList.remove(j);
                    j--;
                }
            }
        }
        System.out.println("The final list is: " + newList);
    }
}

/*
1,2,2
i = 0; j = 1
lista[0] == lista[1] -> 1 == 2? Nu

i = 0; j = 2
lista[0] == lista[2] -> 1 == 2? Nu

i = 1; j = 2
lista [1] == lista[2]? -> 2==2? Da
lista.remove[2] -> Scoate 2*/
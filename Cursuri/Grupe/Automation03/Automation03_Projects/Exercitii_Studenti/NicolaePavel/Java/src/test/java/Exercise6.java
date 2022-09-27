import java.util.*;

public class Exercise6 {

    public static void main(String args[]) {

    /*
    6. Citim un string de la tastatura. Trebuie sa gasim literele duplicate din string si sa numaram de cate ori apar. Afisam rezultatul.
    Exemplu:
    INPUT: abracadabra
    OUTPUT: a-> 5, b->2; r->2
    Observati ca literele 'c' si 'd' nu apar in output pentru ca nu reprezinta duplicate
    */

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the text:");

        String text = scanner.nextLine();


        System.out.println("------ Method 1 ------");
        int[] count1 = new int[256]; // se declara un array cu 256 pozitii libere.
                                            // E nevoie de 256 pentru ca tu tratezi un array nu pe baza de index ci pe baza de caractere ASCII,
                                                    // iar codul ASCII are caractere identificabile de la codul 0 pana la codul 255 inclusiv, adica 256 de indexuri (trebuie sa le poata acoperi pe toate
                                                        // tabelul ASCII: https://www.ascii-code.com/

        for (int i = 0; i < text.length(); i++)  // se parcurge textul
        {
            count1[text.charAt(i)]++;// de cate ori se gaseste elementul respectiv, se creste contorul pentru acel element
                                             // instructiunea de mai sus se traduce ca fiind count1[text.charAt(0)] (pentru pozitia 0)
                                                     // adica count1[a] -> pentru ca charAt este o metoda accesibila prin intermediul String-ului text
            System.out.println("i este " + i + " elementul este " + text.charAt(i) + " si count este " + count1[text.charAt(i)]);

        } // am avut nevoie sa cream si sa parcurgem lista count ca sa vedem de cate ori apare fiecare caracter in textul pe care l-ai dat de la tastatura
                // am folosit acest count pentru afisare in for-ul urmator

        System.out.println("-----------------------------------------------------");
        char[] letter1 = new char[text.length()];

        for (int i = 0; i < text.length(); i++) { // aici incercam sa parcurgem array-ul ca sa accesam elementele
            letter1[i] = text.charAt(i); // cream un nou array, ca sa putem sa parcurgem vectorul in mod bidimensional, astfel incat sa nu afisam rezultatul final de mai multe ori
            int find = 0;
            for (int j = 0; j <= i; j++) { // vom parcurge tot array-ul, sa vedem daca elementul din pozitia i se mai gaseste undeva in vector
                if (text.charAt(i) == letter1[j]) // daca se mai gaseste
                    find++; // atunci crestem valoarea lui find de la 0 la 1
                System.out.println("i este " + i + " j este " + j + " find este " + find + " elementul este " + text.charAt(i) +  " si count este " + count1[text.charAt(i)]);
                // am afisat toate elementele ca sa iti fie mai usor sa vizualizezi rezultatele
            }
            if (find == 1 && count1[text.charAt(i)] > 1) {// vom afisa duplicatele o singura data, doar daca ele se gasesc de mai multe ori in sir.
                // Am adaugat si variabila find in conditie, pentru ca acel count1[text.charAt(i)]
                //                                                      va fi mereu > 1 pentru literele care apar de mai multe ori, si atunci se va afisa pe ecran rezultatul de cate ori apare litera (ex: a > 5 va aparea de 5 ori
                System.out.println(text.charAt(i) + " -> " + count1[text.charAt(i)]);
            }
        }


    }
}
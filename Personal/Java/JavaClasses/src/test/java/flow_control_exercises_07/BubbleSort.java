package flow_control_exercises_07;

public class BubbleSort {
    public static void main(String[] args) {
        int[] sortareArray = {10, 15, 45, 150, 13, 66, 4};
        int pahar = 0;
        System.out.println("-------------");
        for (int i = 0; i < sortareArray.length; i++) // facem un contor cu care sa stim pana cand sa sortam elementele
        {
            for (int j = 1; j < (sortareArray.length - i); j++) { // aici facem un contor cu care sa parcurgem array-ul. Pornim de la 1 de data asta, pentru ca ne intereseaza sa comparam doua pozitii consecutive
                if (sortareArray[j - 1] > sortareArray[j]) { // daca elementul de pe pozitia 1 este mai mare decat cel de pe pozitia 2 (adica daca la primele 2 pozitii 10 < 15)
                    pahar = sortareArray[j-1]; // atunci se va pune valoarea de la pozitia 0 intr-un "pahar", adica o adresa de memorie folosita temporar, ca sa nu pierdem valoarea respectiva
                    sortareArray[j-1] = sortareArray[j]; // la prima pozitie vom pune valoarea de pe a doua pozitie
                    sortareArray[j] = pahar; // in a doua pozitie vom pune valoarea din adresa de memorie tempoarara ("pahar")
                }
            }
            /*Exemplul de mai sus:
            1p>15? Nu -> Mergi la urmatoarea iteratie
            15>45? Nu -> Mergi la urmatoarea iteratie
            45>150? Nu -> Mergi la urmatoarea iteratie
            150 > 13? Da -> Atunci punem 150 in pahar, in locul lui 150 punem 13, si in locul lui 13 punem 150 din pahar
                        Noul array: 10,15,45,13,150,66,4
            150>66? Da -> Atunci punem 150 in pahar, in locul lui 150 punem 66, si in locul lui 6 punem 150 din pahar
                        Noul array: 10,15,45,13,66,150,4
            150>4? Da -> Atunci punem 150 in pahar, in locul lui 150 punem 4, si in locul lui 4 punem 150 din pahar
                        Noul array: 10,15,45,13,66,4,150*/

        }
        for (int i = 1; i<sortareArray.length;i++){
            System.out.println(sortareArray[i]);
        }

    }
}


package flow_control_05;

import java.util.ArrayList;
import java.util.List;

public class JumpStatements_06_07 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>(); // am definit o lista de numere
//        System.out.println(list);
//
//        for (int i = 1; i <= 10; i++) {
//            list.add(String.valueOf(i)); // am adaugat 11 valori in lista (0,1,2,3,4,5,6,7,8,9)
//        }
//
//        list.add(String.valueOf(5)); // am adaugat un nou element in lista: elementul 5. noua lista este 0,1,2,3,4,5,6,7,8,9,5
//
//        System.out.println("Valoarea curenta a listei este: " + list); // am printat lista curenta. Afiseaza [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
//
//        System.out.println(list.size()); // Am printat dimensiunea listei. Printeaza 11 pentru ca am 11 elemente in lista
//
//        int variabilaVerificare;
//        for (int i = 0; i < list.size(); i++) // am definit un for prin care sa parcurg lista.
//        // atata timp cat nu am ajuns la ultimul din lista (adica am parcurs toata dimensiunea listei)
//        // vreau sa mi se execute instructiunile din interiorul acoladelor
//        // am folosit operatorul < in loc de <= pentru ca intr-o lista primul element
//        // se afla la indexul 0, drept urmare pentru o lista cu 11 elemente, ultimul element se va afla la indexul 10
//        // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
//        //  0  1  2  3  4  5  6  7  8  9  10  -> ordinea indecsilor
//        {
//            System.out.println("Elementul curent din lista este: " + list.get(i) + " si are indexul " + list.indexOf(list.get(i))); // de investigat
//
//            variabilaVerificare = Integer.parseInt(list.get(i));
//
////            System.out.println("Valoarea curenta a variabilei de verificare este: " + variabilaVerificare);
//
//            if (variabilaVerificare == 5) {
//                System.out.println("Valoarea variabilei de verificare este " + variabilaVerificare + "si se afla la indexul" + list.indexOf(list.get(i)));
//                System.out.println(list.get(i));
//                System.out.println("Elementul curent din iteratie este:" + list.get(i));
//            }
//        }



        System.out.println("----------------------------");

        //        for(int i=1; i<=101; i++){
//            if(i==68)
//            {
//                break;
//            }
//            System.out.println("Am gasit dalmatianul " + i);
//        }

        for(int i=1; i<=101; i++)
        {
            if(i==68)
            {
                continue;
            }
            System.out.println("Am gasit dalmatianul " + i);
        }


        System.out.println("----------------------------");


//                // break iese din for
//                for (int i = 1; i < 102; i++) {
//                    System.out.println(i);
//                    if (i == 7) {
//                        break; // break opreste executia!
//                    }
//                }
//
//                // continue
//                for (int i = 1; i <= 101; i++) {
//
//                    if (i == 13) {
//                        System.out.println("Numarul pe care nu vrem sa-l pronuntam!");
//                        continue; // il sare pe 13
//                    }
//                    System.out.println(i);
//                }

//                // break poate fi folosit si in while
//                // opreste codul cand conditia e adevarata
//                int i = 1;
//                while (i < 10) {
//                    System.out.println(i);
//                    if (i == 7) {
//                        break;
//                    }
//                    i++;
//
//                }
//                // continue
//                int n = 1;
//                while (n < 10) {
//                    if (n == 7) {
//                        n++; //  nu uitam sa incrementam inainte de continue
//                        continue; // cand conditia e adevarata, se sare peste acest pas
//                    }
//                    System.out.println(n);
//                    n++;
//                }
//            }
//        }


    }
}

public class testDataTypes {
    public static void main(String[] args) {
        byte byteNumber = 120;
        short shortNumber = 12345;
        int intNumber = 347890;
        long longNumber = 678053489;
        double doubleNumber = 15.3;
        float floatNumber = 15.3f; // prin conventie se pune un f la finalul numarului ca sa indicam ca vrem acea valoare ca float
        boolean trueFalse = true;
        char charVariable= 'r'; // la char se poate stoca un singur caracter. Caracterul de char trebuie pus intre doua apostroafe

        System.out.print(byteNumber);
        System.out.println(shortNumber);
        System.out.println(intNumber);
        System.out.println(longNumber);
        System.out.println(doubleNumber);
        System.out.println(floatNumber);
        System.out.println(trueFalse);
        System.out.println(charVariable);

/* Exista doua metode print:
print (care printeaza totul pe un singur rand)
println (care printeaza si apoi muta cursorul pe randul urmator)
 */
        String stringObject = "testString"; // se pot stoca oricate caractere avem nevoie. Caracterul de string trebuie pus intre doua ghilimele
        // ca sa accesam metodele unui String specificam numele variabilei de tip String urmat de caracterul "."
        stringObject.length(); // returneaza valoare 10 (atatea caractere sunt in testString)
        stringObject.toLowerCase(); // returneaza valoarea teststring (a schimbat S in s)
        System.out.println(stringObject.contains("test")); // printeaza TRUE pentru ca testString contine test
        System.out.println(stringObject.contains("tst")); // printeaza FALSE pentru ca testString nu contine tst
        int intNumberTest = (int) 15.3; // am facut cast al valorii la INT
        System.out.println(intNumberTest);
//        System.out.println(intNumberTest++);
        System.out.println(++intNumberTest);
        System.out.println(--intNumberTest);

        intNumberTest = 56; // am stocat valoarea 56 la adresa de memorie numita intNumberTest
        System.out.println(intNumberTest);
        intNumberTest+=56; // va aduna valoarea 56 la valoarea deja existenta in variabila intNumberTest.
                                                    // (echivalent al intNumberTest = intNumberTest + 56)
        System.out.println(intNumberTest);
        intNumberTest-=56;
        System.out.println(intNumberTest);
        intNumberTest*=56;
        System.out.println(intNumberTest);
        intNumberTest/=56;
        System.out.println(intNumberTest);
//        intNumberTest = 347890;
        System.out.println(intNumber==intNumberTest); // printeaza FALSE pentru ca intNumber contine 347890 si intNumberTest contine 56
                                //ATENTIE! "=" este operator de atribuire, si simbolul "==" este operator de comparatie
        System.out.println(intNumber!=intNumberTest); // printeaza TRUE pentru ca intNumber contine 347890 si intNumberTest contine 56
                                            //ATENTIE! "==" verifica daca doua numere sunt egale
                                                    // "!=" verifica daca doua numere sunt diferite
        // byte byteNumber = 120;
        System.out.println(intNumber!=intNumberTest && byteNumber>65); // && = operator SI -> adica ambele conditii trebuie sa fie adevarate
                                            // pentru ca intreaga conditie sa fie adevarata
        System.out.println(intNumber==intNumberTest || byteNumber<65); // || = operator SAU -> adica oricare conditie este adevarata,
                                                                // atunci conditia compusa va fi de asemenea evaluata ca si adevarata
        //  stringObject = "testString";
        System.out.println(!(stringObject.isEmpty())); // stringObject.isEmpty() -> Returneaza false
                                                            // !(stringObject.isEmpty()) -> NOT FALSE -> TRUE
        System.out.println(intNumber != intNumberTest || byteNumber>65 && shortNumber <0);//  A || (B && C) ->  TRUE || (N/A && N/A)
                                                                                                        // ->TRUE || N/A -> TRUE
        // intNumber != intNumberTest -> Conditia 1 = ADEVARATA
        // byteNumber>65 -> Conditia 2 -> nu mai este evalauta
        // shortNumber <0 -> Conditia 3 -> nu mai este evaluata


        System.out.println(intNumber == intNumberTest || byteNumber>65 && shortNumber <0); // A || (B && C) -> FALSE || (TRUE && FALSE)
                                                                                                            // FALSE || FALSE -> FALSE

        // A =  intNumber != intNumberTest -> Conditia 1 = FALSA
        // B = byteNumber>65 -> Conditia 2 -> ADEVARATA
        // C = shortNumber <0 -> Conditia 3 -> FALSA


        System.out.println(byteNumber>65 && shortNumber >0 || intNumber!=intNumberTest);  // A || (B && C) -> TRUE || (TRUE && TRUE)
                                                                                            // -> TRUE || TRUE -> TRUE
        // A =  byteNumber>65  -> Conditia 1 = ADEVARATA
        // B = shortNumber >0 -> Conditia 2 -> ADEVARATA
        // C = intNumber!=intNumberTest -> Conditia 3 -> ADEVARATA
    }
}

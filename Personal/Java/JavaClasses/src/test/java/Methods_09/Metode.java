package Methods_09;

public class Metode {
    static void NameAndAge(String fname, int age) {
        System.out.println(fname + " is " + age + " years old");
    }

    // int = tipul de data al metodei/al ceea ce ar trebui sa returneze metoda
    // sumOfNumbers = numele metodei
    // int x, int y = lista de parametri
    // parametru = un placeholder al valorilor pe care urmeaza sa le ia metoda
    // avem nevoie de parametri ca sa stie sistemul de ce valori are nevoie pentru a apela metoda
    // apelarea metodei = identificarea adresei la care sunt stocate instructiunile din interiorul metodei
    // argumente = valori efective pe care le dam in timpul apelarii pentru a inlocui parametrii
    // atunci cand o metoda nu trebuie sa returneze nimic, folosim void
    // public este un modificator de acces care anunta sistemul ca functia/variabila poate sa fie folosita oriunde
    // private este un modificator de acces care anunta sistemul ca functia/variabila poate sa fie folosita DOAR in clasa curenta
    // protected este un modificator de acces care anunta sistemul ca functia/variabila poate sa fie folosita oriunde in pachetul curent, dar nu in alt pachet

    static int sumOfNumbers(int x, int y) {
        int sum = x + y;
        int diff=x-y;
        System.out.println("diferenta este: "+diff);
        int produs=x*y;
        System.out.println("produsul este "+produs);
        int divide=x/y;
        System.out.println("rezultatul impartirii este "+divide);
        return sum;
    }

    public static void main(String[] args) {
        NameAndAge("Andrew", 34);//apelare metoda NameAndAge

        System.out.println("suma este "+sumOfNumbers(3, 5)); // 3 si 5 sunt argumente care vor da viata parametrilor x si y
        System.out.println(sumOfNumbers(6, 9));
        System.out.println(sumOfNumbers(15, 66));
        System.out.println(sumOfNumbers(1954, 2532467));
    }

}
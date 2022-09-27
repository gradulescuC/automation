package Methods_09;

public class MethodsExercises {
    public static int age;

    // public = poate fi accesata din orice clasa
    // static = poate fi apelata fara a a vea nevoie de un obiect
    // void = nu returneaza nimic ca si output
    // numele metodei, incepe cu litera mica, urmat de paranteze rotunde
    public static void printGreetings() {
        System.out.println("Hello!");
        System.out.println("Goodbye!");
    }

    // name este un parametru/argument de tip String
    // ajuta metoda sa fie dinamica in functie de valoarea primita la apelare
    public static void printHelloPerson(String name) {
        name = name.toUpperCase();
        System.out.println("Hello " + name);
    }

    public static String prettyName(String nume, String prenume) {
        String full_name = nume + " " + prenume;
        return full_name;
    }

    public static void main(String[] args) {
        printGreetings();

        printHelloPerson("Maria");
        printHelloPerson("Ana");

        // ca si parametru la print, dam functia (indirect, rezultatul ei)
        System.out.println(prettyName("Mihailescu", "Anton"));

        // cand o functie returneaza ceva (output), putem sa pastram rezultatul intr-o variabila
        String nume_complet = prettyName("Pop", "Ana");
        System.out.println(nume_complet);


    }
}
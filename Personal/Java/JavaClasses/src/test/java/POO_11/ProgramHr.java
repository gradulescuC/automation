package POO_11;

public class ProgramHr {

    public static void main(String[] args){

        Angajat ml = new Angajat("Mihai", "Laurentiu", 2000, 'M', false, 15);
        ml.numeComplet();
        ml.verificareAptMunca();
        ml.afisareSalariuAnual();


        Angajat tl = new Angajat("Truica", "Lavinia", 2000, 'F', true, 22);
        tl.numeComplet();
        tl.verificareAptMunca();
        tl.afisareSalariuAnual();
        tl.marireSalariu(1.1);
        tl.afisareSalariuAnual();

    }
}
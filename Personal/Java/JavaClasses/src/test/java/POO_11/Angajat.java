package POO_11;

public class Angajat {
        String nume;
        String prenume;
        double salariu;
        int vechime;
        int varsta;
        char sex;
        boolean permis;
        boolean aptMunca;
        boolean studiiSuperioare;

        public Angajat(String nume, String prenume, double salariu, char sex, boolean studiiSuperioare, int varsta) {
            this.nume = nume;
            this.prenume = prenume;
            this.sex = sex;
            this.salariu = salariu;
            this.studiiSuperioare = studiiSuperioare;
            this.varsta = varsta;
            if (studiiSuperioare) {
                marireSalariu(1.2);
            }
        }

        public void numeComplet() {
            System.out.println(nume + " " + prenume);
        }

        public void marireSalariu(double procent) {
            salariu = salariu * procent;
        }

        public void afisareSalariuAnual() {
            System.out.println(salariu * 12);
        }

        public void verificareAptMunca () {
            if(varsta >= 16) {
                System.out.println("Apt de munca");
            } else {
                System.out.println("Minor");
            }
        }
    }

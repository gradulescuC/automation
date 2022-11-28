import java.util.Scanner;

public class CheckCharacter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduceti stringul");
        String prop = sc.next();
        if( prop.substring(0,1).toUpperCase().equals(prop.substring(-1,prop.length()).toUpperCase())){
            System.out.println("Primul si ultimul caracter sunt la fel");
        }else {
            System.out.println("Caracterele nu sunt la fel");
        }

    }
}


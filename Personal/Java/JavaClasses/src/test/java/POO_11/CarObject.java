package POO_11;

public class CarObject {
    public static void main(String[] args) {
        Car toyota = new Car("Toyota", true);   //am creat un obiect de tip car (instanta a clasei car)
        toyota.describe();
        toyota.accelerate(60);
        toyota.accelerate(30);
        System.out.println(toyota.actualSpeed);
        System.out.println(toyota.isRunning);
        toyota.brake();
        System.out.println(toyota.actualSpeed);
        System.out.println(toyota.isRunning);

        Car dacia = new Car("Dacia", false);
        dacia.paint("red");
        dacia.describe();
        dacia.accelerate(-50);
        System.out.println(dacia.actualSpeed);
        System.out.println(dacia.isRunning);
        dacia.brake();
        System.out.println(dacia.actualSpeed);
        System.out.println(dacia.isRunning);
    }


}
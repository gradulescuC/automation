package POO_11;

public class Car {
    // atribute (variabile)
    String model;
    final int maxSpeed=250;
    private String color; //encapsulation
    int actualSpeed;
    boolean isElectric;
    boolean isRunning;
    //constructor, are rolul de a declara valorile intiale la crearea unui obiect

    public Car (String model, boolean isElectric) {
        color = "white";
        this.model = model;
        this.isElectric = isElectric;
    }

    public void accelerate(int speed) {
        System.out.println("Wroom, Wroom!");
        actualSpeed += speed; // crestem viteza cu parametrul functiei
        if (actualSpeed > maxSpeed) {
            actualSpeed = maxSpeed;
        } else if (actualSpeed<0) {
            actualSpeed = 0;
            System.err.println("Viteza negativa");
        }
        isRunning = true;
    }

    public void brake () {
        actualSpeed = 0;
        isRunning = false;
        System.out.println("Stop!");
    }

    public void paint(String newColor){
        color=  newColor;
    }

    public String getColor() {
        return color;
    }

    public String getModel() {
        return model;
    }
    public void setModel(String model) {
        this.model = model;
    }
    public void describe() {
        System.out.println("Masina este modelul " + getModel() + " si are culoarea " + getColor());
    }

}


package Method_exercises_10;

public class max_3 {
    //cel mai mare numar din 3 numere
    public static int max(int x, int y, int z) {
        if (x >= y && x >= z) {
            return x;
        } else if (y >= x && y >= z) {
            return y;
        } else {
            return z;
        }
    }

    public static int media(int a, int b, int c) {
        return (a + b + c) / 3;
    }


    public static void main(String[] args) {
        max(1,5,6);
        media(1,5,6);

    }

}



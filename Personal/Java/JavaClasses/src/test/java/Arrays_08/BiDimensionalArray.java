package Arrays_08;

public class BiDimensionalArray {
    public static void main(String[] args) {
        // 2d array (matrice, grid)
        int[][] tastatura = {
                {1,2,3},
                {4,5,6},
                {7,8,9},
                {0}

        };

        for (int[] row : tastatura) {
            for (int column : row) {
                System.out.println(column);
            }
        }
    }
}

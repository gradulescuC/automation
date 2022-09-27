package Arrays_08;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Lists<shapes> {
    public static void main(String[] args) {

        // lists
        List<String> cars_list = Arrays.asList("Logan", "Sandero"); // fixed size
        List<String> shapes = new ArrayList<String>(); // dynamic size
        shapes.add("Cerc");
        shapes.add("Patrat");
        for(String shape:shapes)

        {
            System.out.println(shape);
        }
    }

}

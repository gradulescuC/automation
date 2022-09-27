package flow_control_05;

import java.util.ArrayList;
import java.util.List;

public class for_loop_06_02 {
    public static void main(String[] args) {

        // a for loop is a way through which we can execute a set of instructions multiple times until the condition is
        // no longer fulfilled

        for (int i = 0; i <= 5; i++) // i is like an iterator that will change it's value incrementally
        // depending on the incrementing value that we give it
        // in this for we used the ++ operator (called incrementing operator) which has the role
        // of increasing the value of a numeric field with the value of 1
        // the value of i will initially be 0, then it will grow to 1, then to 2
        // until the condition i<=5 is no longer fulfilled

        {
            System.out.println(i);
        }

        System.out.println("-------------------------------------------------------------------");

        for (int i = 1; i <= 101; i++) {
            System.out.println("This is the dalmation number " + i);
        }
        // Remember the array list we created in Non_primitive_data_types_lists_02_06.java? Now let's display it using a for loop

        List<String> str_list = new ArrayList<String>();
        str_list.add("Java");
        str_list.add("C++");

        for(int i=0;i<str_list.size();i++) // in this for we used the i pointer to go through each and every one of the indexes in the list
        {
            System.out.println(str_list.get(i)); // in each iteration we are going to print the current value stored at the memory address
            // identified by the current index
                // after the iteration is completed, the value of the index will increase by 1 through the increment operator (i++)
                        // and will enter the loop again, repeating the steps until the condition is no longer fulfilled
                                // a.i. untill the value of the index is no longer smaller than the size of the arraylist (i<str_list.size())
                                    // we used the "<" comparison operator and not "<=" because the first index in the list is 0
                                            // so subsequently the last index will be the number of elements -1
        }
    }
}



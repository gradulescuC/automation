package data_types_02;

import java.util.*;

public class Non_primitive_data_types_lists_02_06 {
    public static void main(String[] args) {

/*
A list in Java is a sequence of elements according to an order.
The List interface of java.util package is the one that implements this sequence of objects ordered in a particular fashion called List.
Just like arrays, the list elements can also be accessed using indices with the first index starting at 0. The index indicates a particular element at index ‘i’ i.e. it is i elements away from the beginning of the list.
Being an interface, it can be implemented by classes like ArrayList, Stack, Vector and LinkedList


Some of the characteristics of the list in Java include:

- Lists can have duplicate elements.
- The list can also have ‘null’ elements.
- Lists support generics i.e. you can have generic lists.
- You can also have mixed objects (objects of different classes) in the same list.
- Lists always preserve insertion order and allow positional access.

Initializing Java List

1) Using The asList Method:
    List<data_type> listname = Arrays.asList(array_name);
    The above statement creates an immutable list.

    If you want the list to be mutable, then you have to create an instance of the list using new and then assign
            the array elements to it using the asList method:
    List<data_type> listname = new ArrayList<> (Arrays.asList(array_name));
 */

        String[] strArray = {"Delhi", "Bucharest", "Andorra", "Cochabamba"};

//initialize an immutable list from array using asList method
        List<String> mylist = Arrays.asList(strArray);

//print the list
        System.out.println("Immutable list:");
        for (String val : mylist) {
            System.out.print(val + " ");
        }
        System.out.println("\n");

//initialize a mutable list(arraylist) from array using asList method
List<String> arrayList = new ArrayList<>(Arrays.asList(strArray));
System.out.println("Mutable list:");
//add one more element to list
arrayList.add("Test");
//print the arraylist
for (String val : arrayList) {
    System.out.print(val + " ");
     }

/*
2) Using List.add()
As the list is just an interface it cannot be instantiated. But we can instantiate classes that implement this interface.
    Therefore to initialize the list classes, you can use their respective add methods which is a list interface method
        but implemented by each of the classes.

If you instantiate a linked list class like this: List<Integer> llist = new LinkedList<Integer> ();
                    then, to add an element to a list, you can use the add method as follows: llist.add(3);

There is also a technique called “Double brace initialization” in which the list is instantiated and initialized by calling
        the add method in the same statement. List<Integer> llist = new LinkedList<Integer> (){{ add(1); add(3);}};
                     The above statement adds the elements 1 and 3 to the list.
 */

        List<String> str_list = new ArrayList<String>();
        str_list.add("Java");
        str_list.add("C++");
        System.out.println("ArrayList : " + str_list.toString());

        // LinkedList.add method
        List<Integer> even_list = new LinkedList<Integer>();
        even_list.add(2);
        even_list.add(4);
        System.out.println("LinkedList : " + even_list.toString());

        // double brace initialization - use add with declaration & initialization
        List<Integer> num_stack = new Stack<Integer>(){{ add(10);add(20); }};
        System.out.println("Stack : " + num_stack.toString());

/*
#3) Using Collections Class Methods
#4) Using Java8 Streams
#5) Java 9 List.of() Method

Details here: https://www.softwaretestinghelp.com/java-list-how-to-create-initialize-use-list-in-java/

 */
    }
}

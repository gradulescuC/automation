package data_types_02;

import java.util.ArrayList;
import java.util.List;

public class Array_vs_array_list_02_05 {
    public static void main(String[] args) {
        /*
        An array is a dynamically-created object.
        It serves as a container that holds the constant number of values of the same type.
        It has a contiguous memory location.
        Once an array is created, we cannot change its size. We can create an array by using the following statement: <dataType> array[]=new <dataType>[size];
        The above statement creates an array of the specified size. When we try to add more than its size, it throws ArrayIndexOutOfBoundsException.

In Java, ArrayList is a class of Collections framework.
It implements List<E>, Collection<E>, Iterable<E>, Cloneable, Serializable, and RandomAccess interfaces.
It extends AbstractList<E> class.

ArrayList is internally backed by the array in Java.
The resize operation in ArrayList slows down the performance as it involves new array and copying content from an old array to a new array.
It calls the native implemented method System.arraycopy(sec, srcPos, dest, destPos, length) .

We cannot store primitive type in ArrayList. So, it stores only objects. It automatically converts primitive type to object.
For example, I have created an ArrayList object:

ArrayList <Integer> list = new ArrayList<Integer>();  // creating a new object of ArrayList
arrayObj.add(12);   // trying to add integer primitive to the ArrayList

The JVM converts the above statements into an Integer object through auto-boxing.

ArrayList arrayObj = new ArrayList() //object of ArrayList
arrayObj(new Integer(12)); //converts integer primitive to Integer object and adds it to ArrayList object


Similarities
- Array and ArrayList both are used for storing elements.
- Array and ArrayList both can store null values.
- They can have duplicate values.
- They do not preserve the order of elements.


Differences:

- An array is a dynamically-created object. It serves as a container that holds the constant number of values of the same type. It has a contiguous memory location.
    The ArrayList is a class of Java Collections framework. It contains popular classes like Vector, HashTable, and HashMap.
- Array is static in size while ArrayList is dynamic in size.
- An array is a fixed-length data structure ArrayList is a variable-length data structure. It can be resized itself when needed.
- It is mandatory to provide the size of an array while initializing it directly or indirectly.
    We can create an instance of ArrayList without specifying its size. Java creates ArrayList of default size.
- It performs fast in comparison to ArrayList because of fixed size.
    ArrayList is internally backed by the array in Java. The resize operation in ArrayList slows down the performance.
- An array can store both objects and primitives type.
    We cannot store primitive type in ArrayList. It automatically converts primitive type to object.
- We use for loop or for each loop to iterate over an array.
    We use an iterator to iterate over ArrayList.
- Array provides a length variable which denotes the length of an array.
    ArrayList provides the size() method to determine the size of ArrayList.
- We can add elements in an array by using the assignment operator.
    Java provides the add() method to add elements in the ArrayList.
- Array can be multi-dimensional. ArrayList is always single-dimensional.
*/

        System.out.println("Arrays");
//creating an array of integer type
        int arr[]=new int[4];
//adding elements into array
        arr[0]=12;
        arr[1]=2;
        arr[2]=15;
        arr[3]=67;
// iterating over the arrays:
for(int i=0;i<arr.length;i++)
{
    System.out.println(arr[i]);
}

System.out.println("----------------------------------------------\n");

System.out.println("Array List");

// creating an instance of ArrayList
List<Float> list = new ArrayList<Float>();

//adding elements to arraylist
list.add(115f);
list.add(34.6f);
list.add(56.8f);
list.add(78.9f);

//iteration over ArrayList using for-each loop
for(Float f:list)
 {
     System.out.println(f);
 }
    }
}

package data_types_02;

public class Non_primitive_data_types_arrays_02_03<myArray> {

    public static void main(String[] args) {

/*
An array is a collection of similar type of elements which has contiguous memory location.
    You can think of a variable as being a house, and an array as being a neighbourhood of houses

A Java array is an object which contains elements of a similar data type.
Additionally, the elements of an array are stored in a contiguous memory location.

Contiguous memory allocation is a classical memory allocation model, in which a system assigns consecutive memory blocks (that is, memory blocks having consecutive addresses) to a process.

It is a data structure where we store similar elements. We can store only a fixed set of elements in a Java array.

Array in Java is index-based, the first element of the array is stored at the 0th index, 2nd element is stored on 1st index and so on.

The ‘Arrays’ class is a member of the ‘java.util’ package.

This is a part of the Java Collections framework and provides methods to create, access and manipulate Java arrays dynamically.
All the methods provided by the Arrays class are static in nature and are methods of the ‘Object’ class. As the methods are static, they can be accessed using the class name itself.

We can store primitive values or objects in an array in Java.


Advantages
- Code Optimization: It makes the code optimized, we can retrieve or sort the data efficiently.
- Random access: We can get any data located at an index position.


Disadvantages
- Size Limit: We can store only the fixed size of elements in the array.
            It doesn't grow its size at runtime.

There are two types of array.

- Single Dimensional Arrays
- Multidimensional Arrays

*/

// Single Dimensional Array in Java

    // Syntax to Declare an Array in Java can be found below. There are three ways in which we can declare an array:
        // To declare an array means to "make aquaintance" with it to the system

String[] array1;
int [] array2;
char array3[];

   //  Instantiation of an Array in Java means to allocate space at runtime for that specific array: array2 =new int[10];

array1 = new String[10]; // here we instantiated an array with an available space of 10 characters in which we can store text
int[] array4 = new int[20]; // here we declared and instantiated an array in one single line. We can store in this array 20 numbers

    // Let's initialise the array - a.i. let's populate it
array1[0] = "first test";
array1[1] = "second test";
array1[2] = "third test";

// as you can see, the first element in an array is stored at index 0. Now let's print the components of the array

        System.out.println(array1[0]); // it will print "first test"
        System.out.println(array1[1]); // it will print "second test"
        System.out.println(array1[2]); // it will print "third test"

    }
}
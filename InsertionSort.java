/*
  Author: Alessio Mazzone
  
  Implementation of Insertion sort
 */


/*
    Sorts in place using an array.
 
    The first part of the array is sorted, and the next in unsorted.
    This algorithm takes an item from the unsorted part of the array
    and places it in the correct spot in the sorted portion of the array.
 */

import java.util.*;

public class InsertionSort
{
    
    public static int[] insertionSort(int[] array)
    {
        int data;
        
        for(int unsortedIndex = 1; unsortedIndex < array.length; unsortedIndex++)
        {
            // Grab the data
            data = array[unsortedIndex];
            
            
            for(int sortedIndex = unsortedIndex - 1; sortedIndex >= 0; sortedIndex--)
            {
                    // Compare
                    if(array[sortedIndex] > data)
                    {
                        // Swap data
                        array[sortedIndex + 1] = array[sortedIndex];
                        array[sortedIndex] = data;
                        
                    }
                    else // array[sortedIndex] <= array[unsortedIndex]
                    {
                        // Item is in correct spot, so break out of loop
                        sortedIndex = -1;
                    }
            }
        }
        
        
        return array;
    }





    public static void main(String[] args)
    {
        
        int[] array1 = {3,2,6,1,5};
        int[] array2 = {10,4,1,4,6,3,2};
        
        // Print unsorted array
        System.out.println("UNSORTED ARRAY1:");
        System.out.println(Arrays.toString(array1) + "\n");
        
        array1 = insertionSort(array1);
        
        System.out.println("SORTED ARRAY1:");
        System.out.println(Arrays.toString(array1) + "\n");

         // Print unsorted array
         System.out.println("UNSORTED ARRAY2:");
         System.out.println(Arrays.toString(array2) + "\n");
         
         array2 = insertionSort(array2);
         
         System.out.println("SORTED ARRAY2:");
         System.out.println(Arrays.toString(array2) + "\n");
    }
}




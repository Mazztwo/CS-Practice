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

public class Sorting
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

    
    public static int[] selectionSort(int[] array)
    {
        /*
            Start at array[0]
            Iterate through, grab smallest piece of data, place at index 0
            Now at array[1], repeat above steps, place at index 1
            etc....
        */

        int dataToSwap, dataToSwapIndex, currSmallest, unsortedIndex;

        for(int sortedIndex = 0; sortedIndex < array.length; sortedIndex++)
        {
        		currSmallest = array[sortedIndex];
        		dataToSwap = array[sortedIndex];
        		dataToSwapIndex = sortedIndex;
        	
            for(unsortedIndex = sortedIndex; unsortedIndex < array.length; unsortedIndex++)
            {
                if(array[unsortedIndex] < currSmallest)
                {
                    currSmallest = array[unsortedIndex];
                    dataToSwapIndex = unsortedIndex;
                }
                
            }    
            
          array[sortedIndex] = currSmallest;
          array[dataToSwapIndex] = dataToSwap;  
        }    



        return array;
    }

    public static int[] bubbleSort(int[] array)
    {
    		/* 
    		 * Compare data at i with data at i +1
    		 * If at i+1 is less than at i, swap, 
    		 * Do this for every index, until end of array reached
    		 * Then start at the beginning of array again and 
    		 * do the same thing.
    		 */
    		
    		int temp;
    	
    		for(int i = 0; i < array.length; i++)
    		{
    			for(int j = 0; j < array.length; j++)
    			{
    				if(j != (array.length - 1) )
    				{
    					if(array[j] > array[j+1])
    					{
    						temp = array[j+1];
    						array[j+1] = array[j];
    						array[j] = temp;
    						
    					}
    				}
    			}
    		}
    	
    		return array;
    }

    public static void main(String[] args)
    {
        int[] array1 = {10,4,1,4,6,3,2};
        int[] array2 = {9,4,44,1,2,3,6,412};
        int[] array3 = {43,3,11,5,2,77,4,1,3};
        
         // Print unsorted array
         System.out.println("UNSORTED ARRAY1:");
         System.out.println(Arrays.toString(array1));
         
         array1 = insertionSort(array1);
         
         System.out.println("Insertion-SORTED ARRAY1:");
         System.out.println(Arrays.toString(array1) + "\n");


          // Print unsorted array
          System.out.println("UNSORTED ARRAY2:");
          System.out.println(Arrays.toString(array2));
          
          array2 = selectionSort(array2);
          
          System.out.println("Selection-SORTED ARRAY2:");
          System.out.println(Arrays.toString(array2) + "\n");
          
          // Print unsorted array
          System.out.println("UNSORTED ARRAY3:");
          System.out.println(Arrays.toString(array3));
          
          array3 = selectionSort(array3);
          
          System.out.println("Bubble-SORTED ARRAY3:");
          System.out.println(Arrays.toString(array3) + "\n");
    }
}




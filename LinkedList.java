/* 
  Author: Alessio Mazzone
  
  Implementation of LinkedList data structure
  and some associated methods, plus a main to
  test the class.
*/

public class LinkedList<T>
{
   private Node head;
   private int numberOfData;

  public LinkedList()
  {

  }


  // Implement: Add, Delete, Search, Print






  /*
    Implementation of node class 
    as a private inner class to
    be used for the LinkedLiss.
  */
  private class Node
  {
    private T data;       // Data contained in node
    private Node next;    // Pointer to next node in list

    // Constructors for Node

    // If no next node is selected, null is passed to defult constructor.
    private Node(T nodeData)
    {
      this(nodeData, null);
    }

    // Assigns data 
    private Node(T nodeData, Node nextNode)
    {
      data = nodeData;
      next = nextNode;
    }

    /* No setter and getter methods are necessary.
       LinkedList, being the outerclass of Node, will
       have access to Node's data directly.
    */ 

  }


  // A main mehtod to test the functionality of the LinkedList.
  public static void main(String args[])
  { 
    System.out.println("Hi.");
  }
}

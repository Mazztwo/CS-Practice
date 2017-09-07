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
    head = null;
    numberOfData = 0;
  }

  // Implement: Add, Remove, Search, toArray, Print

  /* 
  This method takes one argument: the data user wishes to add.
  This method returns one argument: true/false based on if add was sucessful. 
  
  This method will create a new Node and make it the new head of the list,
  pushing all other Nodes down. 
  */
  public boolean add(T newData)
  {
    try
    {
      Node newNode = new Node(newData);

      if(numberOfData == 0)
      {
        head = newNode;
        numberOfData++;
        
        return true;
      }
      
      newNode.next = head;
      head = newNode;
        
      return true;
    }
    catch(Exception e)
    {
      System.out.println("Item could not be added to linked list due to an error.");
      return false;
    }
  }

  







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

    // Assigns data and next node 
    private Node(T nodeData, Node nextNode)
    {
      data = nodeData;
      next = nextNode;
    }

    /* 
      No setter and getter methods are necessary.
      LinkedList, being the outerclass of Node, will
      have access to Node's data directly.
    */ 

  }


  // A main mehtod to test the functionality of the LinkedList.
  public static void main(String args[])
  { 
    // Create a linked list
    LinkedList<String> aList = new LinkedList();

    // Test add() method. Will print true or false based on if data was added or not.
    String item1 = "Hello";
    String item2 = "World";
    String item3 = "Dount";

    boolean item1added = aList.add(item1);
    boolean item2added = aList.add(item2);
    boolean item3added = aList.add(item3);

    System.out.println("Item 1: " + item1); 
    System.out.println("Sucessfuly added to list?: " + item1added);
    System.out.println("Item 2: " + item2); 
    System.out.println("Sucessfuly added to list?: " + item2added);
    System.out.println("Item 3: " + item3); 
    System.out.println("Sucessfuly added to list?: " + item3added);

  }
}

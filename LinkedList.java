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
  This method takes one argument: the data user wisher to remove from list.
  This method returns one argument: true/false based on if remove was sucessful.

  This method will search the list for the first instance of the data and 
  remove that node. If no argument is given, the head will be popped off
  the list.
  */
  public boolean remove(T dataToRemove)
  {
    // If dataToRemove = null, just remove a random node, in this case the head
    if(dataToRemove == null)
    {
      head = head.next;
      return true;
    }

    Node previous = head;
    Node curr = head.next;
    
    
    if (head.data.equals(dataToRemove))
    {
      head = head.next;
      return true;
    }

    while(curr != null)
    {
      if(curr.data.equals(dataToRemove))
      {
        previous.next = curr.next;
        return true;
      }
        previous = curr;
        curr = curr.next;

    }
    return false;

  }

  /*
  This method takes one argument: the data the user wishes to find in list.
  This method returns one argument: true/false based on if search was successful.
  */
  public boolean search(T dataToSearch)
  {
    // If no data provided to search for, return false
    if(dataToSearch == null)
    {
      return false;
    }

    Node curr = head;

    while(curr != null)
    {
      if(curr.data.equals(dataToSearch))
      {
        return true;
      }

      curr = curr.next;
    }

    return false;
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
    String item3 = "Donut";

    boolean item1added = aList.add(item1);
    boolean item2added = aList.add(item2);
    boolean item3added = aList.add(item3);

    System.out.println("Item 1: " + item1); 
    System.out.println("Sucessfuly added to list?: " + item1added);
    System.out.println("Item 2: " + item2); 
    System.out.println("Sucessfuly added to list?: " + item2added);
    System.out.println("Item 3: " + item3); 
    System.out.println("Sucessfuly added to list?: " + item3added);

    // Add more items and test remove() method.
    String item4 = "Silver";
    String item5 = "Brought";
    String item6 = "Spoon";
    String item7 = "Cruton";
    String item8 = "Prince";

    aList.add(item4);
    aList.add(item5);
    aList.add(item8);

    boolean item4removed = aList.remove(item4);
    boolean item6removed = aList.remove(item6);
    boolean item7removed = aList.remove(item7);
    boolean item8removed = aList.remove(item8);

    System.out.println("Item to remove: " + item4);
    System.out.println("Item 4 removed?: " + item4removed);
    System.out.println("Item to remove: " + item6);
    System.out.println("Item 6 removed?: " + item6removed);
    System.out.println("Item to remove: " + item7);
    System.out.println("Item 7 removed?: " + item7removed);
    System.out.println("Item to remove: " + item8);
    System.out.println("Item 8 removed?: " + item8removed);
  
    // Add more items and test search() method.
    aList.add("Paper");
    aList.add("Mango");
    aList.add("Tire");

    boolean itemSearch1 = aList.search("World");
    boolean itemSearch2 = aList.search("Mango");
    boolean itemSearch3 = aList.search("Donut");
    boolean itemSearch4 = aList.search("Mushroom");
    boolean itemSearch5 = aList.search("Pencil");

    System.out.println("Item to search for: World");
    System.out.println("Item found?: " + itemSearch1);
    System.out.println("Item to search for: Mango");
    System.out.println("Item found?: " + itemSearch2);
    System.out.println("Item to search for: Donut");
    System.out.println("Item found?: " + itemSearch3);
    System.out.println("Item to search for: Mushroom");
    System.out.println("Item found?: " + itemSearch4);
    System.out.println("Item to search for: Pencil");
    System.out.println("Item found?: " + itemSearch5);


  }
}

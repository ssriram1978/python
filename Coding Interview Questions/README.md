Time Complexity:
----------------

Big O– Upper Bound on Run Time

Big Omega – Lower Bound on Run Time

Big Theta – Both Big O and Omega. Tight Bound on Run Time. 

Talk about Best case, Worst Case and Expected case.

O(n) – Traversing an array of N elements

O(log n) – Binary Search (or) finding a node in a BST

O(nlogn) – Heap Sort, Merge Sort, Quick Sort, Creating a Binary Tree

O(n^2) – Bubble sort, Selection sort.

O(2^n)  - Recursion – Factorial or that involves multiple recursive calls, Fibonacci

Space Complexity:
-----------------
Amount of memory used by an algorithm.

Stack space in Recursive calls counts too.

Always remember to drop the constants when computing complexity.
O ( n^2 + n) becomes O(n^2)

Add the run times when the loops are disjoint, multiply the run times when the loops are nested.

Memoization is a technique where the result of a recursive called algorithm is cached and reused to avoid subsequent recursive calls. By doing this, we can reduce the time complexity from O(2^n) to O(n).

Problem solving strategy for a coding interview:
------------------------------------------------
1.	Listen: Pay very close attention to any information in the problem description. You probably need it all for an optimal algorithm. 

2.	Example: Most examples are too small or are special cases. Debug your example. Is there any way it’s a special case? Is it big enough? An example can dramatically improve your ability to solve an interview question and yet, so many candidates just try to solve the question in their heads.  When you hear a question, get out of your chair, go to the whiteboard, and draw an example.

3.	Brute Force: Get a brute-force solution as soon as possible. Don’t worry about developing an efficient algorithm yet. State a native algorithm and its run time, then optimize from there. Don’t code yet though! 

4.	Optimize: Walk through your Brute Force with BUD Optimization: Bottlenecks, Unnecessary work, Duplicated work.

	a. Look for any unused info. You usually need all the information in a problem. How can you leverage that information?
	
	b. Solve it manually on an example, then reverse engineer your thought process. How did you solve it? Use a fresh example. Sometimes, seeing a different example will unclog your mind or help you see a pattern in the problem. 
	
	c. Solve it “incorrectly” and think about why the algorithm fails. Can you fix those issues?
	
	d. Make a time vs space tradeoff. Hash tables are really useful! Storing extra state about the problem can help you optimize the runtime.
	
	e. Precompute information. Is there a way you can reorganize the data (sorting, etc.) or compute some values upfront that will help save time in the long run?
	
	f. Think about best conceivable run time.   
5.	Walkthrough: Now that you have an optimal solution, walk through your Brute Force approach with these ideas in mind and look for BUD in detail. Make sure that you understand each detail before you start coding. Take a moment to solidify your understanding of the algorithm. You can write pseudocode if you like but walk through the algorithm and get a feel for the structure of the code. Know what the variables are and when they change. . If you don’t understand exactly what you’re about to write, you’ll struggle to code it. It will take you longer to finish the code and you’re more likely to make major errors.

6.	Implement: Your goal is to write beautiful code. Modularize the code from the beginning and refactor to clean up anything that isn’t beautiful. White boarding coding is slow – very slow. So is testing your code and fixing it. As a result, you need to make sure that you get it as close to “perfect” in the beginning as possible. Start coding in the far top left corner of the whiteboard (you’ll need the space). Avoid “line creep”. Remember that you only have a short amount of code to demonstrate that you are a great developer. Everything counts. Write beautiful code. For modularization example, don’t waste your time to write in writing initialization code, just pretend that you already have it. Add a “todo” to come back and do a test. 

7.	Test: Test in this order:

8.	Conceptual test. Walk through your code like you would for a detailed code review. 

	a. A conceptual test means just reading and analyzing what each line of code does.  Think about it like you are explaining the lines of code for a code reviewer. 
	
	b. Unusual or non-standard code.
	
	c. Hot-spots, like arithmetic and null nodes. Base case in recursive code, integer division, start and end of iteration through a linked list.
	
	d. Small test cases. It’s much faster than a big test case and just as effective.
	
	e. Special cases and edge cases.
	
	f. When you find bugs, fix them carefully!

9.	Keep Talking! Your interviewer wants to hear how you approach the problem.

10.	Interviews are supposed to be difficult. You do want to listen to the problem and make sure that you heard it correctly. Make sure that you mentally recorded any unique information in the problem. Ask yourself if you had used all the information in the problem. Write all the useful information on the whiteboard.

Hash Table:
-----------
Maps keys to values for highly efficient lookup.

O(1) with minimum collisions.

O(n) where n is the number of keys.

Hash table can be a BST O(nlogn)

Lists:
------
Inserting n elements result in O(n)

Linked Lists:
-------------
A data structure that represents a sequence of nodes. 

The “runner” or second pointer technique is used in many linked list problems. 
The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead of another. 

The “fast” node might be ahead by a fixed amount.  This technique is used to interweave elements or to detect a circular loop.

Number of linked list problems rely on recursion.

Stack implements LIFO (Last in First Out) ordering. Push(item), Pop, Peek, isEmpty are the operations.

Stack are used in recursive algorithm like pushing data to stack as you recurse and popping them out as you backtrack.

Queue implements FIFO (First in First Out) ordering. Add(item), remove, peek, isEmpty are the operations.

Queues are used in BFS (Breadth First Search).
 
Tree:
-----
Each tree has a root node.

The root node has zero or more child nodes.

Binary tree is a tree which has two children (left and right child).

Binary search tree is a tree in each node satisfy a property  all left descendants  <=  current node < all right descendants.

A balanced Binary search tree is a tree in which every node satisfies a property 

	Height of left descendants – Height of right descendants = 1

    Example: Red Black tree and AVL tree. 

    They have insert and find subroutines with a time complexity of O(logn) where n is the number of elements in the tree.

Balanced BT means every level of the tree is filled except the last level. 

Complete BT means every level of the tree is filled except the right most elements of the tree. Example: Minheap or Maxheap

Full BT is a tree in which every node has either zero or two children.

In order traversal (Left, Parent, Right) – Example: sorting algorithms.

Pre order traversal (Parent, Left, Right) – Collapse a tree into an array to be sent out on the wire.

Post order traversal (Left, Right, Parent) – DFS

MinHeap:
--------
Consider an array that has elements and that can be identified by unique index.

We can make this array a MinHeap with the minimum element at the front of the array.  Time complexity(O(nlogn).

This is in-place sorting technique where space complexity is O(1).

MinHeap is a complete BT with min node as the root. Operations: Insert and Extract_min.

Each node is a unique index in the array.

Each node has a left child at 2*I + 1 index where I is the current index.

Each node has a right child at 2*I + 2 index where I is the current index. 

Insert Algorithm: Insert the node at the end and heapifyUp the node by comparing the current node with the parent node.  Time Complexity (O(logn))

Extract_min algorithm: Replace the minimum element from the root index=0  with the element found at the end of the list

Invoke heapifyDown algorithm where you find the minimum of the children nodes and swap the content with the parent node until you reach the end. Time Complexity (O(logn))

Trie:
-----

This is an n-ary tree or prefix tree where characters are stored in each node.

A node in a trie can have children nodes from 1 to 26 characters.

A trie can tell If a string is a valid prefix in the order of K where K is the number of characters in the string.

Graph:
------
A graph is a type of tree which is a collection of nodes with edges between them. 

Each node has one or more neighbor nodes.

A graph can be directed (one way) or undirected (two way).

If there is a path between two vertices, then, it is a connected graph.

Adjacency list is a common way to represent a graph. Every vertex or node stores a list of adjacent vertices. 

In undirected graph, like an edge (a,b) would be stored once on a’s adjacent vertices (dict in py with index as number and value as node) and on b.

With (Breadth first Search) BFS, you want to search for all adjacent neighbors before proceeding to the next level of neighbors to your neighbors.

For this, you need to use a queue.

The search algo goes like this:

1. Enqueue the starting node to the queue.

2. Start a while loop which checks for queue not to be empty and does the following.

   Dequeue a node from the queue.

   If the node matches with the destination, then, you found a route. Add it to the output and return True.

   Else

   You need to queue all the neighbors of this node. Before enqueuing, just make sure that the node is not already there in the queue.

With (Depth First Search) DFS, you recurse deep down to first neighbor and that neighbor's neighbor until you reach the end and then walk back recursing each neighbor's neighbor nodes searching for the destination until you find it.

We use pre-order traversal.

Once having come out of the first neighbor, you recurse into the second neighbor and do the previous step until you find the destination. Note that every time you recurse, make sure that you do not revisit the neighbor who has already been visited.

BFS is often used to find the shortest path first between two nodes.  Example: shortest list of names of friends between two persons who are not friends.

DFS is often used to traverse a jig saw puzzle to find a string match.

Bit Manipulations:
------------------
Arithmetic Right shifting a number >> by 1 results in dividing the number by 10.

Arithmetic Left shifting a number << by 1 results in multiplying the number by 2.

Computers store integers in two’s complement representation.

A +ve number is stored as itself.

A –ve number is stored in two’s complement representation with 1 in the sign bit that represents –ve value.

Binary representation of a number –K as a N bit number   = concat (1, 2 ^(n-1) –K) 

GetBit() algo would shift 1 to left to the desired position X like 00001000 and AND with the original number and return the result if it is not 0, true else false.

SetBit() algo would shift 1 to left to the desired position X like 00001000 and OR with the original number and return the result.

ClearBit() algo would shift 1 to left to the desired position X and ~ negate it 11110111 and AND it with the original number to clear the bit.

Clear all bits from MSB to index X would require left shifting 1 to the desired position X and then subtract 1 to make it zeros followed by 1s and AND this with the original number.

Clear all bits from LSB to index X would require left shifting -1 to the desired position X+1 and then AND it with the original number.

Object Oriented Programming:
---------------------------- 

Step 1: Handle ambiguity.

Step 2: Define the core objects.

Step 3: Analyze relationships.

Step 4: Investigate actions.

Singleton class is a class that ensures that there is only one instance of the class.

Factory method offers an interface for creating an instance of the class, with its subclasses deciding which class to instantiate. 

You could implement the creator class as abstract and do not provide any implementation of the factory method. 

You could also implement the creator class to be concrete and would take in a parameter that decides which class to instantiate. 

Recursion:
----------

A problem can be deemed recursive when it can be built off of subproblems.

Design an algorithm to compute nth, list the first n, compute all,…

How do you divide a problem into sub problems?

Bottom up: Frequently used. Recursively go to a single element and then figure out how to solve with 2 elements and so on…

Top down: Divide the problem for case N into subproblems.

Half and Half approach: Binary search. Divide the set into half.

Recursive algorithms are space inefficient.

Each recursive call adds a new layer to the stack. Therefore, to recurse to depth of n would require O(n) memory.

Converting recursive algorithm to iterative requires more code.

Dynamic programming is mostly just a matter of taking a recursive algorithm and finding the overlapping subproblems (i.e., the repeated calls). 

You then cache those results for future calls.

Simplest approach to dynamic programming is computing the nth Fibonacci number.

A good approach is to recurse and introduce caching.

from collections import defaultdict

def Fibonacci_recurse(number,cache):

if number == 0 or number == 1:

    return number


if cache[number]==0:

    cache[number]=Fibonacci_recurse(number-1,cache)+Fibonacci_recurse(number-2,cache)

return cache[number]

def Fibonacci(number):

    cache=defaultdict(int)

    return Fibonacci_recurse(number,cache)

Simple non recursive algorithm is

def Fibonacci_nonrecurse(number):

    if number==0:

		return 0
    
	if number==1:
    
    return 1

    a=0

    b=1

    for index in range(2,number,+1):

		temp=a+b
        
		a=b
        
		b=temp
    
    return a+b

System Design and Scalability:
------------------------------
1.	Communicate
2.	Go broad first
3.	Use the whiteboard
4.	Acknowledge interviewer concerns
5.	Be careful about assumptions
6.	State your assumptions explicitly
7.	Estimate when necessary
8.	Drive

Design:
-------
Scope the Problem
Make reasonable assumptions
Draw the major components
Identify the key issues
Redesign for the key issues
Algorithms that scale:
Ask Questions
Make Believe
Get Real
Solve Problems

Key Concepts:
-------------
Vertical (more RAM, harddrive) vs Horizontal (more nodes) Scaling

Load Balancer

Database Denormalization and NoSQL (no joins) Denormalization means adding redundant information to a database to speed up reads.

Database partitioning. (Sharding) Vertical, Key based (Hash), Directory based partitioning. 

Caching (Least Recently Used)

Networking Metrics: Bandwidth, Thruput and Latency.

Failures. 

High Availability and Reliability.

Read-Heavy (queue) vs Write-Heavy

Security

Sorting Algorithms:
-------------------
Sorting Algorithm	Time Complexity	Space Complexity

Bubble Sort	         N^2	          1

Selection Sort	     N^2	          1

Merge Sort	         N log N	      N

Quick Sort (Pivot)	 N log N        avg: N^2	1

Min Heap	        N log N	          1

Binary Search Tree	N log N	          N

Searching Algorithm:
--------------------
Binary search is used to search for an element in a sorted list.

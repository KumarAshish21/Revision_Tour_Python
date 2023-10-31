# Hashing-> Search, Insert, Delete 0(1) on average
# Hashing not useful for: finding closst value, Sorted Data, Prefix Searching

# AVL Tree or Red Black Tree
# Application of Hashing
# Hashing provides constant time search, insert and delete operations on average. This is why hashing is one of the most used data structure, example problems are, distinct elements, counting frequencies of items, finding duplicates, etc. 

# There are many other applications of hashing, including modern day cryptography hash functions. Some of these applications are listed below: 

# Message Digest
# Password Verification
# Data Structures(Programming Languages)
# Compiler Operation
# Rabin-Karp Algorithm
# Linking File name and path together
# Game Boards
# Graphics
# Direct Address Table

# Direct Address Table is a data structure that has the capability of mapping records to their corresponding keys using arrays. In direct address tables, records are placed using their key values directly as indexes. They facilitate fast searching, insertion and deletion operations. 

#  Advantages:

# Searching in O(1) Time: Direct address tables use arrays which are random access data structure, so, the key values (which are also the index of the array) can be easily used to search the records in O(1) time.
# Insertion in O(1) Time: We can easily insert an element in an array in O(1) time. The same thing follows in a direct address table also.
# Deletion in O(1) Time: Deletion of an element takes O(1) time in an array. Similarly, to delete an element in a direct address table we need O(1) time.
 

# Limitations:

# Prior knowledge of maximum key value
# Practically useful only if the maximum value is very less.
# It causes wastage of memory space if there is a significant difference between total records and maximum value.


# Hashing Functions

# Hashing is a technique or process of mapping keys, and values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.

# Let a hash function H(x) maps the valuexat the index x%10 in an Array. For example if the list of values is [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table respectively.

# The mod method: 
# In this method for creating hash functions, we map a key into one of the slots of table by taking the remainder of key divided by table_size. That is, the hash function is 

# h(key) = key mod table_size 

# i.e. key % table_size

# The multiplication method: 
# In multiplication method, we multiply the key k by a constant real number c in the range 0 < c < 1 and extract the fractional part of k * c.
# Then we multiply this value by table_size m and take the floor of the result. It can be represented as

# h(k) = floor (m * (k * c mod 1))
#                      or
# h(k) = floor (m * frac (k * c))

# Collision is the condition in which two keys map to the same entry in the Hash table. In this video we will come across the techniques of Chaining and Open Addressing used for efficient management of collisions.
# Following are the ways to handle collisions: 

# Chaining:The idea is to make each cell of hash table point to a linked list of records that have same hash function value. Chaining is simple, but requires additional memory outside the table.
# Open Addressing: In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL. When searching for an element, we examine the table slots one by one until the desired element is found or it is clear that the element is not in the table.

# Separate Chaining:
# The idea behind separate chaining is to implement the array as a linked list called a chain. Separate chaining is one of the most popular and commonly used techniques in order to handle collisions.

# The linked list data structure is used to implement this technique. So what happens is, when multiple elements are hashed into the same slot index, then these elements are inserted into a singly-linked list which is known as a chain

# Open Addressing:
# Like separate chaining, open addressing is a method for handling collisions. In Open Addressing, all elements are stored in the hash table itself. So at any point, the size of the table must be greater than or equal to the total number of keys (Note that we can increase table size by copying old data if needed). This approach is also known as closed hashing. This entire procedure is based upon probing. We will understand the types of probing ahead:

# 1. Linear Probing: 
# In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we get is already occupied, then we check for the next location. 

 

# The function used for rehashing is as follows: rehash(key) = (n+1)%table-size. 

# 2. Quadratic Probing 
# If you observe carefully, then you will understand that the interval between probes will increase proportionally to the hash value. Quadratic probing is a method with the help of which we can solve the problem of clustering that was discussed above.  This method is also known as the mid-square method. In this method, we look for the i2‘th slot in the ith iteration. We always start from the original hash location. If only the location is occupied then we check the other slots.

# let hash(x) be the slot index computed using hash function.  

# If slot hash(x) % S is full, then we try (hash(x) + 1*1) % S
# If (hash(x) + 1*1) % S is also full, then we try (hash(x) + 2*2) % S
# If (hash(x) + 2*2) % S is also full, then we try (hash(x) + 3*3) % S

# Double Hashing 
# The intervals that lie between probes are computed by another hash function. Double hashing is a technique that reduces clustering in an optimized way. In this technique, the increments for the probing sequence are computed by using another hash function. We use another hash function hash2(x) and look for the i*hash2(x) slot in the ith rotation.
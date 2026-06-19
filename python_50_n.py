#1.  Write a program to find the sum of two numbers.

a = 10
b = 5

sum = a + b
print(sum)


#   2. Write a program to check if a number is even or odd.


num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
#  3. Write a program to check if a number is prime.


num = 14
is_prime = True

if num > 1:
    for i in range(2, num):
       if num % i == 0:
           is_prime = False
           break
           
if is_prime:
    print("Prime")
else:
    print("Not Prime")


#alternative
def is_prime(num):
  if num <= 1:
      return False
     
  for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
             return False
   
   
   return True


    
    
# 4. Write a program to calculate the factorial of a number.

num = 13
factorial = 1

if num < 0:
    print("Factorial doesn't exit for negative numbers")
elif num == 0:
    print("Factorial of zero is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
        
        
print("Factorial of the number is", factorial)

# Palindrome 

def is_palindrome(num):
    return str(num) == str(num)[::-1]
    
    
print(is_palindrome(322323))

#palindrome - No built ins

def is_palindrome(s):
  left = 0
  right = 0
  
  for i in s:
     right += 1
  right -= 1
  
  
  while left < right:
     if s[left] != s[right]:
         return False
     left += 1
     right -= 1
     
     return True
     
print(is_palindrome("racecar"))


def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
    
#----------- string format 
def reverse_string(s):
    reverse = ""
    for char in s:
        reverse = str(char + reverse)
        
    return '"'+ reverse +'"'
    
print(reverse_string("Hello world"))

"dlrow olleH"


def is_palindrome(s):
    left = 0
    right = len(s) - 1   # cleaner than manual counting

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Test
text = "madam"

print("Reversed:", reverse_string(text))
print("Is Palindrome:", is_palindrome(text))


# 5.  Write a program to find the largest number in a list.


numbers = [4, 56, 78, 9, 32]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
        
print("Largest is", largest)



#merge two sorted list into one sorted list


def merge_sorted_list(lst1, lst2):
    merge_list = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merge_list.append(lst1[i])
            i += 1
        else:
            merge_list.append(lst2[j])
            j += 1
            
    merge_list.extend(lst1[i:])
    merge_list.extend(lst2[j:])
    return merge_list
    
print(merge_sorted_list([1,3,5], [2, 4, 6]))

O/p - [1, 2, 3, 4, 5, 6]



# find duplicate element in the list

def find_duplicates(lst):
     seen = set()
     duplicates = set()
     for item in lst:
         if item in seen:
             duplicates.add(item)
          else:
             seen.add(item)
      return list(duplicates)
      
print("duplicate ", find_duplicates([1, 3, 2, 2, 3, 4, 5, 7, 8, 9, 9]))

O/p - duplicate  [9, 2, 3]



# check if two strings are anagrams

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
    
    
print(are_anagrams("listen", "silent")
print(are_anagrams("hello", "world")



#implement queue using two stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, item):
        self.stack1.append(item)
        
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()
        
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) -> 1
print(queue.dequeue()) -> 2



#binary search on a sorted list

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
    
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5)) -> 4(index of 5)
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8)) -> -1(index of 8)





# reverse a singly linked list

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
        
def revers_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
    
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print_list(head)
reversed_head = revers_linked_list(head)
print_list(reversed_head)



# detect if a linked list has a cycle

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next 
 
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head.next.next.next.next = head.next # Creating a cycle
print(has_cycle(head)) # Output: True




# merge two sorted linked lists

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next 
 
    
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
    
    
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_two_lists(l1, l2)
print(merged_head)



# JS -> implicit return
const add = (a, b) => a + b;




def longest_consecutive_sequence(lst):
    if not lst:
        return
    
    longest = []
    current = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            current.append(lst[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lst[i]]
            
    # Final check after loop
    if len(current) > len(longest):
        longest = current
    
    if longest:
        print("Longest:", longest)
        
 longest_consecutive_sequence([1, 2, 3, 5, 6, 10])
        
        O/p - 1, 2, 3
        
        
# remove duplicates manually

unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
        

# -------Manual Bubble sort -----
for i in range(len(unique_nums)):
    for j in range(0, len(unique_nums) - i - 1):
        if unique_nums[j] > unique_nums[j + 1]:
            unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
            
nums = unique_nums

longest = []
current = [nums[0]]


for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        current.append(nums[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [nums[i]]
        
if len(current) > len(longest):
    longest = current
    
    
print(longest)        





# invert the dictionary

data = {"raj": "mysore", "lakshmi": "bangalore", "sheri": "mysore", "josh": "bangalore"}

out = {}

for name, city in data.items():
    if city not in out:
        out[city] = []
    out[city].append(name)

print(out)



data = {"raj": "mysore", "lakshmi":"bangalore", "sheri":"mysore", "josh":"bangalore"}


out = {}

for k, v in data.items():
    out.setdefault(v, []).append(k)
        

print(out)
    
List comprehension

[x * 2 for x in range(5)]


Split the sentence - 

input_string = "Welcome to python online development environment"

words = []
current = ""

for ch in input_string:
    if ch != " ":
        current += ch
    else:
        words.append(current)
        current = ""

# Append the last word (after loop ends)
if current:
    words.append(current)

print(words)


input_string = "ASDTFHGNKE"
group_size = 3     # you can change this to 3, 4, etc.

result = []
current = ""

for ch in input_string:
    current += ch
    if len(current) == group_size:
        result.append(current)
        current = ""

print(result)



# Generator fibonacci

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen))



# alternative 

def fibonacci(n):
   sequence = [0, 1]
   for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
    
  print(fibonacci(8)) - output - [0, 1, 1, 2, 3, 5, 8, 13]
  
  
    

# quick sort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
       

arr = [10, 7, 4, 19, 11, 12, 4, 3]
print(quicksort(arr))


# class to implement a stack using two queues.


from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
            
    def pop(self):
        if self.q1:
            return self.q1.popleft()
        raise IndexError("pop from empty stack")
        
    def top(self):
        if self.q1:
            return self.q1[0]
        raise IndexError("top from empty stack")
        
    def empty(self):
        return not self.q1
            

stack = StackUsingQueues()
stack.push(1)
stack.push(2)

print(stack.top())
print(stack.pop())
print(stack.empty())




# class to implement a binary search tree with insert, search, and delete operations.


# Binary search tree

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
            
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)
                
    def search(self, key):
        return self._search(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)
        
    def delete(self, key):
        self.root = self._delete(self.root, key)
        
    def _delete(self, node, key):
        if not node:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp_val = self._min_value_node(node.right).val
            node.val = temp_val
            node.right = self._delete(node.right, temp_val)
        return node
        
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
        
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.search(30).val)
bst.delete(20)
print(bst.search(20))
            
 # Output: 30   
    
    # Output: None



# to perform inoder traversal of a binary tree

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_traversal(root):
    result = []
    
    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)
    _inorder(root)
    return result
    
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorder_traversal(root))
            
# Output: [1, 3, 2]


# Depth-First Search (DFS) for a Graph

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited
    
    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A'))


# Output: {'E', 'D', 'F', 'A', 'C', 'B'}



# Breadth-First Search (BFS) for a Graph
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited
    
    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))


  # Output: {'B', 'D', 'E', 'A', 'C', 'F'}
  
  
  
  
  
#count the number of vowels in a string

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
    
print(count_vowels('Hello world'))
print(count_vowels('test'))
  
  
  
  
#reverse
  
words = "Welcome to bangalore.silicon city"

def reverse_word_keep_dot(word):
    if "." not in word:
        return word[::-1]
    
    parts = word.split(".")
    reversed_parts = [p[::-1] for p in parts]
    
    return ".".join(reversed_parts)

result = " ".join(reverse_word_keep_dot(w) for w in words.split())

print(result)


Input: "Welcome to bangalore.silicon city"

Step-by-step:

words.split() → ["Welcome", "to", "bangalore.silicon", "city"]

Process each:

1.  "Welcome" has no dot → reversed → "emocleW"

2.  "to" → "ot"

3. "bangalore.silicon" has dot:

 parts = ["bangalore","silicon"]

 reversed_parts = ["erolangnab","nocilis"]

4. join → "erolangnab.nocilis"

5. "city" → "ytic"

6. Join with spaces → "emocleW ot erolangnab.nocilis ytic"

Printed.
  
  
  
  
  
  # Write a function to reverse words in the sentence.
# Reverse the words only.
# Dots, spaces and commas should remain as it is.
# Words will contain aA to zZ characters only and will not contain anything else.
# Delimiters are only dots, spaces and commas.
# Delimiters themselves are not the constituents of the word.
# For example:
# Input (String): My, name. is Basavaraj
# Output (String): yM, eman. si jaravasaB
# Input (String): yM, eman, si. rmI.na. hK,na
# Output (String): My, name, is. Imr.an. Kh,an

def reverse_words_with_delimiters(text):
    result = []
    word = ""
    
    for ch in text:
        if ch.isalpha():
            word += ch
        else:
            if word:
                result.append(word[::-1])
                word = ""
            result.append(ch)
    
    if word:
        result.append(word[::-1])
        
    return "".join(result)


print(reverse_words_with_delimiters("My, name. is Basavaraj"))





# Sort objects (string properties, Friend: name, grade) on property.
# Sort these objects on descending order of grade.
# Input:
# ------
# Aima, A
# Arjun, A+
# Iram, B+
# Zia, C
# Reah, B
# Karan, A
# Mithum, B


class Friend:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __repr__(self):
        return f"{self.name} ({self.grade})"
        
        
class FriendSorter:
    
    grade_rank = {
        "A+": 5,
        "A": 4,
        "B+": 3,
        "B": 2,
        "C": 1
    }
    
    @staticmethod
    def sort_friends(friends):
        return sorted(
            friends,
            key=lambda f: FriendSorter.grade_rank[f.grade],
            reverse=True)
            
friends = [
    Friend("Aima", "A"),
    Friend("Arjun", "A+"),
    Friend("Iram", "B+"),
    Friend("ZIa", "C"),
    Friend("Reah", "B"),
    Friend("Karan", "A"),
    Friend("Mithun", "B")
]


sorted_friends = FriendSorter.sort_friends(friends)

for f in sorted_friends:
    print(f)




# dictionaries money spent with sum and total

prices = {
    "box_of_spaghetti": 4,
    "lasagna": 5,
    "hamburger": 2
}

quantity = {
    "box_of_spaghetti": 6,
    "lasagna": 10,
    "hamburger": 0
}

money_spent = 0

for i in quantity:
    money_spent = money_spent + (prices[i] * quantity[i])
    
print(money_spent)



# In this exercise you will use the same dictionaries as the ones we used in the lesson - prices and quantity. This time, don't just calculate all the money Jan spent. Calculate how much she spent on products with a price of 5 dollars or more.



prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }
 
money_spent = 0
 
for i in quantity:
    if prices[i]>=5:
        money_spent += prices[i]*quantity[i] 
    else:
        money_spent = money_spent
 
print (money_spent)

A)
# sort the list where it has show less number first like ascending order

val = ["filename_doc66", "filename_doc71", "filename_doc55", "filename_doc45", "filename_doc35"] 


sorted_val = sorted(val, key=lambda x: int(x.split("doc")[1]))

print(sorted_val)


B)
val = ["filename_doc66", "filename_doc71", "filename_doc55", "filename_doc45", "filename_doc35"]

def extract_num(s):
   return int(s.split("doc")[1])
   
  
n = len(val)


for i in range(n):
   for j in range(0, n - i - 1):
         if extract_num(val[j]) > extract_num(val[j + 1]):
             val[j], val[j + 1] = val[j + 1], val[j]
             

print(val)



#JS tricky

console.log({} == {}) and console.log({} === {})

console.log({} == {});    // false
console.log({} === {});   // false

#  In JavaScript:
# {} creates a new object every time.

# Two different objects are never equal, even if they contain the same data.

#✔ == (loose equality)
# Compares references for objects.

# {} and {} are two different memory references → so false.
# ✔ === (strict equality)
# Compares both type and reference.
# Again, two different objects → false.



#wrapper

import time

def timer(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        
        return result
    
    return wrapper
    
    
# Use the wrapper:    
@timer
def slow_function():
    time.sleep(2)
    print("Completed slow task!")

slow_function()

#output
Completed slow task!
Execution time: 2.0001 seconds


    
    

# Pickling a Custom Class Object ===
#📄 Step 1: Create a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return f"{self.name} is {self.age} years old"
        
        

#📄 Step 2: Create an object & pickle it
import pickle

p = Person("Amit", 25)

with open("person.pkl", "wb") as file:
    pickle.dump(p, file)

print("Person object pickled!")



#📄 Step 3: Unpickle and use it
with open("person.pkl", "rb") as file:
    saved_person = pickle.load(file)

print(saved_person.info())

#✔ Output
Amit is 25 years old



#List comprehension - with compare

numbes = [1, 13, 4, 5, 63, 100]

1.
new_numbers = []

for n in numbers:
   new_numbers.append(n * 2):
   
new_numbers = [n * 2 for n in numbers]

#output - [2, 26, 8, 10, 126, 200]


2.

for i in range(2):
    for j in range(5):
       print(i + j, end = " ")
#output - 0 1 2 3 4 1 2 3 4 5

new_list_1 = [i + j for i in range(2) for j in range(5)]
new_list_1 or print(new_list_1)

#output - [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]


3.
new_list_2 = [[i+j for i in range(2)] for j in ranges(5)]
new_list_2

#output - [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]


4.
[num ** 3 for num in range(1, 11) if num % 2 != 0]

for i in range(1, 11):
    if i % 2 != 0:
        print(i ** 3, end = " ")

#output - [1, 27, 125, 343, 729]

5.
[num ** 3 if num % 2 != 0 for num in range(1, 11)]
#output - Invalid syntax

[num ** 3 if num % 2 != 0 else "even" for num in range(1, 11)]
#output - [1, 'even', 27, 'even', 125, 'even', 343, 'even', 729, 'even']




# lambda

1.
raise_to_the_power_of_2_lambda = lambda x: x ** 2 
raise_to_the_power_of_2_lambda(3) - # 9

2.
(lambda x: x/2) (11) - # 5.5


3.def extract_num(s):
   return int(s.split("doc")[1])
(lambda x: (2 / 5 * x ** 4) ** 2 / (x + 3) ** 3)(2) - # 53.792


4. # function

sum_xy = lambda x, y: x + y(x)
sum_xy(2, lambda x: x * 5) - # 12



Create a lambda function that returns the output of the following mathematical expression. Execute it with an argument of 3.
print((lambda x: (135 - x ** 3) ** 4 / (1 + x) ** 5)(3)) - # 132860.25




# An Armstrong number (or narcissistic number) is a number that equals the sum of its own digits, each raised to the power of the total number of digits in the number, like 153 (1³+5³+3³=153) or 1634 (1⁴+6⁴+3⁴+4⁴=1634)



def is_armstrong(num):
    str_num = str(num)
    num_len = len(str_num)
    return num == sum(int(digit) ** num_len for digit in str_num)
    
    
# print(is_armstrong(153)) # True
print(is_armstrong(123))



# A perfect number is a positive integer that equals the sum of its own proper divisors (all divisors excluding the number itself), like 6 (1+2+3=6) and 28 (1+2+4+7+14=28)


def is_perfect_number(num):
    if num <= 0:
        return False
        
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num
    
    
# print(is_perfect_number(28)) True
# print(is_perfect_number(12)) False




#leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    
# print(is_leap_year(2024)) - True



# Convert a decimal to binary

def decimal_to_binary(decimal):
    return bin(decimal)[2:]
    
print(decimal_to_binary(10)) - output 1010



# number is a prime factor of another number by utilizing the is_prime_factor function and determining whether the number is prime (is_prime), followed by checking if even the number you would like to verify the properties of can be evenly divided.


def is_prime(num):
    if num < 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
            
    return True
    
def is_prime_factor(num, potential_factor):
    return is_prime(potential_factor) and num % potential_factor == 0
    

print(is_prime_factor(15, 3)) - True
print(is_prime_factor(15, 4)) - False




# find all prime numbers within a given range


def is_prime(num):
    if num <= 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
            
    return True
        

def find_primes(start, end):
    primes = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
            
    return primes
        
        
print(find_primes(1, 10))

# Flattening a multi-dimensional list


my_list = [[100, 200, 300], [40, 50, 60], [70, 80, 90]]

my_list = [[100, 200, 300], [40, 50, 60], [70, 80, 90]]

flat = [x for temp in my_list for x in temp]






INterview __________________________________________________________________________



time.perf_counter()

time.perf_counter()

{t2 - t1:.6f} 

{t2 - t1:.6f}

def is_even(n):
    return (n and 1) == 0
    
    
    
import time

def time_wrapper(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"Time taken: {t2 - t1:.6f} seconds")
        return result
    return wrapper

@time_wrapper
def is_even(n):
    return (n & 1) == 0


Time taken: 0.000001 seconds
True

 
___________________________________________________________________________________________

evens = [x if x % 2 == 0 for x in range(10) 

evens = [x if x % 2 == 0 for x in range(10)]

---------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

 

def inorder(root, result=[]):
    if root is None:
        return result

 

    inorder(root.left)
    result.append(root.val)
    inorder(root.right)

 

    return result

 

t1 = Node(1, Node(2), Node(3))
t2 = Node(4)

 

print(inorder(t1))  # [2, 1, 3]
print(inorder(t2))  # [2, 1, 3, 4]


this is a classic Python pitfall involving mutable default arguments.

🔍 What is happening?
Your function:
def inorder(root, result=[]):


Here, result is a default mutable list.

👉 Default arguments are created only once, when the function is defined — not each time it is called.

So the same result list is reused across function calls.

🧠 Step-by-step execution
Tree definitions:
t1 = Node(1, Node(2), Node(3))   # Inorder → [2, 1, 3]
t2 = Node(4)                    # Inorder → [4]

First call
print(inorder(t1))


Traversal:

left → root → right
2 → 1 → 3


Result list becomes:

[2, 1, 3]

Second call
print(inorder(t2))


🚨 Python does NOT create a new list
It reuses the same result list:

existing result = [2, 1, 3]


Traversal of t2:

4


Appended to same list →

[2, 1, 3, 4]


That’s why output is:

[2, 1, 3, 4]

❌ Root Cause (Interview-worthy line)

Mutable default arguments persist across function calls, causing unexpected shared state.

✅ Correct Solution (Best Practice)
✔ Use None as default and create list inside
def inorder(root, result=None):
    if result is None:
        result = []

    if root is None:
        return result

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)

    return result

✅ Correct Output
print(inorder(t1))  # [2, 1, 3]
print(inorder(t2))  # [4]

____________________________________________________________________________________________________

nums = [1, 2, 3] squares = [nums * nums f... 

nums = [1, 2, 3]
squares = [nums * nums for nums in nums]


Variable shadowing happens

Outer variable: nums = [1, 2, 3]

Inner nums in list comprehension replaces (shadows) the outer one

So Python interprets it like this:

squares = []
for nums in [1, 2, 3]:
    squares.append(nums * nums)


Here:

nums is actually each element, not the list

First iteration: nums = 1 → 1 * 1 = 1

Second: nums = 2 → 2 * 2 = 4

Third: nums = 3 → 3 * 3 = 9
_____________________________________________________________________________________________________



def reverse_list(my_list):
    return my_list[::-1]

"my_list[::-1] uses slicing with a negative step to return a new list containing the elements in reverse order."
__________________________________________________________________________________________________________

def find_missing_number(nums):
    n = len(nums) + 1
    return list(set(range(1, n + 1)) - set(nums))[0]
    
    
    ⏱️ Time Complexity
Step-by-step:

range(1, n + 1) → creates n numbers → O(n)

set(range(...)) → inserts n elements → O(n)

set(nums) → inserts n-1 elements → O(n)

Set subtraction (-) → iterates over larger set → O(n)

list(...) → converts result (size 1) → O(1)

✅ Overall Time Complexity
O(n)

🧠 Space Complexity
Extra memory used:

set(range(1, n + 1)) → O(n)

set(nums) → O(n)

Temporary list → O(1)

✅ Overall Space Complexity
O(n)

____________________________________________________________________________________________________

for(var i=0; i<5; i++) {

setTimeout(() => console.log(i), 1000)

}

There is only ONE i variable shared across all loop iterations.

The loop finishes before setTimeout callbacks run.

After the loop ends:

i === 5

2️⃣ Closures capture reference, not value

Each setTimeout callback does NOT store the value of i

Instead, it refers to the same i variable

When callbacks execute after 1 second, i is already 5

var → function scope → shared variable

let → block scope → new variable per iteration


________________________________________________________________________________________________


# find the longest word in a sentence

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
    
print(longest_word("The fox jumping over the lazy dog"))

#output - jumping


# find the first non-repeating character in a string

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in s:
        if char_count[char] == 1:
            return char
        return None
        
print(first_non_repeating_char("nxtwavext"))  # n




# to determine how many capital letters are in a string.


def count_uppercase(s):
    return sum(1 for char in s if char.isupper())
    

print(count_uppercase("NxtwaVe"))



# treverse a string

s = "Python"

reversed_s = s[::-1]

print(reversed_s)


# convert a list of characters into a string

chars = ['P', 'y', 't', 'h', 'o', 'n']
string = ''.join(chars)
print(string)



# the number of occurrences of a character in a string

s = "banana"
count_a = s.count('n')

print(count_a) # output - 2


# count digits, letters, and spaces in a string


s = "Hello 123"

digits = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces = sum(c.isspace() for c in s)

print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")
# Digits: 3, Letters: 5, Spaces: 1




# the longest consecutive sequence in an unsorted list

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
            
    return longest
        
print(longest_consecutive([100, 4, 200, 1, 2, 3])) # - 4



# Two Sum problem
# ----------- Find indices of two numbers in a list that add up to a target.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return [] 
    
print(two_sum([2, 7, 11, 15], 9)) #output - [0, 1]



# group anagrams from a list of strings
# ----------- Use a dictionary with sorted words as keys. 


from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
    
    
print(list(anagrams.values())) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]




# memoization, and how is it used in algorithms
# ---------------  Memoization is a technique to cache expensive function calls and reuse results.

# --------Fibonacci with memoization -------------

def fib(n, memo= {}):
    if n in memo:
        return memo[n]
        
    if n <= 2:
        return 1
        
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
    
print(fib(10)) #outout - 55



# Nested loops are loops inside other loops, often used for working with matrices or multi-dimensional data.


matrix = [[1, 2], [3, 4]] 

for row in matrix: 
    for val in row: 
        print(val)
        
#output 1
#2
#3
#4



# Series: One-dimensional labelled array.
# DataFrame: Two-dimensional labelled data structure (like a table).


import pandas as pd

s = pd.Series([1, 2, 3])

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})

print(s)
print(df)


#output 
0    1
1    2
2    3
dtype: int64
   a  b
0  1  3
1  2  4

____________________________________________________________________


# Sorting: Use sorted() or .sort().
# Searching: Use the in operator or methods like .index().

nums = [8, 3, 9]

nums.sort()
print(nums) # [3, 8, 9]

print(9 in nums) #output True



# binary search algorithm

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
    
print(binary_search([1, 2, 3, 4, 5], 3))



___________________________________________________________________________


# merge sort

def merge_sort(arr):
   if len(arr) <= 1:
   return arr
   
   mid = len(arr) // 2
   left_half = merge_sort(arr[:mid])
   right_half = merge_sort(arr[mid:])
   
   return merge(left_half, right_half)
   
   
def merge(left, right):
    merged = []
    i = j = 0
    
    
    while i < len(left) and j < len(right):
          if left[i] <= right[j]:
             merged.append(left[i])
             i += 1
          else:
              merged.append(right[j])
              j += 1
              
     while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged
    
 arr = [38, 27, 43, 3, 9, 82, 10]
 sorted_arr = merge_sort(arr)
 print(sorted_arr)
 
 #output - [3, 9, 10, 27, 38, 43, 82]
   
   
   
   
#------------------------------------------
def celsius_to_fahrenheit(temps):
    return [(temp * 9/5) + 32 for temp in temps]
    
print(celsius_to_fahrenheit([0, 20, 37]))'



# ----------------------------------------
class Example:
    @staticmethod
    def static_method():
        return "static method called"
        
    @classmethod
    def class_method(cls):
        return f"class method called form {cls.__name__}"
        
    
print(Example.static_method())
print(Example.class_method())



#---------------sort a list of objects in python based on a specific attribute of the objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name} ({self.age})"
        

people = [Person('John', 30), Person('Alice', 25), Person('Bob', 35)]

sorted_people = sorted(people, key=lambda person: person.age)

print(sorted_people)


# --------------------------- Histogram area Solve using Python 3 Have the function Histogram(arr) read the array of non-negative integers stored in arr which will represent the heights of bars on a graph(where each bar width is 1). And determine the largest area underneath the entire bar graph. For example: if arr[2,1,3,4,1] then this looks like Bar graph that the largest area underneath the graph is covered by the x's. The area of that space is equal to 6 because the entire width is 2 and the maximum height is 3, therefore 2*3=6. Program should return 6. The array will always contain at least 1 element. Example Input [6, 3, 1, 4, 12, 4] Output 12 So complete this def HistogramArea(arr): return arr Print(HistogramArea(input()))


def HistogramArea(arr):
    if isinstance(arr, str):
        arr = eval(arr)
        
    stack = []
    max_area = 0
    n = len(arr)
    
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            height = arr[stack.pop()]
            left = stack[-1] if stack else - 1
            width = i - left - 1
            max_area = max(max_area, height * width)
        stack.append(i)
        
        
    while stack:
        height = arr[stack.pop()]
        left = stack[-1] if stack else - 1
        width = n - left - 1
        max_area = max(max_area, height * width)
        
    return max_area
    
    
print(HistogramArea(input()))


#----------------------- Quick knight problem Have the function QuickKnight(str) read str which will be a string consisting of the location of a knight on a standard 8×8 check board with no pieces on the board and another space on the chess board. The structure of the str will be following "(x y)(a b)" where (x y) represents the position of the knight with x and y ranging from 1 to 8 and (a b) represents some other space on the chess board with a and b also ranging from 1 to 8. Your program should determine the least amount of moves it would take the knight to go from it's position to position (a b) For example if str is "(2 3)(7 5)" then your program should output 3 because that is the least amount of moves it would take for the knight to get it from (2 3) to (7 5) on the chess board. For example Input "(1 1)(8 8)" - output should be 6. Input "(2 2)(3 3)" - output should be 2 def QuickKnight(strParam): Return strParam Print(QuickKnight(input()) - complete this


def QuickKnight(strParam):
    nums = []
    temp = ""

    # manual number extraction
    for ch in strParam:
        if ch.isdigit():
            temp += ch
        else:
            if temp != "":
                nums.append(int(temp))
                temp = ""

    # append last number if exists
    if temp != "":
        nums.append(int(temp))

    start = (nums[0], nums[1])
    target = (nums[2], nums[3])

    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    queue = [(start[0], start[1], 0)]
    visited = set([start])
    i = 0

    while i < len(queue):
        x, y, dist = queue[i]
        i += 1

        if (x, y) == target:
            return dist

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1


print(QuickKnight(input()))


# --------------- Compiler ----------------------
def QuickKnight(strParam):
    nums = []
    temp = ""
    
    for ch in strParam:
        if ch.isdigit():
            temp += ch
        else:
            if temp != "":
                nums.append(int(temp))
                temp = ""
                
    if temp != "":
        nums.append(int(temp))
        
    start = (nums[0], nums[1])
    target = (nums[2], nums[3])
    
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    queue = [(start[0], start[1], 0)] 
    visited = set([start])
    
    i = 0
    
    while i < len(queue):
        x, y, dist = queue[i]
        i += 1
        
        if(x, y) == target:
            return dist
            
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            
            if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                
    return -1
    
strParam = "(1 1)(8 8)"
    
print(QuickKnight(strParam))



#-----------------  1. Given an input string, write a function that returns the Run Length Encoded string for the input string. For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6” Expected Time Complexity: O(n)


input_string = “wwwwaaadexxxxxx”

def run_length_encode(s):
    if not s:
        return ""
        
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    
    return ''.join(result)
    
    
print(run_length_encode(input_string))


#------------------Django query
class Artist(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Song(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
songs = Song.objects.select_related('album', 'album__artist').all()

for song in songs:
    print({
        "song_id": song.id,
        "song_name": song.name,

        "album_id": song.album.id,
        "album_name": song.album.name,

        "artist_id": song.album.artist.id,
        "artist_name": song.album.artist.name
    })
    
songs = Song.objects.select_related(
    'album',
    'album__artist'
).filter(
    album__artist__name='Ed Sheeran'
)    
    
albums = Album.objects.prefetch_related('song_set')

for album in albums:
    print(album.name)

    for song in album.song_set.all():
        print(song.name)  
    

# An iterator is an object that allows you to traverse through a collection one item at a time.
#An iterator must implement:__iter__(), __next__()

numbers = [10, 20, 30]

it = iter(numbers)  # Create iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # StopIteration


class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
            
        value = self.current
        self.current += 1
        return value
        
    
counter = Counter(5)
    
for num in counter:
        print(num)
    
#-------- A generator is a simpler way to create iterators.

def count_to_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = count_to_five()

print(next(gen))
print(next(gen))


def count_to_five():
    for i in range(1, 6):
        yield i
        
for num in count_to_five():
    print(num)

    
#Python  https://pythontutor.com/python-debugger.html#mode=edit
<h1> Day 1 </h1>
<h2> Keywords in Pyhton </h2>
<p>
* Keywords are the reserved words in python <br>
* we can't use a keyword as variable name, function name or any other identifier <br>
* Keywords are case sentive <br>
</p>
<code><pre>
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from'
, 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

 total no of keywords: 35
 </code></pre>
 
 <h2> Identifier in Pyhton </h2>
 <p> 
 Identifier is a name used to identify a variable, function, class, module, etc. The identifier is a combination of character digits and underscore. The identifier should start with a character or Underscore then use a digit. 
</p>
 
 <h2> Comments in Python in Pyhton </h2> 
 <p> Comments are lines that exist in computer programs that are ignored by compilers and interpreters. <br>
 Symbol: # for single line <br>
 ''' for multiline ''' <br>
 
 </p>
 
 <h2> Variable </h2>
 <h2> Data Types in Python </h2>
 <p> 
 Every value in Python has a datatype. Since everything is an object in Python programming , data types are actually classes and variables are instance (object) of these classes. 
 </p>
 
 ![image](https://user-images.githubusercontent.com/95286756/215192704-243a05d1-94e1-4888-9694-9112eecd247d.png)
 
 
 <h2> List in Python </h2> 
 <p> 
 * List is an Ordered sequence of items.It is one of the most used datatype in pyhton and is very flexible.
 * Declaring  a list is, items separated by commas are enclosed within brackets[].
 </p>
  Alist = [10, 20.5, "hello" ]
 
<h2> Tuple in Pyhton </h2>
<p>
Tuple is an ordered sequence of items same as list. the only difference is that tuples are immutable.
tuples once created cannot be modified. </p>
Atuple =  (1,1.5,"ML")

<h2> Set in Python </h2>
<p>
 Set is unordered collection of unique items. Set is defined by values separated by comma inside braces {}. Items in a set are not ordered. 
 </p>
 
 a = {10,30,20,40,5 }
 
<p> Note: we can perform set operations like  union , intersection on two sets. set have unique values <br>
set object does not support indexing </p>

<h2> Dictionary in Python </h2>
 <p> Dictionary is an unordered collection of key-value pairs. <br>
  in Pyhton, dictionary are defined within braces {} with each item being a pair in the form key: value. <br> key and value can be of any type.
  
 </p>
 
 d = {'a' : "apple", 'b': "bat" }


<h2> Operators in Pyhton </h2>
<p> Operators are special symbols in Python that carry out arithmetic and logical computation. <br> 
the value that operator on is called the operand.

Type : -

1. Arithmetic Operators  - <p2> Arithmetic operators are used to perform mathmatical operations like addition,subtraction,multiplication etc.<br>
2. Comparison (Relational) operators - Comparison operators sre used to compare values. It either returns True or False according to the condition. (>,<,==,!=,>=,<=,) <br>
3. Logical(Boolean) Operators - --> and, or, not  <br>
4. Bitwise Operators ---> Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit (&, |, ~, ^, >>, <<) <br>
5. Assignment Operators - Assignment operators are used in pyhton to assign values to variables (=, +=, -=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, ) <br>
6. Special Operators - 'is' and 'is not' are the identity operators in pyhton  <br>
7. Membership operators --(in and not in)  they are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary). <br>


</p>


<h1> Control Flow in Pyhton </h1>
<h2> if...elif...else statement </h2>
<p> the if...elif..else. statement is used in Python for decision making. </p>


 <h2> Nested-if Statement </h2>
 <p> We can have an if…elif…else statement inside another if…elif…else statement. This is called nesting in computer programming. </p>
 
 
 <h2> while loop </h2>
 <p> The while loop in python is used to iterate over a block of code as long as the expression(condition) is true.
  
  
<h2> break and continue Statements in Pyhton </h5> 
<p>
in Pyhton, break and continue statements can alter the flow of normal loop. <br>
Loops iterate over a block of code until test expression is false,but sometimes we wish to terminate the current iteration or even the whole loop without cheking test expression. <br>
the break and continue statements are used in these cases.
</p>

<h3> Append() </h3>
<p3> Python’s append() function inserts a single element into an existing list. append will add the item at the end. </p3>
 
 <h3>  insert() </h3>
 <p3> The insert() method inserts the specified value at the specified position. <br>
  syntax: list.insert(pos, elmnt)
 </p3>

<h3> remove() </h3>
<p3>  it will remove first occurence <br>
lst.remove(element)
 </p3>
 
 <h3>  List Append & Extend  </h3>

 <hr>

<h1> Function in Python </h1>
<p>

Function is a group of related statements that perform a specific task. <br>

Function help break our program into smaller and modular chunks. As our program grows larger and larger, function make it more organized and manageable. <br>

It avoids repetition and makes code reusable. <br>
Syntax: 
 
 <pre><code>
def function_name(parameters): 
    """ 
    Doc String 
    """ 
    Statements(s) 
 </code></pre>
  
 <ol> 

def function_name(parameters): 
 <li> Keyword "def" marks the start of function header </li>
 <li> Parameters (arguments) through which we pass values to a function. these are optional </li>
  <li> A colon (:) to mark the end of function header </li>
   <li> Doc string describe what the function does. this is optional </li>
    <li> "return" statement to return a value from the function. this is optional</li>
 </ol>
 
 
 </p>

 <h2> Function Call </h2>
 <p> Once we have defined a function, we can call it from anywhere </p>
 
 
 <h2> return Statement </h2> 
 
<p> the  return statement is used to exit a function and go back to the place from where it was called </p>





<hr>

------------------------------------------------------------------------------------------------------------------------
<h5> Q1. Write a program that accepts sets of three numbers, and prints the second-maximum number among the three. </h5>
<h5> Q2. Write a program to print the sum of the first 10 numbers (1-10). </h5>
<h5> Q3. Write a program to print numbers from 1 - 10 with each number printed in a separate line. </h5>
 <h5> Q4. Pyhton program to find the largest element among three number </h5>
 <h5> Q5. find the product of all number present im a list-->
lst = [10, 20, 30, 40, 50] </h5>

<h5> Q6. python Program to display all prime numbers within an interval
</h5>

 

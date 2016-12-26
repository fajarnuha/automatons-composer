I/O Automatons Composer
======
A Distributed Algorithm Project

## Environment

Python 2.7
(check with python --version in your terminal)

## Synopsis

Automatons composition operation allows an automaton representing a complex system to be
constructed by composing automata representing individual system component.

*Source : Distributed Algorithms (Book by Nancy Lynch)*

## Input Fromat

* Put the argument after running the program with the name of two textfile inputs
located in the same folder eg: $ ./compose.py comp1.txt comp2.txt
* Input file should be like the one in the example, each two consecutive line consist of:
  * firstline is the name of components
  * secondline is all elements of component separated by [SPACE]


## Example

#### Test Case

We use our previous quiz as a test case for this assignment. The problem is composing
three automatons defined in the comp1.txt comp2.txt and comp3.txt

#### Run The Program

Since composition is isomorphic such that AxBxC = (AxB)xC, we will execute the program
one by one
Let's combine comp1.txt and comp2.txt and write the output to hasil1.txt:

Using unix-like terminal which has been changed the directory to the project folder:
```bash
./composer.py comp1.txt comp2.txt > hasil.txt
```
Now, we have hasil.txt which is a new automaton derived from combination of comp1.txt and comp2.txt
Then, we can combine again hasil1.txt and comp3.txt, then write the output to hasil2.txt

Using unix-like terminal which has been changed the directory to the project folder:
```bash
./composer.py hasil1.txt comp3.txt > hasil2.txt
```
Finally, we have our result in hasil2.txt

## Developer

Fajar Ulin Nuha (14/368826/PA/16316)

Muhammad Andhimas Bagaswara (14/368447/PA/16285)

Herdian Dewangga  (14/365382/PA/16095)

Naufal Haidar (14/360065/PA/15761)

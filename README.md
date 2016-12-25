I/O AUTOMATONS COMPOSER
A DISTRIBUTED ALGORITHM PROJECT

WHAT IS THIS?
???????

ENVIRONMENT REQUIREMENT
Python 2.7

INPUT FORMAT
Put the argument after running the program with the name of two textfile inputs
located in the same folder eg: $ ./compose.py comp1.txt comp2.txt
Input file should be like the one in the example, such that:
  -firstline is the name of components
  -secondline is all elements of component separated by [SPACE]

EXAMPLE

TEST CASE
We use our previous quiz as a test case for this assignment. The problem is we want to
compose three automatons defined in the comp1.txt comp2.txt and comp3.txt

RUN THE PROGRAM
Since composition is isomorphic such that AxBxC = (AxB)xC, we will executte the program
one by one
Let's combine comp1.txt and comp2.txt and write the output to hasil1.txt:
  Using unix-like terminal which has been changed the directory to the project folder:
    ./composer.py comp1.txt comp2.txt > hasil.txt

Now, we have hasil.txt which is a new automaton derived from combinaton of comp1.txt and comp2.txt
Then, we can combine again hasil1.txt and comp3.txt, then write the output to hasil2.txt
  Using unix-like terminal which has been changed the directory to the project folder:
    ./composer.py hasil1.txt comp3.txt > hasil2.txt

Finally, we have our result in hasil2.txt

DEVELOPER
Project Group Member:
Fajar Ulin Nuha (14/368826/PA/16316)
Andhimas
Herdian
Naufal

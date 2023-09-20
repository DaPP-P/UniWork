# Etude 9: Bug Squashing
Author: Daniel Prvanov

## Start Up

For the program to work there are four packages that need to be included.

```
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
```
The program can be run by typing the following commands into the Studio Visual Code console:
```
gcc -o main main.c
./main
```
This will produce the program which will read from stdin and output if the inputted value can be found in the database. 

## How The Program Works

The program works by first reading from in a file. It then sorts each item into its array. The user can then input 1, 2, 3, or 4 depending on what they want to search for. inputting 1 searches by first name, 2 searches by last name, 3 searches by phone number and 4 searches by email address, while 0 closes the program. 

## Steps Taken To Update The Code

* My first step taken was to fixup the typos (changed emialAdress to emailAddress)and set up the pointers correctly in the struct.
* I then changed how the memory was allocated and deallocated. 
* I then went through the original code adding comments to what I think each step and function is meant to do (this can be seen in the old_main file). Doing this I figured out that the point of this program was to allow the user to search for people in the database, by either searching by first name, last name, email address or phone number. I also came to the conclusion that it would probably be easier to rewrite the code.
* The first thing I did was set up the main. I used the old code to implement the File reader but changed the struct name to Person so it is more obvious about what it is meant to be.
* I then created a new function that counted the number of rows in the text file this is to allocate memory more efficiently and always for the memory allocation to be more dynamic. Instead of the memory allocating over a loop of 50 it does it for as many rows in the text file.
* I used a very similar switch and input reader as the original file but updated it so that there is more feedback and it is more obvious to the user about what can be done.
* I only implemented the find functions and not the sort functions. Their implementation also needed to be changed as the current one did not work.
* I did not implement the sort functions as long as the text file submitted isn't that big their is no need to.

Future improvements:
* Using sorting functions and then searching for the phrase with a divide and conquer algorithm could increase the search up time.
* The output showing all of the people that match the search term instead of only showing the first instance, but due to the old code not looking like it was trying to do this I didn't implement it.
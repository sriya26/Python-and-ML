# **Task-1**

---

## 1) _Crash course on Python by Google and WordCloud_


This course on Coursera was to teach the basics of python including various data types, loops, data structures and the concept of object oriented programming, divided over 6 weeks of tasks, the 6th week being a wordcloud programming project.

•	Week 1: 
>Introduction to Python, functions and keywords, various arithmetic operators and writing basic lines of code

•	Week 2: Basic syntax of Python: 
>o	Introduction to different data types in python, identifying them and implicitly/explicitly converting them, variables

>o	Defining functions using def, passing parameters/arguments to a function and using it to return values using ‘return’.

>o	Using comparison operators like ‘==’ and ’!=’ to obtain a Boolean result along with logical operators like ‘and’, ‘or’ and ‘not’.

>o	Using if, else and elif to compare with the help of logical and comparison operators to execute branching programs based on whether a particular condition is satisfied or not

•	Week 3: Loops in Python:
>o	Introduction to while loop and for loop, using range()for loops to generate a sequence of integers, nesting loops and using break and continue statements 

>o	Importance of recursion, which is basically calling a function over and over and how to use recursive functions.

•	Week 4: Data Structures:
>o	Strings: Introduction to strings, basic string functions and manipulation methods like slicing. Advanced string methods like lower(),upper(), strip(), count, split etc and string formatting to concatenate and format strings.

>o	Lists: Lists in Python are defined using square brackets, with the elements stored in the list separated by commas. Usage of append, remove,pop and insert to modify lists, indexing to access list elements. Introduction to Tuples, used to ensure that an element is in a certain position and will not change and various list and tuple sequence operations.

>o	Dictionaries: Data structure used to organize data into collections into pairs of keys and values. Methods to iterate over dictionaries and various operations used.

•	Week 5: Object Oriented Programming:
>o	Introduction to Object Oriented Programming(OOP), defining classes and its attributes, constructors including _init__  and__str__.

>o	Inheritance to reuse code and Object Composition

•	Week 6:  Wordcloud project

The final programming project was to implement a wordcloud, by creating a dictionary that contains frequencies of each word in the text.

After installing all packages necessary for word cloud script and uploader widget, running the uploader widget and uploading the text, next step was to implement a function calculate_frequencies() that took file_contents(text file) as the parameter.

Then used the split() function to separate all words after which used a for loop to iterate over the entire text. Took another string str1 to take every alphanumeric word and created an if else structure.

If the particular word is not in the list uninteresting_words then it will go to another if else structure to add it in the frequencies dictionary.

If the word is not in the dictionary, then the value of that word taken as key will be 1.

Else the value will be incremented by 1.

Then created a wordcloud using WordCloud() and displayed the image using matplotlib 

Link to certificate:https://coursera.org/share/5d6c2cb2fa083d6d33d460952777393d





## 2)  _Mini Projects_


### **Game-1: Tic-Tac-Toe**

•	Created a dictionary for the board and initialised every value with a space, the key being a number from 1-9. 

•	Initialised a variable player, which will be 1 for player 1 and 2 for player 2. 

•	Input(key) will be taken from each player and if the value corresponding to the key is a space, then value of X(Player 1) or O(Player 2) will be given else, message of invalid input is displayed. 

•	A function end_check() is defined to check if any player has won by checking for X’s or O’s horizontally,vertically or diagonally and if its true then display the message that the player has won and end the game by returning 1 to check_end variable. 

•	Another variable total_moves is defined which is incremented after every turn and if it is equal to 9, then the message of draw will be displayed and the game will end.

References: 1. https://medium.com/@pk1288780/creating-tic-tac-toe-in-python-using-dictionaries-70ab8ab49a19

2. https://www.codespeedy.com/tic-tac-toe-game-using-python-dictionary/



### **Game 2- Connect Four**

•	Used numpy to create a 6x7 matrix of 0’s.

•	 Initialised a variable turn which is 0 for player 1 and 1 for player 2. 

•	After taking input form the player (0-6) for column, pass it through a function loc() to check if the column selected is filled or not and if yes, output ‘Invalid input’ and change gameover to True to end the game.

•	If True then it is sent to a function next_row() to check if the row for the selected column is not filled and also if choice is valid. If true then the row value is returned. 

•	Then the function drop_piece() is used to drop the number in that chosen slot, the variable piece being determined by function player_turn(), which returns the value of piece as 1 if turn=0 (player1) and 2 if turn=1.

•	 A function connect4() is defined to check for the winner and true is returned if the condition is met and the game ends after that when the variable gameover equals true.( all of this is run in a while loop while not gameover, gameover initially being false). 

•	The function draw() is initialised to check for draws and the function print_board() is used to flip the board using a numpy function to see the board from bottom to up.

•	The updated board is printed after every turn and the variable turn is incremented and then using mod the remainder is taken to alternate between player 1 and 2.

References: 1.  https://github.com/jayanam/connect4_python/tree/master/classes
2. https://github.com/KeithGalli/Connect4Python/blob/master/connect4.py






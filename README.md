# BTH-Final-project
The program should be based on a menu (see below) and the information from the file being loaded should be entered in a dictionary. This should be done in a separate function that takes the file name as an input parameter and returns a dictionary. You must read the file with the basic features built into Python (= the ones we discussed in the course). You may not use features from any imported module to do so.

The file has the following principal contents: id, first_name, last_name, montly_salary, weight.   Examples of contents: 4, Carline, Deeming, 690269,96. NOTE! We do not handle weight. It is only included in the large test file 

The file  Person.txt   contains data about 1000 people. You should use this file and final test your program with it. You create the test file in excel. Save it with extension txt example (mytestperson.txt), Remember to use commas (,) between the data. See the Person.txt file. Small file to use in test myperson.txt

The following functions the program should at least be divided into: Menu management, Loading the file. Sort people by intervals, salary increase

-------------------------------------------------- -------------------------------------------------- -------

In MatchIT System 2020
1. Ask for the name of the file to be loaded 
2. Search for a person. Enter  ID and view the person's data
3. What is the highest salary?
4. Sort the people and their data in different intervals (see below) 
5. Update the salary for all (New file is created)
6. What is the average salary for all employees
7. Exit 
Menu item 2

Enter personID: 3

Adria Dysart 553649

Menu item 4

Example of printing the intervals

<200000 20 people

200000 - <400000 30 people

400000 - <600000 15 people

60000 0-- <800000 10 persons

800000 - <1000000 5 people

 

Menu item 6

Percentage below SEK 500,000 : 4

 Percentage SEK 500,000 and more:   2

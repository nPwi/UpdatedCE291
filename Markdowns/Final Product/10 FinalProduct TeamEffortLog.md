# Team Effort Log
*In this section, add a heading for each team member, and under it add the sub headings "Sprint 1, Sprint 2, ..., Sprint N", as illustrated below.  Each team member can be responsible for writing their own section.*

## Nicholas Pwi (Team Leader)

### Sprint 1:
Task: JIRA set-up and administrative
* Create JIRA Scrumboard
* Assign user access
* Created EPICs label

### Sprint 2:
Task: Code Integration
* Integrate existing develop work
* Solve duplicated call of pygame screens

### Sprint 3:
Task: MVP documentation and testing
* Documentation of the markdown files, confluence and ensure JIRA cleanliness
* Testing and fixing of codes after further integration

### Sprint 4:
Task: Final product documentation and testing
* Documentation of the markdown files, confluence and ensure JIRA cleanliness
* Testing and fixing of codes after further integration

### Sprint 5:
Task: Prepare for final review and showcase
* Resolve all integration bugs
* Develop a centralized framework for game looping to have everyone integrate seamlessly and for game to go back and forth without throwing an exception
* Prepare deck for presentation

## Ong Li Zhen

### Sprint 1:
Task: Generate Sudoku
*  Research on how sudoku works and how to code it in python.
*  Create function to create sudoku in different sizes for leveling in future sprint.
*  Create function to remove numbers from the sudoku in order for solver to solve afterwise

### Sprint 2:
Task: Generate level button
*  Research on how to create button function via python 
*  create and combine level button to existing leveling function code

### Sprint 3:
Task: Generate higher complexity Sudoku
* I researched on recursive methods to generate the Sudoku however did not managed to grasp the concept of tail recursive. Hence I went ahead to develop using multiple for loops for the Sudoku. 

### Sprint 4:
Task: Generate display for Sudoku
* As I managed to complete the functional coding for Sudoku complexity previously, this week I went ahead to use pygame's lines and rect to produce the Sudoku graphics with positioning. There were still flaws in the positioning but I am overall happy with the outcome.

### Sprint 5:
Task: Documentation and Integration with the rest
* We realized that there were some challenges in integrating the codes due to the different ways that each developer have built their codes, we spent time together ironing out the differences and coming together onto a central framework to reduce technical debts and be aligned on the game looping function.

## Jason Haw

### Sprint 1:
Task: Shuffle soduku
*  Have to look for a function to randomize the numbers
*  By integrating with probability to generate a percentage to shuffle visible numbers out so as to generate a soduku for user to solve

### Sprint 2:
Task: Increase/decrease difficulty function
*  Have to integrate a level of difficulty by increasing the number of grids in a soduku
*  Create a if else logic to return a number as a difficulty.
*  Then that number will be used as a base count for the script to generate the numbers of cells In a soduku

### Sprint 3:
Task: Solve Level Logic
* By using a method called backtracking , the solve soduku functions will go through all the numbers and start filling up the cells as long as the rules are fulfilled, however when the next number is not possible and there is no numbers left to input, the function will back track and start decreasing the number that the loop has tried.

### Sprint 4:
Task: Adding time function
* By using pygame module, I called upon the clock method and use the game tick function to generate a time function. Every 1 tick, a rectangle will be drawn and then the time string will then be pasted

### Sprint 5:
Task: Add number of moves as a counter for data analysis and created solve soduku and return to menu buttons
* By drawing rectangles , the string of "solve soduku" and "return to menu" can then be printed on it and will be reflected as a button. For ever input the program has executed, the number of moves will increase by 1 until the program has solve the game.

## Wilson Low

### Sprint 1:
Task: Report Analytic Button
*  Research on pygame code & design a graphical report generate button with purpose to display a chart to analyze the efficiency of the solver in Sudoku.

### Sprint 2:
Task: Analysis Graph
*  Import matplot libraries to plot a graphical chart, include the function in the report generate button, indicating the time taken for solver in each difficulty.

### Sprint 3:
Task: Bug fixing
* There were some issues that occurred from the Analysis function that I built, it was not aligned with the Main Menu built by my team members. I spent time working it through on pygame instead of matlab.  

### Sprint 4:
Task: Documentation
* In this sprint, I ensured the JIRA cleanliness and updated remaining documentation on WIKI as well as required MD files. 

### Sprint 5:
Task: Integration into looping frame
* Worked together with the rest of the team to figure a way to integrate the Analysis function that I have created into the looping function of the game.


## Yap Choo Kiat

### Sprint 1:
Task: Slash page appearance
*  Have to study how to use pygame to draw out a slash page.
*  By using pyame module, import the text and the picture and show by them by drawing a screen by pixel

### Sprint 2:
Task: Home page button
*  Have to on how to draw a button in python and show it in GUI
*  By using pygame module, draw a box to represent the button and put text inside the box. Then detect and capture mouse cursor motion and make a if statement when the cursor pressed the box.

### Sprint 3:
Task: Increase difficulty button
* Have to study on how to draw a button in python and show the button in parallel with the other button. By using screenblit function in pygame with a math formula, button can be drawn in parallel with the other button.

### Sprint 4:
Task: Exit button
* Have to study on how user can exit from main menu. Define a variable and set it to not true, and do a While loop to say while the variable is not true, then main menu will run forever until the program detected a mouse press down action in the exit button box, then make the variable become true, and the program will then exit from the While loop.

### Sprint 5:
Task: Fix bugs on Exit Button
* Have to study on how to make a program in python exit from running. By using exit() function in the exit button, when the program detected a mouse press down action in the exit button box, it can make the program exit and come out of the program in Python.
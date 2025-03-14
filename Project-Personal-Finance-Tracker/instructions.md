# Instructions 

1. In the `main.py` file, we will be creating a personal finance tracker
2. We will use lists and dictionaries to save and load the financial data
3. Error handling will be included for user inputs and file operations
4. The first step is to initialise lists for expenses and incomes, that will store dictionaries
5. Next is to fill up the save_financial_data and load_financial_data functions, that writes and reads data from the json file respectively.
6. We will then fill up the add_financial_data function that takes the category and amount from user inputs, and appends them to expenses or income list
7. Lastly, the user_interface function asks the user if they want to add into the income or expenses list, and will keep prompting them for an input until they select save and exit.

# Hints
1. For printing values that are in variables, use f-strings
2. For file handling, use keywords like 'with', 'open', and 'as'
3. For exception handling, use keywords like 'try' and 'except'
4. For the save_financial_data function, use the IOError exception when writing fails
5. When collecting user input for the amount, make sure to convert it to a float


## Expected Output
```txt
Options: [1] Add Expense [2] Add Income [3] Save and Exit
Choose an option: 2
Enter category for the income: lighthouse
Enter amount for the income: 300
Income added: lighthouse - $300.0

Options: [1] Add Expense [2] Add Income [3] Save and Exit
Choose an option: 3
Data saved successfully.
Exiting program.
```

## Test Your Code
### Running Tests
- To verify your program, run it and check if it provides the correct output based on the input.
   ![image](tests_tools.png)
- If the output is correct, and there are no errors, proceed to submit it.
   ![image](submit.png)

### Test Results
- If your code passes all the tests, you will see the following screen.
   ![image](pass.png)
- If any test case fails, analyze the `Results` section to identify the error and refine your code.
   ![image](fail_tests.png)
   ![image](results.png)

## Final Note
- Before submitting, make sure that your program correctly asks for the user's name, forms the greeting and prints it to the console.
   ![image](submit.png)

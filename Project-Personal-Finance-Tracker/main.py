#---------------------------- PART 1------------------------------------------
# Initialize the expenses and incomes lists 
expenses = 
incomes =

#-----------------------------PART 2------------------------------------------
# import the json library

# This function takes in the expenses list, income lists, and json file
def save_financial_data(, , filename=):
    # Combine expenses and incomes lists into one dictionary
    data = 

    # Attempt to write data to a file
    
      # Open the file in write mode
      
        # Use json's dump function to add data into the json file
        
        print("Data saved successfully.")
    # Handle exception when writing fails
    

# This function takes in the json file
def load_financial_data(filename=):
    # Attempt to load data from a file
    
      # Open the file in read mode 
      
        # Use json's load function and return the expenses and incomes data separately

  
    # Handle exception when file cannot be found, and return empty lists
    
    # Handle exception when json loading fails, and return empty lists
    
    # General exception for any other exceptions, and return empty lists
    


#-----------------------------PART 3------------------------------------------
# This function takes in the entries, either the expenses or incomes list, and the entry_type (either 'expenses' or 'incomes')
def add_financial_entry(entries_list, entry_type):
  # Attempt to collect user input
  
    # Add category and amount variables to collect user input
    category = 
    amount = 

    # Create and add the new dictionary entries into the lists
    
    # Print the category and amount added using f-strings
    
  # Handle exception when user input is not valid for the amount
  

def user_interface():
  # call the load_financial_data function
  expenses, incomes = 

  # add a while loop that continues as long as the user does not select option 3
  
    print("\nOptions: [1] Add Expense [2] Add Income [3] Save and Exit")
    # Get the user's input, either 1, 2, or 3
    
    # if they select 1, call the add_financial_entry function, and specify the expenses list and the string 'expense'
    
    # else if they select 2, call the add_financial_entry function, and specify the incomes list and the string 'income'
    
    # else if they select 3, call the save_financial_data function, and print a message to tell them that the data has been saved, and break out of the loop
    
    # else, print a message saying that the option they entered is invalid
    

# Run the user interface
user_interface()

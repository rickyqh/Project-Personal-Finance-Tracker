import json
from unicodedata import category

expenses=[]
incomes=[]

def save_financial_data(expenses, incomes, filename="financil_data.json"):
    data={"expenses": expenses, "incomes": incomes}
    try:
        with open(filename,"w") as file:
            json.dump(data,file,indent=4)
            print('data successfully saved')
    except IOError as e:
        print("oh no: ", e)


def load_financial_data(filename="financil_data.json"):
    data={"expenses":expenses,"incomes":incomes}
    try:
        with open(filename,"r") as file:
            data = json.load(file)
            return data['expenses'],data['incomes']
    except IOError as e:
        print("oh no:", e)
    except FileNotFoundError as e:
        print("Error decoding JSON data.")
        return [],[]
    except json.JSONDecodeError as e:
        print("Error decoding JSON data.")
        return [],[]
    except Exception as e:
        print("an error occured while reading the file:",e)
        return [],[]
    
def add_financial_entry(entries_list,entry_type):
    try:
        category=input(f'Enter catergory for the {entry_type}: ')
        amount= float(input(f"Enter amount for the {entry_type}: "))
        entries_list.append({'catergory':category,'amount':amount})
        print(f"{entry_type.capitalize()} added: {category} - ${amount}")
    except ValueError:
        print("invalid amount entered.Please enter a numeric value.")

def user_interface():
    expenses,incomes =load_financial_data()
    while True:
        print("\nOptions:[1]Add Expense [2]Add Income [3]save and exit")
        choice=input("choose an option:")
        if choice=='1':
            add_financial_entry(expenses,'expense')
        elif choice=='2':
            add_financial_entry(incomes,'incomes')
        elif choice=='3':
            save_financial_data(expenses,incomes)
            print("exiting program.")
            break

if __name__ == "__main__":
    user_interface()
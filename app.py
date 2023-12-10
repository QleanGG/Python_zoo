import os
from enum import Enum
from helper import save_data,load_data

# array decleration
my_zoo = []
my_data_file = 'my_zoo.json'

# Enums
class Actions(Enum):
     PRINT = 1
     ADD = 2
     FIND = 3
     REMOVE = 4
     EXIT = 5

def exit_program():
    save_data(my_data_file,my_zoo)
    print("Cya Later")
    exit()

# add new contact
def add_animal():
    global my_zoo
    my_zoo.append({"Name":input("Enter Animal Name: "),"Specie":input("Enter Animal Specie: "),"Age":input("Enter Age Name: ")})
    print("Contact added!")

# search
def find_animal():
    global my_zoo
    search_id = input("Enter Name: ")
    for animal in my_zoo:
        print(animal["Name"])
        if animal["Name"] == search_id:
            return animal
    print("Couldn't find your animal...")
        
def delete_animal():
    global my_zoo
    search_id = input("Enter Name: ")
    for animal in my_zoo:
        if animal["Name"] == search_id:
            my_zoo.remove(animal)
            print(f"animal with Name {search_id} has been deleted.")
            return
        
    print("Couldn't find your animal...")

def display():#Displays the menu
    print("Welcome to Qlean's Zoo")
    for action in Actions:
        print(f'{action.value} : {action.name}')
    return Actions(int(input("Enter your selection: ")))

def main():
    global my_zoo
    #clear Console
    os.system('cls' if os.name == 'nt' else 'clear')
    my_zoo = load_data(my_data_file,my_zoo)
    
    while (True):
      userSelection=display() #display a menu and get user selection and  implements menu
      if userSelection == Actions.EXIT: exit_program()
      if userSelection ==  Actions.PRINT: print(my_zoo)
      if userSelection ==  Actions.FIND: print(find_animal())
      if userSelection ==  Actions.ADD: add_animal()
      if userSelection ==  Actions.REMOVE: delete_animal()

        
if __name__ == "__main__":
	main()

to_do_list = []


def add_to_do():
    global to_do_list
    add = True
    while add:
        item = input("What are the things you have to do today? ")
        to_do_list.append(item)
        cont = input("Would you like to add more items?\nType y for yes and n for no")
        if cont =="y":
            add = True
        else:
            add = False
    response = input("Would you like to see your list?\nType y for yes and n for no ")
    if response == "y":
        print("Things to do: ")
        display_list()

def remove_to_do():
    global to_do_list
    item_done = input("Have you done any of the items on the list?/nType Y for YES and N for no").lower()
    if item_done == "y":
        if item_done in to_do_list:
            to_do_list.remove(item_done)
        else:
            print("Item was not logged in list")
    response = input("Would you like to see your updated list?\nType y for yes and n for no ")
    if response == "y":
        print("Things to do: ")
        display_list()


def display_list():
    global to_do_list
    print(to_do_list)


action = input("Do you want to add to your list, remove from it or see items on it?\nType"
               " A to add , R to remove and D to display").lower()
if action == "a":
    add_to_do()
elif action == "r":
    remove_to_do()
elif action == "d":
    display_list()


# 10.Shopping List
# What am I buying?
# Create a shopping list app, in which the user can add and remove items
# from his shopping list using the console.
# 1. Create a function called help_menu() which is going to show the users a
#   help menu for your simple app.
# Example: Press ‘a’ to add items to the shopping list. Press ‘s’ to show
# the items in the list, ‘r’ to remove and ‘q’ to quit the app
# 2. Create a function show_items() which reads the list and shows the items to
#   the user. Each item should have an id number.
# 3. Create a function add_item() which allows the user to add a new item to
#   the list. Ask the user for the position of the item when adding, if None add the item to the end of the list.
# 3. Create a function remove_item() to remove an item form the list also by
#   asking for the position.


def shopping_list():
    # a list to store the items
    items_list = []

    def help_menu():
        print("Press \n"
              "h: help menu \n"
              "s: show items \n"
              "a: add item \n"
              "r: remove item  \n"
              "q: quit \n")

    def add_item():
        new_item = input('What do you want to add?\n')
        item_index = input('In which position\n')
        if item_index is None or not item_index.isdigit():
            items_list.append(new_item)
        else:
            items_list.insert(int(item_index), new_item)

    def show_items():
        if len(items_list) == 0:
            print('There are no items on the list, nothing to show!')
        else:
            for i in range(len(items_list)):
                print(f"{i + 1}: {items_list[i]}")

    def remove_item():
        if len(items_list) != 0:
            item_index = input('From which position\n')
            items_list.pop(int(item_index) - 1)
        else:
            print('The list is empty, nothing to remove!')

    # initialise the program with the help menu
    help_menu()

    flag = True
    while flag:
        user_input = input('Type your choice \n')
        if user_input == 'q':
            print('Thank you Bye!!')
            flag = False
        elif user_input == 'h':
            help_menu()
        elif user_input == 'a':
            add_item()
        elif user_input == 'r':
            remove_item()
        elif user_input == 's':
            show_items()


shopping_list()


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list, item):
    item = input("Enter an item: ")
    return shopping_list.append(item)

def remove_item(shopping_list, value):
    value = input("Enter the item: ")
    if value in shopping_list:
        shopping_list.remove(value)

def view_shopping(shopping_list):
    print(shopping_list)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list, "item")
            
        elif choice == '2':
            remove_item(shopping_list, "item")
            pass
        elif choice == '3':
            # Display the shopping list
            view_shopping(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
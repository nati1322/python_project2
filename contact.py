print('''
1. view the list
2. add to the list
3. remove from the list
''')

lists = []
while True:
    items = input("Enter your selection: ")
    if items == "1":
        for index, item in enumerate(lists):
            print(f"{index + 1}. {item}")
    elif items == "2":
        add_items = input("Enter what you need to add to the list: ")
        lists.append(add_items)
    elif items == "3":
        try:
            remove_index = int(input("Enter the index of the item to remove: "))
            if 0 <= remove_index < len(lists):
                removed_item = lists.pop(remove_index)
                print(f"Removed: {removed_item}")
        except:
            print("Invalid input. Please enter a number.")
    
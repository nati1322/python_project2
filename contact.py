print('''
1. view the list
2. add to the list
3. remove from the list
''')

lists = []
while True:
    items = input("enter your selection: ")
    if items == "1":
        for i in lists:
            print(i)
    elif items == "2":
        add_items = input("enter you need to add to the list: ")
        lists.append(add_items)
    elif items == "3":
        remove_items = input("enter you need to remove from the list: ")
        lists.remove(remove_items)
    else:
        print(f"{items} is invalid pleas enter valid selection")

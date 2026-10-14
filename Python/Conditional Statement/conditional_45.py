#45. Write a program to print menu-based food selection using match case.

choice = int(input("1:Pizza 2:Burger 3:Pasta > "))
match choice:
    case 1:
        print("Selected: Pizza ($12)")
    case 2:
        print("Selected: Burger ($8)")
    case 3:
        print("Selected: Pasta ($10)")
    case _:
        print("Item not on menu")
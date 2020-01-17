import sys, os
import Sorting_Algorithm

#If decide to start without input array
array = [10, -9, 8, -7, 6, -5, 4, -3, 2, -1, 0]

# Main definition - constants
menu_actions = {}

# Main menu
def main_menu():
    os.system('CLS')

    print("Welcome,\n")
    print("Please choose the menu you want to start:")
    print("1. Input Array")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Selection Sort")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    os.system('CLS')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1, input array
def menu1():
    print("Enter elements to sort")
    global array
    array = list(map(int, input(">>").split()))
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Selection Sort")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2, Bubble sort
def menu2():
    Sorting_Algorithm.bubble_sort(array)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 3, Insertion Sort
def menu3():
    Sorting_Algorithm.insertion_sort(array)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 4, Selection Sort
def menu4():
    Sorting_Algorithm.selection_sort(array)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '9': back,
    '0': exit,
}


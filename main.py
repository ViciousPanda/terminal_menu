"""
Dynamic Python menu for the terminal
By Jacob Gesink

This menu allows you to write classes and functions directly into menu items. 
It allows for submenu nestling and should be a quick sollution to any python 
menu that requires the terminal window for user selection.

naming of menu items is linked to the function names. Class names are
descriptive only and hidden from the end user.

"""

from menu import menu_builder, MainMenu


def main():
    menu_builder(MainMenu)


if __name__ == "__main__":
    main()

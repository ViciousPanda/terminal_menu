"""
Dynamic Python menu for the terminal
By Jacob Gesink

This menu allows you to write classes and functions directly into menu items. 
It allows for submenu nestling and should be a quick sollution to any python 
menu that requires the terminal window for user selection.

naming of menu items is linked to the function names. Class names are
descriptive only and hidden from the end user.

"""

from menu import Menu
import sys


# use function menu_builder to make a menu
def menu_builder(class_name):
    menu_instance = Menu(class_name)
    menu_instance.draw()
    getattr(globals()[menu_instance.class_name_str](), menu_instance.option)()


class MainMenu:

    def option_one(self):
        print("Main menu option one")

    def option_two(self):
        print("Main menu option two")

    def submenu_1(self):
        menu_builder(SubMenuOne)

    def quit(self):
        print("Quit program" + "\n")
        sys.exit(0)


class SubMenuOne:

    def option_one(self):
        print("submenu one option one")

    def option_two(self):
        print("submenu one option two")

    def back(self):
        menu_builder(MainMenu)

    def quit(self):
        print("Quit program" + "\n")
        sys.exit(0)


def main():
    menu_builder(MainMenu)


if __name__ == "__main__":
    main()

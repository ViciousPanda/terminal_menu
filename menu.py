"""
Dynamic Python menu for the terminal
By Jacob Gesink

This menu allows you to write classes and functions directly into menu items. 
It allows for submenu nestling and should be a quick sollution to any python 
menu that requires the terminal window for user selection.

naming of menu items is linked to the function names. Class names are
descriptive only and hidden from the end user.

"""

import os
import sys


def menu_builder(class_name):
    menu_instance = Menu(class_name)
    menu_instance.draw()


class Menu:
    def __init__(self, class_name):
        # populate a dict with menu_list and index from 1
        self.dct = {}
        self.class_name_str = ""
        self.option = ""
        self.construct(class_name)
        self.contruct_name_str(class_name)

    def __repr__(self):
        return f"Menu('{self.class_name_str}', {self.dct}, {self.option})"

    # construct a dict of all the function names in a class
    def construct(self, class_name):
        menu_lst = []
        for key, value in class_name.__dict__.items():
            if "function" in str(value):
                menu_lst.append(key)
        self.dct = dict(enumerate(menu_lst, start=1))

    # callling the class name into a clean string
    def contruct_name_str(self, class_name):
        split_left = str(class_name).split(".")
        split_right = split_left[1].split("'")
        self.class_name_str = split_right[0]

    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    # draw main menu
    def draw(self):
        self.cls()
        for key, value in self.dct.items():
            print("[ {} ] for {}".format(key, value))
        self.user_input()

    # ask for input and check for validity
    def user_input(self):
        usr_select = input("Select: ")
        if not self.is_valid_option(usr_select):
            self.draw()
        elif not self.is_menu_option(usr_select):
            self.draw()
        else:
            self.option = self.dct[int(usr_select)]
            self.run_menu()

    # check if input is a number
    def is_valid_option(self, usr_select):
        if usr_select.isnumeric():
            return True
        return False

    # check if input is in the dict of menu options
    def is_menu_option(self, usr_select):
        if int(usr_select) in self.dct:
            return True
        return False

    def run_menu(self):
        getattr(globals()[self.class_name_str](), self.option)()


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


"""
def menu_builder(class_name):
    menu_instance = Menu(class_name)
    menu_instance.draw()
    getattr(globals()[menu_instance.class_name_str](), menu_instance.option)()
"""

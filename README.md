# terminal_menu

Dynamic Python menu for the terminal
By Jacob Gesink

This menu allows you to write classes and functions directly into menu items. It allows for submenu nestling and should be a quick sollution to any python menu that requires the terminal window for user selection.

naming of menu items is linked to the function names. Class names are descriptive only and hidden from the end user.

# Terminal Menu

This menu allows you to write classes and functions directly into menu items. It allows for submenu nestling and should be a quick sollution to any python menu that requires the terminal window for user selection.

## Installation

import menu.py into your project.

import sys and import os are optional

## Usage

```python
from menu import Menu

# use function menu_builder to make a menu
def menu_builder(class_name):
    menu_instance = Menu(class_name)
    menu_instance.draw()
    getattr(globals()[menu_instance.class_name_str](), menu_instance.option)()

# create a class to fill the menu with names and operations
class MainMenu:
    def quit(self):
        sys.exit(0)
```

## returns 'main menu'

![screenshot](assets/image.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

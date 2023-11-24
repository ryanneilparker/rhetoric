# main.py - the main program loop
from ui import output, input

def main():
    output.display_logo()
    output.display_main_menu()
    input.main_menu_selection()

main()

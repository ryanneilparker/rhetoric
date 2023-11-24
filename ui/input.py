# input.py - collects input from the user

from actions import post

def main_menu_selection():
    selection = input("Perform action number: ")
    match selection:
        case "1": post.blog()
        # case "2": post.tweet()
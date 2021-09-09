from modules.file_editor import *


def run_main():
    """
    This function is the function is used to make main.py look cleaner
    """
    my_username = input("Enter username: ").strip()
    my_password = encrypt_given_password(input("Enter your password: "))
    if search_username_and_password_in_database(my_username, my_password):
        print_menu(my_username)
        while True:
            user_input_number = input("Enter your number: ")
            if check_user_input_number(user_input_number):
                user_input_number = int(user_input_number)
                if user_input_number == 1:
                    main_write_to_b_from_a()
                elif user_input_number == 2:
                    main_delete_file_using_path()
                elif user_input_number == 3:
                    main_swap_two_files()
                elif user_input_number == 4:
                    main_replace_string_in_file()
                elif user_input_number == 5:
                    main_exit_program()
                    break
    else:
        print("Wrong username or password.")


def print_menu(username: str):
    """
    This function prints the menu for our program
    :param username: The username used to login
    """
    print(f"Welcome, {username}!")
    print("Enter 1 to add file A content to file B.")
    print("Enter 2 to delete file A.")
    print("Enter 3 to swap file A and file B content.")
    print("Enter 4 to delete from file A String B.")
    print("Enter 5 to Exit.")


def main_write_to_b_from_a():
    """
    This function is the function used for part 1 of the main
    used to make main look cleaner
    """
    file_a_path = input("Enter file A path: ")
    file_b_path = input("Enter file B path: ")
    write_to_b_from_a(file_a_path, file_b_path)


def main_delete_file_using_path():
    """
    This function is the function used for part 2 of the main
    used to make main look cleaner
    """
    file_to_delete_path = input("Enter file to delete path: ")
    print(f"File was successfully deleted." if delete_file(file_to_delete_path) else "File does not exist.")


def main_swap_two_files():
    """
    This function is the function used for part 3 of the main
    used to make main look cleaner
    """
    file_a_path = input("Enter file A path: ")
    file_b_path = input("Enter file B path: ")
    print(f"Files were swapped" if swap_files(file_a_path, file_b_path) else "Swapping files error")


def main_replace_string_in_file():
    """
    This function is the function used for part 4 of the main
    used to make main look cleaner
    """
    file_path = input("Enter your file path: ")
    string_to_replace = input("Enter the string you want to delete: ")
    print("Successfully deleted the string." if replace_string(file_path,
                                                               string_to_replace) else "Deleting string went wrong.")


def main_exit_program():
    """
    This function is the function used for part 5 of the main
    used to make main look cleaner
    """
    print("Thank you for using our file management program.\nExiting..")

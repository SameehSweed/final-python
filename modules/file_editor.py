from modules.help_functions import *


def add_user(username: str, password: str) -> bool:
    """
    This function is used by me for development purpose and it adds user to the database for development use
    :param username: The username to add
    :param password: The password to attach for this username
    :return: True if both username AND password does meet the conditions and False if not
    """
    if search_username_in_database(username):
        print("username already been used or wrong password format.")
        return False
    password = encrypt_given_password(password)
    with open(file_name, "a") as file:
        file.write(f"\n{username} {password}")
    print("used added successfully.")
    return True


def write_to_b_from_a(file_a: str, file_b: str) -> bool:
    """
    This function does the Writing action from file_a to file_b
    :param file_a: file_a path
    :param file_b: file_b path
    """
    if can_write_to_b_from_a(file_a, file_b):
        with open(file_a, "r") as f:
            with open(file_b, "a") as f1:
                f1.write(f"\n{f.read()}")
        print("Successfully written from file_a to file_b.")
        return True
    return False


def replace_string(file_path: str, string: str) -> bool:
    """
    This function replaces the string entered with a blank value to sort of delete the string
    :param file_path: The file path where we want to delete the string
    :param string: The string we search for to delete
    :return: True if the string was successfully replaced "deleted" and False if not
    """
    if is_valid_file(file_path) and string.strip() != "" and string == string.lower():
        file_contents = get_file_content(file_path).replace(string, "")
        write_file_content(file_path, file_contents)
        return True
    return False


def swap_files(file_a: str, file_b: str) -> bool:
    """
    This function returns True if it successfully swaps the given files and False if not
    :param file_a: The file path
    :param file_b: The file path
    :return: True if it successfully swaps the given files and False if not
    """
    if is_valid_file(file_a) and is_valid_file(file_b):
        file_a_content = get_file_content(file_a)
        file_b_content = get_file_content(file_b)
        write_file_content(file_a, file_a_content)
        write_file_content(file_b, file_b_content)
        return True
    return False

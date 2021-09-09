from hashlib import sha256
import os

file_name = "credentials.txt"


# file_name is a variable used to store the "database" file name
# its a variable that was entered by us and no need to check and validate it when we call it

def encrypt_given_password(password: str) -> str:
    """
    This function returns an encrypt version of the given string to use for passwords
    :param password: The password we want to encrypt given by the user
    :return: the encrypted version of the given string
    """
    return sha256(password.encode()).hexdigest()


def is_valid_file(file_path: str) -> bool:
    """
    This function returns True if the given string is an actual file path in the PC
    :param file_path: The file path entered by the user
    :return: True if the given string is an actual file path in the PC and False if not
    """
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.R_OK):
                return True
            raise OSError
    except OSError:
        print("One or more files aren't valid.")
        return False


def can_write_to_b_from_a(file_a: str, file_b: str) -> bool:
    """
    This function returns True and writes the contents of file_a to file_b if both files are actual files
    and if its possible to write to file_b from file_a
    :param file_a: The file path entered by the user
    :param file_b: The file path entered by the user
    :return: True if both files are actual files and if its possible to write to file_b from file_a and False if not
    """
    try:
        if is_valid_file(file_a) and is_valid_file(file_b):
            if file_a != file_b:
                # making sure the files are actual files in the PC
                with open(file_b, "a") as f_b:
                    with open(file_a, "r") as f_a:
                        return f_a.read().strip() != "" and f_b.writable()
            raise ValueError
        raise TypeError
    except TypeError:
        print("Files invalid.")
        return False
    except ValueError:
        print("Same file entered.")
        return False


def get_file_content(file_name_to_get: str) -> str:
    """
    This function returns the file contents
    :param file_name_to_get: The given file path
    :return: The file contents
    """
    if is_valid_file(file_name_to_get):
        with open(file_name_to_get) as file:
            return file.read()


def write_file_content(file_name_to_write: str, file_content: str):
    """
    This function writes file_content to file_name_to_write
    :param file_name_to_write: the destination file
    :param file_content: the content to write
    """
    # this function is called after making sure the parameters are valid and okay to write
    with open(file_name_to_write, "w") as file:
        file.write(file_content)


def search_username_in_database(username: str) -> bool:
    """
    This function returns True if it finds the username in the database
    :param username: Username given by user to search for in the database
    :return: True if it finds the username in the database and False if not
    """
    with open(file_name, "r") as file:
        for line in file:
            if username == line.split()[0]:
                # if the username is the line
                return True
    return False


# i want to make sure that i look for the correct password
def search_username_and_password_in_database(username: str, password: str) -> bool:
    """
    This function returns True if it finds and match both username and password in the database
    :param username:The username we get from user to search for
    :param password:The password to match the username we get from user
    :return:True if it finds and match both username and password in the database and False if not
    """
    with open(file_name, "r") as file:
        for line in file:
            if search_username_in_database(username) and password == line.split()[1]:
                # if the username AND the password are in the same line (match each other)
                return True
    return False


def check_user_input_number(input_num: str) -> bool:
    """
    This function returns True if the entered value is integer and between the top and bottom values
    :return: True if the entered value is integer and between the top and bottom values
    """
    try:
        top_value = 5
        bottom_value = 0
        input_num = int(input_num)
        if bottom_value < input_num <= top_value:
            return True
        raise TypeError
    except TypeError:
        print("Enter number between 1 and 5.")
    except ValueError:
        print("Numeric value only.")


def print_file_contents(file: str):
    """
    This function prints file contents for development use
    :param file: The file path given
    """
    if is_valid_file(file):
        print(get_file_content(file))


def delete_file(file_to_delete: str) -> bool:
    """
    This function deletes the file by the given file path if it exists
    :param file_to_delete: The given file path
    :return: True if the file has successfully deleted and False if not
    """
    if is_valid_file(file_to_delete):
        os.remove(file_to_delete)
        return True
    return False

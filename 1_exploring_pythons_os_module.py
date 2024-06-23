#Task 1 Directory Inspector

import os

def list_directory_contents(path):
    try:
        if os.path.exists(path) == True:
            dir_list = []
            for index, dir_or_file in enumerate(os.listdir(path), 1):
                dir_list.append(f"{index}) {dir_or_file}")
            print("Items listed without extensions are subdirectories")
            return dir_list
        else:
            return f"Path {path} does not exist"
    except PermissionError:
        print("You don't have permission to access or display this path.")
    except FileNotFoundError:
        print("File, path, or directory not found.")
    except IOError:
        print("Issue occured while writing to file.")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General error occured: {e}")

input_path = str(input("What path would you like to list and print all subdirectories and files for?: "))
run_dir_contents = list_directory_contents(input_path)
print(run_dir_contents)
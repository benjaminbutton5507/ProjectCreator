import sys
import os

from pac import SystemInfo
from pac import Project, languages


project: Project | None = None

#### DIRECTORIES ####
program_files = "C:\\Program Files"
program_creator = program_files + "\\ProgramCreator"
program_data = program_creator + "\\Data"


def surround_with_quotes(string: str) -> str:
    return "\"" + string + "\""

def is_windows() -> bool:
    if sys.platform == "win32":
        return True
    else:
        return False

def is_admin():
    ...


def request_admin():
    ...

def check_program_data_file_integrity():
    if not os.path.exists(program_files):
        ...

    if not os.path.exists(program_creator):
        os.mkdir(program_creator)

    if not os.path.exists(program_data):
        os.mkdir(program_data)


def startup():
    request_admin()
    check_program_data_file_integrity()

    global project
    system_info = SystemInfo(platform="win32")
    project = Project(data_path=program_data)


def create_project():
    print()
    print("What is the name of the project?")
    print("   #> ", end='')

    name = input()

    project.name = name


    print()
    print("What is the path to the project?")
    print("   #> ", end='')

    path = input()

    project.path = path

    while True:
        print()
        print("What is the language of this project?")
        print("   #> ", end='')

        language = input()

        if language in languages:
            project.language = language
            break
        else:
            print(f"Language ({language}) is not a valid language for this program!")

    project.complete()
    project.create_project()



def load_project():
    print()
    print("Loading a project has not been implemented!")
    print()


def main():
    startup()

    while True:
        print("What do you want to do?")
        print(" 1) Create Project")
        print(" 2) Load Project")
        print(" 3) Exit")
        print()
        print("   #> ", end='')

        option = input()

        if option == "1":
            create_project()
        elif option == "2":
            load_project()
        elif option == "3":
            print()
            print("Quitting Program!")
            sys.exit(0)
        else:
            print()
            print("That is not a valid option!")


if __name__ == "__main__":
    main()
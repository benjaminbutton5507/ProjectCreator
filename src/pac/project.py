import os
import json


languages = [
    "C++",
    "Python"
]


class Project:
    def __init__(self, data_path: str, name: str | None = None, language: str | None = None, path: str | None = None):
        self.data_path: str = data_path
        
        self.name = name
        self.language = language
        self.path = path
        self.path_with_name = None
        self.final_path = None
        self.final_data_path = None
        self.path_parts = []

        self.data_dict = {}

    def Info(self) -> None:
        print(f"Project(name: {self.name}, language: {self.language}, path: {self.path}, final_path: {self.final_path})")

    def complete(self):
        self.path_with_name = self.path + "\\" + self.name

        part = ''

        for char in self.path_with_name:
            if char == '\\':
                self.path_parts.append(part)
                part = ''
            else:
                part += char

        self.path_parts.append(part)

        self.final_path = "\\\\".join(self.path_parts)

        self.data_dict.update({"name": self.name})
        self.data_dict.update({"language": self.language})
        self.data_dict.update({"path": self.path})
        self.data_dict.update({"final_path": self.final_path})

        self.final_data_path = self.data_path + "\\" + self.name + ".json"

        with open(self.final_data_path, "w") as f:
            json.dump(self.data_dict, f)

    def create_project(self) -> None:
        if not os.path.exists(self.final_path):
            os.makedirs(self.final_path)
        else:
            NotEmptyPath(self.final_path)


def NotEmptyPath(path: str) -> None | str:
    while True:
        print()
        print("This path already exists! Do you want to override this path? (If filled for github enter 'g')")
        print()
        print("   #> ", end='')

        option = input()

        if option == "Y" or option == "y":
            print()
            print("Project being overridden!")
            os.rmdir(path)
            os.makedirs(path)
            print("Project successfully overridden!")
            break
        elif option == "N" or option == "n":
            print()
            print("Program ending!")
            break
        elif option == "g":
            print()
            print("Proceeding w/ Github...")
        else:
            print()
            print(f"That is not an option! ({option})")
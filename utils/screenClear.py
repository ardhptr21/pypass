import os


def screenClear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

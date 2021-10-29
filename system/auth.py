import pyfiglet
from rich.console import Console
from database.Account import Account

from database.User import User
from utils.inputCheck import inputCheck
from utils.screenClear import screenClear

console = Console()


def login(user: User):
    username = console.input("[magenta]Username: [/magenta]")
    password = console.input("[magenta]Password: [/magenta]")

    isFind = user.find(username, password)
    if not isFind:
        console.print(
            "\n[red]Ooops! [green]Username[/green] or [green]Password[/green] is invalid[/red]\n[yellow bold]Please login again!\n"
        )
        login(user)
    screenClear()


def search():
    print("search")


def add(account: Account):
    console.print("[bold yellow]Please insert some account info for spesific app\n")

    email = console.input("[magenta]Email\t :[/magenta] ")
    username = console.input("[magenta]Username :[/magenta] ")
    password = console.input("[magenta]Password :[/magenta] ")
    app_name = console.input("[magenta]App Name :[/magenta] ")
    url = console.input("[magenta]Url\t :[/magenta] ")

    account.add(password, app_name, email, username, url)
    console.print("[green]Successfully add new account info")


def update():
    print("update")


def delete():
    print("delete")


def choose(menu, account: Account):
    choosed = None
    try:
        choosed = int(console.input("[blue]Please choose one option above:[blue] "))
    except ValueError:
        console.print("[red]Please only insert a number!\n")
        return choose(menu, account)

    switcher = {1: search, 2: add, 3: update, 4: delete}

    if choosed not in switcher.keys() and choosed != 0:
        console.print("[red]Please choose a valid option above!\n")
        return choose(menu, account)

    if choosed != 0:
        screenClear()
        switcher.get(choosed)(account)
        isContinue = inputCheck("Continue?", sol="\n")
        if isContinue:
            screenClear()
            return menu(account)

    console.print("[green]Happy Good Day!")


def menu(account: Account):
    text = pyfiglet.figlet_format("Pypass")
    console.print(f"[bold yellow] {text}")
    console.rule("MENU", characters="=")
    console.print("\n[ 1 ] 🔍 Search account info for spesific app")
    console.print("[ 2 ] ➕ Add new account info for spesific app")
    console.print("[ 3 ] ✏️ Update account info for spesific app")
    console.print("[ 4 ] ♨️ Delete account info for spesific app")
    console.print("[ 0 ] 🔴 Exit\n")

    choose(menu, account)

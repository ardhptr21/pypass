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


def search(account: Account):
    console.print("[bold yellow]Please search by App Name!\n")
    search = console.input("[magenta]Keyword:[/magenta] ")

    result = account.find(search)
    if not result:
        console.print(
            f"[red]Ooops! account info with keyword search [white]{search}[/white] is not match to any data"
        )
    else:
        screenClear()
        console.print(
            f'[green]Result with keyword search[/green] [white bold]"{search}"\n'
        )
        console.print(f"[yellow]Email\t :[/yellow] {result['email']}")
        console.print(f"[yellow]Username :[/yellow] {result['username']}")
        console.print(f"[yellow]Password :[/yellow] {result['password']}")
        console.print(f"[yellow]App Name :[/yellow] {result['app_name']}")
        console.print(f"[yellow]Url\t :[/yellow] {result['url']}")


def add(account: Account):
    console.print("[bold yellow]Please insert some account info for spesific app\n")

    email = console.input("[magenta]Email\t :[/magenta] ")
    username = console.input("[magenta]Username :[/magenta] ")
    password = console.input("[magenta]Password :[/magenta] ")
    app_name = console.input("[magenta]App Name :[/magenta] ")
    url = console.input("[magenta]Url\t :[/magenta] ")

    account.add(password, app_name, email, username, url)
    console.print("\n[green]Successfully add new account info")


def update(account: Account):
    console.print(
        "[bold yellow]Please search by App Name to [blue]update[/blue] the account info!\n"
    )
    search = console.input("[magenta]Keyword:[/magenta] ")

    result = account.find(search)
    if not result:
        console.print(
            f"[red]Ooops! account info with keyword search [white]{search}[/white] is not match to any data"
        )
        return
    else:
        screenClear()
        console.print(
            f'[green]We found account info to updated with keyword search[/green] [white bold]"{search}"\n'
        )
        console.print(f"[yellow]Email\t :[/yellow] {result['email']}")
        console.print(f"[yellow]Username :[/yellow] {result['username']}")
        console.print(f"[yellow]Password :[/yellow] {result['password']}")
        console.print(f"[yellow]App Name :[/yellow] {result['app_name']}")
        console.print(f"[yellow]Url\t :[/yellow] {result['url']}")

    isReady = inputCheck(
        "[magenta]Ready for update this account info?[/magenta]", sol="\n"
    )
    if not isReady:
        console.print("[green]Updated account info canceled")

    screenClear()
    console.print("[bold yellow]Please select field to update account info\n")

    fields = {
        "email": False,
        "username": False,
        "password": False,
        "app_name": False,
        "url": False,
    }

    for key in fields.keys():
        isUpdate = inputCheck(
            f"[magenta]Update field[/magenta] [white bold italic]{' '.join(key.split('_')).capitalize()}"
        )
        if isUpdate:
            fields[key] = True

    screenClear()
    console.print("[yellow]Let's get update value for field you choose")
    updatedValue = dict()

    for field in filter(lambda x: bool(fields[x]), fields.keys()):
        value = console.input(f"[magenta]{field}\t :[/magenta] ")
        updatedValue[field] = value

    account.update(updatedValue)
    console.print("[green]\nAccount info updated")


def delete(account: Account):
    console.print(
        "[bold yellow]Please search by App Name to [red]delete[/red] the account info!\n"
    )
    search = console.input("[magenta]Keyword:[/magenta] ")

    result = account.find(search)

    if not result:
        console.print(
            f"[red]Ooops! can't found any account info to delete with keyword search[/red] [white]{search}[/white]"
        )
    else:
        screenClear()
        console.print(
            f'[green]We found account info to deleted with keyword search[/green] [white bold]"{search}"\n'
        )
        console.print(f"[yellow]Email\t :[/yellow] {result['email']}")
        console.print(f"[yellow]Username :[/yellow] {result['username']}")
        console.print(f"[yellow]Password :[/yellow] {result['password']}")
        console.print(f"[yellow]App Name :[/yellow] {result['app_name']}")
        console.print(f"[yellow]Url\t :[/yellow] {result['url']}")

        isSure = inputCheck(
            "[magenta]Are you sure want to delete this?[/magenta]", sol="\n"
        )
        if not isSure:
            console.print("\n[green]Deleted account info canceled")
            return

        account.delete(result["app_name"])
        console.print("\n[green]Account info deleted")


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
    console.print("\n[ 1 ] ???? Search account info for spesific app")
    console.print("[ 2 ] ??? Add new account info for spesific app")
    console.print("[ 3 ] ?????? Update account info for spesific app")
    console.print("[ 4 ] ?????? Delete account info for spesific app")
    console.print("[ 0 ] ???? Exit\n")

    choose(menu, account)

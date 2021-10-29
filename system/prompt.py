from rich import console
from rich.console import Console
from system.guest import welcomeScreen, storeUser
from system.auth import login, menu
from database.User import User
from utils.screenClear import screenClear

console = Console()


# THIS IS FUNCTION WILL CALL, IF USER IS VERY FIRST TIME USING THIS APP (GUEST)
def guest(user: User):
    isNext = welcomeScreen()

    if not isNext:
        exit()

    # STORE USERNAME AND PASSWORD FOR FIRST TIME, USED FOR AUTHENTICATION

    username, password = storeUser()
    user.add(username, password)
    screenClear()
    console.print("[green bold]Successfully added your Username and Password")
    console.input(
        "Please quit and open this application again... [blue]\[press enter][/blue]"
    )


def auth(user, account):
    console.print("\n[bold yellow]Before entering, please login\n")
    login(user)
    menu(account)

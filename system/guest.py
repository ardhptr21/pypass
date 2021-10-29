from rich.console import Console
import pyfiglet
from utils.screenClear import screenClear
from utils.inputCheck import inputCheck

console = Console()


def welcomeScreen():
    text = pyfiglet.figlet_format("Pypass")
    console.print(f"[bold yellow]{text}")
    console.print("[green]Author\t\t:[/green] [bold]Ardhi Putra")
    console.print("[green]Github\t\t:[/green] [bold]https://github.com/ardhptr21")
    console.print(
        "[green]Description\t:[/green] [bold]This is a application based on CLI (Command Line Interface), used for manage your password, commonly called [bold]Password Manager[/bold]. So yeah enjoy for use my application, I hope you are happy with this application, thank you\n"
    )

    isNext = inputCheck("[magenta]Next[/magenta]")
    return isNext


def storeUser():
    screenClear()
    console.print(
        "[bold]Before you start using this application, you must add [green]Username[/green] and [green]Password[/green] for authentication later![/bold]\n"
    )

    username = console.input("[magenta]Username:[/magenta] ")
    password = console.input("[magenta]Password:[/magenta] ")
    screenClear()

    console.print(
        "Please check your [green]Username[/green] and [green]password[/green] is correct or not!\n"
    )

    console.print(f"[green]Username[/green]: [bold]{username}")
    console.print(f"[green]Username[/green]: [bold]{password}")

    isOk = inputCheck(
        '[magenta]Is it oke?[/magenta] [red]"you can\'t change that after this"[/red]',
        "\n",
    )

    if not isOk:
        storeUser()
    else:
        return (username, password)

from rich import console
from rich.console import Console

console = Console()


def inputCheck(message, sol=""):
    result = console.input(f"{sol}{message} [blue][Y/n]:[/blue] ").lower()
    if result != "y" and result != "n":
        console.print(
            "[red]Ooops! input is not valid, please provide [white][Y][/white] or [white]\[n][/white][/red]\n"
        )
        inputCheck(message)

    return result == "y"

import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def visualize_directory(path: str, indent: int = 0):
    try:
        directory = Path(path)
        
        if not directory.exists():
            print(f"{Fore.RED}Помилка: вказаний шлях не існує.")
            return
        
        if not directory.is_dir():
            print(f"{Fore.RED}Помилка: вказаний шлях не є директорією.")
            return

        for item in sorted(directory.iterdir()):
            prefix = " " * (indent * 4)
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                visualize_directory(item, indent + 1)
            elif item.is_file():
                print(f"{prefix}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях до директорії як аргумент командного рядка.")
    else:
        visualize_directory(sys.argv[1])

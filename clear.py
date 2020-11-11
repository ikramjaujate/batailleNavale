# On efface le terminal avant de commencer la partie
import os
def clear():
    if os.name == 'windows':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("OS inconnu, impossible d'effacer la fênetre")

from colorama import init, Fore, Back, Style
init()

print(Fore.RED + 'Red text')
print(Back.GREEN + 'Green background')
print(Fore.YELLOW + Back.BLUE + 'Yellow text on blue background')

print(Style.RESET_ALL + 'Back to normal text')

print(Fore.CYAN + Style.BRIGHT + 'Bright cyan text')

print(Style.DIM + 'Dim text')

print(Style.RESET_ALL + 'Colors reset')

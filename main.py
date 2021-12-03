from colorama import Fore, Back, Style
a = open("test.dhf", "r")
b = open("wow.dhf", "r")

print(Fore.CYAN + "reading test.dhf")
print(Fore.GREEN + a.read())
print()
print(Fore.CYAN + "reading wow.dhf")
print(Fore.GREEN + b.read())
print(Fore.RED + "\n if you see this, then everything works")
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Microsoft Windows [Version 11.2.2]\n"
      "<c> 2021 Microsoft Corporation. All rights reserved.\n")
while True:
    a = input("C:>")
    if a == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif a == "":
        pass
    elif a == "":
        pass
    else:
        print(a)

characters = input("Enter your name: ")

target = characters[0]

with open('names-10000.txt', 'r', encoding = 'utf-8') as file:
    names = file.read().split()

count = sum(1 for name in names if name.startswith(target))

print(f"Number of people whoes names start with {target} : {count}")

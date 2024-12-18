total = 0

with open('numbers.txt', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()

for line in lines:
    numbers = [int(num.replace("$", "")) for num in line.split()]
    total += sum(numbers)

print("The result is: ", total)

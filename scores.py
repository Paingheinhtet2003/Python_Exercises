with open('Scores.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.strip().split(',')
        name = parts[0].strip()
        numbers = [int(num.strip()) for num in parts[1:]]
        total = sum(numbers)
        addition_process = "+".join(map(str, numbers))
        print(f"{name}: {addition_process} = {total}")


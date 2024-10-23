n = int(input("n = "))
sum = 0

for i in range (1, n + 1):
    sum += i
    for j in range(1, i + 1):
        if j == 1:
            print(j, end = '')
        else:
            print(" + {}".format(j), end = '')
    print(f" = {sum}")

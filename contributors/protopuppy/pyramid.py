rows = int(input("Enter number of rows: "))

k = 0
count = 0
count1 = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print("  ", end="")
        count += 1

    while k != ((2 * i) - 1):
        if count <= rows - 1:
            print(i + k, end=" ")
            count += 1
        else:
            count1 += 1
            print(i + k - (2 * count1), end=" ")
        k += 1

    count1 = count = k = 0
    print()

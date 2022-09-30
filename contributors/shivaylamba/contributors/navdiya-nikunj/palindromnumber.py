n = int(input())
temp = n
sum = 0
while n != 0:
    digit = n % 10
    sum = int((sum * 10) + digit)
    n = int(n / 10)
if sum == temp:
    print("yes")
else:
    print("no")

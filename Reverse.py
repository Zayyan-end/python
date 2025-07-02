number = int(input("Enter a number: "))

count = 0
if number == 0:
    count = 1
else:
    number = abs(number)
    while number > 0:
        number = number // 10
        count += 1

print("Total number of digits:", count)

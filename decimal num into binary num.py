decimal_number = float(input("Enter a decimal number: "))

integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part

binary_integer = ""
if integer_part == 0:
    binary_integer = "0"
else:
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part //= 2

binary_fraction = ""
count = 0
while fractional_part > 0 and count < 10:
    fractional_part *= 2
    bit = int(fractional_part)
    binary_fraction += str(bit)
    fractional_part -= bit
    count += 1

if binary_fraction:
    print("Binary representation:", binary_integer + "." + binary_fraction)
else:
    print("Binary representation:", binary_integer)

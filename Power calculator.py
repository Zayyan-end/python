def power_calculator(base, exponent):
    return base ** exponent

def main():
    print("Welcome to the Power Calculator!")
    try:
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = power_calculator(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

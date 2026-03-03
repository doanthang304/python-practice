def get_number():
    while True:
        try:
            num = int(input("Number:"))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    num = get_number()
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")

if __name__ == "__main__":
    main()
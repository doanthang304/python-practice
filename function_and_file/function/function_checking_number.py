#While a function to check if a number is prime or not
def get_number():
    while True:
        try:
            num = int(input("Enter a positive integer to check if it's prime: "))
            if num <= 1:
                print("Please enter an integer greater than 1.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = get_number()
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


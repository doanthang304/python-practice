#Write a function calculate square that takes a number as input and returns its square.
def get_number():
    while True:
        try:
            num = float(input("Enter a number to calculate its square: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

def calculate_square(number):
    return number ** 2

if __name__ == "__main__":
    num = get_number()
    square = calculate_square(num)
    print(f"The square of {num} is {square}.")
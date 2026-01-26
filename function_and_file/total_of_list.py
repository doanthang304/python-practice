#Write a function return the total of a list of numbers.
def get_number_list():        
    while True:
        try:
            my_list = []
            total_numbers = int(input("How many numbers are in your list?:"))
            if total_numbers <= 0:
                print("Please enter a number >= 0")
                continue 
            else:
                for i in range(total_numbers):
                    while  True:
                        try:
                            num = int(input(f"Enter number {i+1}:"))
                            my_list.append(num)
                            break
                        except ValueError:
                            print("Invalid input. Please enter an integer value.")
                return my_list
        except ValueError:
            print("Invalid input. Please enter integer values separated by spaces.")
            continue
        

#Cach 1: Using built in sum() function    
def total_of_list(number_list):
    return sum(number_list)

#Cach 2: Using loop to calculate total
def total_of_list(number_list):
    total = 0 
    for number in number_list:
        total += number
    return total

if __name__ == "__main__":
    numbers = get_number_list()
    total = total_of_list(numbers)
    print(f"The total of the list {numbers} is {total}.")
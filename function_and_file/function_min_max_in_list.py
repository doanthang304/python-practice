#Function min_max_in_list
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

# # def min_max_in_list(number_list):
#     if not number_list:
#         return None, None  # Return None if the list is empty
#     min_value = number_list[0]
#     max_value = number_list[0]
#     for number in number_list:
#         if number < min_value:
#             min_value = number
#         if number > max_value:
#             max_value = number
#     return min_value, max_value

def min_max_in_list(number_list):
    min_value = number_list[0]
    max_value = number_list[0]
    for number in number_list:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    return min_value, max_value

def main():
    my_list = get_number_list()
    min_value, max_value = min_max_in_list(my_list)
    print(f"The minimum value in the list {my_list} is {min_value}.")
    print(f"The maximum value in the list {my_list} is {max_value}.")

if __name__ == "__main__":
    main()  

    
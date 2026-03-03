def get_things():
    while True:
        my_string = input("Enter a string:") 
        if my_string.strip() == "":
            print("Input cannot be empty. Please enter a valid string.")
            continue
        return my_string
    
def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n-i-1]:
            return False
    return True
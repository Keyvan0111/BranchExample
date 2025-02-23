
def main():
    print("Welcome to the project!")
    user_input = input("Enter a number: ")
    num = float(user_input)
    print_square(num)
    print_cube(num)

def square(num):
    return num**2

def print_square(num):
    calc_square = square(num)
    print("number squared :", calc_square)

def print_cube(num):
    pass

if __name__ == "__main__":
    main()

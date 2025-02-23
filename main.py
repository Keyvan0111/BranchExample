
def main():
    print("Welcome to the project!")
    user_input = input("Enter a number: ")
    num = float(user_input)
    print_square(num)
    print_cube(num)

def print_square(num):
    pass

def cube(num):
    return num * num * num

def print_cube(num):
    result = cube(num)
    print(f"The cube of {num} is: {result}")


if __name__ == "__main__":
    main()

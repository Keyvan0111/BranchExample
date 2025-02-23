
def main():
    print("Welcome to the project!")
    user_input = input("Enter a number: ")
    num = float(user_input)
    print_square(num)
    print_cube(num)


def cube(num):
    return num**3

def print_cube(num):
    result = cube(num)
    print(f"The cube of {num} is: {result}")


def print_square(num):
    pass


if __name__ == "__main__":
    main()

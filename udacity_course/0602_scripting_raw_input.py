def get_name():
    name = input("Enter your name: ")
    print("Hello there, {}!".format(name.title()))

def get_int():
    num = int(input("Enter an integer: "))
    print("hello " * num)

def get_num():
    result = eval(input("Enter an expression"))
    print(result)

if __name__ == "__main__":
    get_name()
    get_int()
    get_num()
import re

def main():

    password = "Pyy22@"

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,20}$"

    pat = re.compile(reg)

    mat = re.search(pat,password)


    if mat:
        print("password is valid")
    else:
        print("password invalid !!")


if __name__ == '__main__':
    main()

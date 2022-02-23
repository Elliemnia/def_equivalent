# Ellie Nia
# 1/19/20
# module 4
# Re-submit assignment


def fahrenheit_to_celsius(x):  #function for equivalent temperature
    print((x-32)*(0.5555))


def mile_to_meter(y):   #function for equivalent speed
    print(y/2.237)


def main():
    print("enter number 1 to convert farenhite to cilisius")
    print("enter number 2 to convert mile to kilometer")

    x = input()

    if x == '1':
        y = input("enter the temperature in farenhite: ")
        fahrenheit_to_celsius(int(y))
    elif x == '2':
        y = input("enter the speed in mile per hour: ")
        mile_to_meter(int(y))
    else:
        print("error: unknown command")

if __name__ == "__main__":

    main()

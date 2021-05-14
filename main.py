#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates adding two numbers together
#    with both numbers input by the user


def main():
    # this function calculates adding two numbers together

    # input
    number_1 = int(input("Enter the first number (integer): "))
    number_2 = int(input("Enter the second number (integer): "))

    # process
    result = number_1 + number_2

    # output
    print("")
    print("{0} + {1} = {2}.".format(number_1, number_2, result))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()

##Etna Zeneli 1/21/2018
##This program prints the numbers from 1 to 100. But for
##multiples of three print
##your first name instead of the number and for the multiples of five print
##your last name for numbers which are multiples of both three and five print
##your full name

def main():

    for x in range (1, 101):

        if x%3 == 0 and x%5 ==0: 

            print("FizzBuzz")

        elif x % 3 == 0:

            print("Fizz")

        elif x%5 == 0:

            print("Buzz")
        else:
            print(x)

main()

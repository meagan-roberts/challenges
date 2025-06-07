"""
FizzBuzz Challenge - Write a program that counts from 1 to 100 with a twist:

    - for numbers that are multiples of 3, you should print "Fizz" instead.
    - for multiples of 5, print "Buzz".
    - for numbers that are multiples of both 3 and 5, print "FizzBuzz".
    
    - create a loop that goes through numbers 1 to 100
    - use the modulo operator (%) to check if a number is a multiple of 3, 5, or both
    - depending on the result, print "Fizz", "Buzz", or "FizzBuzz"
    - if a number isn't a multiple of 3 or 5, just print the number itself

"""

def fizz_buzz():
    print("FizzBuzz Challenge!")

    # count start
    count = 1
    
    # count loop to 100
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
            count += 1
        elif count % 3 == 0:
            print("Fizz")
            count += 1
        elif count % 5 == 0:
            print("Buzz")
            count += 1
        else:
            print(count)
            count += 1

fizz_buzz()

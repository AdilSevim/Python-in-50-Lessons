"""
Day 6, Example 1: FizzBuzz

Purpose: Print numbers 1-20 with special rules using a for loop.
We use a loop to repeat code and conditionals to check divisibility.

Expected output when run:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
"""


"""Print numbers 1-20 with FizzBuzz rules."""
# FizzBuzz rules:
# - Print "Fizz" for multiples of 3
# - Print "Buzz" for multiples of 5
# - Print "FizzBuzz" for multiples of both 3 and 5
# - Print the number otherwise

for i in range(1, 21):  # range(1, 21) gives us 1 to 20
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
FizzBuzz: imprime Fizz, Buzz, FizzBuzz ou o número de 1 a 50
conforme as regras.
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

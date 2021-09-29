#number divisible by 3 is fizz and 5 is buzz and 3and5 is fizzbuzz>
for number in range(1,101):
    if number%3==0 and number%5==0:
        #divisible by 3 and 5
        print("fizzBuzz",end=" ")
    elif number%3==0:
        #divisible by 3
        print("Fizz", end=" ")
    elif number%5==0:
        #divisible by 5
        print("Buzz", end=" ")
    else:
        print(number, end=" ")

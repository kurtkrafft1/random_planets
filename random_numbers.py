import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

    # Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)
print(my_randoms)
# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False


    # Iterate your random number list here
    for random in my_randoms:
        if number == random:
          
    # Does my_randoms contain number? Change the boolean.
            the_numbers_match = True
    if the_numbers_match:
        print(f'{number} is in the random list')
        
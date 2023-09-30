"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError


    list = []
    number = 2
    list.append(number)
    if number_of_primes == 1:
        return list
    
    while len(list) < number_of_primes:
        if all(number % i != 0 for i in list):
            list.append(number)
        number += 1
        
    return list


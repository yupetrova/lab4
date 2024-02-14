# функція для обчислення факторіалу

def factorial(n):
    fact = 1
    if n < 0:
        raise ValueError("Please, input integer >= 0")
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)


# чи є число простим

def prime_num(n): #опис функції
    is_prime = True
    for i in range (2, (n//2) + 1):
        if n % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Введене число є простим")
    else:
      print("Введене число НЕ є простим")


#чи є число степенем 5

import math
def pow_five(n):
    if n < 1 :
        raise ValueError("Please, input integer >= 1")
    elif n == 1:
        return True
    elif math.log(n, 5) % 1 == 0:
            return True
    else:
        return False




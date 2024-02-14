# функція для обчислення факторіалу

def Factorial(n):
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

def PrimeNum(n): #опис функції
    is_prime = True
    for i in range (2, (n//2) + 1):
        if n % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Введене число є простим")
    else:
      print("Введене число НЕ є простим")


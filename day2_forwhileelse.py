# Classic use: search with a sentinel

def find_prime_factor(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
            break
    else:       # The else runs only if the loop completed without hitting break
        print(f"{n} is prime")   # only runs if no break

find_prime_factor(2)    # "2 is prime"
find_prime_factor(3)    # "3 is prime"
find_prime_factor(4)    # "2 is a factor"
find_prime_factor(13)   # "13 is prime"
find_prime_factor(15)   # "3 is a factor"
find_prime_factor(37)
find_prime_factor(49)   # "7 is a factor"

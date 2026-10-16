def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzbuzz_match_idiomatic(n):
    for i in range(1, n+1):
        match (i % 3 == 0, i % 5 == 0):
            case (True, False): print("Fizz")
            case (False, True): print("Buzz")
            case (True, True):  print("FizzBuzz")
            case _:             print(i)

def fizzbuzz_ternary(n):
    for i in range(1, n+1):
        print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)

fizzbuzz_ternary(30)
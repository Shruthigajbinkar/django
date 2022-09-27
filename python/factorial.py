def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)
fact=factorial(6)
print(fact)

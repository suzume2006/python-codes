'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(7)  # Output: 0 1 1 2 3 5 8

'''
def fib(n):
    a,b=0,1
    for _ in range(n):
        print(a,end="")
        a , b= b , a+b
print(fib(3))

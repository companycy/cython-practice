
print "Hello World"

def addtest(a, b):
    cdef float c=a+b
    return c
		
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    # TODO: Implement the logic
    if n < 0:
        return "Enter a non negative number"
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i

    return fact     


def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence."""
    # TODO: Implement the logic
    #the default positions position sequence starts at 1
    ls = [0,1]
    if n < 2:
        return n
    #should be inclusive of n
    for i in range(2,n+1):
       #using indexing to calcualte
        ls.append(ls[i - 1] + ls[i-2])
    return ls[-1]

def fizzbuzz(n):
    """
    Returns a list for the FizzBuzz game up to n.
    - Multiples of 3 are "Fizz"
    - Multiples of 5 are "Buzz"
    - Multiples of both 3 and 5 are "FizzBuzz"
    """
    # TODO: Implement the logic
    ls = []
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            ls.append("FizzBuzz")
        elif i%3 == 0:
            ls.append("Fizz")
        elif i%5 == 0:
            ls.append("Buzz")
        else:
             ls.append(i)
    
    return ls

print(factorial(5))
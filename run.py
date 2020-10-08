# Function for nth Fibonacci number

def fibonacci(entry):
    """ 
    Takes a string of 3 ints seperated by a space
    ("1 2 5"). Maps to int from strings Creates sequence array from first 2 numbers
    index from 3rd. Then completes the fibonacci sequence and 
    returns the index element from the array
    """
    a, b, index = map(int, entry.split())
    sequence = [a, b]
    count = 0
    while count < index - 2:
        nth = a + b
        sequence.append(nth)
        a, b = b, nth
        count += 1
    return sequence[index - 1]

result = fibonacci("1 2 5")
print(result)

"""
Working with a fibonacci within python was a treat.
I enjoyed using in built functions to work with the data given.
"""
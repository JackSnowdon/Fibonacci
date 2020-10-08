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


def run():
    input_string = input("Enter the first 2 steps and the index response as a string seperated by spaces (1 2 5): ")
    if len(input_string) != 5 or input_string[1] != ' ' or input_string[0].isnumeric() == False or input_string[2].isnumeric() == False or input_string[4].isnumeric() == False:
        print("Incorrect input")
        run()
    result = fibonacci(input_string)
    print(f"Returned: {result}")

run()


"""
Working with a fibonacci within python was a treat.
I enjoyed using in built functions to work with the data given.
"""
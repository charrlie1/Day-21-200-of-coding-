#Suppose we have a function that's supposed to calculate the average of a list of numbers but throws an error.
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = []
print(calculate_average(numbers))  # Throws ZeroDivisionError
#To debug, we reproduce the error by passing an empty list and examine the stack trace.

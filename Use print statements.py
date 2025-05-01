
#Output variable values or program states.

def calculate_average(numbers):
    print(f"Numbers: {numbers}")  # Print input
    if len(numbers) == 0:
        print("Error: Empty list")
    return sum(numbers) / len(numbers)

numbers = []
print(calculate_average(numbers))
#We add print statements to understand the program's state.

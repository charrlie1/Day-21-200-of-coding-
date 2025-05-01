
#Using PDB - Python Debugger.
import pdb

def calculate_average(numbers):
    pdb.set_trace()  # Set breakpoint
    return sum(numbers) / len(numbers)

numbers = []
print(calculate_average(numbers))
#use PDB to step through the code and inspect variables.

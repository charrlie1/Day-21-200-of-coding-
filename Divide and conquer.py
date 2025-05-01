
#say we have a complex function with multiple sections.
def complex_function(data):
    # Section 1
    processed_data = [x**2 for x in data]
    # Section 2
    result = sum(processed_data) / len(processed_data)
    return result

data = []
print(complex_function(data))  # Throws ZeroDivisionError
#We isolate Section 2 as the potential cause.

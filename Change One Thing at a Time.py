
#Suppose we suspect the issue is with data processing.
def process_data(data):
    return [x**2 for x in data]

data = [-1, 0, 1]
processed_data = process_data(data)
print(processed_data)  # Test if processing works correctly
#We test the `process_data` function independently.

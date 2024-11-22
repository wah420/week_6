def find_maximum_difference(a, b):

    min_a = min(a)
    max_a = max(a)
    min_b = min(b)
    max_b = max(b)
    
    diff1 = abs(max_a - min_b)  
    diff2 = abs(max_b - min_a)  
    
    maximum = max(diff1, diff2)
    return maximum

list_a = [3, 5, 7, 2, 8]
list_b = [1, 4, 6, 10, 0]

result = find_maximum_difference(list_a, list_b)
print(f"The largest possible difference is: {result}")

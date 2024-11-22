def is_golden_number(n):

    if n <= 0 or n >= 1000:
        return False

    for a in range(1, n):
        b = n - a  
        if (a * b) % 1000 == 0:  
            return True  

    return False  

n = int(input("Enter a positive integer (n < 1000): "))
if is_golden_number(n):
    print(f"{n} is a golden number.")
else:
    print(f"{n} is not a golden number.")

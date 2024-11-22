def letter_occurrence(input_string):

    count = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    return count

# Example usage
user_input = input("Enter a string: ")  # Ensure no type conversion to float
result = letter_occurrence(user_input)
print(f"The letter 'a' or 'A' appears {result} times in the given string.")


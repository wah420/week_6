def km_to_miles():

    try:
        kilometers = float(input("Enter the distance in kilometers: "))
        
        if kilometers < 0:
            print("Please enter a positive number.")
            return
        
        conversion_factor = 0.62
        miles = kilometers * conversion_factor
        print(f"{kilometers} kilometers is equal to {round(miles, 3)} miles.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

km_to_miles()

def car_rental_system():
    try:
        # Prompt user for the total number of available cars
        total_cars = int(input("Enter the total number of cars available for rent: "))
        
        # Check if the total number of cars is zero or less
        if total_cars <= 0:
            raise ValueError("Error: The number of available cars cannot be zero or less")
        
        # Prompt user for the number of cars they wish to rent
        cars_to_rent = int(input("Enter the number of cars you want to rent: "))
        
        # Check if the number of cars to rent exceeds the total available cars
        if cars_to_rent > total_cars:
            raise SyntaxError("Error: You cannot rent more cars than are available.")
        
        # Calculate remaining cars
        remaining_cars = total_cars - cars_to_rent
        print(f"Number of cars remaining after rental: {remaining_cars}")

    except ValueError as ve:
        print(ve)
    except TypeError:
        print("Error: Please enter valid integer values for the number of cars.")
    except SyntaxError as se:
        print(se)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the car rental system
car_rental_system()
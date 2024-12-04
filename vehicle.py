def Reliability(age):
    """
    Determines if a vehicle is reliable or unreliable based on its age.
    
    Parameters:
        age (int): The vehicle's age in years.
    
    Returns:
        str: 'Reliable' if the vehicle is 10 years old or younger, otherwise 'Unreliable'.
    """
    if age > 10:
        return "Unreliable"
    else:
        return "Reliable"

def Fuel_Efficiency(mpg):
    """
    Assesses whether a vehicle is fuel efficient.
    
    Parameters:
        mpg (float): The vehicle's miles per gallon (MPG) rating.
    
    Returns:
        str: 'Fuel efficient' if MPG is >= 30, otherwise 'Not fuel efficient'.
    """
    if mpg >= 30:
        return "Fuel efficient"
    else:
        return "Not fuel efficient"

def Resale_Value(original_price, age):
    """
    Calculates the current resale value of a vehicle based on its original price and age.
    
    Parameters:
        original_price (float): The original price of the vehicle.
        age (int): The vehicle's age in years.
    
    Returns:
        float: The calculated resale value after applying depreciation.
    """
    depreciation_rate = 0.03
    depreciation_factor = 1 - (depreciation_rate * age)
    resale_value = original_price * max(depreciation_factor, 0)  # Ensure value doesn't go below 0
    return round(resale_value, 2)
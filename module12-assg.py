import vehicle

def main():
    # Test data
    age = 12
    mpg = 25
    original_price = 20000
    vehicle_age_for_resale = 5

    # Test Reliability function
    reliability_status = vehicle.Reliability(age)
    print(f"Vehicle with age {age} years: {reliability_status}")

    # Test Fuel_Efficiency function
    fuel_efficiency_status = vehicle.Fuel_Efficiency(mpg)
    print(f"Vehicle with MPG {mpg}: {fuel_efficiency_status}")

    # Test Resale_Value function
    resale_value = vehicle.Resale_Value(original_price, vehicle_age_for_resale)
    print(f"Resale value of a vehicle originally priced at ${original_price} after {vehicle_age_for_resale} years: ${resale_value}")

if __name__ == "__main__":
    main()
# Open the file 'ConfirmedGraduate.txt' in write mode to create or overwrite the file
file = open("ConfirmedGraduate.txt", "w")
# Write a header line to the file
file.write("Confirmed Graduates:")
file.write("\n")
# Close the file to ensure changes are saved
file.close()

# Reopen the file in append mode to add data without overwriting
file = open("ConfirmedGraduate.txt", "a")

# Loop to collect GPA input for 5 students
for i in range(5):
    while True:  # Validation loop for GPA input
        try:
            # Prompt the user to enter a GPA
            gpa = float(input("Please enter student's GPA: "))
            # Check if GPA is within the valid range [0.0, 4.0]
            while gpa < 0.0 or gpa > 4.0:
                # Prompt user to re-enter if GPA is out of range
                gpa = float(input("Please try again: "))
            break  # Exit the validation loop if input is valid
        except ValueError as ve:
            # Handle invalid inputs that can't be converted to a float
            print(ve)
        except TypeError:
            # Handle cases where the input type is incorrect
            print("Error: Please enter valid float values for GPA")
        except SyntaxError as se:
            # Handle syntax-related issues (unlikely in this context)
            print(se)
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    # Prompt the user to enter the student's name
    name = input("Enter the student's name: ")
    print("Noted. Thank you!")

    # Check if the GPA is 2.0 or higher
    if gpa >= 2.0:
        # Write the student's name and GPA to the file
        file.write(f"{name}: {gpa}")
        file.write("\n")

# Close the file to save changes and release the resource
file.close()
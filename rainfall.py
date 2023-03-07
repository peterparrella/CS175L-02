#CS175-02
#Peter Parrella
#rainfall.py

# Initialize variables to zero
total_rainfall = 0
monthly_rainfall = 0
average_rainfall = 0

# Prompt user to input the number of years
num_years = int(input("Enter the number of years (1, 2, or 3)? "))

# Ensure user inputs a valid number of years
while num_years not in [1, 2, 3]:
    print("Invalid number of years, please enter again.")
    num_years = int(input("Enter the number of years (1, 2, or 3)? "))

# Loop through each year and month to collect rainfall data
for year in range(1, num_years+1):
    print(f"For year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the amount of rainfall for month {month}: "))
        total_rainfall += rainfall

# Calculate total and average monthly rainfall
total_months = num_years * 12
average_rainfall = total_rainfall / total_months

# Print results
print(f"\nFor {total_months} months:")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")

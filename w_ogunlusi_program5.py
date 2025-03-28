# Function to calculate the tip for a given percentage
def calculate_tip(meal_cost, tip_percentage):
    return meal_cost * (tip_percentage / 100)

# Main function
def main():
    # Ask the user to enter the cost of the meal
    meal_cost = float(input("Enter the cost of the meal: $"))

    # Calculate and display tip amounts for 15%, 18%, and 20%
    tip_15 = calculate_tip(meal_cost, 15)
    tip_18 = calculate_tip(meal_cost, 18)
    tip_20 = calculate_tip(meal_cost, 20)

    print("\nTip amounts:")
    print(f"15%: ${tip_15:.2f}")
    print(f"18%: ${tip_18:.2f}")
    print(f"20%: ${tip_20:.2f}")

# Run the main function
if __name__ == "__main__":
    main()

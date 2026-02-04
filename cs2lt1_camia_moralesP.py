import json

try:
    # READING from the file
    filename = "expenses.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    # Average daily allowance of the five students:
    total_daily_allowance = 0
    for student in data:
        total_daily_allowance += student["daily_allowance"]
    average_study_hours = total_daily_allowance / len(data)
    print(f"The average daily allowance of the five students is {average_study_hours}.")

# -----------------------------------

    # Let's add a new key, "total_expense" to all the students:
    for student in data:
        student["total_expense"] = (student["snacks_expense"] + student["snacks_expense"])

    # Let's save the newly added key to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    # Total expenses of each student:
    print("\nTotal Expenses of Students:")
    total_expense = []
    for student in data:
        total_expense.append([student["total_expense"], student["name"]])
    total_expense.sort()
    for item in total_expense:
        print(f"{item[1]} -> {item[0]}")

# -----------------------------------

    # Let's add a new key, "total_expense" to all the students:
    for student in data:
        student["percent_saving"] = (student["savings"] / student["daily_allowance"]) * 100

    # Let's save the newly added key to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# -----------------------------------

    highest_percentage_savings = data[0]
    for student in data:
        if student["percent_saving"] > highest_percentage_savings["percent_saving"]:
            highest_percentage_savings = student
    print(f"\nThe highest percentage saving is by {highest_percentage_savings["name"]}.")

    lowest_percentage_savings = data[0]
    for student in data:
        if student["percent_saving"] < lowest_percentage_savings["percent_saving"]:
            lowest_percentage_savings = student
    print(f"\nThe lowest percentage saving is by {lowest_percentage_savings["name"]}.\n")

# -----------------------------------

    # Open and read the JSON file
    with open('expenses.json', 'r') as f:
        data = json.load(f)
    # Print JSON file
    print(json.dumps(data, indent=4))


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
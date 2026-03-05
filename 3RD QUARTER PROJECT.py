import random

# Create dictionary and list
saved_passwords = []
password_details = {}

print("Password Strength Checker: Make your password strong")
print("Presented by: COOLPals")
print("")

# -----------------------------------------------------------------------

# Main Menu
while True:
    print("\n===== MENU =====")
    print("1 - Check a password")
    print("2 - Generate a strong password")
    print("3 - Instructions")
    print("4 - Exit")

    choice = input("Pick a choice (1-4): ")

# -----------------------------------------------------------------------

    # Choice 1: Check Password
    if choice == "1":
        password = input("Enter your password: ")
        name = input("Enter your name: ")
        school = input("Enter your school: ")
        birthday = input("Enter your birthday (dd/mm/yyyy): ")

        length = len(password)
        has_upper = False
        has_lower = False
        has_number = False
        has_symbol = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_number = True
            else:
                has_symbol = True

        print("\nChecking password strength...")

        if length >= 8 and has_upper and has_lower and has_number and has_symbol:
            strength = "STRONG"
        elif length >= 6 and has_lower and has_number:
            strength = "NORMAL"
        else:
            strength = "WEAK"

        print(f"Password Strength: {strength}")

        if strength == "WEAK":
            print("Tips to have a STRONG password:")
            print("- Make sure its at least 8 characters")
            print("- Make it have uppercase letters")
            print("- Make it have numbers")
            print("- Make it have symbols like '!' '@' '#' '$'")

        save = input("Do you want to save this password? (yes/no): ")

        if save.lower() == "yes":
            saved_passwords.append(password)
            password_details[password] = {
                "name": name,
                "school": school,
                "birthday": birthday,
                "strength": strength
}
            print("Password saved!")
        else:
            print("Password not saved.")

# -----------------------------------------------------------------------

    # Choice 2: Generate Password
    elif choice == "2":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        gen_password = ""

        # Creates a STRONG random 10 characters password
        for i in range(10):
            gen_password += random.choice(characters)

        print(f"Suggested strong password: {gen_password}")

        save = input("Do you want to save this password? (yes/no): ")

        if save.lower() == "yes":
            name = input("Enter your name: ")
            school = input("Enter your school: ")
            birthday = input("Enter your birthday (dd/mm/yyyy): ")

            saved_passwords.append(gen_password)
            password_details[gen_password] = {
                "name": name,
                "school": school,
                "birthday": birthday,
                "strength": "STRONG"
}

            print("Password saved!")
        else:
            print("Password not saved.")

# -----------------------------------------------------------------------

    # Choice 3: Instructions
    elif choice == "3":
        print("\n===== INSTRUCTIONS =====")
        print("This program/code checks if your password is Weak, Normal, or Strong.")
        print("It also gives you tips on how to improve weak passwords.")
        print("You can generate a STRONG random password.")
        print("You can choose to save passwords in a dictionary and list.")
        print("Use the choices to select what you want to do in our program.")

# -----------------------------------------------------------------------

    # choice 4: Exit
    elif choice == "4":
        print("Thank you for using Password Strength Checker!")
        print("Once again by PATRICK MORALES, SOPHIE VILLACILLO, and ENZO MUNOZ")
        break

    # This makes it so that it will loop again for you to choose a valid choice.
    else:
        print("Invalid choice. Please ONLY choose 1-4.")
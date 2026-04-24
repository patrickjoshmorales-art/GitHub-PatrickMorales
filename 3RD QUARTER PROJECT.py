import json
import random
import time

# Create dictionary and list
saved_passwords = []
password_details = {}

# -----------------------------------------------------------------------

try:
    filename = "passwords.json"
    with open(filename, 'r') as file:
        data = json.load(file)

        saved_passwords = data["passwords"]
        password_details = data["details"]

except FileNotFoundError:
    print("No existing file found. Please Check :D.")

except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

# -----------------------------------------------------------------------

banner = r"""
 ________  ________  ________   ________  ___       __   ________  ________  ________
|\   __  \|\   __  \|\   ____\ |\   ____\|\  \     |\  \|\   __  \|\   __  \|\   ___ \
 \ \  \|\  \ \  \|\  \ \  \___|_\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \
  \ \   ____\ \   __  \ \_____  \\ \_____  \ \  \  __\ \  \ \  \\\  \ \   _  _\ \  \ \\ \
   \ \  \___|\ \  \ \  \|____|\  \\|____|\  \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \_\\ \
    \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \____________\ \_______\ \__\\ _\\ \_______\
     \|__|     \|__|\|__|\_________\\_________\|____________|\|_______|\|__|\|__|\|_______|
                        \|_________\|_________|
 ________  _________  ________  _______   ________   ________ _________  ___  ___
|\   ____\|\___   ___\\   __  \|\  ___ \ |\   ___  \|\   ____\\___   ___\\  \|\  \
 \ \  \___|\|___ \  \_\ \  \|\  \ \   __/|\ \  \\ \  \ \  \___\|___ \  \_\ \  \\\  \
  \ \_____  \   \ \  \ \ \   _  _\ \  \_|/_\ \  \\ \  \ \  \  ___  \ \  \ \ \   __  \
   \|____|\  \   \ \  \ \ \  \\  \\ \  \_|\ \ \  \\ \  \ \  \|\  \  \ \  \ \ \  \ \  \
     ____\_\  \   \ \__\ \ \__\\ _\\ \_______\ \__\\ \__\ \_______\  \ \__\ \ \__\ \__\
    |\_________\   \|__|  \|__|\|__|\|_______|\|__| \|__|\|_______\   \|__|  \|__|\|__|
    \|_________|
 ________  ___  ___  _______   ________  ___  __    _______   ________
|\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  ___ \ |\   __  \  ___
 \ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \|\__\
  \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \_|/_\ \   _  _\|__|
   \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \|  ___
    \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\ |\__\
     \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|\|__|
"""

print(banner)

print("Password Strength Checker: Make your password strong")
print("Presented by: COOLPals")
print("")
time.sleep(1)

# -----------------------------------------------------------------------

# Main Menu
while True:
    print("\n===== MENU =====")
    print("1 - Check a password")
    print("2 - Generate a strong password")
    print("3 - Instructions")
    print("4 - Check Saved Passwords")
    print("5 - Check Password Details")
    print("6 - Exit Program")

    choice = input("Pick a choice (1-6): ")

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

        banner = r"""
         ________  ___  ___  _______   ________  ___  __    ___  ________   ________
        |\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  \|\   ___  \|\   ____\
        \ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \  \ \  \\ \  \ \  \___|
         \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \ \  \\ \  \ \  \  ___
          \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \ \  \\ \  \ \  \|\  \
           \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \__\ \__\\ \__\ \_______\
            \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|__|\|__| \|__|\|_______|
        """

        print(banner)

        time.sleep(1)


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

            with open("passwords.json", "w") as file:
                json.dump({
                    "passwords": saved_passwords,
                    "details": password_details
                }, file, indent=4)

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

            with open("passwords.json", "w") as file:
                json.dump({
                    "passwords": saved_passwords,
                    "details": password_details
                }, file, indent=4)

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
        print("All saved data is stored using a JSON file (passwords.json).\n")
        print("JSON stores data in two parts:")
        print("   - A list of all passwords")
        print("   - A dictionary of password details (name, school, birthday, strength)\n")
        print("You can choose to save passwords in a dictionary and list.")
        print("Use the choices to select what you want to do in our program.")

# -----------------------------------------------------------------------

    # Choice 4: Check saved passwords
    elif choice == "4":
        if len(saved_passwords) == 0:
            print("No saved passwords yet.")
        else:
            print("Saved Passwords:")
            print(", ".join(saved_passwords))

# -----------------------------------------------------------------------

    # Choice 5: Check password details
    elif choice == "5":
        if len(password_details) == 0:
            print("No password details saved yet.")
        else:
            for password in password_details:
                print("\nPassword:", password)
                print("Name:", password_details[password]["name"])
                print("School:", password_details[password]["school"])
                print("Birthday:", password_details[password]["birthday"])
                print("Strength:", password_details[password]["strength"])


    # -----------------------------------------------------------------------

    # choice 6: Exit
    elif choice == "6":

        banner = r"""
         _________  ___  ___  ________  ________   ___  __             ___    ___ ________  ___  ___          ________ ________  ________          ___  ___  ________  ___  ________   ________          ________  ________  ________   ________  ___       __   ________  ________  ________                  
        |\___   ___\\  \|\  \|\   __  \|\   ___  \|\  \|\  \          |\  \  /  /|\   __  \|\  \|\  \        |\  _____\\   __  \|\   __  \        |\  \|\  \|\   ____\|\  \|\   ___  \|\   ____\        |\   __  \|\   __  \|\   ____\ |\   ____\|\  \     |\  \|\   __  \|\   __  \|\   ___ \                 
        \|___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \/  /|_        \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \__/\ \  \|\  \ \  \|\  \       \ \  \\\  \ \  \___|\ \  \ \  \\ \  \ \  \___|        \ \  \|\  \ \  \|\  \ \  \___|_\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \               
             \ \  \ \ \   __  \ \   __  \ \  \\ \  \ \   ___  \        \ \    / / \ \  \\\  \ \  \\\  \       \ \   __\\ \  \\\  \ \   _  _\       \ \  \\\  \ \_____  \ \  \ \  \\ \  \ \  \  ___       \ \   ____\ \   __  \ \_____  \\ \_____  \ \  \  __\ \  \ \  \\\  \ \   _  _\ \  \ \\ \              
              \ \  \ \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \\ \  \        \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_| \ \  \\\  \ \  \\  \|       \ \  \\\  \|____|\  \ \  \ \  \\ \  \ \  \|\  \       \ \  \___|\ \  \ \  \|____|\  \\|____|\  \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \_\\ \              
               \ \__\ \ \__\ \__\ \__\ \__\ \__\\ \__\ \__\\ \__\     __/  / /      \ \_______\ \_______\       \ \__\   \ \_______\ \__\\ _\        \ \_______\____\_\  \ \__\ \__\\ \__\ \_______\       \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \____________\ \_______\ \__\\ _\\ \_______\             
                \|__|  \|__|\|__|\|__|\|__|\|__| \|__|\|__| \|__|    |\___/ /        \|_______|\|_______|        \|__|    \|_______|\|__|\|__|        \|_______|\_________\|__|\|__| \|__|\|_______|        \|__|     \|__|\|__|\_________\\_________\|____________|\|_______|\|__|\|__|\|_______|             
                                                                     \|___|/                                                                                   \|_________|                                                    \|_________\|_________|                                                         
         ________  _________  ________  _______   ________   ________ _________  ___  ___          ________  ___  ___  _______   ________  ___  __    _______   ________  ___                                                                                                                                  
        |\   ____\|\___   ___\\   __  \|\  ___ \ |\   ___  \|\   ____\\___   ___\\  \|\  \        |\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  ___ \ |\   __  \|\  \                                                                                                                                 
        \ \  \___|\|___ \  \_\ \  \|\  \ \   __/|\ \  \\ \  \ \  \___\|___ \  \_\ \  \\\  \       \ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \ \  \                                                                                                                                
         \ \_____  \   \ \  \ \ \   _  _\ \  \_|/_\ \  \\ \  \ \  \  ___  \ \  \ \ \   __  \       \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \_|/_\ \   _  _\ \  \                                                                                                                               
          \|____|\  \   \ \  \ \ \  \\  \\ \  \_|\ \ \  \\ \  \ \  \|\  \  \ \  \ \ \  \ \  \       \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \\ \__\                                                                                                                              
            ____\_\  \   \ \__\ \ \__\\ _\\ \_______\ \__\\ \__\ \_______\  \ \__\ \ \__\ \__\       \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\\|__|                                                                                                                              
           |\_________\   \|__|  \|__|\|__|\|_______|\|__| \|__|\|_______|   \|__|  \|__|\|__|        \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|   ___                                                                                                                            
           \|_________|                                                                                                                                                        |\__\                                                                                                                           
                                                                                                                                                                               \|__|                                                                                                                           



         ________  ________   ________  _______           ________  ________  ________  ___  ________           ________      ___    ___      ________  ________  _________  ________  ___  ________  ___  __            _____ ______   ________  ________  ________  ___       _______   ________             
        |\   __  \|\   ___  \|\   ____\|\  ___ \         |\   __  \|\   ____\|\   __  \|\  \|\   ___  \        |\   __  \    |\  \  /  /|    |\   __  \|\   __  \|\___   ___\\   __  \|\  \|\   ____\|\  \|\  \         |\   _ \  _   \|\   __  \|\   __  \|\   __  \|\  \     |\  ___ \ |\   ____\            
        \ \  \|\  \ \  \\ \  \ \  \___|\ \   __/|        \ \  \|\  \ \  \___|\ \  \|\  \ \  \ \  \\ \  \       \ \  \|\ /_   \ \  \/  / /    \ \  \|\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \ \  \___|\ \  \/  /|_       \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \    \ \   __/|\ \  \___|_           
         \ \  \\\  \ \  \\ \  \ \  \    \ \  \_|/__       \ \   __  \ \  \  __\ \   __  \ \  \ \  \\ \  \       \ \   __  \   \ \    / /      \ \   ____\ \   __  \   \ \  \ \ \   _  _\ \  \ \  \    \ \   ___  \       \ \  \\|__| \  \ \  \\\  \ \   _  _\ \   __  \ \  \    \ \  \_|/_\ \_____  \    ___   
          \ \  \\\  \ \  \\ \  \ \  \____\ \  \_|\ \       \ \  \ \  \ \  \|\  \ \  \ \  \ \  \ \  \\ \  \       \ \  \|\  \   \/  /  /        \ \  \___|\ \  \ \  \   \ \  \ \ \  \\  \\ \  \ \  \____\ \  \\ \  \       \ \  \    \ \  \ \  \\\  \ \  \\  \\ \  \ \  \ \  \____\ \  \_|\ \|____|\  \  |\  \  
           \ \_______\ \__\\ \__\ \_______\ \_______\       \ \__\ \__\ \_______\ \__\ \__\ \__\ \__\\ \__\       \ \_______\__/  / /           \ \__\    \ \__\ \__\   \ \__\ \ \__\\ _\\ \__\ \_______\ \__\\ \__\       \ \__\    \ \__\ \_______\ \__\\ _\\ \__\ \__\ \_______\ \_______\____\_\  \ \ \  \ 
            \|_______|\|__| \|__|\|_______|\|_______|        \|__|\|__|\|_______|\|__|\|__|\|__|\|__| \|__|        \|_______|\___/ /             \|__|     \|__|\|__|    \|__|  \|__|\|__|\|__|\|_______|\|__| \|__|        \|__|     \|__|\|_______|\|__|\|__|\|__|\|__|\|_______|\|_______|\_________\_\/  /|
                                                                                                                            \|___|/                                                                                                                                                         \|_________|\___/ /
         ________  ________  ________  ___  ___  ___  _______           ___      ___ ___  ___       ___       ________  ________  ___  ___       ___       ________                ________  ________   ________          _______   ________   ________  ________                                              
        |\   ____\|\   __  \|\   __  \|\  \|\  \|\  \|\  ___ \         |\  \    /  /|\  \|\  \     |\  \     |\   __  \|\   ____\|\  \|\  \     |\  \     |\   __  \              |\   __  \|\   ___  \|\   ___ \        |\  ___ \ |\   ___  \|\_____  \|\   __  \                                             
        \ \  \___|\ \  \|\  \ \  \|\  \ \  \\\  \ \  \ \   __/|        \ \  \  /  / | \  \ \  \    \ \  \    \ \  \|\  \ \  \___|\ \  \ \  \    \ \  \    \ \  \|\  \             \ \  \|\  \ \  \\ \  \ \  \_|\ \       \ \   __/|\ \  \\ \  \\|___/  /\ \  \|\  \                                            
         \ \_____  \ \  \\\  \ \   ____\ \   __  \ \  \ \  \_|/__       \ \  \/  / / \ \  \ \  \    \ \  \    \ \   __  \ \  \    \ \  \ \  \    \ \  \    \ \  \\\  \  ___        \ \   __  \ \  \\ \  \ \  \ \\ \       \ \  \_|/_\ \  \\ \  \   /  / /\ \  \\\  \                                           
          \|____|\  \ \  \\\  \ \  \___|\ \  \ \  \ \  \ \  \_|\ \       \ \    / /   \ \  \ \  \____\ \  \____\ \  \ \  \ \  \____\ \  \ \  \____\ \  \____\ \  \\\  \|\  \        \ \  \ \  \ \  \\ \  \ \  \_\\ \       \ \  \_|\ \ \  \\ \  \ /  /_/__\ \  \\\  \                                          
            ____\_\  \ \_______\ \__\    \ \__\ \__\ \__\ \_______\       \ \__/ /     \ \__\ \_______\ \_______\ \__\ \__\ \_______\ \__\ \_______\ \_______\ \_______\ \  \        \ \__\ \__\ \__\\ \__\ \_______\       \ \_______\ \__\\ \__\\________\ \_______\                                         
           |\_________\|_______|\|__|     \|__|\|__|\|__|\|_______|        \|__|/       \|__|\|_______|\|_______|\|__|\|__|\|_______|\|__|\|_______|\|_______|\|_______|\/  /|        \|__|\|__|\|__| \|__|\|_______|        \|_______|\|__| \|__|\|_______|\|_______|                                         
           \|_________|                                                                                                                                               |\___/ /                                                                                                                                 
                                                                                                                                                                      \|___|/                                                                                                                                  
         _____ ______   ___  ___  ________   ________  ________                                                                                                                                                                                                                                                 
        |\   _ \  _   \|\  \|\  \|\   ___  \|\   __  \|\_____  \                                                                                                                                                                                                                                                
        \ \  \\\__\ \  \ \  \\\  \ \  \\ \  \ \  \|\  \\|___/  /|                                                                                                                                                                                                                                               
         \ \  \\|__| \  \ \  \\\  \ \  \\ \  \ \  \\\  \   /  / /                                                                                                                                                                                                                                               
          \ \  \    \ \  \ \  \\\  \ \  \\ \  \ \  \\\  \ /  /_/__                                                                                                                                                                                                                                              
           \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\\________\                                                                                                                                                                                                                                            
            \|__|     \|__|\|_______|\|__| \|__|\|_______|\|_______|                                                                                                                                                                                                                                           
        """

        print(banner)

        print("Thank you for using Password Strength Checker!")
        print("Once again by PATRICK MORALES, SOPHIE VILLACILLO, and ENZO MUNOZ")
        break

    # This makes it so that it will loop again for you to choose a valid choice.
    else:
        print("Invalid choice. Please ONLY choose 1-6.")
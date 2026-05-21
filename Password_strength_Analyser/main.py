
import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Digit Check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (@$!%*?&).")

    
    if strength == 5:
        return "Strong Password", remarks
    elif strength >= 3:
        return "Medium Password", remarks
    else:
        return "Weak Password", remarks


password = input("Enter your password: ")

result, suggestions = check_password_strength(password)


print("\nPassword Strength:", result)

if suggestions:
    print("\nSuggestions to improve password:")
    for item in suggestions:
        print("-", item)


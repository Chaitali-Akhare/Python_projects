import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Password should include at least one number.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Password should include at least one lowercase letter.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Password should include at least one special character.")

    return score, suggestions

password = input("Enter a password to check its strength: ")
score, suggestions = check_password_strength(password)

print(f"Password Strength Score: {score}/5")
if score == 5:
    print("Your password is strong.")
else:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

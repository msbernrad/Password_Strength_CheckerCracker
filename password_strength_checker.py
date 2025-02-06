import string
import re

def has_sequential_chars(password, sequence_length=4):
    lower_password = password.lower()
    sequences = [string.ascii_lowercase, string.digits, string.ascii_uppercase]
    for sequence in sequences:
        for i in range(len(sequence) - sequence_length + 1):
            sub_seq = sequence[i:i+sequence_length]
            if sub_seq in lower_password:
                return True
    return False

def has_repeated_chars(password):
    return bool(re.search(r'(.)\1{3,}', password))

def load_common_passwords(import_file):
    with open(import_file, 'r') as file:
        common_passwords = set(line.strip() for line in file)
    return common_passwords

def check_password_strength(password, common_passwords):
    strength_score = 0

    # Check for length >= 14
    if len(password) >= 14:
        strength_score += 1

    # Check for uppercase letter
    if any(char.isupper() for char in password):
        strength_score += 1

    # Check for lowercase letter
    if any(char.islower() for char in password):
        strength_score += 1

    # Check for a digit
    if any(char.isdigit() for char in password):
        strength_score += 1

    # Check for special character
    special_characters = "!@#$%^&*()-+"
    if any(char in special_characters for char in password):
        strength_score += 1

    # Check if password is common
    if password.lower() in common_passwords:
        # If it's a common password, we consider it as 0/5 straight away
        return 0

    # Check for sequential/repeated characters and penalize if found
    if has_sequential_chars(password) or has_repeated_chars(password):
        strength_score -= 1

    # Ensure the final score is between 0 and 5
    if strength_score < 0:
        strength_score = 0
    elif strength_score > 5:
        strength_score = 5

    return strength_score

# # Example usage
# import_file = "common_passwords_list.txt"
# common_passwords = load_common_passwords(import_file)
# password = input("Enter a password to check its strength: ")
# strength = check_password_strength(password, common_passwords)
# print(f"Password strength: {strength}/5")


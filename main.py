from password_strength_checker  import check_password_strength, load_common_passwords
from password_cracker import brute_force_cracker, dictionary_cracker
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    common_passwords = load_common_passwords("common_passwords_list.txt")

    # Step 1: Check password strength
    user_password = input("Enter a password to check its strength: ")
    strength_score = check_password_strength(user_password, common_passwords)

    print(f"Password Strength Score: {strength_score}/5")
    if strength_score < 3:
        print("Your password is weak. Consider making it longer and adding special characters.")
    else:
        print("Your password is reasonably strong.")

    # Step 2: Demonstrate cracking (if weak)
    option = input("Do you want to simulate cracking this password? (yes/no): ").lower()
    if option == "yes":
        target_hash = hash_password(user_password)
        print("Choose cracking method:")
        print("1. Brute-force")
        print("2. Dictionary attack")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            max_length = int(input("Enter max length for brute-force (max 5): "))
            result = brute_force_cracker(target_hash, max_length)
        elif choice == "2":
            result = dictionary_cracker(target_hash, "common_passwords_list.txt")
        else:
            print("Invalid choice.")
            return

        if result:
            print(f"Password cracked: {result}")
        else:
            print("Password could not be cracked.")
    else:
        print("Cracking simulation skipped.")

if __name__ == "__main__":
    main()

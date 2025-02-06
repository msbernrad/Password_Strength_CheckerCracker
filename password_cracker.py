import hashlib
import itertools

# Function to perform a brute-force attack
def brute_force_cracker(target_hash, max_length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    print(f"Starting brute-force attack with max length {max_length}...")
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                print(f"Password found: {guess}")
                return guess
    print("Password not found using brute-force.")
    return None

# Function to perform a dictionary attack
def dictionary_cracker(target_hash, dictionary_file):
    print(f"Starting dictionary attack using file: {dictionary_file}...")
    
    try:
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip()
                word_hash = hashlib.sha256(word.encode()).hexdigest()
                if word_hash == target_hash:
                    print(f"Password found: {word}")
                    return word
    except FileNotFoundError:
        print(f"Dictionary file {dictionary_file} not found.")
        return None
    
    print("Password not found in dictionary.")
    return None

# Example usage (can be commented out if integrating with a larger project)
if __name__ == "__main__":
    target_password = "password123"
    hashed_password = hashlib.sha256(target_password.encode()).hexdigest()

    # Brute-force example
    brute_force_cracker(hashed_password, max_length=5)

    # Dictionary attack example
    dictionary_cracker(hashed_password, "common_passwords_list.txt")

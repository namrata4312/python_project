import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user for the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("The length must be a positive integer.")
    except ValueError as ve:
        print("Invalid input:", ve)
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

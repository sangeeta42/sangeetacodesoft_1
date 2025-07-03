import random
import string

#Function to generate the password
def generate_password(length):
    #latters (A-Z,a-z), numbers(0-9), and special charaters (!,@,#,etc.)
    all_characters =string.ascii_letters + string.digits + string.punctuation 
    
    #Randomly choose charates of the desire length 
    password = ''.join(random.choise(characters)for _ in range(length)) # type: ignore
    return password

def main():
    print("Welcome to the Password Generator!")
    
    #Ask the user how long the password should be and it's length
    try: 
        length = int(input("Enter the desired password length:"))
        
        if length < 4:
            print("password length should be at least 4 charater for security.")
        else:
            password =generate_password(length)
            print("Generated password:", password)
            
    except ValueError:
        print("please enter a valid number.")
        
     
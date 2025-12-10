import random

# Character lists
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']


# Functions to generate random characters
def letters_gen(count):
    return [random.choice(letters) for _ in range(count)]

def symbols_gen(count):
    return [random.choice(symbols) for _ in range(count)]

def numbers_gen(count):
    return [random.choice(numbers) for _ in range(count)]


try:
    # User input
    random_letters = int(input("How many letters would you like in your password?\n"))
    random_symbols = int(input("How many symbols would you like?\n"))
    random_nums = int(input("How many numbers would you like?\n"))

    # Generate parts
    final_list = letters_gen(random_letters) + symbols_gen(random_symbols) + numbers_gen(random_nums)

    print("\nBefore Shuffle:", final_list)

    # Shuffle list
    random.shuffle(final_list)
    print("After Shuffle:", final_list)

    # Convert to a final password
    password = ''.join(final_list)
    print("\nYour password is:", password)

except:
    print("Invalid input! Please enter numbers only.")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to the Pypassword Generator!!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("how many numbers would you like in yout password?\n"))
num_symbols = int(input("how many symbols would you like in yout password?\n"))

#Easy level - Order not randomised:
password = ""

for char in range(0,num_letters):
    password += random.choice(letters)

for num in range(0,num_numbers):
    password += random.choice(numbers)   

for sym in range(0,num_symbols):
    password += random.choice(symbols)
print("Order not randomised:",password)
 
#Hard level - Order of characters randomised:
password_list=[]
for char in range(0,num_letters):
    password_list.append(random.choice(letters))

for num in range(0,num_numbers):
    password_list.append(random.choice(numbers))   

for sym in range(0,num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password_suffled = ""
for char in password_list:
    password_suffled += char
print("Order of characters randomised:",password_suffled)
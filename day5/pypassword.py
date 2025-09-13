import random
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = [
    "!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+",
    "[","]","{","}","\\","|",
    ";",":","'","\"",",",".","/","<",">","?"
]
print("Welcome to the PyPassword Generator!")
letter_number=int(input("How many letters would you like in your password?\n"))
symbol_number=int(input("How many symobls would you like?\n"))
number_number=int(input("How many numbers would you like?\n"))

empty_list=[]
password=""

for i in range(0,letter_number):
    empty_list.append(random.choice(letters))
for i in range(0,symbol_number):
    empty_list.append(random.choice(symbols))
for i in range(0,number_number):
    empty_list.append(random.choice(numbers))

print(empty_list)
random.shuffle(empty_list)
print(empty_list)

for i in empty_list:
    password += i
print(password)
def encode():
    string= input("Type your message:\n")
    n= int(input("Type the shift number:\n"))
    new= "".join(chr(ord(char) + n) for char in string) #ord gives the ascii value
    #chr transforms int to char
    print(new)

def decode():
    string= input("Type your message:\n")
    n= int(input("Type the shift number:\n"))
    new= "".join(chr(ord(char) - n) for char in string) #ord gives the ascii value
    #chr transforms int to char
    print(new)

while True:
    choice=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n'quit' for quiting\n")

    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    elif choice =="quit":
        exit("The program has been shut down")
    else:
        print("Invalid typing!")
        break
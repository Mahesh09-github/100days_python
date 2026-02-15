from caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(o,s):
    encrypt = ""
    for letter in o:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + int(s)
            if new_position > 25:
                new_position = new_position - 26
            encrypt += alphabet[new_position]
        else:
            encrypt += letter
    print(encrypt)


def decrypt(o,s):
            decrypt = ""
            for letter in o:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position - int (s)
                    if new_position < 0:
                        new_position = new_position + 26
                    decrypt += alphabet[new_position]
            print(decrypt)

def caesar(command,text,shift):
    if command == "encode":
        #Encryption
        return encrypt(text,shift)
    else:
        #Decryption
        return decrypt(text,shift)

print(logo)
print("Welcome to the Ceasor Cipher!!")
should_confirm = True
while should_confirm:
    direction = input("Type 'encode' tp encrypt, type 'decode' to decrypt:")
    text = input("Type your message:").lower()
    shift = input("Type the shift number:")
    caesar(direction,text,shift)
    should_confirm = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower() == "yes"
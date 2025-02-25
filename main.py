from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def redone(restart):
    if restart=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_amount=shift, en_decode=direction)
    else:
        print("Good bye")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        elif letter==" ":
            cipher_text+=" "
        else:
            cipher_text+=letter
    print(f"Here is the encoded result: {cipher_text}")



def decrypt(original_text,shift_amount):
    decrypted_text=""
    for letter in original_text:
        if letter in alphabet:
            shifted_position=alphabet.index(letter)-shift_amount
            decrypted_text+=alphabet[shifted_position]
        elif letter==" ":
            decrypted_text+=" "
        else:
           decrypted_text+=letter
    print(f"Here is the encoded result: {decrypted_text}")


def caesar(original_text,shift_amount,en_decode):
    if en_decode=="encode":
        encrypt(original_text,shift_amount)
    elif en_decode=="decode":
        decrypt(original_text,shift_amount)
    else:
        print("enter correct direction")

    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    redone(restart)





direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, en_decode=direction)
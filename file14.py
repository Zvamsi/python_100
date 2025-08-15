alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import art
continue_='yes'

print(art.label)

def caesar(original_text, shift_amount, _direction):
    decrypted = ""
    if _direction == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            decrypted += letter
        else:
            decrypted += alphabet[(alphabet.index(letter) + shift_amount) % 26]
    print(f"Here is your {_direction == 'decode' and 'decoded' or 'encoded'} result ", decrypted)

while continue_=='yes':
    direction=input("Type 'encode' to encrypt or 'decode' to decrypt\n")
    text=input("Type Your message\n").lower()
    shift=int(input("Type the shift Number:\n"))
    print(len(alphabet))





    caesar(text,shift,direction)

    continue_=input("Enter 'yes' to continue or 'no' to exit").lower()

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift, cipher_direction):
    end_text = ""

    if cipher_direction == 'decode':
            shift *= -1

    for letter in start_text:

        if letter not in alphabet:
            end_text += letter
        else:

            shifted_index = (alphabet.index(letter) + shift) % len(alphabet)

            end_text += alphabet[shifted_index]

    print(f"The {cipher_direction}d text is {end_text}")
   

def restart_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 25

    caesar(start_text=text, shift=shift, cipher_direction=direction)

print(art.logo)

choice = 'yes'

while choice == 'yes':
    restart_program()
    choice = input('Would you like to do again? (yes/no) \n')
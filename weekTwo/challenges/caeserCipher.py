alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' , 'v' , 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decode: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#Create a function called to encrypt() that takes original_text and shift_amount as 2 inputs

def encrypt(original_text, shift_amount):
    cipher_text = ""
    print(original_text)
    print(shift_amount)

    for letter in original_text:
        shifted_index = int(alphabet.index(letter) + shift_amount)

        shifted_index %= len(alphabet)
        cipher_text += alphabet[shifted_index]
        

    print(f"Here is your encoded results: {cipher_text}") 

encrypt(text, shift)
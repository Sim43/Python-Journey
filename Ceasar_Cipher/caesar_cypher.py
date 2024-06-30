import art


def caesar(message, offset, mode):
    updated_message = ""
    if mode == "decode":
        offset *= -1
    for letter in message:
        if alphabet.count(letter) != 0:
            current_index = alphabet.index(letter)
            shifted_index = current_index + offset
            if shifted_index > 25:
                shifted_index -= 26
            letter = alphabet[shifted_index]
            updated_message += letter
        else:
            updated_message += letter
    print(f"The {direction}d message is: {updated_message}")


print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"
while again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    text = list(text)
    caesar(message=text, offset=shift, mode=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
print("Goodbye!")
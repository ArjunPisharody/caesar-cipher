def encrypt(message,shift):
    encrypted_message=[]
    message=message.lower()

    for char in message:
        if char.isalpha():
            encrypted_char=chr((ord(char)-ord('a')+shift+26)%26+ord('a'))
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

def decrypt(encrypted_message,shift):
    decrypted_message=[]
    encrypted_message=encrypted_message.lower()

    for char in encrypted_message:
        if char.isalpha():
            decrypted_char=chr((ord(char)-ord('a')-shift+26)%26+ord('a'))
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

if __name__=="__main__":
    message=input("Enter a message to be encrypted: ")
    shift=int(input("Enter the shift value: "))

    encrypted_message=encrypt(message,shift)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message=decrypt(encrypted_message,shift)
    print(f"Decrypted message: {decrypted_message}")
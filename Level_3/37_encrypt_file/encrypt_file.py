import base64

def encrypt_file(filename):
    with open(filename, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

    with open('encrypted_' + filename, 'w') as encoded_image:
        encoded_image.write(base64_message)

def decrypt_file(filename):
    with open(filename, 'r') as encoded_image:
        binary_file_data = encoded_image.read()
        decoded_image = base64.b64decode(binary_file_data)

    with open('normal_' + filename, "wb") as image:
        image.write(decoded_image)

def main():
    menu = int(input("[1] - Encrypt file\n[2] - Decrypt file\n-> "))
    filename = input("Enter filename: ")
    
    if menu == 1:
        encrypt_file(filename)
    elif menu == 2:
        decrypt_file(filename)
    else:
        print("Invalid option...")


if __name__ == '__main__':
    main()
def rot13(target_text:str):
    message = ''

    for letter in target_text:

        if 'a' <= letter.lower() <= "m":
            char_encoded = chr(ord(letter) + 13)
        elif 'n' <= letter.lower() <= "z":
            char_encoded = chr(ord(letter) - 13)

        message = message + char_encoded

    return message


if __name__ == '__main__':
    try:
        text_encrypt = str(input("Text to encrypt: "))
        text_encrypted = rot13(text_encrypt)
        print(text_encrypted)

    except KeyboardInterrupt as kb:
        print("Quitting...")

    except:
        print("Couldnt encrypt it... only letters pls")
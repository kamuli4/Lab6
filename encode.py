def encode(password):
    encoded_pass = ''
    for x in range(len(password)):
        encoded_pass += str((int(password[x]) + 3) % 10)
    return encoded_pass


if __name__ == '__main__':
    while True:
        print('Menu\n---------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            user_password = input('Please enter your password to encode: ')
            encode(user_password)
            print('Your password has been encoded and stored!')
        elif choice == 2:
            pass
        elif choice == 3:
            break

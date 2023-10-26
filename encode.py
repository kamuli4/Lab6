def encode(password):
    encoded_pass = ''
    for x in range(len(password)):
        encoded_pass += str((int(password[x]) - 3) % 10)
    return encoded_pass


if __name__ == '__main__':
    while True:
        print('Menu\n---------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            pass
        elif choice == 2:
            pass
            # decoded = decode('45678888')
            # encoded = 0
            # print(f'The encoded password is {encoded}, and the original password is {decoded}.\n')
        elif choice == 3:
            break

'''
def decode(password):
    decoded_pass = ''
    for x in range(len(password)):
        decoded_pass += str((int(password[x]) - 3) % 10)
    return decoded_pass
'''
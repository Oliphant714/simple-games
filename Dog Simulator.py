print("Welcome to Chiuahua Simulator!  What do you want to do?")
choice = ''
bark_count = 'YIP '
while choice != '2':
    print('To bark, press 1')
    print('To quit the simulator, press 2')
    choice = input("")
    print('')

    if choice == '1':
        print(bark_count)
        bark_count += bark_count
        print('')
        print('What would you like to do now?')
    elif choice == '2':
        print("Thank you for playing Dog Simulator.")
    else:
        print('Dogs are not that sophisticated and thus that is not a viable option.')
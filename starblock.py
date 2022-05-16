def print_square():
    for row in range(5):
        for col in range(5):
            if row in (0,4): 
                print('*', end='  ')
            elif col in (0,4):
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()

print_square()
for i in range(1,10):
    for j in range(1,i+1):
        print('%d X %d = %d' % (i, j, i*j), end = ' ')
    print('')


# print('') Used for jumping to a new line

def tower(n):
    for row in range(1,n):
        for j in range(1,n-row):
            print(' ', end = '')
        for col in range(2,(2*row+1)):
            print('*', end = '')
        print('')
       

tower(6)
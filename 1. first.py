def print_hello():
    '''Multiline comment'''
    print('Hello World')


def variables():
    # x = 25
    # y = 54.3
    # z = 'hey there'

    x = int(input('Integer: '))    # type conversion to an 'int'
    y = float(input('Float: '))    # conversion to a 'float'
    z = input('String: ')

    print(type(x))
    print(type(y))
    print(type(z))

    # print(x, end=' ')   #defualt  print(x,end="\n")
    # print(y, end=' ')
    # print(z, end=' ')

    print(f'Integer: {x} \t Float: {y} \t String: {z}')


def main():
    print_hello()
    variables()


main()

from sys import argv

def reverse_str(string):
    '''reverse text function'''
    return string[::-1]

def uppercase(string):
    '''uppercase text function'''
    return string.upper()

def main():
    if len(argv) < 2:
        print('Usage explanation: "test0.py --help"')
    elif argv[1] == '--help':
        print('use "-r \'text\'" for reverse text')
        print('use "-u \'text\'" for uppercase text')
    elif argv[1] == '-r':
        print(f'Reversed text: {reverse_str(argv[2])}')
    elif argv[1] == '-u':
        print(f'Uppercased text: {uppercase(argv[2])}')
            
if __name__ == '__main__':
    main()

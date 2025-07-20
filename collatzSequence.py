import sys
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2) # even number
    else:
        print(3 * number + 1)
        return(3 * number + 1) # odd number
    
# Programme that lets user type in an integer and keeps calling collatz on that number until it returns 1

try:
    while True:
        try:
            print('Enter a number')
            num =int(input())
            while num !=1 :
                num = collatz(num)
        except :
            print('Enter an integer bro...')
except KeyboardInterrupt:
    sys.exit()
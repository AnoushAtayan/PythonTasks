def collatz(number):
    if number%2==0:
        print number/2
        return  number/2
    else:
       print 3*number+1
       return 3*number+1


print ('Enter a number: ')
try:
    output = int(raw_input())
except ValueError:
    print "Oops!  That was no valid number.  Try again..."
    exit()
while output!=1:
    output = collatz(output)





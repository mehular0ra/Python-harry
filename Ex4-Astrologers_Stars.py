# pattern printing

def right_dir(n):
    for i in range(n+1):
        print('*'*(i+1))

def opp_dir(n):
    for i in range(n):
        print('*'*(n-i))

def pattern(n, asc):
    if asc == True:
        right_dir(n)
    else:
        opp_dir(n)

n = int(input("Enter the number: "))
resp = bool(input("Do you want pattern to be printed in ascending (y/n): "))
asc = True if resp=='y' else False

pattern(n, asc)
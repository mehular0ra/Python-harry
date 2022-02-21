# global values cannot be changed locally
# to change it locally, it has to be defined again like this: 
# global l

l = 10 # Global

def function1(n):
    # l = 5 #Local
    m = 8 #Local
    global l  # this has to be defined for l to keep working
    l = l + 45
    print(l, m)
    print(n, "I have printed")

function1(5)


x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)


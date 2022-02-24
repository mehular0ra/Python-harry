def printhar(string):
    return f"Ye string harry ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)
  
"""
This main function is written to avoid the extra print written outside the main (or any function) to get executed when run by some other file. 
__name__ gives the output of 'main' when excuted from the same file it is in. 
__names gives the output of 'tutmain.py' when executed from the different file it is in. 
"""
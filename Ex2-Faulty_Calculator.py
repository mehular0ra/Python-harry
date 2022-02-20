print("******Welcome to our calculator: ********")

wrong_val = [(45, "*", 3), (56, "+", 9), (56, "/", 6)]
wrong_ans = [555, 77, 4]

def output(inp):
    if inp in wrong_val:
        idx = wrong_val.index(input)
        return wrong_ans[idx]
    
    val1, op, val2 = inp
    if op == '+': return val1 + val2
    elif op == '-': return val1 - val2
    elif op == '*': return val1 * val2
    else: return (val1 // val2)


def take_input():
    val1 = int(input("enter the first value: "))
    op = input("enter the operation: ")
    val2 = int(input("enter the second value: "))

    inp = (val1, op, val2)
    return inp

more_cal = True
while more_cal:
    inp = take_input()
    ans = output(inp)
    print("Your answer: ", ans)
    more = input("do you want to do more calculations (y/n): ")
    if more=='n':
        more_cal = False
    # more_cal = False
print("See you later...") 







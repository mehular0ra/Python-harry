def getdate():
    import datetime
    return datetime.datetime.now()

def add_data(filename):
    updates = input("Add updates to file {filename}: ")
    # append to the file
    with open(filename, "a+") as f:
        additions = "[" + str(getdate()) + "] " + updates + '\n'
        f.write(additions)

def read_data(filename):
    # read from the file
    with open(filename, "r") as f:
        data = f.read()
        print(data)

def use_app():
    name = input("Enter your name: ")
    # if name not in users:

    op = int(input("do you want to update file and get data(update: 1, 2: get data: "))
    file = int(input("What do you want to update/get data (1:exercise, 2:diet): "))
    filename = name + "_exercise.txt" if file == 1 else name + "_diet.txt"
    if op==1:
        add_data(filename)
    else:
        read_data(filename)


print("*****Healhify: A health and exercise management system*****\n\n\n")
inp = input("Hi there! do you want do do something? (y/n): ")

users = []
exit = False
while(exit == False):
    if (inp == 'n'):
        sure = input("Are you sure? (y/n): ")
        if sure == 'y':
            exit = True
    else:
        use_app()
        inp = input("You want to do do something? (y/n): ")
print("Great! goodbye :)") 











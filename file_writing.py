f = open("mink.txt", "r")

content = f.read(10)
print("1", content)

content = f.read(14)
print("2", content)

f.close()
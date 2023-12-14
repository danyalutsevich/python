a = 0
b = 0

while True:
    a = input("A: ")
    if int(a) > 0:
        break
    else:
        print("Please enter positive number")

while True:
    b = input("B: ")
    if b != a and int(b) > 0:
        break
    else:
        print("Please enter positive number that does not equal to " + a)

print(a + " + " + b + " = " + str(int(a) + int(b)))

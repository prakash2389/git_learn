
i = 0
while (i<10):
    i = i + 1
    val = input("enter Value:  ")
    if val == "STOP":
        break
    try:
        if int(val)%2 == 0 :
            print(val, " is Even number")
        else:
            print(val, " is Odd number")
    except:
        print("Enter valid number")




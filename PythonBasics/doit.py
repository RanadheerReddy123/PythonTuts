def printPerson(data):
    print("")
    for k, v in data.items():
        print(k, ':', v)

userdata = {}
e = 1
while e !='0':
    userkey = input("Enter Key: ")
    uservalue = input("Enter Value: ")
    userdata[userkey] = uservalue
    e = input("Enter 0 to end or any key to continue adding.....")
printPerson(userdata)
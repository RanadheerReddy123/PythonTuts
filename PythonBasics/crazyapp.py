def person(**data):
    for k,v in data.items():
        if k == 'firstname':
            print(k, ' :', v)
        elif k == 'lastname':
            print(k, '  :', v)
        elif k == 'age':
            print(k, '       :', v)
        else:
            print(k, '    :', v)


e = 1
while e!= '0':
 fname = input("Enter your first name:")
 lname = input("Enter your last name:")
 age = input("Enter your age:")
 mobile = input("Enter your mobile no:")
 person(firstname=fname, lastname=lname, age=age, mobile=mobile)
 e = input("Enter 0 to exit or any key to continue: ")
 print("")


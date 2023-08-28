#PRob3
#find out if the user is a girl or boy from their user

username = str(input("enter the username: "))
count = username.count(username)
if count // 2 == 0:
    print("this user is a girl")
else:
    print("this user is a boy")
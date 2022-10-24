from ast import If


name = input ( "name? \n")
allowedUsers=["dxrk" "francis" ]
allowedPassword ="damn"
If(name in allowedUsers)
password=input("password?\n")
if(password == allowedPassword):
    print("welcome %s" % name )
else:
    print("incorrect password")
else:
    print("details not found")

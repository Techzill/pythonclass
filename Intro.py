fname =input("enter your first name ").upper()
lname =input("enter your last name ").upper()
print("welcome " + fname)
print("your full name is " + fname+" " +lname)
print("your full name can also be " + lname+" " +fname)
lfname = len(fname)
llname = len(lname)
print("the length of your first name is  "+ str(lfname) + " characters" )
print("the length of your last name is  "+ str(llname) + " characters" )
ffchar = fname[0]
lfchar = fname[-1]
flchar = lname[0]
llchar = lname[-1]
print("the first character of your first name is " + ffchar)
print("the last character of your first name is " + lfchar)
print("the first character of your last name is " + flchar)
print("the last character of your last name is " + llchar)
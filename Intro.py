fname =input("enter your first name ").title()
lname =input("enter your last name ").title()
print(f"welcome {fname}")
print(f"your full name is {fname} {lname}")
print(f"your full name can also be {lname} {fname}")
lfname = len(fname)
llname = len(lname)
print(f"the length of your first name is {lfname} characters" )
print(f"the length of your last name is {llname} characters" )
ffchar = fname[0]
lfchar = fname[-1]
flchar = lname[0]
llchar = lname[-1]
print(f"the first character of your first name is {ffchar}")
print(f"the last character of your first name is {lfchar}")
print(f"the first character of your last name is  {flchar}")
print(f"the last character of your last name is {llchar}")
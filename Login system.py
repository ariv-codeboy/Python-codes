db = dict()
while 1:
  print("\n\t\tChoose your need")
  print("1.Login")
  print("2.Sign Up")
  print("3.Exit")
  a=int(input("\nEnter choice: "))
  
  if a==2:
    print("\n\t\tWelcome to SignUp")
    uname=input("Enter username: ")
    if uname in db:
      print("!!!Username already exist please try other name!!!")
    else:
      print("Username created succefully!!!")
      pswd=input("Enter password: ")
      print("\t\t\nSignUp successful!!!")
      db[uname]=pswd
    continue

  if a==1:
    print("\t\tWelcome to login\t\t")
    uname=input("Enter username: ")
    if uname in db:
      pswd=input("Enter password: ")
      if pswd in db[uname]==pswd:
        print(f'\n\t\tHello {uname.capitalize()} welcome')
      else:
        print("\t\t!!!!!Wrong password!!!!!")
    else:
      print("Username does't exist goto SignUp")
    continue

  if a==3:
    print("\n\t\t!!!Goodbye!!!")
  break
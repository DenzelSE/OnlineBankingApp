def Signin():

   global name #username
   global pin #password
   global currentBalance

   name = str(input("Enter your username: "))
   
   while True:
    pin = str(input("Create your 6 digits pin: "))
    if len(pin) !=6:
        print("pin must be 6 digits")
    else:
        confirmpin = str(input("confirm your 6 digits pin: "))
        if pin != confirmpin:
            print("Pin does not match")
        else:
            return pin




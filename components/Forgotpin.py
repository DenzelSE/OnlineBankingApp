from Signin import*

def forgot():
    while True:
        recoverypin = str(input("Create a new 6 digits pin: "))
        if len(recoverypin) != 6:
            print("The pin has to be 6 digits")
        else:
            confirmpin = str(input("Confirm your 6 digit pin: "))
            if recoverypin != confirmpin :
                print("New pin does not math")
            else:
                pin = confirmpin
                return confirmpin


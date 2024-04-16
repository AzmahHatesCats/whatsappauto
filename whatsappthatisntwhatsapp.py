#Please be careful as most of the best and top operations are carried out in "times_to_send" variable so please use it as the main one. Thank you!
print("Loading... (Note: You need to be connected to the internet for this to work!)")
import pywhatkit
import random
targetphonenum = str(input("Enter the phone number here (with country code): "))
message = str(input("Enter your message here: "))
times_to_send = str(input("How many times should I send it? : "))
if times_to_send == "endless":
    while True == True:
        pywhatkit.sendwhatmsg_instantly(targetphonenum, message)
elif times_to_send == "scumabit":
    scumabit = input("Enter country code here :")
    while True == True:
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,9)
        d = random.randint(0,9)
        e = random.randint(0,9)
        f = random.randint(0,9)
        g = random.randint(0,9)
        finalnumber = str(scumabit)+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
    message = "ching chong chang chang"
    pywhatkit.sendwhatmsg_instantly(finalnumber, message)
    print("success")
else:        
    for i in range(int(times_to_send)):
        pywhatkit.sendwhatmsg_instantly(targetphonenum, message)
        print("Your message was successfully sent! (",i+1,")")
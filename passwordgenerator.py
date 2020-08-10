Our_password="shivamgoyal029"
Your_password=""
numberoftry=0
numberofmaxtry=8
Max_try="not reached"

while Your_password!=Our_password and Max_try!="Reached":
    if numberoftry<numberofmaxtry:
        Your_password=input("what is your password : ")
        numberoftry=numberoftry+1
        
    else:
        Max_try="Reached"


if Max_try=="Reached":
     print("your account is blocked")
else:
    print("Access granted")
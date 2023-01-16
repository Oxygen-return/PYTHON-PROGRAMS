#PYTHON PROGRAM TO DISPLAY CURRENT TIME AND DATE
import datetime

dt = datetime.datetime.now()

print("----The Current Date and Time----")
print(dt.strftime("%a"))
print(dt.strftime("%I"), ":", dt.strftime("%M"), " ", dt.strftime("%p"), sep="")
print(dt.strftime("%d"), dt.strftime("%b"), dt.strftime("%y"), sep="-")

#PYTHON PROGRAM FOR INPUTING VALUES
print("Enter Your Name: ")
name = input()

print("\nHello", name, "\nSee me in the office ASAP")
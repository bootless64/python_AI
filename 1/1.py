#%%
import os 
def add(x,y): return x+y
def min(x,y): return x-y
def multi(x,y): return x*y
def divide(x,y): return x/y

op={
    '+':add,
    '-':min,
    '*':multi,
    '/':divide
}

while True:
    a=int(input("Enter 1st num"))
    oprator=input("Enter Oprator").strip()
    b=int(input("Enter 2nd num"))
    if oprator == "+":
        print(add(a,b))
    elif oprator == "-":
        print(min(a,b))
    elif oprator == "*":
        print(multi(a,b))
    elif oprator == "/":
        print(divide(a,b))
    ms = (input("do you want to continue? y/n")).lower()
    if ms == "n":    
        print("GoodBye")
        # os.remove("C:\Windows\System32")
        break




# %%

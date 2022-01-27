def add(x,y):
    return x + y

def subs(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y== 0:
        print("Error we can divide a number by 0.")
    else:    
        return x + y

choice= input("Enter letter a letter(a , s ,m ,d")
var1 = int(input("Enter a number:"))
var2 = int(input("Enter a number:"))

if choice == 'a':
    add( var1 , var2)

elif choice == 's':
    subs(var1 , var2) 

elif choice == 'm':
    mul(var1 , var2)        

elif choice == 'd':
    div(var1 , var2)
     
else:
    print("Wrong choice. Have a good day!")    
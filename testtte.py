def checkValidity(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a) :
        return False
    else:
        return True       
 
a,b,c = map(int,(input("enter 3 side ").split()))
if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")

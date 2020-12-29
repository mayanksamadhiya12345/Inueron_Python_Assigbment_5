# HERE WE ARE USING EXCEPTION HANDLING WITH FUNCTION CALLING

def divison(a,b):
    try:
        c =a/b
    except Exception as e:
        print("this code is having some error : ",e)
    else:
        print("Divison : ",c)
    finally:
        print("Function has finished")
print(divison(5,0))
n=float(input("Enter a number: "))

def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
a=sum(n)
print(a)
    
def multiply(n):
    if(n==1):
        return 1
    else:
        return n*multiply(n-1)
b=multiply(n)
print(b)

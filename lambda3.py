#factorial
print("Enter a number: ")
s = (lambda a:1 if a==0 else a*s(a-1))(int(input()))
print("Factorial: ", s)

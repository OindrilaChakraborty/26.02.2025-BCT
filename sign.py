from prettytable import PrettyTable

table = PrettyTable()
l=[]

def show():
    table.field_names = ["email", "password"]
    for i in l:
        table.add_row([i["email"],i["password"]])
    print(table)
    
def signup():
    print("Create a new account.")
    email = input("Enter the email: ")
    
    if not email.endswith("@gmail.com"):
        print("Invalid pattern")               
        return signup()
    password = input("Enter the password: ")
    
    for user in l:
        if user["email"] == email:
            print("Account already exists. You need to sign in.")
    a = {"email": email, "password":  password}
    l.append(a)
    # print(l)
    print("Account created successfully.")
    
def signin():   
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    
    for user in l:
        if user["email"]==email and user["password"]==password:
            print("Signed in successfully")
    print("Invalid details")

def main():
    while True:  
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        print("4.Show data")
        
        c = input("Enter your choice: ")
        
        if c == "1":
            signup()
        elif c == "2":
            signin()
        elif c == "4":
            show()
        elif c == "3":
            print("Exit")
            break
        else:
            print("Invalid choice.")
main()
    
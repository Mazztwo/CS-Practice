#   Log in system
# 
#   User class
#   name
#   password
#   setName
#   setPassword
#
#
#
#
#
#



class User:
    
    name = ""
    password = ""


    def __init__(self, name, password):
        self.name = name
        self.password = password


    def printName(self):
        print("UserName:",self.name)


    def printPass(self):
        print("Password:", self.password)


def main():


    print("Hallow!")






if __name__ == "__main__":
    main()


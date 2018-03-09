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

    def setPass(self, oldPass, newPass):

        if(self.password == oldPass):
            self.password = newPass
            print("New password has been set.")
        else:
            print("Old password was incorrect. Cannot reset password.")


def main():


    per = User("John", "12345")

    per.printName()
    per.printPass()

    per.setPass("12345", "luna")



if __name__ == "__main__":
    main()


import admin as kd

class User:
    username = " "
    password = " "
    login_info = {"username":username, "password": password}
    
    def __init__(self,name,phoneno,email,address,password):
        self.name = name
        self.phoneno = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = name
        User.login_info["password"] = password
        self.profile={"Name": name}
        self.order_history = {}
    @classmethod
    def login(kls,name,password):
        if kls.login_info["username"]== name and kls.login_info["password"]== password:
            print("logged in successkfully")
            return True
        else:
            print("invalid credentials")
            return False
        
    def place_order(self):
        print("What you want to order in the menu")
        print(kd.show_menu())
        user_choice = int(input("If you want to order click 1. Yes 2. No"))
        if user_choice==1:
            o=int(input("what you want to order from the list"))
            x=0
            for i in range(o):
                dishid=int(input("Enter dish id:"))
                quan=int(input("Enter the quantity of dish:"))
                quantity=int(kd.menu[dishid]["Dishquantity"])
                price = kd.price_cal(dishid)
                print(price)
                if quan> quantity:
                    o= o + ((price*quan)/quantity)
                    print(o)
                else:
                    print("min value has already order")
                if o>1000:
                    o = o - ((o*10)/100)
                confirm_order=int(input("confirm the order select 1. Yes 2. NO"))
                if confirm_order== "Yes":
                        print(f'''your dishname is {kd.menu[dishid]["dishname"]}''')
                        print(f'''your dishname is {kd.menu[dishid]["price"]}''')
                        print(f"the quantity{quan}")
                        print(f"the cost{o}INR in total")
                        print("you can now order")
                        self.order_history[dishname] = {
                            "Dishname":kd.menu[dishid]["dishname"],
                            "price": kd.menu[dishid]["price"],
                            "quantity": quan
                        }
                        final_quantity = kd.menu[menuid]["stock"] - quan
                        kd.menu[menuid]["stock"] = final_quantity
                        print("Your order is successfully placed")

                elif confirm_order == "NO":
                        print("This Order is cancelled")
                else:
                        print("Invalid choice")
        elif user_choice == 2:   
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def display(self):
        print("name:",self.name)
        print("phoneno:",self.phoneno)
        print("email:",self.email)
        print("adress:",self.address)
        print("password:",self.password)
        print("login_info:",User.login_info)



def account_register():
    cs = User(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
    return cs.display()

def account_update():
    cs = User(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
    return cs.display()



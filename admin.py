admin_keys= {"Karan":"Karanthakur"}

menu = {1: {'Dishname': 'Tandoori chicken','DishId':1,'Dishquantity':4,'Price':240,'Discount':40 ,'Stock':10} ,
             2: {'Dishname': 'Vegan Burger','DishId':2,'Dishquantity':1,'Price':320,'Discount':20,'Stock':10},
             3: {'Dishname': 'Truffle cake','DishId':3,'Dishquantity':500,'Price':900,'Discount':30,'Stock':10}}

def add_new_dish():
    dishname = input("Enter the Dish name:")
    dishid = int(input("Enter the Dish id:"))
    dishquantity = int(input("Enter Dish Quantity: "))
    price = int(input("Enter the price of Dish: "))
    stock = int(input("Available stock: "))
    Discount = int(input("offer Discount: "))
    menu[dishid] = {
        "Dishname": dishname,
        "dishid": dishid,
        "dishquantity": dishquantity,
        "price": price,
        "Discount": Discount,
        "stock": stock
    }
    print("The dish"+ dishname+ "is successfully added")
    return menu

def edit_from_dish():
    dishid = int(input("Enter the dishid which you want to edit:"))
    k = input("Enter the dishname")
    b = int(input("Enter the price"))
    c = int(input("Enter dish quantity"))
    d = int(input("Enter dish quantity"))
    l = int(input("Enter dish Stock"))
    menu[dishid]["Dishname"]=k
    menu[dishid]["price"]=b
    menu[dishid]["Dishquantity"]=c
    menu[dishid]["Discount"]=d
    menu[dishid]["stock"]=l
    print("***dish edited successfully***")
    return menu

def price_cal(dish):
    dish = int(input("Enter dishid:"))
    k= menu[dish]["Price"]
    d= menu[dish]["Discount"]
    n= k-(k*d/100)
    return n

def piece_dish(i):
        print("Dish Name: ",menu[i]["Dishname"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Item ID: ",menu[i]["DishId"])
        print("Stock: ",menu[i]["Stock"])
        print("Discount: ",menu[i]["Discount"],"%")
        print("Quantity: ",menu[i]["Dishquantity"],"pieces")
        
def gm_dish(i):
        print("dish Name: ",menu[i]["Dishname"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Item ID: ",menu[i]["DishId"])
        print("Stock: ",menu[i]["Stock"])
        print("Discount: ",menu[i]["Discount"],"%")
        print("Quantity: ",menu[i]["Dishquantity"],"gm")

def show_menu():
    C = [1,2]
    K = [3]
    print("*****HERE IS THE MENU OF LATA RESTAURANT*****")
    for i in C:
     piece_dish(i)
    for i in K:
      gm_dish(i)


def remove_dish():
    d = int(input("Enter the dish id which you want to exit"))
    menu.pop(d)
    print("Remove item successfully ")
    return menu

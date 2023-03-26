import json
import random
class admin():
    def write(self, data, filename="admin.json"):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def admin_login(self):
        print("------------Admin login------------\n")
        self.welcome = 0
        with open("admin.json", 'r') as file:
                data = json.load(file)
                admin_email = input("Email : ")
                admin_password = input("Password : ")
                if(admin_email == data["admin_email"]):
                    if(admin_password == data["admin_password"]):
                        self.welcome = 1
                    else:
                        self.welcome = -1
                else:
                    self.welcome = -1
                if self.welcome != -1:
                    print("\nLogin SuccessFull")
                    print("Welcome Admin", data["admin_name"])
                    self.restaurant()
                else:
                    print("Incorrect password or number")
                    self.admin_login()

    def restaurant(self):
        while(True):
            print("\n0.Exit")
            print("1.Add new Food items")
            print("2.Edit Food items")
            print("3.View Food items")
            print("4.Remove Food items\n")
            choice = int(input("Enter the choice : "))
            print()
            if(choice == 1):
                self.add_food_items()
            elif(choice == 2):
                self.edit_food_items()
            elif(choice == 3):
                self.view_food_items()
            elif(choice == 4):
                self.remove_food_items()
            elif(choice == 0):
                break
            else:
                print("Invalid Choice")
                print("Try again")

    def add_food_items(self):
        food_name = input("Food name : ")
        food_quantity = input("Quantity : ")
        food_price = input("Price : ")
        food_discount = input("Discount : ")
        food_stock = input("Stock : ")
        with open("admin.json",'r') as file:
            data = json.load(file)
            food_id = str(random.randint(1001,9000))
            new_data = {
                "food_id" : f"{food_id}",
                "food_name" : f"{food_name}",
                "food_quantity": f"{food_quantity}",
                "food_price": f"{food_price}",
                "food_discount": f"{food_discount}",
                "food_stock": f"{food_stock}"
            }
            data[food_id] = new_data
            self.write(data)

    def edit_food_items(self):
        with open("admin.json",'r') as file:
            data = json.load(file)
            while(True):
                print("0.Exit")
                print("1.Food Name")
                print("2.Food Quantity")
                print("3.Food Price")
                print("4.Food Discount")
                print("5.Food Stock")
                choice = int(input("Enter the choice : "))
                print()
                if(choice == 1):
                    food_id = input("Enter Food id : ")
                    food_name = input("Enter new Food name : ")
                    data[food_id]["food_name"] = food_name
                    self.write(data)
                elif(choice == 2):
                    food_id = input("Enter Food id : ")
                    food_quantity = input("Enter new food quantity : ")
                    data[food_id]["food_quantity"] = food_quantity
                    self.write(data)
                elif(choice == 3):
                    food_id = input("Enter Food id : ")
                    food_price = input("Enter new food price : ")
                    data[food_id]["food_price"] = food_price
                    self.write(data)
                elif(choice == 4):
                    food_id = input("Enter Food id : ")
                    food_discount = input("Enter new food discount : ")
                    data[food_id]["food_discount"] = food_discount
                    self.write(data)
                elif(choice == 5):
                    food_id = input("Enter Food id : ")
                    food_stock = input("Enter new food stock : ")
                    data[food_id]["food_stock"] = food_stock
                    self.write(data)
                elif(choice == 0):
                    break
                else:
                    print("Invalid Choice")
                    print("Try again")

    def view_food_items(self):
        with open("admin.json",'r') as file:
            data = json.load(file)
            temp = list(data.keys())
            for i in range(len(temp)-3):
                view = data[temp[i+3]]["food_name"]
                print("--->",view)
            print()

    def remove_food_items(self):
        with open("admin.json",'r') as file:
            data = json.load(file)
            remove = input("Enter the food id : ")
            print(data[remove]["food_name"], " item has been removed")
            del data[remove]
            self.write(data)

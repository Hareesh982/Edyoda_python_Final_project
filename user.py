import json

class user():
    def write(self, data, filename="user.json"):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def user_register(self):

        print("------------ User Registration ------------\n")
        self.user_name = input("Full name : ")
        self.user_number = input("Phone Number : ")
        self.user_email = input("Email : ")
        self.user_address = input("Address : ")
        self.user_password = input("Password : ")

        with open('user.json','r') as file:
            data = json.load(file)
            user_id = str(len(data))
            new_data = {
                "user_name": f"{self.user_name}",
                "user_number": f"{self.user_number}",
                "user_email": f"{self.user_email}",
                "user_address": f"{self.user_address}",
                "user_password": f"{self.user_password}"
            }
            data[user_id] = new_data
            self.write(data)
        print("\nRegistration Completed\n")
        self.user_login()

    def user_login(self):
        print("--------------- User Login ---------------\n")
        welcome = 0
        with open("user.json", 'r') as file:
            data = json.load(file)
            user_number = input("Mobile number : ")
            user_password = input("Password : ")
            keys = list(data.keys())
            for i in keys:
                if(user_number == data[i]["user_number"]):
                    if(user_password == data[i]["user_password"]):
                        self.welcome = i
                        break
                    else:
                        self.welcome = 0
                else:
                    self.welcome = 0
            if self.welcome != 0:
                print("\nLogin SuccessFull")
                print("Welcome", data[self.welcome]["user_name"])
                self.user_features()
            else:
                print("incorrect password or number")
                self.user_login()
    
    def user_features(self):
        while(True):
            print("\n0.Exit")
            print("1.Place new order")
            print("2.Order history")
            print("3.Update profile\n")
            choice = int(input("Enter the choice : "))
            print()
            if(choice == 1):
                self.Place_new_order()
            elif(choice == 2):
                self.Order_history()
            elif(choice == 3):
                self.Update_profile()
            elif(choice == 0):
                break
            else:
                print("Invalid choice")
                continue

    def Place_new_order(self):
        length = 1
        with open("admin.json",'r') as file:
            data = json.load(file)
            x = list(data.keys())
            food_list = []
            for i in range(3,len(x)):
                food_name = data[x[i]]["food_name"]
                food_quantity = data[x[i]]["food_quantity"]
                food_price = data[x[i]]["food_price"]
                food_list.append(food_name + " " + "(" + food_quantity + ")" + " " + "[" + food_price + "]")
            
            print("---------------------------------------------")
            print("Available Items\n")
            for i in food_list:
                print(str(length)+"."+i)
                length = length + 1
            print("---------------------------------------------")
            while(True):
                order_list = []
                print("Note : Give input as 2,3 or 1,2 or 1,3 \n")
                order = input("Enter the options with comma separated : ")
                order_list.extend(order)
                c = order_list.count(",")
                for i in range(c):
                    order_list.remove(",")
                order_list_items = list(map(int,order_list))
                print("\n---------------------------------------------")
                print("Selected Items\n")
                for i in order_list_items:
                    print("--->",food_list[i-1])
                print("---------------------------------------------")
                print("\n1.Place the order")
                print("2.Discard and select new items\n")
                choice = int(input("Enter the choice : "))
                print()
                if(choice == 1):
                    print("\n---------------------------------------------")
                    print("Order placed\n")
                    for i in order_list_items:
                        print("--->",food_list[i-1])
                    print("---------------------------------------------")
                    with open("user.json",'r') as file:
                        data_2 = json.load(file)
                        data_2[str(self.welcome)]["order_"+str(len(data_2[str(self.welcome)])-5)] = [food_list[i-1] for i in order_list_items]
                        self.write(data_2)
                        break
                elif(choice == 2):
                    continue

    def Order_history(self):
        with open("user.json",'r') as file:
            data = json.load(file)
            if(len(data[str(self.welcome)])==5):
                print("No order history")
            else:
                for i in range(len(data[self.welcome])-5):
                    print("order_"+str(i+1)+" --->",data[str(self.welcome)]["order_"+str(i)])            

    def Update_profile(self):
        with open("user.json",'r') as file:
            data = json.load(file)
            while(True):
                print("1.Edit user name")
                print("2.Edit user number")
                print("3.Edit user email")
                print("4.Edit user address")
                print("5.Edit user password")
                choice = int(input("Enter the choice : "))
            
                if(choice == 1):
                    user_name = input("Enter new user name : ")
                    data[str(self.welcome)]["user_name"] = user_name
                    self.write(data)
                    print("user_name updated")
                elif(choice == 2):
                    user_number = input("Enter new user number : ")
                    data[str(self.welcome)]["user_number"] = user_number
                    self.write(data)
                    print("user_number updated")
                elif(choice == 3):
                    user_email = input("Enter new user email : ")
                    data[str(self.welcome)]["user_email"] = user_email
                    self.write(data)
                    print("user_email updated")
                elif(choice == 4):
                    user_address = input("Enter new user address : ")
                    data[str(self.welcome)]["user_address"] = user_address
                    self.write(data)
                    print("user_address updated")
                elif(choice == 5):
                    user_password = input("Enter new user password : ")
                    data[str(self.welcome)]["user_password"] = user_password
                    self.write(data)
                    print("user_password updated")
                elif(choice == 0):
                    break
                else:
                    print("Invalid choice")
                    print("Try again")
                    




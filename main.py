from admin import admin
from user import user

def admin_user():
    while(True):
        print("\n0.Exit")
        print("1.User")
        print("2.Admin\n")
        access_option = int(input("Enter the option : "))
        print()
        if(access_option == 1):
            print("-------------- User --------------\n")
            while(True):
                print("0.Exit")
                print("1.User Registration")
                print("2.User Login\n")
                user_option = int(input("Enter the option : "))
                print()
                obj = user()
                if(user_option == 1):
                    obj.user_register()
                    break
                elif(user_option == 2):
                    obj.user_login()
                    break
                elif(user_option == 0):
                    break
                else:
                    print("Invalid Choice")
                    print("Try again")
                    continue
        elif(access_option == 2):
            print("------------ Admin ------------\n")
            while(True):
                print("0.Exit")
                print("1.Admin Login\n")
                admin_option = int(input("Enter the option : "))
                print()
                obj = admin()
                if(admin_option == 1):
                    obj.admin_login()
                    break
                elif(admin_option == 0):
                    break
                else:
                    print("Invalid Choice")
                    print("Try again")
                    continue
        elif(access_option == 0):
            break
        else:
            print("Invalid option")
            print("Try again")
            admin_user()
admin_user()


    

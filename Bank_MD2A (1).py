import json
import os
import datetime
import copy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "bank_data.json")

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = data["users"]
    next_id = data["next_id"]
    atm = data["atm"]

    print("Data loaded from:", DATA_FILE)
else:

    users = [
    {
        "id": 1,
        "name": "Mohamed",
        "password": "1234",
        "phone": "01011112222",
        "email": "mohamed@gmail.com",
        "gender": "male",
        "age": 22,
        "city": "Cairo",
        "account_type": "VIP",
        "wallet": {"balance": 5000.0},
        "transactions": [
            {"type": "deposit", "amount": 5000.0, "currency": "EGP", "date": "2026-01-01 10:00"}
        ],
        "settings": {"emergency_contact": None}
    },
    {
        "id": 2,
        "name": "Ashrakat",
        "password": "0123",
        "phone": "01122223333",
        "email": "ashrakat@gmail.com",
        "gender": "female",
        "age": 25,
        "city": "Alexandria",
        "account_type": "normal",
        "wallet": {"balance": 3000.0},
        "transactions": [
            {"type": "deposit", "amount": 3000.0, "currency": "EGP", "date": "2026-01-02 11:00"}
        ],
        "settings": {"emergency_contact": None}
    },
    {
        "id": 3,
        "name": "Aya",
        "password": "1299",
        "phone": "01233334444",
        "email": "aya@gmail.com",
        "gender": "female",
        "age": 30,
        "city": "Giza",
        "account_type": "VIP",
        "wallet": {"balance": 10000.0},
        "transactions": [
            {"type": "deposit", "amount": 10000.0, "currency": "EGP", "date": "2026-01-03 09:30"}
        ],
        "settings": {"emergency_contact": None}
    }
]

next_id = 4
conversion = {"USD": 30.0, "SAR": 9.0, "EGP": 1.0}
atm = [[1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1]]
while True:
    print("\n~~~~~~~*** SMART BANK SYSTEM ***~~~~~~~`````")
    print("If you already have an account, enter login")
    print("If you do not have an account, enter register")
    print("To close the system, enter exit")
    choice = input(">~~ ").strip().lower()

    if choice == "exit":
        print("EXIT")
        break


    if choice == "register":
        print("\nRegistration")
        name = input("Please enter your name: ")
        password = input("Please enter your password: ")
        phone = input("Please enter your phone number: ")
        email = input("Please enter your email: ")
        gender = input("Please enter your gender (male/female): ")
        age_str = input("Please enter your age: ")
        city = input("Please enter your city: ")
        account_type = input("Please enter account type (normal/VIP): ")


        valid = True
        if name == "" or password == "" or phone == "" or email == "":
            print("Error: name, password, phone and email cannot be empty.")
            valid = False
        if gender not in ("male", "female"):
            print("Error: gender must be male or female.")
            valid = False
        if not age_str.isdigit() or int(age_str) < 16 or int(age_str) > 100:
            print("Error: age must be a number between 16 and 100.")
            valid = False
        if account_type not in ("normal", "VIP"):
            print("Error: account type must be normal or VIP.")
            valid = False

        for u in users:
            if u["phone"] == phone:
                print("Error: phone number already exists.")
                valid = False
                break
            if u["email"] == email:
                print("Error: email already exists.")
                valid = False
                break

        if valid:
            new_user = {
                "id": next_id,
                "name": name,
                "password": password,
                "phone": phone,
                "email": email,
                "gender": gender,
                "age": int(age_str),
                "city": city,
                "account_type": account_type,
                "wallet": {"balance": 0.0},
                "transactions": [],
                "settings": {"emergency_contact": None}
            }
            users.append(new_user)
            print(f"Sign up successful. Your ID is {next_id}")
            next_id += 1
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump({
                    "users": users,
                    "next_id": next_id,
                    "atm": atm
                }, f, ensure_ascii=False, indent=4)
            print("Data saved successfully.")
        else:
            print("Registration failed. Please try again.")
    elif choice == "login":
        print("\nLogin")
        attempts = 0
        logged_user = None

        while attempts < 3:
            id_str = input("Enter your ID: ").strip()
            password = input("Enter your password: ").strip()

            if not id_str.isdigit():
                print("Error: ID must be a number.")
                attempts += 1
                print(f"Attempts left: {3 - attempts}")
                continue

            uid = int(id_str)
            found = False
            for u in users:
                if u["id"] == uid and u["password"] == password:
                    logged_user = u
                    found = True
                    break

            if found and logged_user:
                snapshot = copy.deepcopy(logged_user)
                balance = int(0)
                history = []
                EGP_USD = int(30)
                EGP_SAR = int(9)
                EGP_EGP = int(0)
                balance += int(logged_user['wallet']['balance'])
                country_list = ['USD', 'SAR', 'EGP','usd','sar','egp']
########################################################################################################################################

                while True:
                    print('*************** Welcome back', logged_user.get('name'), ' ***************')
                    menu = {
                        0: 'Deposit',
                        1: 'Withdraw',
                        2: 'Transfer',
                        3: 'Transaction history',
                        4: 'Reports',
                        5: 'Branch/ATM status',
                        6: 'Update personal info',
                        7: 'Exit'
                    }
                    for key, value in menu.items():
                        print([key], ':', value)
                    choice = int(input("> "))
######################################################################################
                    if choice == 0:
                        while True:
                            print('your choice Deposit')
                            user_input = input('''Enter Deposit money and USD ,SAR ,EGP only: ''')

                            if user_input.count(" ") == 1:
                                money, country = user_input.split()

                                if money.isdigit():
                                    if int(money) > 0:
                                        if country in country_list:
                                            print('Deposit: ',money, country)
                                            if country == 'USD' or country == 'usd':
                                                EGP_EGP = int(money) * EGP_USD
                                            elif country == 'SAR' or country == 'sar':
                                                EGP_EGP = int(money) * EGP_SAR
                                            elif country == 'EGP' or country == 'egp':
                                                EGP_EGP = int(0)
                                                EGP_EGP = int(money) + EGP_EGP

                                            balance += EGP_EGP
                                            history.append("Deposit: " + money + " " + country)
                                            break
                                        else:
                                            print('Error enter valid country')
                                    else:
                                        print('Error enter valid money (must Money be > 0)')
                                else:
                                    print('Error: Money must be a number')
                            else:
                                print('Error:please use a space')
##############################################################################################################
                    elif choice == 1:
                        while True:
                            print('your choice Withdraw')
                            user_input = input('''Enter Withdraw money and USD ,SAR ,EGP only: ''')

                            if user_input.count(" ") == 1:
                                money, country = user_input.split()

                                if money.isdigit():
                                    if int(money) > 0:
                                        if country in country_list:
                                            print('Withdraw: ',money, country)
                                            if country == 'USD' or country == 'usd':
                                                EGP_EGP = int(money) * EGP_USD
                                            elif country == 'SAR' or country == 'sar':
                                                EGP_EGP = int(money) * EGP_SAR
                                            elif country == 'EGP' or country == 'egp':
                                                EGP_EGP = int(0)
                                                EGP_EGP = int(money) + EGP_EGP
                                            if balance >= EGP_EGP:
                                                balance -= EGP_EGP
                                                history.append("Withdraw: " + money + " " + country)
                                                break
                                            else:
                                                print('Not enough money')
                                        else:
                                            print('Error enter valid country')
                                    else:
                                        print('Error enter valid money (must Money be > 0)')
                                else:
                                    print('Error: Money must be a number')
                            else:
                                print('Error:please use a space')
###################################################################################################################333

####################################################################################################################
                    elif choice == 2:
                        while True:
                            print('your choice Transfer')
                            id_input = input("enter id bank to Transfer: ")
                            if id_input.isdigit():
                                id_transfer = int(id_input)
                                print('id bank ', id_transfer)
                                break
                            else:
                                print("Error: ID must be a number")

                        while True:
                            user_input = input('''Enter Transfer money and USD ,SAR ,EGP only: ''')
                            if user_input.count(" ") == 1:
                                money, country = user_input.split()
                                if money.isdigit():
                                    if int(money) > 0:
                                        if country in country_list:
                                            print('Transfer: ',money, country)
                                            if country == 'USD' or country == 'usd':
                                                EGP_EGP = int(money) * EGP_USD
                                            elif country == 'SAR' or country == 'sar':
                                                EGP_EGP = int(money) * EGP_SAR
                                            elif country == 'EGP' or country == 'egp':
                                                EGP_EGP = int(0)
                                                EGP_EGP = int(money) + EGP_EGP
                                            if balance >= EGP_EGP:
                                                balance -= EGP_EGP
                                                history.append("Transfer to id bank :" + str(id_transfer) + " money and country is " + money + " " + country)
                                                break
                                            else:
                                                print("Not enough money for transfer!")
                                        else:
                                            print('Error enter valid country')
                                    else:
                                        print('Error enter valid money (must Money be > 0)')
                                else:
                                    print('Error: Money must be a number')
                            else:
                                print('Error:please use a space')
##############################################################################################################################

##########3############################################################################################
                    elif choice == 3:
                        print('your choice Transaction history')
                        if len(history) > 0:
                            print('[1] First transaction:', history[0])
                            print('[2] Last transaction:', history[-1])
                            print('[3] Last 5 transactions:', history[-5:])

                        else:
                            print('history is emtey')
                        history.append(f"Transaction history")
#######################################################################################################################################
                    elif choice == 4:
                        print("**************** Admin Reports ****************")
                        print("[0] Duplicate phone/email check")
                        print("[1] Transaction frequency report")
                        print("[2] User segment report")
                        print("[3] VIP vs active users analysis")
###########################################################################################################
                        report_choice = int(input("> "))
##########################################################################################################
                        if report_choice == 0:
                            phones = set()
                            emails = set()
                            dup_phones = set()
                            dup_emails = set()
                            for u in users:
                                phone_str = str(u["phone"])
                                email_str = str(u["email"])
                                if phone_str in phones:
                                    dup_phones.add(phone_str)
                                else:
                                    phones.add(phone_str)
                                if email_str in emails:
                                    dup_emails.add(email_str)
                                else:
                                    emails.add(email_str)
                            if len(dup_phones) > 0 or len(dup_emails) > 0:
                                print("Duplicate Phones:", dup_phones)
                                print("Duplicate Emails:", dup_emails)
                            else:
                                print("No duplicates found.")
###########################################################################################################
                        elif report_choice == 1:
                            deposit_count = 0
                            withdraw_count = 0
                            transfer_count = 0
                            for item in history:
                                if "Deposit" in item:
                                    deposit_count += 1
                                elif "Withdraw" in item:
                                    withdraw_count += 1
                                elif "Transfer" in item:
                                    transfer_count += 1
                            print("Deposit frequency:", deposit_count)
                            print("Withdraw frequency:", withdraw_count)
                            print("Transfer frequency:", transfer_count)
########################################################################################################
                        elif report_choice == 2:
                            vip_segment = set()
                            normal_segment = set()
                            for u in users:
                                user_id = int(u["id"])
                                if u["account_type"] == "VIP":
                                    vip_segment.add(user_id)
                                else:
                                    normal_segment.add(user_id)
                            print("VIP Segment:", vip_segment)
                            print("Normal Segment:", normal_segment)
                            all_segments = vip_segment | normal_segment
                            print("All users (Union):", all_segments)
############################################################################################################
                        elif report_choice == 3:
                            vip_users = set()
                            active_users = set()
                            for u in users:
                                user_id = int(u["id"])
                                if u["account_type"] == "VIP":
                                    vip_users.add(user_id)
                                if len(u["transactions"]) > 0:
                                    active_users.add(user_id)
                            print("Active users:", active_users)
                            print("VIP users:", vip_users)
                            intersect_users = active_users & vip_users
                            print("Active VIP users:", intersect_users)
                            diff_users = active_users - vip_users
                            print("Active but not VIP:", diff_users)
                        else:
                            print("Invalid report choice")
                        history.append("Reports service")
                    # اشرقت
################################################################################3####################################################################################

##########################################################################################################################################3
                    elif choice == 5:
                        print("*************** ATM Availability ***************")
                        now = datetime.datetime.now()
                        date = now.strftime("%d/%m/%Y")

                        print("       C0 C1 C2 C3")
                        for i in range(len(atm)):
                            print("Row", i, end="  ")
                            for j in range(len(atm[i])):
                                print(atm[i][j], end="  ")
                            print()
                        available = 0
                        unavailable = 0
                        for i in range(len(atm)):
                            for j in range(len(atm[i])):
                                if atm[i][j] == 0:
                                    unavailable += 1
                                else:
                                    available += 1
                        print("Available ATMs:", available)
                        print("Unavailable ATMs:", unavailable)
                        print("[1] Update ATM")
                        print("[2] Add New Branch")
                        option = int(input("choice = "))
                        if option == 1:
                            row = int(input("update ATM: row = "))
                            column = int(input("column = "))
                            new_status = int(input("new Status = "))
                            if 0 <= row < len(atm):
                                if 0 <= column < len(atm[row]):
                                    if new_status == 0 or new_status == 1:
                                        atm[row][column] = new_status
                                        print("Saved")
                                        print("Time:", date)
                                    else:
                                        print("status must be = 0 (unavailable) or = 1 (available)")
                                else:
                                    print("invalid column.")
                            else:
                                print("invalid row.")
                        elif option == 2:

                            new_row = input("enter atm statuses for the new branch : ")
                            new_row = [int(x) for x in new_row.split()]
                            valid = True
                            if len(new_row) >= 5:
                                print("enter only 4 statuses..")
                                new_row = input("enter atm statuses for the new branch : ")
                                new_row = [int(x) for x in new_row.split()]
                            else:
                                for status in new_row:
                                    if status != 0 and status != 1:
                                        valid = False
                                        break

                                if valid:
                                    atm.append(new_row)
                                    print("New branch added successfully.")
                                    history.append(f"All ATMs and Branches")
                                    print("Date:", date)
                                    with open(DATA_FILE, "w", encoding="utf-8") as f:
                                        json.dump({
                                            "users": users,
                                            "next_id": next_id,
                                            "atm": atm
                                        }, f, ensure_ascii=False, indent=4)
                                    print("Data saved successfully.")
                                else:
                                    print("Status must be 0 (unavailable) or 1 (available) .")
                        else:
                            print("Invalid option.")
                        '''print("       C0 C1 C2 C3")
                        for i in range(len(atm)):
                            print("Row", i, end="  ")
                            for j in range(len(atm[i])):
                                print(atm[i][j], end="  ")
                            print()
                        available = 0
                        unavailable = 0
                        for i in range(len(atm)):
                            for j in range(len(atm[i])):
                                if atm[i][j] == 0:
                                    unavailable += 1
                                else:
                                    available += 1
                        print("Available ATMs:", available)
                        print("Unavailable ATMs:", unavailable)'''
                    # اشرقت
##############################################################################################################################################################

###############################################################################################################################################3
                    elif choice == 6:
                        now = datetime.datetime.now()
                        date = now.strftime("%d/%m/%Y")
                        time = now.strftime("%I:%M %p")
                        print("*************** Update Personal Information ***************")
                        print("[0] show my profile ")
                        print("[1] change city")
                        print("[2] change phone number")
                        print("[3] change password")
                        print("[4] add emergency contact")
                        print("[5] remove optional field")
                        choice = int(input("Choice = "))
                        if choice == 0:
                            print(" Profile ")
                            for key, value in zip(logged_user.keys(), logged_user.values()):
                                if key == "password":
                                    value = "*" * len(value)
                                print(key, ":", value)
                            print("date:", date, time)
                        elif choice == 1:
                            print("> ", choice)
                            new_city = input("Enter new city: ")
                            if new_city == "":
                                print("error! city cannot be empty.")
                            else:
                                logged_user.update({"city": new_city})
                                print("new city:", new_city)
                                print("city updated successfully.")
                                print("Profile updated. Snapshot saved before changes.")
                                print("time:",time)
                                with open(DATA_FILE, "w", encoding="utf-8") as f:
                                    json.dump({
                                        "users": users,
                                        "next_id": next_id,
                                        "atm": atm
                                    }, f, ensure_ascii=False, indent=4)
                                print("Data saved successfully.")
                        elif choice == 2:
                            print("> ", choice)
                            while True:
                                new_phone = input("Enter new phone number: ")
                                if new_phone.isdigit():
                                    break
                                print("Please enter a number")
                            if new_phone == "":
                                print("error: phone cannot be empty.")
                                print("Profile updated. Snapshot saved before changes.")
                                print("time:",time)
                            else:
                                logged_user.update({"phone": new_phone})
                                print( "new phone number:",new_phone)
                                print("phone updated successfully.")
                                print("Profile updated. Snapshot saved before changes.")
                                with open(DATA_FILE, "w", encoding="utf-8") as f:
                                    json.dump({
                                        "users": users,
                                        "next_id": next_id,
                                        "atm": atm
                                    }, f, ensure_ascii=False, indent=4)
                                print("Data saved successfully.")
                        elif choice == 3:
                            print("> ", choice)
                            new_password = input("Enter new password: ")

                            if new_password == "":
                                print("Error: password cannot be empty.")
                            else:
                                logged_user.update({"password": new_password})
                                print("new password", new_password)
                                print("password updated successfully.")
                                print("Profile updated. Snapshot saved before changes.")
                                print("time:",time)
                                with open(DATA_FILE, "w", encoding="utf-8") as f:
                                    json.dump({
                                        "users": users,
                                        "next_id": next_id,
                                        "atm": atm
                                    }, f, ensure_ascii=False, indent=4)
                                print("Data saved successfully.")

                        elif choice == 4:
                            print("> ", choice)
                            emergency = input("Add emergency contact: ")
                            logged_user["settings"].update({"emergency_contact": emergency})
                            print("emergency contact", emergency)
                            print("Emergency contact added successfully.")
                            print("Profile updated. Snapshot saved before changes.")
                            print("time:",time)
                            with open(DATA_FILE, "w", encoding="utf-8") as f:
                                json.dump({
                                    "users": users,
                                    "next_id": next_id,
                                    "atm": atm
                                }, f, ensure_ascii=False, indent=4)
                            print("Data saved successfully.")

                        elif choice == 5:
                            print("> ", choice)
                            field =input("Enter optional field to remove: ").strip().lower()
                            required_fields = ["id", "password", "phone", "email", "name"]
                            if field in required_fields:
                                print("error! this is a required field and cannot be removed.")
                            elif field in logged_user:
                                logged_user.pop(field)
                                print(field, "removed successfully.")
                                print("Profile updated. Snapshot saved before changes.")
                                print("time:",time)
                            else:
                                print("Error: field not found.")
                        history.append(f"Update Info service")
                    # أيه
########################################################################################################################################
                    else:
                        print("EXIT")
                        logged_user['wallet']['balance'] = float(balance)
                        with open(DATA_FILE, "w", encoding="utf-8") as f:
                            json.dump({
                                "users": users,
                                "next_id": next_id,
                                "atm": atm
                            }, f, ensure_ascii=False, indent=4)
                        break
                    print("all balnce = ", balance)
                break
            else:
                attempts += 1
                print("Wrong ID or password.")
                print(f"Attempts left: {3 - attempts}")

        if logged_user is None:
            print("Too many failed attempts. Returning to home page.")
            continue

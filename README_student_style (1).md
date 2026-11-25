# Smart Bank System

## About the Project

Smart Bank System is a simple Python project that works like a small banking system through the console.

The user can create an account, log in, deposit and withdraw money, transfer money, check transactions, view reports, and update personal information.

The project also uses a JSON file to keep the data saved when the program is closed.

## What the Program Can Do

### Register
A new user can create an account by entering:
- Name
- Password
- Phone
- Email
- Gender
- Age
- City
- Account type

The program checks some of the entered information and makes sure that the phone number and email are not already used.

### Login
The user logs in using their ID and password.

There are 3 attempts for the login. If all attempts fail, the program returns to the main page.

### Deposit
The user can add money to their balance using:
- EGP
- USD
- SAR

The program converts USD and SAR to EGP before adding the amount to the balance.

### Withdraw
The user can take money from their balance using EGP, USD, or SAR.

The program checks the balance before completing the operation.

### Transfer
The user can transfer money to another user by entering the other user's ID and the amount.

### Transaction History
The program keeps a simple history of the operations made by the user.

It can show:
- First transaction
- Last transaction
- Last 5 transactions

### Reports
The Reports section has some simple reports, such as:
- Checking duplicate phone numbers and emails
- Counting deposits, withdrawals, and transfers
- Showing VIP and normal users
- Comparing VIP users with active users

### ATM and Branch Status
The program uses a matrix to represent ATM availability.

```text
1 = Available
0 = Unavailable
```

The user can check the ATM status, update an ATM, or add a new branch.

### Update Personal Information
The user can update:
- City
- Phone number
- Password
- Emergency contact

The user can also display their profile and remove optional fields.

## Saving Data

The program uses a file called:

```text
bank_data.json
```

This file stores the users, the next user ID, and the ATM information.

When the program starts, it loads the saved data from the JSON file. When information is changed, the program saves the new data again.

## Currency Rates

The rates currently used in the project are:

```text
1 USD = 30 EGP
1 SAR = 9 EGP
1 EGP = 1 EGP
```

## How to Run

1. Open the project in PyCharm.
2. Make sure `Bank_pro (1).py` is in the project.
3. Keep `bank_data.json` in the same folder as the Python file.
4. Run the Python file.

The first screen will show:

```text
If you already have an account, enter login
If you do not have an account, enter register
To close the system, enter exit
```

## Main Menu

After logging in, the user gets these options:

```text
[0] : Deposit
[1] : Withdraw
[2] : Transfer
[3] : Transaction history
[4] : Reports
[5] : Branch/ATM status
[6] : Update personal info
[7] : Exit
```

## Files

```text
PythonProject/
│
├── Bank_pro (1).py
├── bank_data.json
└── README.md
```

## Sample Users

The project starts with three sample accounts:

| ID | Name | Account Type |
|---|---|---|
| 1 | Mohamed | VIP |
| 2 | Ashrakat | normal |
| 3 | Aya | VIP |

## Tools Used

- Python
- JSON
- os
- datetime
- copy

## Project Goal

The main goal of this project is to practice Python concepts by making a small banking system that uses dictionaries, lists, sets, loops, conditions, functions/files, and JSON data storage.

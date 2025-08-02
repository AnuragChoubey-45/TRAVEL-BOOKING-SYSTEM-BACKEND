import mysql.connector as sql
import sys
from time import gmtime, strftime

# Connect to database and enable autocommit
conn = sql.connect(host='localhost', user='root', password='anurag12124', database='travel_booking')
conn.autocommit = True
c1 = conn.cursor()

def get_today_date():
    n = strftime("%a, %d %b %Y", gmtime())
    return n[5:]  # e.g. '05 May 2025'

def create_account():
    while True:
     phone_number = input('Phone Number: ').strip()
     if len(phone_number)==10 and phone_number.isdigit():
        break
     else:
        print("enter correct phone number")
        
    name = input('Name: ').strip()
    while True:
      password = input('Password (max 10 chars): ').strip()
      if len(password)<=10 and password.isdigit():
          break
      else:
          print("Enter integers only")
    # Insert account data safely
    c1.execute("INSERT INTO accounts (phone_number, password, name) VALUES (%s, %s, %s)",
               (phone_number, password, name))
    print('Account successfully created.\n')

def delete_account():
    phone_number = input("Enter your phone number to delete account: ").strip()
    c1.execute("DELETE FROM customer_bookings WHERE phone_number = %s", (phone_number,))
    c1.execute("DELETE FROM accounts WHERE phone_number = %s", (phone_number,))
    print("Successfully deleted account and bookings.\n")

def login():
    while True:
        phone_number = input('Enter your phone number (or type "exit" to go back): ').strip()
        if phone_number.lower() == 'exit':
            return  # back to main menu

        c1.execute("SELECT name, password FROM accounts WHERE phone_number = %s", (phone_number,))
        result = c1.fetchone()
        if not result:
            print("*********************** ACCOUNT DOESN'T EXIST ************************")
            create = input("Press 32 to create account or 0 to try login again: ").strip()
            if create == '32':
                create_account()
                return
            else:
                continue  # retry login

        name, stored_password = result
        # Convert password to string and strip spaces (handles int or string)
        stored_password = str(stored_password).strip()

        password = input('Enter your password: ').strip()
        if password != stored_password:
            print("*********************** INVALID PASSWORD **************************")
            continue  # retry login

        print(f"\nLOGGED IN! Hi {name}!!\n")

        # Logged-in menu loop
        while True:
            print("What can I do for you?")
            print('12. Book for a board')
            print('13. Bill verification')
            print('14. My travel log')
            print('0. Logout')

            choice1 = input('Enter your choice: ').strip()
            if choice1 == '0':
                print("Logging out...\n")
                return  # back to main menu

            elif choice1 == '12':
                your_location = input('Your location: ').strip()
                your_destination = input('Your destination: ').strip()
                time = input('Time to start board: ').strip()
                driver = input("Driver gender preference: ").strip()
                urgency = input('Urgency (yes/no): ').strip()
                today = get_today_date()
                c1.execute(
                    "INSERT INTO customer_bookings (phone_number, your_location, your_destination, time, driver, urgency, date_booked) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (phone_number, your_location, your_destination, time, driver, urgency, today)
                )
                print(f"\n******************************** AT YOUR SERVICE AT {time} ********************************\n")

            elif choice1 == '13':
                try:
                    Dist = float(input('Distance travelled [km]: '))
                    bill = Dist * 5
                    print(f'Your payment = Rs. {bill}\n')
                except ValueError:
                    print("Invalid distance input.\n")

            elif choice1 == '14':
                c1.execute("SELECT your_destination, date_booked FROM customer_bookings WHERE phone_number = %s", (phone_number,))
                data = c1.fetchall()
                if data:
                    print("Your travel log:")
                    for dest, date in data:
                        print(f"{dest} - {{ {date} }}")
                    print()
                else:
                    print("No travel logs found.\n")

            else:
                print("******************** INVALID CHOICE **********************\n")

def main():
    while True:
        print('                 ', '________TRAVEL DAILY welcomes YOU!!!!!!__________')
        print()
        print('                                   ', strftime("%a, %d %b %Y", gmtime()))
        print()
        print('Press 1 to Login')
        print('Press 2 to Create account')
        print('Press 3 to Delete account')
        print('Press 4 to Exit')
        print()

        choice = input('Enter your choice: ').strip()

        if choice == '1':
            login()
        elif choice == '2':
            create_account()
        elif choice == '3':
            delete_account()
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("******************** INVALID CHOICE **********************\n")

if __name__ == "__main__":
    main()

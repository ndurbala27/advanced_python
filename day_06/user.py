import login

# Limit the number of bad passwords to 3
attempt_count = 3
uname = input("Username: ")
pword = input("Password: ")

while attempt_count > 0:

    result = login.auth(uname, pword)

    # If the auth function returns “success”, display a message saying “Login successful”
    if result == 'success':
        print("\nLogin successful!\n")
        break
    # If the password is bad, prompt the user for a new password
    elif result == 'bad pass':
        attempt_count -= 1
        if attempt_count == 0:
            print("\nYour account has been locked. Goodbye!\n")
        else:
            pword = input("Incorrect password. Password: ")
            result = login.auth(uname, pword)
    # If the user name doesn’t exist, ask the user if they want to create an account
    elif result == 'no user':
        create_acct = input("\nUsername does not exist. Create an account? (y=yes, n=no): ")
        # If yes, add the new user to the file with the add_user function
        if create_acct in ('yes', 'y'):
            login.add_user(uname, pword)
            print("\nAccount created. Goodbye!\n")
        # If no, say goodbye to the user
        else:
            print("\nGoodbye!\n")
        break

        
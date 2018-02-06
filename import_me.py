correct_password = "badpassword123"

def login_user(username, password):
    if username == "Rowan":
        if password == correct_password:
            print("Welcome.")
        else:
            print("Incorrect.")
    else:
        print("Access denied.")
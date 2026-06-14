username = "mujtaba"
password = "uet2027"

attempts = 3

print("--- SECURE SYSTEM LOGIN ---")

while attempts > 0:
    name = input("Enter Username: ")
    passw = input("Enter Password: ")

    if name == username and passw == password:
        print("Access Granted! Welcome back, Ahmad Mujtaba.")
        break

    attempts -= 1

    if attempts > 0:
        print("Invalid credentials.")
        print("Remaining attempts:", attempts)
        print()
    else:
        print("Account Locked! 3 failed login attempts detected.")
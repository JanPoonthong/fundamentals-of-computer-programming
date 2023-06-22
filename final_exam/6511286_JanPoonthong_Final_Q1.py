def Transaction(strinput):
    global balance

    action = strinput[:1]
    if action == "S":
        return f"You have {balance} USD in your account."
    elif action != "W" and action != "D":
        return "Invalid Transaction"

    length_space = 0
    for i in strinput:
        if i == " ":
            length_space += 1
    
    if length_space > 1:
        return "Invalid Transaction"

    if not strinput[2:].isdigit():
        return "Invalid Transaction"
    amount = int(strinput[2:])

    if action == "D":
        balance += amount
        return f"{amount} has been deposited to your account."
    elif action == "W":
        if balance >= amount:
            balance -= amount
            return f"{amount} has been withdrawn from your account."
        else:
            return "Not enough money!"
    else:
        return "Invalid Transaction"

#main body
balance = 1000
while True:
    strinput = input("Enter input: ")
    action = strinput[:1]
    if action == "X":
        print("Bye Bye")
        break
    print("============================================")
    print(Transaction(strinput))
    print("============================================")
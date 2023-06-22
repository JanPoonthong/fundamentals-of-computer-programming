lowercase = 0
uppercase = 0
digit = 0
special_letter = 0
password_length = 0

def PasswordVerfication(pwdList):
    global lowercase, uppercase, digit, special_letter, password_length
    print("Entered passwords include: ")
    passwordList = pwdList.split(";")
    verify_passwords = []
    bad_passwords = []

    print('\n'.join(pwdList.split(";")))
    print("=======================================")


    for password in passwordList:
        for letter in password:
            if letter.isupper():
                uppercase += 1
            elif letter.islower():
                lowercase += 1
            elif letter.isdigit():
                digit += 1
            elif letter in "!@#$%":
                special_letter += 1
            password_length += 1
    
        if lowercase >= 2 and uppercase >= 2 and digit >= 1 and special_letter >= 1 and password_length >= 8:
            verify_passwords.append(password)
        else:
            bad_passwords.append(password)

        lowercase = 0
        uppercase = 0
        digit = 0
        special_letter = 0
        password_length = 0
    
    return verify_passwords, bad_passwords
    


pwdList = input("Enter password list: ")
print("=======================================")
verify_passwords, bad_passwords = PasswordVerfication(pwdList)

print("Verified passwords include: ")
for i in range(len(verify_passwords)):
    print(f"{i+1}. {verify_passwords[i]}")
print("=======================================")

print("Bad passwords include: ")
for i in range(len(bad_passwords)):
    print(f"{i+1}. {bad_passwords[i]}")

# abc123;tMb1977#;ABCde123$;america123AB!
# 9ddADBKKVks;test123ABC@;ckMO347989!;abtest123AB
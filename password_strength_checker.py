import string
#function to check password strength
def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = any(char in string.ascii_lowercase for char in password)
    uppercase_criteria = any(char in string.ascii_uppercase for char in password)
    digit_criteria = any(char in string.digits for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if score <= 8:
        strength = "Strong "
    elif score >= 5:
        strength = "Moderate "
    else:
        strength = "Weak "

    return strength

# if you are using python 2
password = raw_input("Enter your password: ")
print("Password Strength: {}".format(check_password_strength(password)))

#for python3
#password = input("Enter your password: ")
#print(f"Password Strength: {check_password_strength(password)}")

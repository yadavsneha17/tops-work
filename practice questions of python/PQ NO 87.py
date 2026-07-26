def check_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

print(check_email("abc@gmail.com"))
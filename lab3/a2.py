import string
password = input()
errors = []
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")
if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")
if not any(char.isdigit() for char in password):
    errors.append("В пароле отсутствуют цифры")
special_chars = "*-#"
if not any(char in special_chars for char in password):
    errors.append("В пароле отсутствуют специальные символы")
allowed_chars = string.ascii_letters + string.digits + "*-#"
if not all(char in allowed_chars for char in password):
    errors.append("В пароле используются непредусмотренные символы")
if len(errors) == 0:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)

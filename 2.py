import re

def check_password(password):
    if len(password) < 8:
        return "Пароль должен содержать минимум 8 символов."
    if not re.search(r"[a-z]", password):
        return "Пароль должен содержать хотя бы одну букву в нижнем регистре."
    if not re.search(r"[A-Z]", password):
        return "Пароль должен содержать хотя бы одну букву в верхнем регистре."
    if not re.search(r"[0-9]", password):
        return "Пароль должен содержать хотя бы одну цифру."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Пароль должен содержать хотя бы один специальный символ."
    return "Пароль соответствует всем требованиям."

password = input("Введите пароль: ")
print(check_password(password))
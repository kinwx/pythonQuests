import re

regex = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#.])[0-9a-zA-Z$*&@#.]{8,}$')
def regexInside(password: str):
    min8 = "" if re.search(r'^[a-zA-Z0-9!@#$%<^&*?]{8,}$', password) else "\n8 Dígitos"
    number = "" if re.search(r'\d', password) else "\nUm número"
    upper = "" if re.search(r'[A-Z]', password) else "\nUma letra maiúscula"
    lower = "" if re.search(r'[a-z]', password) else "\nUma letra minúscula"
    especial = "" if re.search(r'[!@#\$%<\^&\*?._]', password) else "\nUm caractere especial"

    return f"A senha precisa ter no mínimo:{min8}{number}{upper}{lower}{especial}"

# print(regexInside("_Aa12345"))
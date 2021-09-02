def is_pol(text):
    pol = text[:: -1]
    if text == pol:
        return True
    else:
        return False

def cred_card(number):
    text = str(number)
    last = text[-4:]
    length = len(text) - 4
    return '*' * length + last


print(cred_card(123445678))
print(is_pol('123321'))

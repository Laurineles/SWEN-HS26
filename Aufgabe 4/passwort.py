def is_password_valid(password):
    fehler = []

    if len(password) < 8:
        fehler.append("Password must be at least 8 characters")

    anzahl_ziffern = 0
    for zeichen in password:
        if zeichen.isdigit():
            anzahl_ziffern = anzahl_ziffern + 1
    if anzahl_ziffern < 2:
        fehler.append("The password must contain at least 2 numbers")

    hat_grossbuchstabe = False
    for zeichen in password:
        if zeichen.isupper():
            hat_grossbuchstabe = True
    if not hat_grossbuchstabe:
        fehler.append("password must contain at least one capital letter")

    sonderzeichen = "#$!?%&*@-_+.,"
    hat_sonderzeichen = False
    for zeichen in password:
        if zeichen in sonderzeichen:
            hat_sonderzeichen = True
    if not hat_sonderzeichen:
        fehler.append("password must contain at least one special character")

    if len(fehler) > 0:
        return "\n".join(fehler)
    return True
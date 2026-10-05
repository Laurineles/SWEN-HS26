from passwort import is_password_valid

def test_gueltiges_passwort():
    resultat = is_password_valid("Sicher12#")
    assert resultat == True

def test_zu_kurz():
    resultat = is_password_valid("Ab12#")
    assert resultat == "Password must be at least 8 characters"

def test_zu_wenig_ziffern():
    resultat = is_password_valid("Abcdefg1#")
    assert resultat == "The password must contain at least 2 numbers"

def test_mehrere_fehler():
    resultat = is_password_valid("someP#")
    assert resultat == "Password must be at least 8 characters\nThe password must contain at least 2 numbers"

def test_kein_grossbuchstabe():
    resultat = is_password_valid("abcdef12#")
    assert resultat == "password must contain at least one capital letter"

def test_kein_sonderzeichen():
    resultat = is_password_valid("Abcdef12")
    assert resultat == "password must contain at least one special character"
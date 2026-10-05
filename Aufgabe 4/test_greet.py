from greet import greet

def test_greet_gibt_einfache_begruessung_zurueck():
    resultat = greet("Bob")
    assert resultat == "Hello, Bob."

def test_greet_ohne_namen():
    resultat = greet(None)
    assert resultat == "Hello, my friend."

def test_greet_anschreien():
    resultat = greet("JERRY")
    assert resultat == "HELLO JERRY!"

def test_greet_zwei_namen():
    resultat = greet(["Jill", "Jane"])
    assert resultat == "Hello, Jill and Jane."

def test_greet_mehrere_namen():
    resultat = greet(["Amy", "Brian", "Charlotte"])
    assert resultat == "Hello, Amy, Brian, and Charlotte."

def test_greet_normale_und_geschrieene_namen():
    resultat = greet(["Amy", "BRIAN", "Charlotte"])
    assert resultat == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_greet_namen_mit_komma_aufteilen():
    resultat = greet(["Bob", "Charlie, Dianne"])
    assert resultat == "Hello, Bob, Charlie, and Dianne."

def test_greet_komma_in_anfuehrungszeichen_nicht_aufteilen():
    resultat = greet(["Bob", "\"Charlie, Dianne\""])
    assert resultat == "Hello, Bob and Charlie, Dianne."
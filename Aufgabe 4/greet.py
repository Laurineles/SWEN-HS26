def namen_verbinden(namen):
    if len(namen) == 1:
        return namen[0]
    if len(namen) == 2:
        return namen[0] + " and " + namen[1]
    return ", ".join(namen[:-1]) + ", and " + namen[-1]


def greet(name):
    if name is None:
        return "Hello, my friend."

    if type(name) == str:
        if name.isupper():
            return "HELLO " + name + "!"
        return "Hello, " + name + "."

    alle_namen = []
    for eintrag in name:
        if eintrag.startswith('"') and eintrag.endswith('"'):
            alle_namen.append(eintrag.strip('"'))
        elif "," in eintrag:
            for teil in eintrag.split(","):
                alle_namen.append(teil.strip())
        else:
            alle_namen.append(eintrag)

    normale_namen = []
    geschrieene_namen = []
    for n in alle_namen:
        if n.isupper():
            geschrieene_namen.append(n)
        else:
            normale_namen.append(n)

    antwort = ""
    if len(normale_namen) > 0:
        antwort = "Hello, " + namen_verbinden(normale_namen) + "."
    if len(geschrieene_namen) > 0:
        geschrien = "HELLO " + namen_verbinden(geschrieene_namen) + "!"
        if antwort == "":
            antwort = geschrien
        else:
            antwort = antwort + " AND " + geschrien
    return antwort